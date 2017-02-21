import csv

## CALENDAR
##with open('calendar.csv', 'r') as f:
##  reader = csv.reader(f)
##  csv_input = list(reader)
##  
##temp = {}
##calendar = []
##
##for row in csv_input:
##    teacher = row[0]
##    temp[teacher] = []
##    
##for row in csv_input:
##    if row[0] in temp.keys():
##        if row[2] == "0":    
##            temp[row[0]].append("false")
##        else:
##            temp[row[0]].append("true")
##
##
##for teacher in temp:
##    calendar.append(temp[teacher])

#print (",".join(calendar))
#print (calendar[1])

## teacherCanDoShift
##temp = {}
##teacherCanDoShift = []
##
##with open('skills.csv', 'r') as f:
##  reader = csv.reader(f)
##  csv_input = list(reader)
##  
##temp = {}
##teacherCanDoShift = []
##
##for row in csv_input:
##    teacher = row[0]
##    temp[teacher] = [] 
##for row in csv_input:
##    if row[0] in temp.keys():
##        if row[2] == "0":    
##            temp[row[0]].append("false")
##        else:
##            temp[row[0]].append("true")
##
##
##for teacher in temp:
##    teacherCanDoShift.append(temp[teacher])
##
###print (",".join(calendar))
##print (teacherCanDoShift)



temp = {}
teacherName = []

with open('teachers.csv', 'r') as f:
  reader = csv.reader(f)
  csv_input = list(reader)
  
temp = {}
teacherName = []

for row in csv_input:
    teacherName.append(row)


#print (",".join(calendar))
print (teacherName)

