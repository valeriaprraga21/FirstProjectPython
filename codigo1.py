"""
Situación Problema
Andrea Ochoa y Valeria Parraga
"""

def read_csv(filename):
    data = []
    with open(filename, "r") as file:
    #line = file.readline()
        for line in file:
            #print(line)
            data.append(line.strip().split(','))
    return data

def print_matrix(data):
    for row in data:
        for item in row:
            print(f"{item}", end = " ")
        print()

def number_of_songs_each_year(new_data):
    year =input("What year would you like to analyze? ")
    songs = 0
    row = 1
    for row in range(1, len(new_data)):
        if new_data[row][4] == year:
            songs +=1
    print(f"In the year {year}, there were {songs} songs that were in the top 10.")
     
def average_length(new_data, col):
    length = 0
    songs = 0
    for row in range(1, len(new_data)):
        length +=  int(new_data[row][col])
        songs += 1    
    average = length/len(new_data)
    return average


def main1():
    filename = "top10s.csv"
    new_data = read_csv(filename)
    #print(new_data[0][2])
    #average = average_length(new_data)
    #print(average)
    number_of_songs_each_year(new_data)
    #write_file(filename, data)
    #new_data = read_csv(filename)
    #print(new_data)
    #print_matrix(new_data)
    
def main():
    filename = "top10s.csv"
    new_data = read_csv(filename)
    print('Info about the top songs of this decade')
    col_list = ['1. Title', '2. Artist', '3.Top genre', '4. Year',
                '5. Beats per Minute', '6. Energy', '7. Danceability','8. Loudness',
                '9. Liveness', '10. Valence', '11. Duration', '12. Acousticness',
                '13. Speechiness', '14. Popularity']
    print(col_list)
    col = int(input("Write the number of the column to calculate average: "))
    average = average_length(new_data, col)
    print(average)

main()
        
