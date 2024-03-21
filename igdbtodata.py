import json
import sqlite3
import math

def add_dict_to_data(d, c, conn):
    id = get_id(d)
    name = get_name(d)
    genres = get_genres(d)
    franch_n = get_franchise_len(d)
    companies = get_companies(d)
    rating = get_rating_and_count(d)
    release_date = get_release_date(d)
    multiplayer = get_multiplayer(d)

    if id is not None and name is not None:
        try:
            c.execute('''INSERT INTO IGDB_Games VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?);''', 
                    (
                        id, name, 
                        genres[0], genres[1], genres[2], genres[3], genres[4], 
                        companies[0], companies[1], 
                        rating[0], rating[1], 
                        franch_n, release_date, multiplayer
                        ))
            conn.commit()
        except Exception: return
        print("ok")




def initialize_db():
    conn = sqlite3.connect('data/igdb.db')
    c = conn.cursor()

    c.execute('DROP TABLE IF EXISTS "IGDB_Games";')

    c.execute('''CREATE TABLE IGDB_Games(
              id int not null,
              name str not null,
              Genre1 int,
              Genre2 int,
              Genre3 int,
              Genre4 int,
              Genre5 int,
              Involved_company1 int,
              Involved_company2 int,
              rating int,
              rating_count int ,
              franchise_len int, 
              first_release_date int,
              multiplayer int,
              primary key(id)
        )''') #involved_company -> company id / multiplayer is a binary (0 or 1)
    conn.commit()
    return c, conn

def get_genres(entry):
    try: 
        genres = entry['genres']
        g_len = len(genres)
        num_g = 5
        ret_list = []
        for i in range(num_g):
            if i < g_len: ret_list.append(genres[i])
            else: ret_list.append(0)
        return ret_list
    except Exception: return [0,0,0,0,0]

def get_franchise_len(entry):
    try: 
        franchise = entry['franchise']
        return len(franchise['games'])
    
    except Exception: return 1
    

def get_id(entry):
    return entry["id"]

def get_name(entry):
    try: return entry["name"]

    except Exception: return None

def get_companies(entry):
    try: 
        comp = entry['involved_companies']
        num_comp = len(comp)
        ret_list = []
        if(num_comp > 0): ret_list.append(comp[0]["company"])
        else: ret_list.append(None)
        if(num_comp > 1): ret_list.append(comp[1]["company"])
        else: ret_list.append(None)
        return ret_list
    
    except Exception: return [0,0]

def get_rating_and_count(entry):
    try: 
        rating = entry['rating']
        rating_num = entry['rating_count']
        return [rating, rating_num]
    except Exception: return [None, None] #will remove if absent

def get_release_date(entry):
    try:
        rd = entry['first_release_date']
        return rd
    
    except Exception: return None

def get_multiplayer(entry):
    try:
        mp = entry['multiplayer_modes']
        return 1 if len(mp) > 0 else 0
    
    except Exception: return 0


# c, conn = initialize_db()
# f =  open('data/igdb.json', 'r')
# data = json.load(f)
# for entry in data:
#     add_dict_to_data(entry, c, conn)

conn = sqlite3.connect('data/igdb.db')
c = conn.cursor()

c.execute(''' DELETE FROM IGDB_Games WHERE rating IS NULL''')
conn.commit()
