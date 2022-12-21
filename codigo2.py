
def read_csv(filename):
    data = []
    with open(filename, "r") as file:
        for line in file:
            data.append(line.strip().split(','))
    return data

def print_matrix(data):
    for row in data:
        for item in row:
            print(f"{item}", end = "")
        print()

def number_of_songs_each_year(new_data,year):
    songs = 0
    row = 1
    for row in range(1, len(new_data)):
        if new_data[row][4] == year:
            songs +=1
    return songs 
     
def average_length(new_data, col):
    length = 0
    songs = 0
    for row in range(1, len(new_data)):
        length +=  int(new_data[row][col])
        songs += 1    
    average = length/len(new_data)
    return average

def artistWithMoreSongsInaYear(new_data):
    year = input("What year would you like to analyze? ")
    artists=[]
    for row in range (0, 3):
        item = new_data[row][4]
        if item == year:
            artists.append(new_data[row][2])
            
        artistsWithSongs = []
        name1 = 0
        name2 = 0
        for position in range(0, len(artists)):
            songs = 1
            for compare in range(position+1, len(artists)):
                name1 = artists[position]
                name2 = artists[compare]
                if name1 == name2:
                    songs +=1
            artistsList = [name1, songs]
            artistsWithSongs.append(artistsList)


def main():
    filename = "top10s.csv"
    new_data = read_csv(filename)
    col_list = ['1. Title', '2. Artist', '3.Top genre', '4. Year',
                '5. Beats per Minute', '6. Energy', '7. Danceability','8. Loudness',
                '9. Liveness', '10. Valence', '11. Duration', '12. Acousticness',
                '13. Speechiness', '14. Popularity']
    
    print('Welcome to the Top Songs of The Decade - Data Set')
    print('What do you want to know?')
    
    repeat = 'y'
    while repeat == 'y':
        print("\ta. The Average of a Column")
        print("\tb. How many songs where in the Top 10 in a certain year")
        print("\tc. ...")
        option = input("Select an option: ")
    
        if option == 'a':
            print_matrix(col_list)
            col = int(input("Enter a the number of the column: "))
            average = average_length(new_data, col)
            print(f"the average of the column {col} is {average}")
                
        elif option == 'b':
            year = int(input("Enter the year: "))
            number = number_of_songs_each_year(new_data, year)
            print('In the year {year}, there were {songs} songs that were in the top 10.')
                 
        elif option == 'c':
            print("Good bye")
            
        repeat = input('Do you want to know anything else? [y]/n: ')
    
filename = "top10s.csv"
new_data = read_csv(filename)
#artistWithMoreSongsInaYear(new_data)
print(artistWithMoreSongsInaYear(new_data))
