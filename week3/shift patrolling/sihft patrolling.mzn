% DOMAIN = SOLDIER x DAY
% CODOMAIN = SHIFT
% so array[SOLDER, DAY] of var SHIFT: roster;
% in general =>  array[DOMAIN] of var CODOMAIN: shedule;

enum SOLDIER;
enum SHIFT = {EVE, NIGHT, NONE, SHIFT3, SHIFT4, SHIFT5, S6,s7,s8,s9,s10,s11,s12,s13,s14,s16,s17,s18,s19,s20,s21,s22,s23,s24,s25,s26,s27,s28,s29,s30,s31,s32,s33,s34,s35,s36,s37,s38,s39,s40,s41,s42,s43,s44,s45,s46,s47,s48,s49,s50,s51,s52,s53,s54,s55};
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

% minimum soldiers in NIGHT shift by day
constraint forall (d in DAY)
                  (sum (s in SOLDIER) (roster[s, d] = NIGHT) = o);
                 
% between l and u soldiers in EVE shift by day
array[DAY] of var l..u: onEve;
onEve = [sum(s in SOLDIER) (roster[s, d] = EVE) | d in DAY ]; 
%constraint forall (d in DAY)
%                 (sum (s in SOLDIER) (roster[s, d] = EVE) >= l);
%constraint forall (d in DAY )
%                  (sum (s in SOLDIER) (roster[s, d] = EVE) <= u);
                  
var int: tOnEve = sum (d in DAY)
                      (sum (s in SOLDIER) (roster[s, d] = EVE));

solve maximize tOnEve;