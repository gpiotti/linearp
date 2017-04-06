#get the model output and pivots columns for easy excel visualization
#input assignment.csv
#output pivot.csv
from collections import OrderedDict
import csv
import sys
myfile = open(sys.argv[2], 'w')

def detectDelimiter(csvFile):
    with open(csvFile, 'r') as myCsvfile:
        header=myCsvfile.readline()
        if header.find(";")!=-1:
            myCsvfile.close()
            return ";"
        if header.find(",")!=-1:
            myCsvfile.close()
            return ","
    #default delimiter (MS Office export)
    myCsvfile.close()
    return ";"

def readCsv(path):
    with open(path, 'r') as f:
        reader = csv.reader(f,delimiter=detectDelimiter(sys.argv[1]))
        return list(reader)

shiftNames = ["a3731000000573uAAA","a3731000000573zAAA","a3731000000573kAAA","off"]

temp = OrderedDict()

csv_input = readCsv(sys.argv[1])
#print (csv_input)
for row in csv_input:
    if row[0] != '----------' and row[0] != '==========':
        teacher = str(row[1])
        temp[teacher] = []


assignment = []
for row in csv_input:
    if row[0] != '----------' and row[0] != '==========':
        if str(row[2]) == shiftNames[0]:
            i = 'INT' 
        elif str(row[2]) == shiftNames[1]:
            i = 'TBP' 
        elif str(row[2]) == shiftNames[2]:
            i = 'MON'
        else:
            i = shiftNames[3]
        temp[row[1]].append(i)

   

text = ''

for teacher in temp:
    text = text +  teacher + ',' + (','.join(temp[teacher])) + '\n'

myfile.write(text)
myfile.close()

