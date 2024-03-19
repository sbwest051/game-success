import json
import requests

# Define the URL for the API
url = "https://api.mobygames.com/v1/games"

# Provide your API key
api_key = "moby_c9fBsti26zpKRGMOmsrSBxRwLIs"

# Define the parameters including the API key
params = {
    "format": "normal",
    "api_key": api_key
}

# Send GET request to the API
response = requests.get(url, params=params)

# Check if request was successful (status code 200)
if response.status_code == 200:
    # Extract JSON data from the response
    data = response.json()

    # Accessing the games data
    games = data.get('games', [])

    # Check if there are games in the response
    if games:
        # List to store all games' data
        all_games_data = []

        # Loop through each game and extract its details
        for game in games:
            game_data = {
                "Title": game.get('title'),
                "Description": game.get('description'),
                "Genres": [genre.get('genre_name') for genre in game.get('genres', [])],
                "Platforms": [platform.get('platform_name') for platform in game.get('platforms', [])],
                "Moby Score": game.get('moby_score'),
                "Moby URL": game.get('moby_url'),
                # "Sample Cover Image": game.get('sample_cover', {}).get('image'),
                # "Sample Screenshots": [{"Caption": screenshot.get('caption'), "Image": screenshot.get('image')} 
                #                        for screenshot in game.get('sample_screenshots', [])]
            }
            all_games_data.append(game_data)

        # Save all games' data to a JSON file
        with open('moby_g_genre_data.json', 'w') as f:
            json.dump(all_games_data, f, indent=4)

        print("All games' data saved to 'games_data.json' file.")
    else:
        print("No games found in the response.")
else:
    print("Failed to fetch data. Status code:", response.status_code)

# import requests

# # Define the API endpoint URL
# url = "https://api.mobygames.com/v1/games/31910/platforms/5"

# # Define the headers including your API key
# headers = {
#     "User-Agent": "Mozilla/5.0",
#     "Authorization": "Bearer moby_c9fBsti26zpKRGMOmsrSBxRwLIs"
# }

# # Send GET request to the API
# response = requests.get(url, headers=headers)

# # Check if the request was successful (status code 200)
# if response.status_code == 200:
#     # Parse the JSON response
#     data = response.json()

#     # Extract relevant information
#     game_id = data.get('game_id')
#     platform_name = data.get('platform_name')
#     first_release_date = data.get('first_release_date')

#     attributes = data.get('attributes', [])
#     for attribute in attributes:
#         print(f"{attribute['attribute_name']}: {attribute['attribute_category_name']}")

#     releases = data.get('releases', [])
#     for release in releases:
#         release_date = release.get('release_date')
#         companies = release.get('companies', [])
#         for company in companies:
#             company_name = company.get('company_name')
#             role = company.get('role')
#             print(f"Released by {company_name} ({role}) on {release_date}")

# else:
#     print("Failed to retrieve data. Status code:", response.status_code)










# import requests

# # Define the API endpoint and parameters
# url = "https://api.mobygames.com/v1/games"
# params = {
#     "format": "normal",
#     "apikey": "moby_c9fBsti26zpKRGMOmsrSBxRwLIs"
# }

# # Send the GET request
# response = requests.get(url, params=params)

# # Check if the request was successful (status code 200)
# if response.status_code == 200:
#     # Parse the JSON response
#     data = response.json()

#     # Extract relevant information
#     if "games" in data:
#         games = data["games"]
#         for game in games:
#             title = game["title"]
#             description = game["description"]
#             moby_score = game["moby_score"]
#             moby_url = game["moby_url"]
#             num_votes = game["num_votes"]
#             platforms = [platform["platform_name"] for platform in game["platforms"]]
#             genres = [genre["genre_name"] for genre in game["genres"]]
#             alternate_titles = [alt_title["title"] for alt_title in game["alternate_titles"]]
#             sample_cover = game["sample_cover"]["image"]
#             sample_screenshots = [screenshot["image"] for screenshot in game["sample_screenshots"]]
            
#             # Print or process the extracted data as needed
#             print("Title:", title)
#             print("Description:", description)
#             print("Moby Score:", moby_score)
#             print("Moby URL:", moby_url)
#             print("Number of Votes:", num_votes)
#             print("Platforms:", platforms)
#             print("Genres:", genres)
#             print("Alternate Titles:", alternate_titles)
#             print("Sample Cover:", sample_cover)
#             print("Sample Screenshots:", sample_screenshots)
#             print("\n")
# else:
#     print("Failed to retrieve data. Status code:", response.status_code)





















#////////////////////BAD SCRAPE////////////////////////

# import requests
# from bs4 import BeautifulSoup

# # URL of the webpage to scrape
# url = "https://www.mobygames.com/game/"

# # Send a GET request to the URL
# response = requests.get(url)

# # Parse the HTML content
# soup = BeautifulSoup(response.content, "html.parser")

# # Find the table containing the game information
# table = soup.find(class_="table mb")

# # Initialize lists to store data
# games = []

# # Loop through each row in the table
# for row in table.find_all("tr"):
#     # Initialize dictionary to store game details
#     game_info = {}
#     # Find all cells in the row
#     cells = row.find_all("td")
#     if len(cells) > 0:  # Ensure it's not a header row
#         # Extract data and store it in the dictionary
#         game_info["title"] = cells[0].a.text.strip()
#         game_info["critic_score"] = cells[1].div.text.strip()
#         game_info["year"] = cells[2].text.strip()
#         game_info["developer"] = cells[3].text.strip()
#         # Append the dictionary to the list of games
#         games.append(game_info)

# # Print the extracted data
# for game in games:
#     print(game)
