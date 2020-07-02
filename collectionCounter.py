# from collections import Counter
# x = int(input())
# # x = 10
# sizes = list(map(int, input().split()))
# # sizes = [2, 3, 4, 5, 6, 8, 7, 6, 5, 18]
# total_customers = int(input())
# # total_customers = 6
# desired_shoes = []
# for _ in range(total_customers):
#     desired_shoes.append(list(map(int, input().split())))
# # desired_shoes = [[6, 55], [6, 45], [6, 55], [4, 40], [18, 60], [10, 50]]

# counterSizes = Counter(sizes)
# moneyEarned = 0
# for order in desired_shoes:
#     if order[0] in counterSizes and counterSizes[order[0]] > 0:
#         moneyEarned += order[1]
#         counterSizes[order[0]] -= 1

# print(moneyEarned)

for _ in range(3):
    size, pay = map(int, input().split())
    print(size, pay)
