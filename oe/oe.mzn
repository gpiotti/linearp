include "global_cardinality_low_up.mzn";
%include "global_cardinality.mzn";
%include "regular.mzn";
include "sliding_sum.mzn";
%include "disjunctive.mzn";
include "diffn_nonstrict.mzn";

array[TIME] of string: timeLabels;

% teachers
int: numTeachers;
set of int: TEACHERs = 1..numTeachers; 
array[TEACHERs] of string: teacherName;
% time
int: maxTime;
int: numDays;
int: numWeeks;
set of int: TIME = 1..maxTime;
set of int: TIME0 = 1..max(shiftDuration);

% shifts
enum SHIFT = {intermediate,tbp,monitor,off};
set of int: SHIFTs = 1..card(SHIFT);
array[SHIFT] of string: shiftName;

%skill
array[TEACHERs, 1..length(SHIFTs)] of bool: teacherCanDoShift;

array[TEACHERs, TIME] of bool: calendar;
array[SHIFTs, TIME] of int: minNeeded;
array[SHIFTs, TIME] of int: values;

array[SHIFT] of int: shiftDuration;
array[SHIFT] of int: shiftValue;

array[TEACHERs, TIME] of var SHIFT: roster;
array[TEACHERs, TIME0] of SHIFT: lastWorkedHours;
array[TEACHERs] of 0..52: previousWeekHours;

array[TEACHERs] of var 0..52: stats;

 
constraint forall(t in TEACHERs) (stats[t] = sum([shiftDuration[roster[t,h]] | h in TIME] ));
constraint forall(t in TEACHERs) (previousWeekHours[t] + stats[t] <= 52) ;


% min_needed quantity
constraint forall(h in TIME) ( global_cardinality_low_up([roster[t, h] | t in TEACHERs], [intermediate, tbp, monitor, off], [0, 0, 0, 0], [ minNeeded[intermediate,h], minNeeded[tbp,h],  minNeeded[monitor,h], numTeachers] ) );

%other way of soft constraint -- also add "- obj2 " in the objective function 
%array[1..3, TIME] of var 0..numTeachers: count ;
%array[1..3, TIME] of int: l = array2d(1..3, TIME, [1,0,0,0, 0,0,0,0, 0,0,0,0]);
%array[1..3, TIME] of int: u = array2d(1..3, TIME, [2,0,0,0, 0,0,0,0, 0,0,0,0]);
 %soft_global_cardinality_low_up(x, cover, l, u)
%constraint forall(h in TIME) (global_cardinality([roster[t, h] | t in TEACHERs], [intermediate, tbp, monitor], [count[s,h] | s in 1..3] ));
%var int: obj2 = sum( h in TIME, i in index_set( [intermediate, tbp, monitor]))
%                  (max([count[i,h] - minNeeded[i,h], minNeeded[i,h] - count[i,h], 0])*2); 


%non overlap
%constraint forall (t in TEACHERs, h in 2..length(TIME)) (roster[t, h] in {intermediate, tbp, monitor} 
%->  h+1  >= h + shiftDuration[roster[t, h-1]]);

%constraint forall (t in TEACHERs, h in 1..length(TIME)) (roster[t, h] != off
%-> not exists(k in h+1..length(TIME) ) ( k < h + shiftDuration[roster[t,h]] /\ roster[t,k] != off ));

%constraint  forall (t in TEACHERs, h in 1..length(TIME)-4)  ( roster[t, h] != off -> forall(k in h+1..h+4 ) (roster[t,k] = off));
%constraint  forall (t in TEACHERs, h in 1..length(TIME)-4)  ( roster[t, h] = intermediate -> forall(k in h+1..h+4 ) (roster[t,k] = off));
%constraint  forall (t in TEACHERs, h in 1..length(TIME)-4)  ( roster[t, h] = tbp -> forall(k in h+1..h+4 ) (roster[t,k] = off));
%constraint  forall (t in TEACHERs, h in 1..length(TIME)-4)  ( roster[t, h] = monitor -> forall(k in h+1..h+4 ) (roster[t,k] = off));

%constraint   forall ( t in TEACHERs) (disjunctive([h | h in TIME], [ 1 | h in TIME ])) ;               

%no more than 2 shifts in a row
%constraint forall (t in TEACHERs, h in 1..length(TIME)-2) (roster[t, h] in {intermediate,tbp,monitor} /\ roster[t, h+shiftDuration[roster[t,h]]-1] in {intermediate,tbp,monitor} ->  h+shiftDuration[roster[t,h]]+1 = off);


constraint forall(t in TEACHERs, h in 1..length(TIME)-9) 
(sliding_sum(0,8,9,
[ shiftDuration[lastWorkedHours[t,i]] | i in TIME0 where h = 1 ] ++ [shiftDuration[ roster[t,j]] | j in h..h+9]  ));

constraint forall(t in TEACHERs, h in 1..length(TIME)-4) 
(sliding_sum(0,4,4,
[ shiftDuration[lastWorkedHours[t,i]] | i in TIME0 where h = 1 ] ++ [shiftDuration[ roster[t,j]] | j in h..h+4]  ));

%constraint diffn_nonstrict([h | t in TEACHERs, h in 1..length(TIME)],
%  [t | t in TEACHERs, h in 1..length(TIME)],
%  [if roster[t, h] = off then 0 else 5 endif | t in TEACHERs, h in 1..length(TIME)],
%  [if roster[t, h] = off then 0 else 1 endif | t in TEACHERs, h in 1..length(TIME)]);
  

%constraint forall(t in TEACHERs, h in TIME) 
%(sliding_sum(0,8,9,
%[ shiftDuration[roster0[t,i]] | i in TIME0 ] ++ [shiftDuration[ roster[t,j]] | j in TIME]  ));

%constraint forall(t in TEACHERs, h in TIME)
%(sliding_sum(0,4,4,
%[ shiftDuration[roster0[t,i]] | i in TIME0 ] ++ [shiftDuration[ roster[t,j]] | j in TIME]  ));

%no more than 2 shifts in a row
%constraint forall(t in TEACHERs, h in 1..length(TIME)-9) (sliding_sum(0,8,9,[ shiftDuration[roster0[t,i]] | i in TIME where i = h ] ++ [shiftDuration[ roster[t,j]] | j in TIME where j in h..h+9]  ))  ;
%non overlap (assumed every shift is 2 hours -> duration of 4)
%constraint forall(t in TEACHERs, h in 1..length(TIME)-4) (sliding_sum(0,4,4,[ shiftDuration[roster0[t,i]] | i in TIME0 where i = h] ++ [shiftDuration[ roster[t,j]] | j in TIME where j in h..h+4]))  ;

%max hours by day/week
%constraint forall(t in TEACHERs, h in dayOfYear) (sum([ shiftDuration[roster[t, i]] | i in TIME where inDayOfYear[i] = h])  <= 16 );
%constraint forall(t in TEACHERs, h in weekOfYear) (sum([shiftDuration[roster[t, i]] | i in TIME where inWeekOfYear[i] = h])  <= 52 );

constraint forall(t in TEACHERs) ( sliding_sum(0, 16, if 48 >= length(TIME) then length(TIME) else 48 endif , [ shiftDuration[roster[t, i] ] | i in TIME] ));
%constraint forall(t in TEACHERs) ( sliding_sum(0, 52, 336+1 , [previousWeekHours[t]] ++ [ shiftDuration[roster[t, i] ] | i in TIME ]  )); %+1 is for the previousWeekHours

%if not needed -> force off 
%constraint forall (s in SHIFTs, h in TIME where s != off)  (minNeeded[s,h] = 0 -> forall(t in TEACHERs)(roster[t,h] != s));

%calendar values
constraint forall(t in TEACHERs, h in TIME) (calendar[t,h] = false -> roster[t,h] = off);

%skills
constraint forall(t in TEACHERs, h in TIME, s in SHIFTs where teacherCanDoShift[t, s] = false) (roster[t,h] != s );

var int: obj;
constraint obj = sum([ (  values[roster[t,h],h]   ) | t in TEACHERs, h in TIME] );
%constraint obj = sum([ ( shiftDuration[roster[t,h]]   ) | t in TEACHERs, h in TIME ]);





%solve maximize obj;

solve :: int_search (
        [ roster[t,h] | t in TEACHERs, h in TIME]
        % ++ [stat[j,t] | j in 1..num_days, t in 1..3]
        , 
        smallest, 
        %anti_first_fail, 
        indomain_reverse_split,
        complete) 
    maximize obj;

%output ["\(timeLabels[i]);" | i in TIME] ++ ["\n"]  ++
%      [ if j==1 then teacherName[i] ++ ";" else "" endif  ++ shiftName[fix(roster[i,j])] ++  if j==maxTime then "\n" else ";" endif
%       | i in TEACHERs, j in TIME ] ++ ["\nTIME0\n"] ++
%       ["\(TIME0[i]);" | i in TIME0] ++ ["\n"]  ++
%       [ if j==1 then teacherName[i] ++ ";" else "" endif  ++ shiftName[fix(lastWorkedHours[i,j])] ++  if j==length(TIME0) then "\n" else ";" endif
%       | i in TEACHERs, j in TIME0 ] ++ ["\(stats)"];
       
output [ timeLabels[j] ++ ";" ++  teacherName[i] ++ ";" ++ shiftName[fix(roster[i,j])] ++ "\n"  | i in TEACHERs, j in TIME ]  ;

    