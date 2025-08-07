list2d=[[1, 3, 4],
        [5, 9, 4],
        [3, 9, 7]
        ]
# print(list2d)
for rows in list2d:
    # for items in rows:
     print(rows)

sum_diagonal=0
for i in range(3):
#      --- Main diagonal
#      sum_diagonal+=list2d[i][i]  
#      ---- Anti diagonal
     sum_diagonal+=list2d[i][2-i]

print("The sum of one diagonal is",sum_diagonal)