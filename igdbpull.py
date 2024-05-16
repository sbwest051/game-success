import requests
import json
import time
import pandas as pd


# Global variable for the API link
CLIENT_ID = "wr2kkrabjyxrryhr8b2tzy8d0lc7br"
CLIENT_SECRET ="93oeuq0de9nr67lmui0xf73dzevjpz"
CRED_LINK = 'https://id.twitch.tv/oauth2/token' #+ "client_id=" + CLIENT_ID + "&client_secret=" + CLIENT_SECRET + "&grant_type=client_credentials"

REQ_LINK = 'https://api.igdb.com/v4/games'
AUTH_TOK = 'zs5j43ixb08w1tyruzx4jzdb47ken7'
LIMIT = 50

def get_genre():

    Request_genre_link = "https://api.igdb.com/v4/genres"
    
    try:
        params = {
                'Client-ID': CLIENT_ID,
                'Authorization': 'Bearer ' + AUTH_TOK,
                'Accept': 'application/json',
            }
        body = 'fields \
                    id, name; limit ' + str(LIMIT) + ';offset=' + n
        response = requests.post(Request_genre_link, headers=params, data = body)
        games = response.json()
        save_data_to_json(games, "data/idgb_genre.json")
        
        
    except requests.exceptions.RequestException as e:
        print("Error making API request for genre, could be finished:", e)


def get_platform(platforms):

    Request_ic_link = "https://api.igdb.com/v4/involved_companies"
    Request_comp_link = "https://api.igdb.com/v4/companies"
    for p in platforms:
        try:
            params = {
                    'Client-ID': CLIENT_ID,
                    'Authorization': 'Bearer ' + AUTH_TOK,
                    'Accept': 'application/json',
                }
            body = f'fields \
                        id, company; where id={p}; limit ' + str(LIMIT) + ';'
            response = requests.post(Request_ic_link, headers=params, data = body)
            r = response.json()
            # body = f'fields \
            #             name; where changed_company_id={r["company"]};'
            # response = requests.post(Request_ic_link, headers=params, data = body)
            # # final = pd.concat([r, response.json()])
        except requests.exceptions.RequestException as e:
            print("Error making API request for platform:", e)
            continue

        save_data_to_json(r, "data/idgb_platform.json")
            
        
def make_api_request(link):
    try:
        params = {
            'Client-ID': CLIENT_ID,
            'Authorization': 'Bearer ' + AUTH_TOK,
            'Accept': 'application/json',
        }
        n0 = 0
        with open('data/igdb.json', 'w' if n0 == 0 else 'a') as file:
            file.write('[')
            while(True):
                body = 'fields \
                    first_release_date,franchise,genres,involved_companies, \
                    multiplayer_modes,name,rating,rating_count; limit ' + str(LIMIT) + '; offset ' + str(n0) + ';'
                response = requests.post(link, headers=params, data = body)
                if response.status_code != 200: break  # Raise an exception for 4xx or 5xx status codes
                
                
                games = response.json()
                # file.seek(file.tell() - 1)
                for i,g in enumerate(games):
                    if not (n0==0 and i==0): file.write(',')
                    json.dump(g, file, indent=4)
                n0 += LIMIT
                print(n0)
                

        # for i in response.json():
        #     print (response.json()[i])
        # return response.json()  # Assuming response is JSON data
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
        with open(filename, 'a') as file:
            json.dump(data, file, indent=4)  # Save data as JSON with indentation for readability
        print("Data saved successfully to", filename)
    except Exception as e:
        print("Error saving data to file:", e)


def main():
    # uncomment what you want to check on
    # Make API request for general dataset
    # make_api_request(REQ_LINK)

    # Request Genre
    # get_genre()
    
    # Get platformn -> couldn't quite get to collect the right data
    platforms = ['70', '13634', '1', '112','26','66','37','0','197','129']
    # get_platform(platforms=platforms)

    # api_data = None #make_api_request()
    # if credentials:
    #     # Save data to .dat file
    #     save_data_to_file(str(api_data), "data/igdb_credentials.dat")

if __name__ == "__main__":
    main()

