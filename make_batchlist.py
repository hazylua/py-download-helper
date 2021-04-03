"""
Makes batch list to be used with youtube-dl.
Example usage command: youtube-dl -f "bestaudio/best" -v -x --audio-format vorbis --audio-quality 0 --batch-file download.txt -o "Tracks/Music_%(autonumber)1d.%(ext)s"
"""

import csv

def main():
    """
    Outputs values containing desired URLs from target column in a .csv to a .txt file.
    """
    inputf = './tracklist.csv'
    outputf = './batchlist.txt'
    target = 3

    txt = open(outputf, 'w+')
    batch_list = []
    with open(inputf) as input_file:
        csv_file = csv.reader(input_file, delimiter=',')
        for row in csv_file:
            batch_list.append(row)
        batch_list = batch_list[1:]

    for row in batch_list:
        txt.write(f'{row[target]}\n')

if __name__ == '__main__':
    main()
