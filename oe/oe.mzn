include "global_cardinality_low_up.mzn";
%teachers
int: numTeachers;
set of int: TEACHERs = 1..numTeachers; 
array[TEACHERs] of string: teacherName;
%time
int: maxTime;
set of int: TIME = 1..maxTime;
%shifts
enum SHIFT = {regular, monitor, off};
set of int: SHIFTs = 1..card(SHIFT);
array[SHIFT] of string: shiftName;

array[TEACHERs, TIME] of bool: calendar;
array[SHIFTs, TIME] of int: minNeeded;

array[SHIFT] of int: shiftDuration;
array[SHIFT] of int: shiftValue;

array[TEACHERs, TIME] of var SHIFT: roster;


%the 4 constraint below are for the min_needed quantity
constraint forall(h in TIME) ( global_cardinality_low_up([roster[t, h] | t in TEACHERs], [regular, monitor] , [minNeeded[regular,h], minNeeded[monitor,h]],  [numTeachers, numTeachers] ) );


%non overlap
constraint forall (t in TEACHERs, h in 2..length(TIME)) (roster[t, h] != off 
-> h+1 >= h + shiftDuration[roster[t, h-1]] );

%no more than 2 shifts in a row
constraint forall (t in TEACHERs, h in 1..length(TIME)-2) (roster[t, h] != off /\ roster[t, h+1] != off -> roster[t, h+2] = off);


var int: obj;
constraint obj = sum([shiftValue[roster[t,h]] | t in TEACHERs, h in TIME]);

solve maximize obj ;


output ["TIME \t"] ++ ["\(TIME[i]) \t" | i in TIME] ++ ["\n"]  ++
      [ if j==1 then teacherName[i] ++ "\t" else "" endif  ++ shiftName[fix(roster[i,j])] ++  if j==maxTime then "\n" else "\t" endif
       | i in TEACHERs, j in TIME ]++ ["\nobj: \(obj) \nnumTeachers: \(numTeachers) \nteacherName:\(teacherName) \ncard TEACHERs:\(card(TEACHERs)) "];
