import sqlite3

def print_menu():

    print('''
    1- Add a track - adds a new track to the DB, with all the relevant information.
    2- Get a playlist - prints an existing playlist to the user.
    3- Create a playlist - creates a new playlist in the DB.
    4- Add a song to a playlist - adds a song to an existing playlist.
    5- Add an employee 
    6- Delete an employee
    7- Report on a purchase - adds information about a purchase to the DB.
    8- Print revenues - reports on store revenues. The function can print revenues based on the following factors:
        a- All the revenues that a specific employee has helped gain.
        b- All the revenues between 2 specific dates.
        c- All the revenues from a specific music genre.
    ''')

def user_interaction(conn):
    # print_menu()

    # user_input = str(input('Pick one of the choices : '))

    # #if user_input == '1':
    #     #print('Provide all these information')
    values = []
    cursor = conn.cursor()
    
    #------------------------------------------------
    cursor.execute("SELECT * FROM tracks")
    num_fields = len(cursor.description)
    field_names = [i[0] for i in cursor.description]
    #------------------------------------------------
    genre_name = input('GenreName: ')
    
    #------------------------------------------------
    media_type = input('MediaType: ')
    
    #------------------------------------------------
    artist_name = input('ArtistName: ')
    
    #------------------------------------------------
    cursor.execute(f'''INSERT INTO genres(Name) VALUES(?)''',(genre_name,))
    cursor.execute(f'''INSERT INTO media_types (Name) VALUES (?)''',(media_type,))
    cursor.execute(f'''INSERT INTO artists (Name) VALUES (?)''',(artist_name,))
    conn.commit()
    album_name = input('AlbumName: ')
    artist_id = list(cursor.execute("SELECT ArtistId FROM artists WHERE Name=?", (artist_name,)))
    
    cursor.execute(f'''INSERT INTO "albums" (Title, ArtistId) VALUES (?,?)''',(album_name,artist_id[0][0],))
    #------------------------------------------------
    genre_id = list(cursor.execute("SELECT GenreId FROM genres WHERE Name=?", (genre_name,)))
    media_id = list(cursor.execute("SELECT MediaTypeId FROM media_types WHERE Name=?", (media_type,)))
    artist_id = cursor.execute("SELECT ArtistId FROM artists WHERE Name=?", (artist_name,))
    ar_id = list(artist_id)[0][0]
    
    album_id = list(cursor.execute("SELECT AlbumId FROM albums WHERE ArtistId=?", (ar_id,)))
    #------------------------------------------------
    
    
    
    track_name = input('TrackName: ')
    composer = input('Composer: ')
    milliseconds = int(input('Milliseconds: '))
    track_bytes = int(input('Bytes: '))
    unit_price = float(input('UnitPrice: '))



    #------------------------------------------------
    # print('Enter the following information \n----------------------------')
    # for name in field_names[1:]:
    #     i = input(name+':')
    #     values.append(i)
        
    
    cursor.execute(f"""INSERT INTO 'tracks'
                          ('Name', 'AlbumId', 'MediaTypeId', 'GenreId', 'Composer', 'Milliseconds', 'Bytes', 'UnitPrice') 
                           VALUES 
                          ('{track_name}','{album_id[0][0]}','{media_id[0][0]}','{genre_id[0][0]}','{composer}','{milliseconds}','{track_bytes}','{unit_price}')""")
    
    conn.commit()
    
    conn.close()
    del cursor
    
    del conn
    

    

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file,timeout=1, isolation_level=None)
    except:
        print('try again')
    

    return conn

def retrieve_info(conn):

 
    
    cursor = conn.cursor()
    cursor.execute( 'select * from employees')
    rows = cursor.fetchall()

    for i in rows:
        print(i)

conn = create_connection('chinook.db')
user_interaction(conn)
#retrieve_info(conn)
