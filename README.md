# Algo_Lab_3

## Task description:

Gorilla Jackie from the Munich Zoo loves to eat bananas. 
The zoo has **N** piles of bananas, the **i**-th basket contains a certain number of bananas **X**. 
The baskets are under guard, but the guard patrols the zoo once per **H** hours, 
during which Jackie can enjoy his favorite dish.

Jackie can eat **K** bananas in an hour. 
Every hour she picks a pile of bananas and eats **K** bananas from there. 
If the basket has less than **K** bananas, 
she will eat all the bananas from it and will no longer eat bananas during that hour.

### Task:

Find the smallest integer **K** so that Jackie can eat all the bananas in the warehouse 
for H hours until the guards return.

### Examples:

**Input:** `piles` = `[3,6,7,11]`, `H` = `8`  
**Output:** 4

**Input:** `piles` = `[30,11,23,4,20]`, `H` = `5`  
**Output:** 30

### Important details:

- 1 <= `piles.length` <= 10^4
- `piles.length` <= `H` <= 10^9
- 1 <= `piles[i]` <= 10^9