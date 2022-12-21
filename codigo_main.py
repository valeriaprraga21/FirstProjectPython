

def main():
    filename = "top10s.csv"
    new_data = read_csv(filename)
    col_list = ["1 for Beats Per Minute (bpm)", "2 for Energy (nrgy)",
                "3 for Danceability (dnce)", "4 for Loudness (dB)",
                "5 for Liveness (liv)", "6 for Valance (val)",
                "7 for Duration (dur)", "8 for Acousticness (acous)",
                "9 for Speechiness (spch)", "10 for Popularity (pop)"]
    
    print('Welcome to the Top Songs of The Decade - Data Set')
    
    
    repeat = 'y'
    while repeat == 'y':
        print('What do you want to analyze?')
        print("\ta. A song ")
        print("\tb. A artist")
        print("\tc. A year")
        option = input("Select an option: ")
        
        if option == 'a':
            song = input('What song do you want to analyze?')
            print(f"What do you want to analyze about {song}")
            print("\ta. Specific data")
            print("\tb. All data ")
            option = input("Select an option: ")
            
            if option == 'a':
                """function that gives the int of an specific row"""
            elif option == 'b':
                """ function that gives all the ints in a row """
                
        elif option == 'b':
            artist = input('What artist do you want ot analyze?')
            print(f"What do you want to analyze about {artist}")
            print("\ta. Artist average")
            print("\tb. Number of songs")
            option = input("Select an option: ")
            
            if option == 'a':
                """the average function but with artist """
            
            elif option == 'b':
                """ function that gives the number of songs of a artist"""
                
        elif option == 'c':
            year = input('What year do you want to analyze?')
            print(f"What do you want to analyze about the year {year}")
            print("\ta. Average in the year")
            print("\tb. Number of songs in the year")
            print("\tc. Top genre in the year")
            option = input("Select an option: ")
            
            if option == 'a':
                """ the average function but only in the year """
                
            elif option == 'b':
                number = number_of_songs_each_year(new_data, year)
                print(f"In the year {year}, there were {songs} songs that were in the top 10.")
            
            elif option == 'c':
                """function that gives the top genre in a year """
                

            
        repeat = input('Do you want to know anything else? [y]/n: ')
    
    