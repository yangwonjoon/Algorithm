import sys

input = sys.stdin.readline
n = int(input())
graph = [[]]+[list(input().strip()) for _ in range(n)]
visited = [False for _ in range(n+1)]
