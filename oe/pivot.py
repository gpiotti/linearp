from collections import OrderedDict
import csv
myfile = open('pivot.csv', 'w')

def readCsv(path):
    with open(path, 'r') as f:
        reader = csv.reader(f)
        return list(reader)


temp = OrderedDict()

csv_input = readCsv('assignment.csv')
  
for row in csv_input:
    teacher = row[0]
    temp[teacher] = []

assignment = []
for row in csv_input:
    if str(row[2]) == 'LP2 - Classic Intermediate':
        i = 'INT'
    elif str(row[2]) == 'LP2 - Classic True Beginner - Portuguese':
        i = 'TBP'
    elif str(row[2]) == 'LP2 - Monitor':
        i = 'MON'
    else:
        i = 'off'
    temp[row[0]].append(i)

        

text = ''
for teacher in temp:
    text = text +  teacher + ',' + (','.join(temp[teacher])) + '\n'

myfile.write(text)


