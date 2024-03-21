import requests
import time
import json

api_key = 'a092cd37dac94196458c49d4b8e3487e5f96a9f5'
file_path = "gb_reviews_json.json"
# game_ids = []

def get_games_from_giant_bomb(api_key, starting_offset):
    base_url = "https://www.giantbomb.com/api/user_reviews/"
    headers = {'User-Agent': 'GameDataResearch/1.0'}
    limit = 100
    offset = starting_offset

    # Check if we are appending to an existing file
    is_appending = starting_offset > 0

    with open(file_path, 'a' if is_appending else 'w') as file:
        if not is_appending:
            # Write the opening bracket for JSON array only if this is a new file
            file.write('[')
        else:
            # Move back before the last closing bracket ']'
            file.seek(file.tell() - 1)
            if starting_offset > limit:
                # Add a comma when
                # not the first set 
                file.write(',')

        first_entry = True

        while True:
            params = {
                'api_key': api_key,
                'format': 'json',
                'offset': offset,
            }
            
            response = requests.get(base_url, headers=headers, params=params)
            if response.status_code == 200:
                data = response.json()
                reviews = data['results']
                if not reviews:
                    break  # Break the loop if no games are returned
                
                for game in reviews:
                    if (game is not None) and (game["game"] is not None) :
                        if not first_entry:
                            file.write(',')
                        json.dump(game, file)
                        first_entry = False
                        # print(game["game"])
                        # game_ids.append([game["game"]["name"],game["guid"],game["score"]])
                    
                if len(reviews) < limit:
                    break  # Break the loop if we retrieved fewer than 'limit' games
                
                offset += limit
            else:
                print(f"Error: {response.status_code}")
                break
            
            print(offset)
            time.sleep(1)
        
        # Write or rewrite the closing bracket for JSON array
        file.write(']')
#Does't fully work because you still need to go back and manually remove the ] from the end of the json file for each time program is run
    
    # return offset - starting_offset  # Return how many new games were added

# REMEMBER update starting_offset to last successful offset
#Last successful offset = 27600 -- missed a few
# new_reviews_added = get_games_from_giant_bomb(api_key, 27700)

# print(f"New games added: {new_reviews_added}")
def get_reviews(file_path):
    with open(file_path, 'r') as file:
        games = json.load(file)

    # names = [game['name'] for game in games if 'name' in game]
    # names = set(names)
    
    return games


names = get_reviews('gb_reviews_json.json')
print(len(names))



# print(len(games_data))
