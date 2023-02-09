import time
from typing import List


def main():
    arr = [61, 3, 38, 5, 47, 15, 36, 26, 27, 44, 46, 39, 47, 50, 48]
    print(bubble_sort(arr))


# time complexity : O(n**2)
def bubble_sort(arr: List[int]) -> List[int]:
    for i in range(1, len(arr)):
        for j in range(len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


if __name__ == '__main__':
    start_time = time.time()
    main()
    print(time.time() - start_time)