include "global_cardinality_low_up.mzn";
include "regular.mzn";
% teachers
int: numTeachers;
set of int: TEACHERs = 1..numTeachers; 
array[TEACHERs] of string: teacherName;
% time
int: maxTime;
set of int: TIME = 1..maxTime;
array[TIME] of int: inDayOfYear;
array[1.. max(inDayOfYear)] of int: dayOfYear;
array[TIME] of int: inWeekOfYear;
array[1..max(inWeekOfYear)] of int: weekOfYear;
% shifts
enum SHIFT = {regular, monitor, off};
set of int: SHIFTs = 1..card(SHIFT);
array[SHIFT] of string: shiftName;

%skill
array[TEACHERs, 1..length(SHIFTs)] of bool: teacherCanDoShift;

array[TEACHERs, TIME] of bool: calendar;
array[SHIFTs, TIME] of int: minNeeded;

array[SHIFT] of int: shiftDuration;
array[SHIFT] of int: shiftValue;

array[TEACHERs, TIME] of var SHIFT: roster;


% min_needed quantity
constraint forall(h in TIME) ( global_cardinality_low_up([roster[t, h] | t in TEACHERs], [regular, monitor, off] , [minNeeded[regular,h], minNeeded[monitor,h], 0],  [numTeachers, numTeachers, numTeachers] ) );


%non overlap
constraint forall (t in TEACHERs, h in 2..length(TIME)) (roster[t, h] in {regular,monitor} 
-> h+1 >= h + shiftDuration[roster[t, h-1]] );

%no more than 2 shifts in a row
constraint forall (t in TEACHERs, h in 1..length(TIME)-2) (roster[t, h] in {regular,monitor} /\ roster[t, h+1] in {regular,monitor} -> roster[t, h+2] = off);

%constraint forall(t in TEACHERs) (regular([roster[t, h] | h in TIME ], 4, 3, transition_array, 1, {2,3,4}));
%array[1..4, SHIFTs] of 0..4: transition_array = [| 2, 3, 4, 
%                                                 | 0, 3, 4,
%                                                 | 2, 0, 4,
%                                                 | 2, 3, 4 |];
                                                



%max hours by day/week
constraint forall(t in TEACHERs, h in dayOfYear) (sum([shiftDuration[roster[t, i]] | i in TIME where inDayOfYear[i] = h])  <= 8 );
constraint forall(t in TEACHERs, h in weekOfYear) (sum([shiftDuration[roster[t, i]] | i in TIME where inWeekOfYear[i] = h])  <= 26 );

%calendar availability
constraint forall(t in TEACHERs, h in TIME) (calendar[t,h] = false -> roster[t,h] = off);
%skills
constraint forall(t in TEACHERs, h in TIME, s in SHIFTs) (teacherCanDoShift[t, s] = false -> roster[t,h] != s );




var int: obj;
constraint obj = sum([shiftValue[roster[t,h]] | t in TEACHERs, h in TIME]);
constraint obj >= 0;

solve maximize obj;


output ["TIME \t"] ++ ["\(TIME[i]) \t" | i in TIME] ++ ["\n"]  ++
      [ if j==1 then teacherName[i] ++ "\t" else "" endif  ++ shiftName[fix(roster[i,j])] ++  if j==maxTime then "\n" else "\t" endif
       | i in TEACHERs, j in TIME ]++ ["\nobj: \(obj) \nnumTeachers: \(numTeachers)   "];
