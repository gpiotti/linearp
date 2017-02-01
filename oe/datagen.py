from random import randint
import math
myfile = open('datagen.dzn', 'w')
WEEKSINYEAR = 52
DAYSINYEAR = 365
NUMTEACHERS = 500
MAXTIME = 336
NUMOFSHIFTS = 3
TIME_WITHIN_DAY = 24
TIME_WITHIN_WEEK = 336

myfile.write("maxTime = %s;\n" % MAXTIME)
myfile.write("shiftDuration = [2,1,0];\n")
myfile.write("shiftValue = [1,1,2];\n")
myfile.write("numTeachers = %s;\n" % NUMTEACHERS)
myfile.write('shiftName = ["regular","monitor","off"];\n')



        
#dayOfYear
thelist = []

for x in range (0, DAYSINYEAR+1):
    thelist.append(x)

myfile.write("dayOfYear = [")
for item in range(1, len(thelist)):
    if item != len(thelist)-1:
        myfile.write("%s, " % thelist[item])
    else:
        myfile.write("%s ];\n" % thelist[item])

#weekOfYear
thelist = []

for x in range (0, WEEKSINYEAR+1):
    thelist.append(x)

myfile.write("weekOfYear = [")
for item in range(1, len(thelist)):
    if item != len(thelist)-1:
        myfile.write("%s, " % thelist[item])
    else:
        myfile.write("%s ];\n" % thelist[item])


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
    for x in range(1, MAXTIME+1):
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

        
myfile.close()

