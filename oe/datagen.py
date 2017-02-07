from random import randint
import math
myfile = open('datagen.dzn', 'w')
WEEKSINYEAR = 52
DAYSINYEAR = 365
NUMTEACHERS = 9
MAXTIME = 4

TIME_WITHIN_DAY = 48
TIME_WITHIN_WEEK = 336
NUMOFSKILLS = 2
shifts = ["intermediate", "tbp","monitor", "off"]
NUMOFSHIFTS = len(shifts)


myfile.write("maxTime = %s;\n" % MAXTIME)
myfile.write("shiftDuration = [2,2,2,0];\n")
myfile.write("shiftValue = [1,1,1,0];\n")
myfile.write("numTeachers = %s;\n" % NUMTEACHERS)
myfile.write('shiftName = ["Intermediate","TBP","Monitor","off"];\n')


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


#minNeeded
thelist = []

for x in range (1, NUMOFSHIFTS+1):
    for y in range(1, MAXTIME+1):
        if x == NUMOFSHIFTS:
            thelist.append(0)
        else:
            thelist.append(1)

myfile.write("minNeeded = array2d(SHIFTs, TIME, [")
#for item in range(0, len(thelist)):
#    if item != len(thelist)-1:
#        myfile.write("%s, " % thelist[item])
#    else:
#       myfile.write("%s ]);\n" % thelist[item])
temp = """2,2,3,2,2,2,3,2,2,2,3,2,4,7,5,3,6,11,7,6,7,12,13,7,7,13,12,4,10,17,15,5,14,22,2,2,3,2,2,2,3,2,2,2,4,4,7,2,5,10,12,3,5,11,16,3,5,11,18,5,3,11,19,8,7,14,22,9,2,2,3,2,2,2,3,2,2,2,4,4,2,8,9,4,6,11,7,6,7,10,10,9,8,14,10,5,12,18,10,5,16,21,2,2,3,2,2,2,3,2,2,2,3,2,7,6,5,3,8,11,7,5,10,10,12,7,8,12,11,4,10,16,11,6,12,19,2,2,3,2,2,2,3,2,2,2,3,4,2,4,7,7,7,4,7,12,8,4,9,14,8,2,9,14,10,4,9,14,11,5,22,16,17,25,21,14,29,21,11,9,13,12,13,17,6,14,14,29,22,8,15,29,14,11,13,22,13,18,23,14,15,6,12,14,8,5,3,3,3,10,10,11,10,8,10,10,9,14,9,16,9,15,7,3,3,3,6,8,7,11,7,15,6,13,10,12,10,10,20,9,11,3,5,26,7,5,5,14,9,6,9,5,8,8,4,7,12,13,20,5,6,5,5,5,15,22,15,10,5,5,19,5,17,5,11,14,5,12,14,5,8,10,2,5,2,2,2,2,2,2,2,2,2,6,4,3,4,5,5,5,5,9,9,9,10,8,9,8,9,3,9,2,2,2,2,2,2,2,2,2,3,7,4,10,11,8,9,9,7,11,9,16,11,13,2,7,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,2,2,1,1,2,2,2,2,2,2,1,2,2,1,1,2,2,1,1,1,2,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,2,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,1,3,1,3,1,4,2,2,2,2,2,1,2,1,1,2,3,1,3,2,2,2,2,2,2,1,1,3,2,4,4,2,2,2,2,2,2,1,1,2,1,1,4,4,2,2,2,2,2,2,1,1,2,2,3,1,3,2,4,5,4,2,1,2,2,4,1,1,4,1,1,4,5,1,3,3,1,1,1,1,2,1,2,1,1,1,1,2,1,1,3,4,4,2,1,1,3,3,1,1,1,2,2,2,2,2,2,2,2,3,4,4,4,2,2,2,2,2,1,1,1,1,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
"""
#remember that the corresponding off minNeeded are ignored by the global_card constraint
temp = temp.split(",")
#temp2 = ",".join(temp)

myfile.write(",".join(temp[0:MAXTIME*NUMOFSHIFTS]))
#myfile.write("""2,2,3,2,2,2,3,2,2,2,3,2,0,0,0,0
#""")
myfile.write ("]);\n")


        
myfile.close()

