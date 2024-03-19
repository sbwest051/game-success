import json

# names = set() 

def get_names(file_path):
    with open(file_path, 'r') as file:
        games = json.load(file)

    names = [game['name'] for game in games if 'name' in game]
    names = set(names)
    
    return names


names = get_names('gb1_json.json')
print(len(names))
