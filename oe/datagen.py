from random import randint
import math
myfile = open('datagen.dzn', 'w')
WEEKSINYEAR = 52
DAYSINYEAR = 365
NUMTEACHERS = 5
MAXTIME = 4
NUMOFSHIFTS = 3
TIME_WITHIN_DAY = 48
TIME_WITHIN_WEEK = 336
NUMOFSKILLS = 2
shifts = ["regular", "monitor", "off"]
NUMOFSHIFTS = len(shifts)


myfile.write("maxTime = %s;\n" % MAXTIME)
myfile.write("shiftDuration = [2,1,0];\n")
myfile.write("shiftValue = [1,1,2];\n")
myfile.write("numTeachers = %s;\n" % NUMTEACHERS)
myfile.write('shiftName = ["regular","monitor","off"];\n')
#myfile.write('shiftNeedSkill = array2d(SHIFTs, SKILLs, [true, true, false, false, false, false ]);\n')



#calendar
thelist = []

for x in range (0, NUMTEACHERS):
    for y in range(0, MAXTIME):
        i = randint(0,1)
        if i == 0:
            thelist.append("false")
        else:
            thelist.append("true")

myfile.write("calendar = array2d(TEACHERs, TIME, [")
for item in range(0, len(thelist)):
    if item != len(thelist)-1:
        myfile.write("%s, " %  thelist[item]) 
    else:
        myfile.write("%s ]);\n" % thelist[item])

#teacherName
thelist = []

for x in range (1, NUMTEACHERS+1):
   thelist.append("teacher%s" % x)

myfile.write("teacherName = [")
for item in range(0, len(thelist)):
    if item != len(thelist)-1:
        myfile.write("\"%s\", " % thelist[item])
    else:
        myfile.write("\"%s\" ];\n" % thelist[item])



#minNeeded
thelist = []

for x in range (1, NUMOFSHIFTS+1):
    for y in range(1, MAXTIME+1):
        if x == NUMOFSHIFTS:
            thelist.append(0)
        else:
            thelist.append(1)

myfile.write("minNeeded = array2d(SHIFTs, TIME, [")
for item in range(0, len(thelist)):
    if item != len(thelist)-1:
        myfile.write("%s, " % thelist[item])
    else:
        myfile.write("%s ]);\n" % thelist[item])


#inDayOfYear
thelist = []

for x in range (1, MAXTIME):
    if len(thelist) >= MAXTIME:
           break
    for y in range(1, TIME_WITHIN_DAY+1):
       thelist.append(x)
       if len(thelist) >= MAXTIME:
           break

myfile.write("inDayOfYear = [")
for item in range(0, len(thelist)):
    if item != len(thelist)-1:
        myfile.write("%s, " % thelist[item])
    else:
        myfile.write("%s ];\n" % thelist[item])

#dayOfYear
i = max(thelist) #takes max value from inDayOfYear
thelist = []

for x in range (0, i+1):
    thelist.append(x)

myfile.write("dayOfYear = [")
for item in range(1, len(thelist)):
    if item != len(thelist)-1:
        myfile.write("%s, " % thelist[item])
    else:
        myfile.write("%s ];\n" % thelist[item])

#inWeekOfYear
thelist = []
for x in range (1, MAXTIME):
    if len(thelist) >= MAXTIME:
           break
    for y in range(1, TIME_WITHIN_WEEK+1):
       thelist.append(x)
       if len(thelist) >= MAXTIME:
           break

myfile.write("inWeekOfYear = [")
for item in range(0, len(thelist)):
    if item != len(thelist)-1:
        myfile.write("%s, " % thelist[item])
    else:
        myfile.write("%s ];\n" % thelist[item])

#weekOfYear
i = max(thelist) #takes max value from inWeekOfYear
thelist = []

for x in range (0, i+1):
    thelist.append(x)

myfile.write("weekOfYear = [")
for item in range(1, len(thelist)):
    if item != len(thelist)-1:
        myfile.write("%s, " % thelist[item])
    else:
        myfile.write("%s ];\n" % thelist[item])
        

#teacherCanDoShift
thelist = []

for x in range (0, NUMTEACHERS):
    for y in range(0, NUMOFSHIFTS):
        if y == NUMOFSHIFTS-1:
            i = 1
        else:
            i = randint(0,1)
        if i == 1:
            thelist.append("true")
        else:
            thelist.append("false")
            
 

myfile.write("teacherCanDoShift = array2d(TEACHERs, 1..length(SHIFTs), [")
for item in range(0, len(thelist)):
    if item != len(thelist)-1:
        myfile.write("%s, " %  thelist[item]) 
    else:
        myfile.write("%s ]);\n" % thelist[item])
        
myfile.close()

