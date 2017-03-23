from random import randint,randrange,choice
import csv
import math
myfile = open('datagen.dzn', 'w')
WEEKSINYEAR = 52
DAYSINYEAR = 365
NUMTEACHERS = 1
MAXTIME = 336
TIME0 = 4
PERC_AVAILABILITY= 100

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
myfile.write("numTeachers = %s;\n" % NUMTEACHERS)
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
        3: 'monitor'
    }[x]     

#calendar
calendar = []

for t in range (0, NUMTEACHERS):
    calendar.append([t])
    calendar[t] = []
    for h in range(0, MAXTIME):
        i = getRandomBoolean()
        if i == 0:
            #calendar[t].append("true")
            calendar[t].append("false")
        else:
            calendar[t].append("true")
            

writeList(calendar, "calendar = array2d(TEACHERs, TIME, [", "]);")

#teacherName
teacherName = []

for t in range (0, NUMTEACHERS):
    teacherName.append([t])
    teacherName[t] = []
    teacherName[t].append("\"teacher%s\"" % t)
    
writeList(teacherName, "teacherName = [", "];")
     
##
###inDayOfYear
##inDayOfYear = []
##
##for x in range (1, MAXTIME):
##    if len(inDayOfYear) >= MAXTIME:
##           break
##    for y in range(1, TIME_WITHIN_DAY+1):
##       inDayOfYear.append(x)
##       if len(inDayOfYear) >= MAXTIME:
##           break
##
##myfile.write("inDayOfYear = [")
##for item in range(0, len(inDayOfYear)):
##    if item != len(inDayOfYear)-1:
##        myfile.write("%s, " % inDayOfYear[item])
##    else:
##        myfile.write("%s ];\n" % inDayOfYear[item])
##
###dayOfYear
##i = max(inDayOfYear) #takes max value from inDayOfYear
##dayOfYear = []
##
##for x in range (0, i+1):
##    dayOfYear.append(x)
##
##myfile.write("dayOfYear = [")
##for item in range(1, len(dayOfYear)):
##    if item != len(dayOfYear)-1:
##        myfile.write("%s, " % dayOfYear[item])
##    else:
##        myfile.write("%s ];\n" % dayOfYear[item])
##
###inWeekOfYear
##inWeekOfYear = []
##for x in range (1, MAXTIME):
##    if len(inWeekOfYear) >= MAXTIME:
##           break
##    for y in range(1, TIME_WITHIN_WEEK+1):
##       inWeekOfYear.append(x)
##       if len(inWeekOfYear) >= MAXTIME:
##           break
##
##myfile.write("inWeekOfYear = [")
##for item in range(0, len(inWeekOfYear)):
##    if item != len(inWeekOfYear)-1:
##        myfile.write("%s, " % inWeekOfYear[item])
##    else:
##        myfile.write("%s ];\n" % inWeekOfYear[item])
##
###weekOfYear
##i = max(inWeekOfYear) #takes max value from inWeekOfYear
##weekOfYear = []
##
##for x in range (0, i+1):
##    weekOfYear.append(x)
##
##myfile.write("weekOfYear = [")
##for item in range(1, len(weekOfYear)):
##    if item != len(weekOfYear)-1:
##        myfile.write("%s, " % weekOfYear[item])
##    else:
##        myfile.write("%s ];\n" % weekOfYear[item])


# timeLabels     
timeLabels = []

  

for i in range (1, MAXTIME+1):
    timeLabels.append( str(i) )


timeLabelsStr = (','.join("\"{0}\"".format(x) for x in timeLabels))

myfile.write ("timeLabels =  [" + timeLabelsStr + "];\n")


#teacherCanDoShift
teacherCanDoShift = []

for t in range (0, NUMTEACHERS):
    teacherCanDoShift.append([t])
    teacherCanDoShift[t] = []
    for s in range(0, NUMOFSHIFTS):
        if s == NUMOFSHIFTS-1:
            i = 1
        else:
            i = getRandomBoolean()
        if i == 1:
            teacherCanDoShift[t].append("true")
        else:
            #teacherCanDoShift[t].append("true")
            teacherCanDoShift[t].append("false")
            
