include "global_cardinality_low_up.mzn";
enum TEACHER = {teacher1, teacher2, teacher3};
enum SHIFT = {regular, monitor};
int: maxtime;
%int: numShifts;
%int: numTeachers;
%set of TEACHER: teacher;
%set of int: SHIFT;
set of int: TIME = 1..maxtime;
array[TEACHER, TIME] of bool: calendar;
array[SHIFT, TIME] of int: minNeeded;
array[SHIFT, TIME] of int: maxNeeded;


array[SHIFT] of int: shiftDuration;

array[SHIFT] of string: shiftName;
array[TEACHER] of string: teacherName;

array[TEACHER, TIME] of var SHIFT: roster;

array[SHIFT, TIME] of var SHIFT: onShift; 

constraint forall (h in TIME) (global_cardinality_low_up([roster[t, h] | t in TEACHER], [SHIFT[i] | i in SHIFT],[minNeeded[s,h] | s in SHIFT], [maxNeeded[s,h] | s in SHIFT]));

solve satisfy;

output ["TIME \t"] ++ ["\(TIME[i]) \t" | i in TIME] ++ ["\n"]  ++
      [ if j==1 then teacherName[i] ++ "\t" else "" endif  ++ shiftName[fix(roster[i,j])] ++  if j==maxtime then "\n" else "\t" endif
       | i in TEACHER, j in TIME ];
