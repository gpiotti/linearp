enum PRISONER;

int: n;
set of int: ROW = 1..n;
int: m;
set of int: COL = 1..m;
array[ROW, COL] of int: cost;

set of PRISONER: danger;
set of PRISONER: female;
set of PRISONER: male = PRISONER diff female;  % dependant parameter declaration

array[PRISONER] of var ROW: r;
array[PRISONER] of var COL: c;


% no two prisoners in the same cell
%constraint forall (p1, p2 in PRISONER where p1 < p2) ( abs(r[p1] - r[p2]) + abs(c[p1] - c[p2]) > 0);
% can be better written as   
include "alldifferent.mzn";
constraint alldifferent( [r[p] * m + c[p] | p in PRISONER ]);

%no adjacent dangareous prisoners (can't use the alldifferent constraint here)
constraint forall (p in PRISONER, d in danger where p != d) ( abs(r[p] - r[d]) + abs(c[p] - c[d]) > 1 );

%gender constraints
constraint forall( p in female ) ( r[p] <= (n + 1) div 2 );
constraint forall( p in male ) ( r[p] >= (n + 1) div 2 + 1 );

var int: tCost = sum(p in PRISONER) ( cost[r[p], c[p]] );

solve minimize tCost;