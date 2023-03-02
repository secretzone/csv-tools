import csv
import random
import os

image_count = 5
input_file = 'PlanetDatabase.csv'
output_file = 'PlanetDatabase_copy.csv'

with open(input_file, 'r') as csvinput:
    if os.path.isfile(output_file):
        os.remove(output_file)
    with open(output_file, 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        reader = csv.reader(csvinput)

        all = []
        row = next(reader)
        row.append('ImageIndex')
        all.append(row)

        for row in reader:
            row.append(str(random.randrange(0, image_count)))
            all.append(row)

        writer.writerows(all)