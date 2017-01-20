int: start ;
array[int] of int: readings;
int: l = length(readings);

set of int: TIME0 = 0..l;
set of int: TIME = 1..l;

array[TIME0] of var 25..30: temp; % this variable is 25..30 to help the solver, 
                                  % it can be just an int, and then have a constraint
                                  % limiting the values (is better this way)
                                
array[TIME] of var ACTION: choice; % this variable will hold the action at any time
array[TIME] of var 25..30: tp = [temp[t] | t in TIME ];

enum ACTION = { heat, strong_heat, cool, strong_cool, do_nothing };
array[ACTION] of int: adjust = { 1, 4, -2, -5, 0 };
array[ACTION] of int: action_cost = {1, 5, 3, 9, 0};

constraint temp[0] = start;
constraint forall (t in TIME) ( temp[t] = (temp[t-1] + readings[t]) div 2
                              + adjust[choice[t]] );
                          
var int: cost = sum(t in TIME) (action_cost[choice[t]]);

solve minimize cost ;

output ["time0: \(TIME0) \ntime: \(TIME) \ntp: \(tp) \nchoice: \(choice) \ncost: \(action_cost) \ntotal_cost: \(cost)"];
