# def diagonal_flip(arr):
#     n = len(arr) #2
#     m = len(arr[0]) #3

#     flipped_array = [[0] * n for _ in range(m)]

#     for i in range(n):
#         for j in range(m):
#             flipped_array[j][i] = arr[i][j] # 가로와 세로를 뒤집으면 됩니다

#     return flipped_array


# a = [
#     [1, 2, 3], [4, 5, 6]
# ]
# print(diagonal_flip(a))

# def diagonal_flip_with_zip(arr):
#     return [list(val) for val in zip(*arr)]

# print(diagonal_flip_with_zip(a))

# def rotate(arr):
#     n = len(arr)
#     rotated_arr = [[0] * n for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             rotated_arr[j][n - 1 - i] = arr[i][j]
#     return rotated_arr

a = [
    [1, 2, 3], [4, 5, 6],[7,8,9]
]
n = len(a)

rotated_arr = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        rotated_arr[j][n - 1 - i] = a[i][j]

