% DOMAIN = SOLDIER x DAY
% CODOMAIN = SHIFT
% so array[SOLDER, DAY] of var SHIFT: roster;
% in general =>  array[DOMAIN] of var CODOMAIN: shedule;
include "global_cardinality.mzn";
enum SOLDIER;
enum SHIFT = {EVE, NIGHT, NONE};
int: nDays;
set of int: DAY = 1..nDays;

int: o; % required number for NIGHT shift
int: l; % lower bound for EVE shift
int: u; % upper bound for EVE shift

array[SOLDIER, DAY] of var SHIFT: roster;

% no two NIGHT shifts in a row
constraint forall (s in SOLDIER, d in 1..nDays-2) 
                  (roster[s, d] = NIGHT /\ roster[s, d+1] = NIGHT -> roster[s, d+2] != NIGHT);

% no EVE shift followed by NIGHT shift
constraint forall (s in SOLDIER, d in 1..nDays-2)
                  (roster[s, d] = EVE -> roster[s, d+1] != NIGHT);  
                 
% between l and u soldiers in EVE shift by day - this is for performance
array[DAY] of var l..u: onEve;
                  
%this constraint reemplaza las constraint que limitan la cantidad de shifts x dia (l, u y o)
constraint forall(d in DAY) (global_cardinality([roster[s, d] | s in SOLDIER], [NIGHT, EVE], [o, onEve[d]]));

solve maximize sum(onEve);