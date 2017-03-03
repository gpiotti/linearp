from random import randint,randrange,choice
import csv
import math
from collections import OrderedDict
myfile = open('datagen.dzn', 'w')
WEEKSINYEAR = 52
DAYSINYEAR = 365
NUMTEACHERS = 544
MAXTIME = 336
TIME0 = 4
PERC_AVAILABILITY= 80

NUM_DAYS = 7
NUM_WEEKS = 1

TIME_WITHIN_DAY = 48
TIME_WITHIN_WEEK = 336
NUMOFSKILLS = 2
shifts = ["intermediate", "tbp","monitor", "off"]
NUMOFSHIFTS = len(shifts)


myfile.write("maxTime = %s;\n" % MAXTIME)
myfile.write("numDays = %s;\n" % NUM_DAYS)
myfile.write("numWeeks = %s;\n" % NUM_WEEKS)
myfile.write("shiftDuration = [4,4,4,0];\n")
myfile.write("shiftValue = [1,1,1,0];\n")
myfile.write('shiftName = ["INT","TBP","MON","off"];\n')

def getRandomBoolean():
    return randrange(100) < PERC_AVAILABILITY

def writeList (list, startString, endString):
    temp = []
    myfile.write("%s" % startString)
    for x in list:
        temp.append((",".join(x)))
    myfile.write(",".join(temp))
    myfile.write("%s\n" % endString  )

def shiftFromInt(x):
    return {
        1: 'intermediate',
        2: 'tbp',
        3: 'monitor',
        4: 'off'
    }[x]     

def readCsv(path):
    with open(path, 'r') as f:
        reader = csv.reader(f)
        return list(reader)
    
#numTeachers
numTeachers = []
csv_input = readCsv('inputs/numTeachers.csv')


myfile.write ('numTeachers = %s ;\n'  % csv_input[0][0] )



#calendar

#temp = {}
temp = OrderedDict()
calendar = []

csv_input = readCsv('inputs/calendar.csv')
  
for row in csv_input:
    teacher = row[0]
    temp[teacher] = []
    
for row in csv_input:
    if row[0] in temp.keys():
        if row[2] == "0":    
            temp[row[0]].append("false")
        else:
            temp[row[0]].append("true")
          
   
for teacher in temp: #make list from dict
    calendar.append(temp[teacher])
    
writeList(calendar, "calendar = array2d(TEACHERs, TIME, [", "]);")

#teacherName
teacherName = []

csv_input = readCsv('inputs/teachers.csv')
  
teacherName = []

for row in csv_input:
    teacherName.extend( row )

teacherName = (','.join("\"{0}\"".format(x) for x in teacherName))

myfile.write ("teacherName = array1d(TEACHERs, [" + teacherName + "]);\n")

# dayOfYear     
dayOfYear = []

csv_input = readCsv('inputs/dayofyear.csv')

for row in csv_input:
    dayOfYear.extend( row )

dayOfYearStr = (','.join(dayOfYear))
myfile.write ("dayOfYear =  [" + dayOfYearStr + "];\n")

#inDayOfYear
inDayOfYear = []

for x in dayOfYear:
    for y in range(1, TIME_WITHIN_DAY+1):
       inDayOfYear.append( x)

inDayOfYearStr = ",".join(inDayOfYear)
myfile.write ("inDayOfYear = [" + inDayOfYearStr + "];\n")


#weekOfYear

weekOfYear = []

csv_input = readCsv('inputs/weekofyear.csv')
  

for row in csv_input:
    weekOfYear.extend( row )

weekOfYearStr = (','.join(weekOfYear))
myfile.write ("weekOfYear =  [" + weekOfYearStr + "];\n")

#inWeekOfYear
inWeekOfYear = []

for x in weekOfYear:
    for y in range (1, MAXTIME+1):
        inWeekOfYear.append( x)

inWeekOfYearStr = ",".join(inWeekOfYear)
myfile.write ("inWeekOfYear = [" + inWeekOfYearStr + "];\n")


# timeLabels     
timeLabels = []

csv_input = readCsv('inputs/timelabels.csv')  

for row in csv_input:
    timeLabels.extend( row )

timeLabelsStr = (','.join("\"{0}\"".format(x) for x in timeLabels))

myfile.write ("timeLabels =  [" + timeLabelsStr + "];\n")

#teacherCanDoShift
csv_input = readCsv('inputs/skills.csv') 
  
temp = OrderedDict()
teacherCanDoShift = []

for row in csv_input:
    teacher = row[0]
    temp[teacher] = [] 
for row in csv_input:
    if row[0] in temp.keys():
        if row[2] == "0":    
            temp[row[0]].append("false")
        else:
            temp[row[0]].append("true")

for teacher in temp:
    temp[teacher].append("true")
    teacherCanDoShift.append(temp[teacher])

writeList(teacherCanDoShift,
          "teacherCanDoShift = array2d(TEACHERs, 1..length(SHIFTs), [",
          "]);")

#minNeeded
minNeeded = []

csv_input = readCsv('inputs/minNeeded.csv')

for row in csv_input:
    minNeeded.append(row[2])
for i in range (0, MAXTIME):
    minNeeded.append(str(0)) #0 needed for the "off"shifts

minNeededStr = ",".join(minNeeded)
myfile.write("minNeeded = array2d(SHIFTs, TIME, [" + minNeededStr + ']);\n')

#availability
availability = []
for s in range (0, NUMOFSHIFTS):
    availability.append([s])
    availability[s] = []
    for h in range(0, MAXTIME):
        availability[s].append([h])
        i = 0
        for t in range(0, NUMTEACHERS):
           if calendar[t][h] == "true" and teacherCanDoShift[t][s] == "true":
               i = i+ 1
        if s != NUMOFSHIFTS-1:
            availability[s][h]= str(i)
        else:
            availability[s][h] = str(NUMTEACHERS*2) #the off shift has always max availability

writeList(availability, "availability = array2d(1..length(SHIFTs), TIME, [", "]);")

availabilityCSV = open('availability.csv', 'w')
sname = ''
textStr = 'shift,time,availability\n'
for s in range(0, NUMOFSHIFTS-1):
    if s == 0:
        sname = 'intermediate'
    elif s == 1:
        sname = 'tbp'
    elif s == 2:
        sname = 'monitor'
    for n in range (0, MAXTIME):
        textStr = textStr + "%s,%s,%s\n" % (sname, timeLabels[n], availability[s][n])        
availabilityCSV.write (textStr)        





#previousWeekHours
previousWeekHours=[]

csv_input = readCsv('inputs/previousWeekHours.csv')

for row in csv_input:
    previousWeekHours.append(row[1])

previousWeekHoursStr = ",".join(previousWeekHours)

previousWeekHoursStr = ",".join(previousWeekHours)
myfile.write ("previousWeekHours = array1d(TEACHERs, [" + previousWeekHoursStr + "]);\n")

#lastWorkedHours
lastWorkedHours=[]
csv_input = readCsv('inputs/lastWorkedHours.csv')

for row in csv_input:
    if str(row[2]) == 'LP2 - Classic Intermediate':
        i = 'intermediate'
    elif str(row[2]) == 'LP2 - Classic True Beginner - Portuguese':
        i = 'tbp'
    elif str(row[2]) == 'LP2 - Monitor':
        i = 'monitor'
    else:
        i = 'off'
    
    lastWorkedHours.append(i)

lastWorkedHoursStr = ",".join(lastWorkedHours)
myfile.write ("lastWorkedHours = array2d(TEACHERs, TIME0, [" + lastWorkedHoursStr + "]);\n")
myfile.close()

