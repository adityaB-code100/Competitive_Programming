def mine_sweeper(n, m, matrix):
    print(n,m)

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == "*":
                continue
            count = 0

            if i != 0:
                if matrix[i - 1][j] == "*":
                    count += 1

            if j != 0:
                if matrix[i][j - 1] == "*":
                    count += 1

            if i != 0 and j != 0:
                if matrix[i - 1][j - 1] == "*":
                    count += 1

            if i < n - 1 and j < m - 1:
                if matrix[i + 1][j + 1] == "*":
                    count += 1

            if i != 0 and j < m - 1:
                if matrix[i - 1][j + 1] == "*":
                    count += 1

            if j < m - 1:
                if matrix[i][j + 1] == "*":
                    count += 1

            if i < n - 1 and j != 0:
                if matrix[i + 1][j - 1]=="*":
                    count += 1

            if i < n - 1:
                if matrix[i + 1][j] == "*":
                    count += 1

            matrix[i][j] = count

    return matrix
    
    
def disply(nums):
    for num in nums:
        print(num) 
        
        
            

#testcase1
test1 = [["*", ".", ".", "."], [".", ".", ".", "."], [".", "*", ".", "."], [".", ".", ".", "."]]
print("Input Matrix")
disply(test1)
temp=mine_sweeper(4, 4, test1)
print("Testcase1 output")
disply(temp)

#testcase2

test2=[["*","*",".",".","."],[".",".",".",".","."],[".","*",".",".","."]]
print("Input Matrix")
disply(test2)
temp=mine_sweeper(3,5,test2)
print("Testcase2 Output")
disply(temp)

#testcase3
test3=[]
print("input matrix")
disply(test3)
temp=mine_sweeper(0,0,test3)
disply(temp)


# output
# ['*', '.', '.', '.']
# ['.', '.', '.', '.']
# ['.', '*', '.', '.']
# ['.', '.', '.', '.']
# 4 4
# Testcase1 output
# ['*', 1, 0, 0]
# [2, 2, 1, 0]
# [1, '*', 1, 0]
# [1, 1, 1, 0]
# Input Matrix
# ['*', '*', '.', '.', '.']
# ['.', '.', '.', '.', '.']
# ['.', '*', '.', '.', '.']
# 3 5
# Testcase2 Output
# ['*', '*', 1, 0, 0]
# [3, 3, 2, 0, 0]
# [1, '*', 1, 0, 0]
# input matrix
# 0 0