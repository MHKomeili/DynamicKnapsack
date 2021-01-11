def knapsack(profits:list, weights:list, capacity:int):
    P = list()
    

    for j in range(len(profits)):
        currentList = [0 for _ in range(capacity+1)]
        for m in range(capacity+1):
            
            if j == 0 and weights[j] > m:
                currentList[m] = 0
            
            elif j == 0 and weights[j] <= m:
                currentList[m] = profits[0]

            elif weights[j] > m:
                currentList[m] = P[j-1][m]

            elif m-weights[j]>=60:
                currentList[m] = max(P[j-1][m], P[j-1][m-weights[j]]+profits[j])
            
            else:
                currentList[m] = P[j-1][m]
        
        P.append(currentList)
    return P

profits = [9, 9, 16]
weights = [10, 10, 19]
capacity = 20
P = knapsack(profits,weights,capacity)
for i in range(len(P)):
    print(P[i])
    print()