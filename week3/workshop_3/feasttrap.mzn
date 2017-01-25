% Beauty Trap
% Create the most magnificient feast 
enum DISH;
enum TASTE = {spicy, sour, salty, sweet, umame, bland};
enum TEMP = {hot, cold, warm};
%int: ndish;
%set of int: DISH = 1..ndish;
%set of int: TASTE = 1..6;
%int: spicy = 1; int: sour = 2; int: salty = 3; int: sweet = 4; int: umame = 5; int: bland = 6;
%set of int: TEMP = 1..3;
%int: hot = 1; int: cold = 2; int: warm = 3;
include "alldifferent.mzn";
include "regular.mzn";
constraint alldifferent(dish);
 
array[DISH] of TASTE: taste;
array[DISH] of TEMP: temp;
array[DISH] of bool: heavy;
array[DISH] of int: value;

int: len; % length of banquet
set of int: COURSE = 1..len;

array[COURSE] of var DISH: dish;

constraint forall(c in 1..len-1) (taste[dish[c]] != taste[dish[c+1]]);
constraint taste[dish[1]] = salty;
constraint taste[dish[len]] = sweet;

constraint regular([taste[dish[i]] | i in COURSE], 7, 6, transition_array, 1, {5});

array[1..7, TASTE] of 0..7: transition_array = [| 0, 0, 4, 0, 0, 0, 
                                                | 0, 0, 0, 5, 0, 7,
                                                | 0, 0, 0, 0, 6, 7,
                                                | 2, 3, 0, 5, 6, 7, 
                                                | 0, 3, 4, 0, 0, 7,
                                                | 2, 3, 4, 5, 0, 7,
                                                | 2, 3, 4, 5, 6, 0 |];

%constraint forall(c in 1..len-1) (taste[dish[c]] != taste[dish[c+1]]);
%constraint forall(c in 1..len-1) (taste[dish[c]] = spicy -> taste[dish[c+1]] in {bland, sweet});
%constraint forall(c in 1..len-1) (taste[dish[c]] = sour -> taste[dish[c+1]] in {bland, umame});
%constraint forall(c in 1..len-1) (taste[dish[c]] = sweet -> taste[dish[c+1]] in {bland, salty, sour});

%constraint forall (c in 1..len-2) ((temp[dish[c]] = hot /\ temp[dish[c+2]] = cold) -> temp[dish[c+1]] = warm);
%constraint forall (i in 1..len-1) ((temp[dish[i]] = hot -> forall(j in i+1..len) (temp[dish[j]] = cold -> exists(k in i+1..j-1) (temp[dish[k]] = warm))));

constraint forall(c in 1..len-2) (heavy[dish[c]] = 1 /\ heavy[dish[c+1]] = 1 -> heavy[dish[c+2]] = 0);

var int: obj;
constraint obj = sum(i in 1..len) (value[dish[i]])
               + len -1 %everytime is a change in taste, except for the last dish
               + sum(i in 1..len-1) (temp[dish[i]] != temp[dish[i+1]])
               + sum(i in 1..len-1) (heavy[dish[i]] != heavy[dish[i+1]]);

solve maximize obj;