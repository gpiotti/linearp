include "global_cardinality.mzn";

set of int: TEACHERs = {i | i in 1..numTeachers };
set of int: SHIFTs = 1..card(SHIFT);
enum SHIFT = {regular, monitor, off};
int: maxTime;
int: numTeachers;

set of int: TIME = 1..maxTime;
array[TEACHERs, TIME] of bool: calendar;
array[SHIFTs, TIME] of int: minNeeded;


array[SHIFT] of int: shiftDuration;
array[SHIFT] of int: shiftValue;

array[SHIFT] of string: shiftName;
array[TEACHERs] of string: teacherName;

array[TEACHERs, TIME] of var SHIFT: roster;

array[TIME] of var int: onRegular;
array[TIME] of var int: onMonitor;
%array[TIME] of var int: offShift;


%the 4 constraint below are for the min_needed quantity
%constraint forall(h in TIME) ( global_cardinality([roster[t, h] | t in TEACHERs], [i | i in SHIFT ],  [i | i in shiftQ[h]] ));
%[onRegular[h], onMonitor[h]]
constraint forall(h in TIME) (onRegular[h] <= minNeeded[regular,h]);
constraint forall(h in TIME) (onMonitor[h] <= minNeeded[monitor,h]);
%constraint forall(h in TIME) (offShift[h] <= minNeeded[off,h]);

%non overlap
constraint forall (t in TEACHERs, h in 2..length(TIME)) (roster[t, h] != off 
-> h+1 >= h + shiftDuration[roster[t, h-1]] );

array[SHIFTs, TIME] of var int: shiftSum;
constraint forall (h in TIME, s in SHIFTs, t in TEACHERs) (card(roster[t,h]) < minNeeded[roster[t,h]]);  

%no more than 2 shifts in a row
constraint forall (t in TEACHERs, h in 1..length(TIME)-2) (roster[t, h] != off /\ roster[t, h+1] != off -> roster[t, h+2] = off);


var int: obj;
constraint obj = sum([shiftValue[roster[t,h]] | t in TEACHERs, h in TIME  ]);

solve maximize  obj ;


output ["TIME \t"] ++ ["\(TIME[i]) \t" | i in TIME] ++ ["\n"]  ++
      [ if j==1 then teacherName[i] ++ "\t" else "" endif  ++ shiftName[fix(roster[i,j])] ++  if j==maxTime then "\n" else "\t" endif
       | i in TEACHERs, j in TIME ]++ ["\nobj: \(obj) \nnumTeachers: \(numTeachers) \nteacherName:\(teacherName) \ncard TEACHER:\(card(TEACHERs)) "];
