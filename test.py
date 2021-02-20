import csv, datetime

with open('features.csv') as f:
    with open('out.csv', 'w') as file1:
        for line in f:
            dt = line.split(',')[1]
            
            datee = datetime.datetime.strptime(dt, "%Y-%m-%d")
            new_line = line[:-1] + "," + str(datee.month) + "\n"
            file1.write(new_line)
