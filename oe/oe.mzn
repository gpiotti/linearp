include "global_cardinality_low_up.mzn";
include "global_cardinality.mzn";
include "regular.mzn";
include "sliding_sum.mzn";

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
enum SHIFT = {intermediate,tbp,monitor,off};
set of int: SHIFTs = 1..card(SHIFT);
array[SHIFT] of string: shiftName;

%skill
array[TEACHERs, 1..length(SHIFTs)] of bool: teacherCanDoShift;

array[TEACHERs, TIME] of bool: calendar;
array[SHIFTs, TIME] of int: minNeeded;
array[SHIFTs, TIME] of int: availability;

array[SHIFT] of int: shiftDuration;
array[SHIFT] of int: shiftValue;

array[TEACHERs, TIME] of var SHIFT: roster;


% min_needed quantity
constraint forall(h in TIME) ( global_cardinality_low_up([roster[t, h] | t in TEACHERs], [intermediate, tbp, monitor, off], [0, 0, 0, 0], [ minNeeded[intermediate,h], minNeeded[tbp,h],  minNeeded[monitor,h], numTeachers ] ) );

%other way of soft constraint -- also add "- obj2 " in the objective function 
%array[1..3, TIME] of var 0..numTeachers: count ;
%array[1..3, TIME] of int: l = array2d(1..3, TIME, [1,0,0,0, 0,0,0,0, 0,0,0,0]);
%array[1..3, TIME] of int: u = array2d(1..3, TIME, [2,0,0,0, 0,0,0,0, 0,0,0,0]);
 %soft_global_cardinality_low_up(x, cover, l, u)
%constraint forall(h in TIME) (global_cardinality([roster[t, h] | t in TEACHERs], [intermediate, tbp, monitor], [count[s,h] | s in 1..3] ));
%var int: obj2 = sum( h in TIME, i in index_set( [intermediate, tbp, monitor]))
%                  (max([count[i,h] - u[i,h], l[i,h] - count[i,h], 0])*2); 


%non overlap
%constraint forall (t in TEACHERs, h in 2..length(TIME)) (roster[t, h] in {intermediate, tbp, monitor} 
%->  h+1  >= h + shiftDuration[roster[t, h-1]]);

constraint forall (t in TEACHERs, h in 1..length(TIME)) (roster[t, h] in {intermediate, tbp, monitor} 
-> not exists(k in h+1..length(TIME)) ( k < h + shiftDuration[roster[t,h]] /\ roster[t,k] in {intermediate,tbp,monitor} ));

%no more than 2 shifts in a row
%constraint forall (t in TEACHERs, h in 1..length(TIME)-2) (roster[t, h] in {intermediate,tbp,monitor} /\ roster[t, h+shiftDuration[roster[t,h]]-1] in {intermediate,tbp,monitor} ->  h+shiftDuration[roster[t,h]]+1 = off);

constraint forall(t in TEACHERs, h in TIME) (sliding_sum(0,8,8,[shiftDuration[ roster[t,i]] | i in TIME where i in h..h+8]))  ;

%max hours by day/week
%constraint forall(t in TEACHERs, h in dayOfYear) (sum([ shiftDuration[roster[t, i]] | i in TIME where inDayOfYear[i] = h])  <= 8 );
%constraint forall(t in TEACHERs, h in weekOfYear) (sum([shiftDuration[roster[t, i]] | i in TIME where inWeekOfYear[i] = h])  <= 52 );

constraint forall(t in TEACHERs) ( sliding_sum(0, 16, 48, [ shiftDuration[roster[t, i] ] | i in TIME ] ));
constraint forall(t in TEACHERs) ( sliding_sum(0, 52, 336, [ shiftDuration[roster[t, i] ] | i in TIME ] ));


%constraint forall (s in SHIFTs, h in TIME) (minNeeded[s,h] = 0 -> forall(t in TEACHERs)(roster[t,h] = off));

%calendar availability
constraint forall(t in TEACHERs, h in TIME) (calendar[t,h] = false -> roster[t,h] = off);
%skills
constraint forall(t in TEACHERs, h in TIME, s in SHIFTs) (teacherCanDoShift[t, s] = false -> roster[t,h] != s );

var int: obj;
constraint obj = sum([ ( - availability[roster[t,h],h]   ) | t in TEACHERs, h in TIME ]);

%solve maximize obj;

solve :: int_search (
        [ roster[t,h] | t in TEACHERs, h in TIME]
        % ++ [stat[j,t] | j in 1..num_days, t in 1..3]
        , 
        first_fail, 
        %anti_first_fail, 
        indomain_split,
        complete) 
    maximize obj;

output ["TIME \t"] ++ ["\(TIME[i]) \t" | i in TIME] ++ ["\n"]  ++
      [ if j==1 then teacherName[i] ++ "\t" else "" endif  ++ shiftName[fix(roster[i,j])] ++  if j==maxTime then "\n" else "\t" endif
       | i in TEACHERs, j in TIME ]++ ["\nobj: \(obj) \nnumTeachers: \(numTeachers) "];
