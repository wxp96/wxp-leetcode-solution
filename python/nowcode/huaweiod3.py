import sys
from collections import deque
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    for i in range(-10,10):
        pre=0
        for num in values: