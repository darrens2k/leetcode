On a fine day, a travel agent gets calls from N newly married couple customers each from different cities asking to plan a trip for them. They also said that during their vacation their house can be given for accommodation so that they can relieve some burden of the tour.

Having heard this, the travel agent now plans to send each couple to a different city and use his customer houses for accommodation so that he can benefit all his customers. At the same time, he wants to plan the trips (one way) in such a way that he makes a maximum profit in the journey fares by maximizing the total travel distance of all couples. Help him plan the trips for all couples such that he maximizes the total distances traveled by all couples.

The travel distance of a couple is the distance between the city he lives in and the city he travels to. These N cities have N-1 highways connecting them. Travelers always choose the shortest path when traveling.

Input:  
Each test case contains several lines. The first line contains an integer N, representing the number of cities. Then the following N-1 lines each contain three integers X, Y, Z, which means that there is a highway between city X and city Y, and Z is the length of that highway.

You can assume all the cities are connected and the highways are bi-directional.

Example
```
Input:
5
1 2 1
2 3 2
2 4 3
1 5 4

Output: 22

One possible arrangement which leads to the maximum total distance traveled by all couples together is:
city 1's couple goes to city 2: 1 km traveled
city 2's couple goes to city 3: 2 km traveled
city 3's couple goes to city 1: 3 km traveled
city 4's couple goes to city 5: 8 km traveled
city 5's couple goes to city 4: 8 km traveled

Hence total distance traveled by all couples together is 22 km.
```
Constraints:
* 2 ≤ N ≤ 1000
* Each row has three elements X,Y, Z(1 ≤ X, Y ≤ N, 1 ≤ Z ≤ 10^6)