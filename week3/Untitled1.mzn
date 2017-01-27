array[1..10] of var bool: obj = [ bernoulli(i mod 2) | i in 1..10]; 
solve satisfy;

output ["\(obj)"];