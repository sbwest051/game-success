import requests
import json
import time


# Global variable for the API link
CLIENT_ID = "wr2kkrabjyxrryhr8b2tzy8d0lc7br"
CLIENT_SECRET ="93oeuq0de9nr67lmui0xf73dzevjpz"
CRED_LINK = 'https://id.twitch.tv/oauth2/token' #+ "client_id=" + CLIENT_ID + "&client_secret=" + CLIENT_SECRET + "&grant_type=client_credentials"

REQ_LINK = 'https://api.igdb.com/v4/games'
AUTH_TOK = 'zs5j43ixb08w1tyruzx4jzdb47ken7'


def make_api_request(link):
    try:
        params = {
            'Client-ID': CLIENT_ID,
            'Authorization': 'Bearer ' + AUTH_TOK,
            'Accept': 'application/json',
            'Body': 'fields age_ratings,aggregated_rating,aggregated_rating_count,first_release_date,franchise,genres,hypes,involved_companies,multiplayer_modes,name,platforms,rating,rating_count,release_dates,total_rating,total_rating_count;'

        }
        response = requests.post(link, params=params)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        for i in response.json():
            print (response.json()[i])
        return response.json()  # Assuming response is JSON data
    except requests.exceptions.RequestException as e:
        print("Error making API request:", e)
        return None

def save_data_to_file(data, filename):
    try:
        with open(filename, 'w') as file:
            file.write(data)
        print("Data saved successfully to", filename)
    except Exception as e:
        print("Error saving data to file:", e)

def save_data_to_json(data, filename):
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)  # Save data as JSON with indentation for readability
        print("Data saved successfully to", filename)
    except Exception as e:
        print("Error saving data to file:", e)


def main():
    # Make API request
    credentials = make_api_request(CRED_LINK)
    
    api_data = None #make_api_request()
    if credentials:
        # Save data to .dat file
        save_data_to_file(str(api_data), "data/igdb_credentials.dat")

if __name__ == "__main__":
    main()
