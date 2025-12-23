# Solutions – Lists

# 1. Access third element
nums = [1, 2, 3, 4, 5]
print(nums[2])  # 3

# 2. Append "end"
lst = ["start"]
lst.append("end")
print(lst)  # ['start', 'end']

# 3. Sum of numbers
print(sum([3, 6, 9, 12]))  # 30

# 4. Remove duplicates preserving order
def dedup(seq):
    seen = set()
    result = []
    for item in seq:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
print(dedup([1,2,2,3,1,4]))

# 5. Squares of odd numbers
orig = [1,2,3,4,5]
print([x*x for x in orig if x % 2 != 0])

# 6. Rotate list right by k
def rotate(lst, k):
    n = len(lst)
    k %= n
    return lst[-k:] + lst[:-k]
print(rotate([1,2,3,4,5], 2))

# 7. Simple queue using list
queue = []
def enqueue(item):
    queue.append(item)
def dequeue():
    return queue.pop(0) if queue else None
enqueue(10); enqueue(20)
print(dequeue())
print(queue)

# 8. Longest increasing subsequence (O(n^2) DP)
def lis(arr):
    n = len(arr)
    dp = [1]*n
    for i in range(1,n):
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < dp[j]+1:
                dp[i] = dp[j]+1
    return max(dp)
print(lis([10,9,2,5,3,7,101,18]))

# 9. 3‑letter strings from 'a'‑'c'
import itertools
alphabet = ['a','b','c']
triples = [''.join(p) for p in itertools.product(alphabet, repeat=3)]
print(triples[:5])

# 10. FizzBuzz via list comprehension
fb = ["FizzBuzz" if i%15==0 else "Fizz" if i%3==0 else "Buzz" if i%5==0 else str(i) for i in range(1,101)]
print(fb[:15])
