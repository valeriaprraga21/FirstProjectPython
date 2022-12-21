"""
This program helps the user to analyze a data set
about the top 10 songs in spotify in the last decade

Valeria Parraga & Andrea Ochoa
A01029428 // A01660137
"""

def read_csv(filename):
    """ Reads the data set """
    data = []
    with open(filename, "r") as file:
        for line in file:
            data.append(line.strip().split(','))
    return data

def print_matrix(data):
    """ Print any matrix """
    for row in data:
        for item in row:
            print(f"{item}", end = "")
        print()
        
def song_value(data, song, col):
    song = '"' + song + '"'
    col += 4
    for row in range(len(data)):
        if data[row][1].lower() == song.lower():
            value = data[row][col]
    return value

def song_row(data, song, col_list_complete):
    song = '"' + song + '"'
    row_list = []
    lista = []
    for row in range(len(data)):
        if data[row][1].lower() == song.lower(): 
            for col in range(1, 14):
                row_list.append(data[row][col])           
    for value in range(len(row_list)): 
        lista.append((col_list_complete[value] + ': ' + row_list[value]))
    return lista

def artist_average(data, col, artist):
    artist = '"' + artist + '"'
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
    artist = '"' + artist + '"'
    songs = 0
    if year == "all":
        for row in range (1, len(data)):
            if artist.lower() == data[row][2].lower():
                songs += 1
        return songs
    else:
        for row in range (1, len(new_data)):
            analyzeYear = new_data[row][4]
            if year == analyzeYear:
                item = new_data[row][2]
                if artist == item:
                    songs += 1
        return songs
    
def year_average(data, col, year):
    col = col + 4
    variable = 0
    count = 0
    for row in range(1, len(data)):
        if data[row][4] == year:
            variable = variable + int(data[row][col])
            count += 1  
    average = variable/count
    return average

def number_of_songs_each_year(data, year):
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
        print('What do you want to analyze?')
        print("\ta. A song ")
        print("\tb. An artist")
        print("\tc. A year")
        option = input("Select an option: ")
        
        if option == 'a':
            song = input('What song do you want to analyze? ')
            print(f"What do you want to analyze about {song}?")
            print("\ta. Specific data")
            print("\tb. All data ")
            option = input("Select an option: ")
            
            if option == 'a':
                print('Here is the list of the information you can obtain')
                print_matrix(col_list)
                col = int(input("Enter the option number: "))
                value = song_value(data, song, col)
                print(f"The value is {value}")
                
            elif option == 'b':
                data = song_row(data, song, col_list_complete)
                print_matrix(data)
                
        elif option == 'b':
            artist = input('What artist do you want to analyze? ')
            print(f"What do you want to analyze about {artist}")
            print("\ta. Artist average")
            print("\tb. Number of songs")
            option = input("Select an option: ")
            
            if option == 'a':
                print('Here is the list of the information you can obtain')
                print_matrix(col_list)
                col = int(input("Enter the option number: "))
                average = artist_average(data, col, artist)
                print(f"The average is {average}")
            
            elif option == 'b':
                year = input(f"Would you like to analyze how many songs {artist} had in a specific year (2010-2019), or in all the years (all)? ")
                songs =  artist_number_of_songs(data, year, artist)
                print(f"{artist} had {songs} songs in the year {year}")

                
        elif option == 'c':
            year = input('What year do you want to analyze? ')
            print(f"What do you want to analyze about the year {year}")
            print("\ta. Average in the year")
            print("\tb. Number of songs in the year")
            option = input("Select an option: ")
            
            if option == 'a':
                print('Here is the list of the information you can obtain')
                print_matrix(col_list)
                col = int(input("Enter the option number: "))
                average = year_average(data, col, year)
                print(f"The average is {average}")
                
            elif option == 'b':
                songs = number_of_songs_each_year(data, year)
                print(f"In the year {year}, there were {songs} songs that were in the top 10.")
            
        repeat = input('Do you want to know anything else? [y]/n: ')

main()
