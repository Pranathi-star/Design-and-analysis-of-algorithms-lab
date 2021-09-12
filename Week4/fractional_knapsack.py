class Solution:
    def fractional_knapsack(self, items, cap):
        items.sort(key = lambda x: x[2], reverse = True)
        no_items = len(items)
        max_possible_profit = 0
        for i in range(no_items):
            if items[i][1] <= cap:
                max_possible_profit += items[i][0]
                cap -= items[i][1]
            else:
                max_possible_profit += (items[i][2] * cap)
                cap = 0
                break

        return max_possible_profit

no_items = int(input("Number of items: ").strip())
cap = int(input("Capacity of knapsack: ").strip())
items = []
print("Enter the value and weight of each item")
for i in range(no_items):
    a, b = [int(i) for i in input().split()]
    items.append([a, b, a/b])
sol = Solution()
print("Maximum profit possible: ", sol.fractional_knapsack(items, cap))
    
