% workshop 2
% select a set of trade negotiation party
enum NEGOTIATOR;
NEGOTIATOR: dummy; 

int: l; % minimum party size
int: u; % maximum party size
int: m; % minimum joint ability

array[NEGOTIATOR] of int: honor;
array[NEGOTIATOR,NEGOTIATOR] of int: joint;

var set of NEGOTIATOR: party;

constraint ( sum (i,j in party where i<j ) (joint[i,j])) >= m;
constraint card(party) <= u;
constraint card(party) >= u;
constraint not (dummy in party);

var int: obj;
constraint obj = min (i in party) (honor[i]);

solve maximize min (i in party) (honor[i]);


