"""
Situación Problema
Andrea Ochoa y Valeria Parraga

This program helps the user to analyze a data set
about the songs that made it to the "top 10 songs" playlist
in spotify in the last decade.
The user can choose to analyze by song, artist or year 
"""

def read_csv(filename):
    """ Function that reads the data set """
    new_data = []
    file = open(filename, 'r', encoding="ISO-8859-1")
    for line in file:
        new_data.append(line.strip().split(','))
    return new_data

def print_matrix(data):
    """ Print any matrix """
    for row in data:
        for item in row:
            print(f"{item}", end = "")
        print()
        
def input_exists(inp, data, col):
    """Function that verifies if the input exist in the data set """
    inp = '"' + inp + '"'
    inp_exists = False
    while inp_exists == False:
        for row in range(len(data)):
            if data[row][col].lower() == inp.lower():
                inp_exists = True
                return inp
                break
            else:
                inp_exists = False
        if inp_exists == False:
            inp = input(f"Oops! We don't have {inp} on the list. Check your spelling or try with something different: ")
            inp = '"' + inp + '"'  
    return inp

def song_value(data, song, col):
    """ Function that analyzes an specific value of the song asked by the user """
    col += 4
    for row in range(len(data)):
        if data[row][1].lower() == song.lower():
            value = data[row][col]
    return value

def song_row(data, song, col_list_complete):
    """Function that returns all the informartion of the song asked by the user """
    row_list = []
    lista = []
    for row in range(len(data)):
        if data[row][1].lower() == song.lower(): 
            for col in range(1,15):
                row_list.append(data[row][col])           
    for value in range(len(row_list)): 
        lista.append((col_list_complete[value] + ': ' + row_list[value]))
    return lista

def artist_average(data, col, artist):
    """ Function that returns the average of an specific parameter of the artist asked by the user"""
    col = col + 4
    variable = 0
    counter = 0
    for row in range(1, len(data)):
        if data[row][2].lower() == artist.lower():
            variable = variable + int(data[row][col])
            counter += 1
    average = variable/counter
    return average

def artist_number_of_songs(data, year, artist):
    """ Function that returns the numer of songs that made it to the top 10 of an artist of a specific year """
    songs = 0
    if year == "all":
        for row in range (1, len(data)):
            if artist.lower() == data[row][2].lower():
                songs += 1
        return songs
    else:
        for row in range (1, len(data)):
            analyzeYear = data[row][4]
            if year == analyzeYear:
                item = data[row][2]
                if artist == item:
                    songs += 1
        return songs

def year_average(data, col, year):
    """ Function that returns the average of a specific parameter of a year asked by the user """
    col = col + 4
    variable = 0
    counter = 0
    for row in range(1, len(data)):
        if data[row][4] == year:
            variable = variable + int(data[row][col])
            counter += 1
    average = variable/counter
    return average

def number_of_songs_each_year(data, year):
    """ Function that returns the number of songs that made it to the top 10 of an specific year given by the user"""
    songs = 0
    for row in range (1, len(data)):
        item = data[row][4]
        if item == year:
            songs += 1               
    return songs

def main():
    filename = "top10s.csv"
    data = read_csv(filename)
    col_list = ["1 for Beats Per Minute (bpm)", "2 for Energy (nrgy)",
                "3 for Danceability (dnce)", "4 for Loudness (dB)",
                "5 for Liveness (liv)", "6 for Valance (val)",
                "7 for Duration (dur)", "8 for Acousticness (acous)",
                "9 for Speechiness (spch)", "10 for Popularity (pop)"]
    col_list_complete = ['1. Title', '2. Artist', '3.Top genre', '4. Year', '5. Beats per Minute',
                         '6. Energy', '7. Danceability','8. Loudness', '9. Liveness', '10. Valence',
                         '11. Duration', '12. Acousticness', '13. Speechiness', '14. Popularity']
    
    print('Welcome to the Top Songs of The Decade - Data Set')
    
    repeat = 'y'
    while repeat == 'y':
        print("______________________________________________")
        print()
        print('What do you want to analyze?')
        print()
        print("\ta. A song ")
        print("\tb. An artist")
        print("\tc. A year")
        print()
        option = input("Select an option: ")
        
        if option == 'a':
            print()
            song = input('What song do you want to analyze? ')
            song = input_exists(song, data, 1)
            print()
            print(f"What do you want to analyze about {song}?")
            print()
            print("\ta. Specific data")
            print("\tb. All data ")
            print()
            option = input("Select an option: ")
            
            if option == 'a':
                print()
                print('Here is the list of the information you can obtain')
                print()
                print_matrix(col_list)
                print()
                col = int(input("Enter option number: "))
                value = song_value(data, song, col)
                print()
                print(f"The value is {value}")
                
            elif option == 'b':
                data_song = song_row(data, song, col_list_complete)
                print()
                print_matrix(data_song)
                
        elif option == 'b':
            print()
            artist = input('What artist do you want to analyze? ')
            print()
            artist = input_exists(artist, data, 2)
            print(f"What do you want to analyze about {artist}")
            print()
            print("\ta. Artist average")
            print("\tb. Number of songs")
            print()
            option = input("Select an option: ")
            
            if option == 'a':
                print()
                print('Here is the list of the information you can obtain')
                print()
                print_matrix(col_list)
                print()
                col = int(input("Enter a the number of the column: "))
                average = artist_average(data, col, artist)
                print()
                print(f"The average is {average}")
            
            elif option == 'b':
                print()
                year = input(f"Would you like to analyze how many songs {artist} had in a specific year (2010-2019), or in all the years (all)? ")
                print()
                songs = artist_number_of_songs(data, year, artist)
                if year == "all":
                    print()
                    print(f"{artist} has {songs} songs in all the years.")
                else:
                    print()
                    print(f"{artist} had {songs} songs in the year {year}.")
             
        elif option == 'c':
            print()
            year = input('What year do you want to analyze? ')
            print()
            print(f"What do you want to analyze about the year {year}?")
            print()
            print("\ta. Average in the year")
            print("\tb. Number of songs in the year")
            print()
            option = input("Select an option: ")
            
            if option == 'a':
                print()
                print('Here is the list of the information you can obtein')
                print()
                print_matrix(col_list)
                col = int(input("Enter a the number of the column: "))
                average = year_average(data, col, year)
                print()
                print(f"The average is {average}")
                
            elif option == 'b':
                print()
                songs = number_of_songs_each_year(data, year)
                print(f"In the year {year}, there were {songs} songs in the top 10.")
                    
        print()   
        repeat = input('Do you want to know anything else? [y]/n: ')

main()
