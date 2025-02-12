# 3*3[sum of the rows and cols be 15]
# [1-9] no digits will be repeated

def print1(mat):
    for i in range(3):
        for j in range(3):
            print(mat[i][j], end=" ")
        print()

def matrix():
    mat = [[8, 1, 6],
             [3, 5, 7],
             [4, 9, 2]]
    return mat

if __name__ == "__main__":
    mat = matrix()
    print1(mat)