writeList(teacherCanDoShift,
          "teacherCanDoShift = array2d(TEACHERs, 1..length(SHIFTs), [",
          "]);")


#minNeeded
minNeeded = []

myfile.write("minNeeded = array2d(SHIFTs, TIME, [")
temp = """2,2,3,2,2,2,3,2,2,2,3,2,4,7,5,3,6,11,7,6,7,12,13,7,7,13,12,4,10,17,15,5,14,22,2,2,3,2,2,2,3,2,2,2,4,4,7,2,5,10,12,3,5,11,16,3,5,11,18,5,3,11,19,8,7,14,22,9,2,2,3,2,2,2,3,2,2,2,4,4,2,8,9,4,6,11,7,6,7,10,10,9,8,14,10,5,12,18,10,5,16,21,2,2,3,2,2,2,3,2,2,2,3,2,7,6,5,3,8,11,7,5,10,10,12,7,8,12,11,4,10,16,11,6,12,19,2,2,3,2,2,2,3,2,2,2,3,4,2,4,7,7,7,4,7,12,8,4,9,14,8,2,9,14,10,4,9,14,11,5,22,16,17,25,21,14,29,21,11,9,13,12,13,17,6,14,14,29,22,8,15,29,14,11,13,22,13,18,23,14,15,6,12,14,8,5,3,3,3,10,10,11,10,8,10,10,9,14,9,16,9,15,7,3,3,3,6,8,7,11,7,15,6,13,10,12,10,10,20,9,11,3,5,26,7,5,5,14,9,6,9,5,8,8,4,7,12,13,20,5,6,5,5,5,15,22,15,10,5,5,19,5,17,5,11,14,5,12,14,5,8,10,2,5,2,2,2,2,2,2,2,2,2,6,4,3,4,5,5,5,5,9,9,9,10,8,9,8,9,3,9,2,2,2,2,2,2,2,2,2,3,7,4,10,11,8,9,9,7,11,9,16,11,13,2,7,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,2,2,1,1,2,2,2,2,2,2,1,2,2,1,1,2,2,1,1,1,2,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,2,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,1,3,1,3,1,4,2,2,2,2,2,1,2,1,1,2,3,1,3,2,2,2,2,2,2,1,1,3,2,4,4,2,2,2,2,2,2,1,1,2,1,1,4,4,2,2,2,2,2,2,1,1,2,2,3,1,3,2,4,5,4,2,1,2,2,4,1,1,4,1,1,4,5,1,3,3,1,1,1,1,2,1,2,1,1,1,1,2,1,1,3,4,4,2,1,1,3,3,1,1,1,2,2,2,2,2,2,2,2,3,4,4,4,2,2,2,2,2,1,1,1,1,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
"""
#remember that the corresponding off minNeeded are ignored by the global_card constraint
temp = temp.split(",")

myfile.write(",".join(temp[0:MAXTIME*NUMOFSHIFTS]))
myfile.write ("]);\n")

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
            availability[s][h]= str(-i)
        else:
            availability[s][h] = str(-NUMTEACHERS*2) #the off shift has always max availability

writeList(availability, "values = array2d(1..length(SHIFTs), TIME, [", "]);")


#previousWeekHours
previousWeekHours=[]

for t in range(0, NUMTEACHERS):
    previousWeekHours.append([t])
    i = choice([4,8,12,16,20,24,28])    
    previousWeekHours[t] = str(i)
    
temp = ",".join(previousWeekHours)
myfile.write ("previousWeekHours = array1d(TEACHERs, [" + temp + "]);\n")

#lastWorkedHours
lastWorkedHours=[]

for t in range (0, NUMTEACHERS):
    lastWorkedHours.append([t])
    lastWorkedHours[t] = []
    shift = shiftFromInt(randint(1,3))
    pos = randint(0,4)
    for h in range(0, TIME0):
        if h == pos:
            lastWorkedHours[t].append(shift)
        else:
            lastWorkedHours[t].append("off")
            

writeList(lastWorkedHours, "lastWorkedHours = array2d(TEACHERs, TIME0, [", "]);")

myfile.close()

