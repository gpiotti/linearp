int: start = 25;
array[int] of int: readings;
int: l = length(readings);

set of int: TIME = 0..l;

array[TIME] of var int: temp;

constraint temp[0] = start;
constraint forall (t in 1..l) (temp[t] = (temp[t-1] + readings[t]) div 2);

solve satisfy;

