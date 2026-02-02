# Challenge: Algorithm Problems 🏆
Notebook: [[15_Challenge_Algorithms.ipynb]]


> **Difficulty:** ⭐⭐⭐⭐ - ⭐⭐⭐⭐⭐
> **Style:** LeetCode / Codewars
> **Topics:** Dynamic Programming, Backtracking, Binary Search, Greedy, Recursion

---

## C1: Climbing Stairs ⭐⭐
**Task:** You can climb 1 or 2 steps. How many distinct ways to reach the top?

```python
def climb_stairs(n: int) -> int:
    pass

# Example:
# climb_stairs(2) → 2  # (1+1) or (2)
# climb_stairs(3) → 3  # (1+1+1), (1+2), (2+1)
# climb_stairs(5) → 8
```

> [!hint]- 💡 Hint 1 (Low)
> This is essentially Fibonacci!

> [!hint]- 💡 Hint 2 (Mid)
> Ways to reach step n = ways to reach (n-1) + ways to reach (n-2).

> [!hint]- 💡 Hint 3 (High)
> Base cases: `f(1) = 1`, `f(2) = 2`. Use iteration to avoid stack overflow.

> [!success]- Solution
> ```python
> def climb_stairs(n: int) -> int:
>     if n <= 2:
>         return n
>
>     prev1, prev2 = 1, 2
>     for _ in range(3, n + 1):
>         prev1, prev2 = prev2, prev1 + prev2
>
>     return prev2
> ```
> **Complexity:** O(n) time, O(1) space

---

## C2: House Robber ⭐⭐⭐
**Task:** Rob houses without robbing two adjacent ones. Maximize money.

```python
def rob(nums: list) -> int:
    pass

# Example:
# rob([1,2,3,1]) → 4  # Rob house 0 and 2
# rob([2,7,9,3,1]) → 12  # Rob house 0, 2, and 4
```

> [!hint]- 💡 Hint 1 (Low)
> For each house: rob it OR skip it.

> [!hint]- 💡 Hint 2 (Mid)
> `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`

> [!hint]- 💡 Hint 3 (High)
> Only need last two values, so O(1) space is possible.

> [!success]- Solution
> ```python
> def rob(nums: list) -> int:
>     if not nums:
>         return 0
>     if len(nums) == 1:
>         return nums[0]
>
>     prev2, prev1 = 0, 0
>     for num in nums:
>         prev2, prev1 = prev1, max(prev1, prev2 + num)
>
>     return prev1
> ```
> **Complexity:** O(n) time, O(1) space

---

## C3: Coin Change ⭐⭐⭐
**Task:** Find minimum coins needed to make amount. Return -1 if impossible.

```python
def coin_change(coins: list, amount: int) -> int:
    pass

# Example:
# coin_change([1,2,5], 11) → 3  # 5+5+1
# coin_change([2], 3) → -1
# coin_change([1], 0) → 0
```

> [!hint]- 💡 Hint 1 (Low)
> Use dynamic programming: build up from smaller amounts.

> [!hint]- 💡 Hint 2 (Mid)
> `dp[i]` = minimum coins to make amount `i`.

> [!hint]- 💡 Hint 3 (High)
> `dp[i] = min(dp[i], dp[i - coin] + 1)` for each coin.

> [!success]- Solution
> ```python
> def coin_change(coins: list, amount: int) -> int:
>     dp = [float('inf')] * (amount + 1)
>     dp[0] = 0
>
>     for i in range(1, amount + 1):
>         for coin in coins:
>             if coin <= i:
>                 dp[i] = min(dp[i], dp[i - coin] + 1)
>
>     return dp[amount] if dp[amount] != float('inf') else -1
> ```
> **Complexity:** O(amount × coins) time, O(amount) space

---

## C4: Longest Increasing Subsequence ⭐⭐⭐⭐
**Task:** Find the length of the longest strictly increasing subsequence.

```python
def length_of_lis(nums: list) -> int:
    pass

# Example:
# length_of_lis([10,9,2,5,3,7,101,18]) → 4  # [2,3,7,101]
# length_of_lis([0,1,0,3,2,3]) → 4
```

> [!hint]- 💡 Hint 1 (Low)
> DP: for each element, find LIS ending at that element.

> [!hint]- 💡 Hint 2 (Mid)
> O(n²): `dp[i] = max(dp[j] + 1)` for all j < i where nums[j] < nums[i].

> [!hint]- 💡 Hint 3 (High)
> O(n log n): Use binary search with patience sorting.

> [!success]- Solution
> ```python
> # O(n²) DP solution
> def length_of_lis(nums: list) -> int:
>     if not nums:
>         return 0
>
>     dp = [1] * len(nums)
>     for i in range(1, len(nums)):
>         for j in range(i):
>             if nums[j] < nums[i]:
>                 dp[i] = max(dp[i], dp[j] + 1)
>
>     return max(dp)
>
> # O(n log n) with binary search
> import bisect
> def length_of_lis_optimal(nums: list) -> int:
>     tails = []
>     for num in nums:
>         pos = bisect.bisect_left(tails, num)
>         if pos == len(tails):
>             tails.append(num)
>         else:
>             tails[pos] = num
>     return len(tails)
> ```
> **Complexity:** O(n²) or O(n log n) time

---

## C5: Generate Parentheses ⭐⭐⭐
**Task:** Generate all valid combinations of n pairs of parentheses.

```python
def generate_parenthesis(n: int) -> list:
    pass

# Example:
# generate_parenthesis(1) → ["()"]
# generate_parenthesis(2) → ["(())", "()()"]
# generate_parenthesis(3) → ["((()))", "(()())", "(())()", "()(())", "()()()"]
```

> [!hint]- 💡 Hint 1 (Low)
> Use backtracking to build valid strings.

> [!hint]- 💡 Hint 2 (Mid)
> Track count of open and close brackets.

> [!hint]- 💡 Hint 3 (High)
> Add '(' if open < n. Add ')' if close < open.

> [!success]- Solution
> ```python
> def generate_parenthesis(n: int) -> list:
>     result = []
>
>     def backtrack(current, open_count, close_count):
>         if len(current) == 2 * n:
>             result.append(current)
>             return
>
>         if open_count < n:
>             backtrack(current + '(', open_count + 1, close_count)
>         if close_count < open_count:
>             backtrack(current + ')', open_count, close_count + 1)
>
>     backtrack('', 0, 0)
>     return result
> ```
> **Complexity:** O(4^n / √n) - Catalan number

---

## C6: Subsets ⭐⭐⭐
**Task:** Return all possible subsets (power set).

```python
def subsets(nums: list) -> list:
    pass

# Example:
# subsets([1,2,3]) → [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]
```

> [!hint]- 💡 Hint 1 (Low)
> Each element is either included or not - 2^n subsets.

> [!hint]- 💡 Hint 2 (Mid)
> Use backtracking or iterative building.

> [!hint]- 💡 Hint 3 (High)
> Start with [[]], for each num, add it to all existing subsets.

> [!success]- Solution
> ```python
> def subsets(nums: list) -> list:
>     result = [[]]
>     for num in nums:
>         result += [subset + [num] for subset in result]
>     return result
>
> # Backtracking:
> def subsets_backtrack(nums: list) -> list:
>     result = []
>
>     def backtrack(start, current):
>         result.append(current[:])
>         for i in range(start, len(nums)):
>             current.append(nums[i])
>             backtrack(i + 1, current)
>             current.pop()
>
>     backtrack(0, [])
>     return result
> ```
> **Complexity:** O(n × 2^n) time and space

---

## C7: Word Search ⭐⭐⭐⭐
**Task:** Find if word exists in grid by adjacent cells (no reuse).

```python
def exist(board: list, word: str) -> bool:
    pass

# Example:
# board = [["A","B","C","E"],
#          ["S","F","C","S"],
#          ["A","D","E","E"]]
# exist(board, "ABCCED") → True
# exist(board, "SEE") → True
# exist(board, "ABCB") → False
```

> [!hint]- 💡 Hint 1 (Low)
> Use DFS/backtracking from each cell.

> [!hint]- 💡 Hint 2 (Mid)
> Mark visited cells to avoid reuse.

> [!hint]- 💡 Hint 3 (High)
> Temporarily modify the cell (e.g., '#'), then restore.

> [!success]- Solution
> ```python
> def exist(board: list, word: str) -> bool:
>     rows, cols = len(board), len(board[0])
>
>     def dfs(r, c, i):
>         if i == len(word):
>             return True
>         if (r < 0 or r >= rows or c < 0 or c >= cols or
>             board[r][c] != word[i]):
>             return False
>
>         temp = board[r][c]
>         board[r][c] = '#'  # Mark visited
>
>         found = (dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or
>                  dfs(r, c+1, i+1) or dfs(r, c-1, i+1))
>
>         board[r][c] = temp  # Restore
>         return found
>
>     for r in range(rows):
>         for c in range(cols):
>             if dfs(r, c, 0):
>                 return True
>     return False
> ```
> **Complexity:** O(m × n × 4^L) where L = word length

---

## C8: Search in Rotated Sorted Array ⭐⭐⭐
**Task:** Search target in rotated sorted array in O(log n).

```python
def search(nums: list, target: int) -> int:
    pass

# Example:
# search([4,5,6,7,0,1,2], 0) → 4
# search([4,5,6,7,0,1,2], 3) → -1
```

> [!hint]- 💡 Hint 1 (Low)
> Use modified binary search.

> [!hint]- 💡 Hint 2 (Mid)
> One half is always sorted. Determine which half.

> [!hint]- 💡 Hint 3 (High)
> Check if target is in the sorted half, then narrow search.

> [!success]- Solution
> ```python
> def search(nums: list, target: int) -> int:
>     left, right = 0, len(nums) - 1
>
>     while left <= right:
>         mid = (left + right) // 2
>
>         if nums[mid] == target:
>             return mid
>
>         # Left half is sorted
>         if nums[left] <= nums[mid]:
>             if nums[left] <= target < nums[mid]:
>                 right = mid - 1
>             else:
>                 left = mid + 1
>         # Right half is sorted
>         else:
>             if nums[mid] < target <= nums[right]:
>                 left = mid + 1
>             else:
>                 right = mid - 1
>
>     return -1
> ```
> **Complexity:** O(log n) time, O(1) space

---

## C9: Jump Game ⭐⭐⭐
**Task:** Can you reach the last index? Each element = max jump length.

```python
def can_jump(nums: list) -> bool:
    pass

# Example:
# can_jump([2,3,1,1,4]) → True
# can_jump([3,2,1,0,4]) → False
```

> [!hint]- 💡 Hint 1 (Low)
> Track the farthest position you can reach.

> [!hint]- 💡 Hint 2 (Mid)
> If current position > max reach, you're stuck.

> [!hint]- 💡 Hint 3 (High)
> Greedy: `max_reach = max(max_reach, i + nums[i])`

> [!success]- Solution
> ```python
> def can_jump(nums: list) -> bool:
>     max_reach = 0
>
>     for i, jump in enumerate(nums):
>         if i > max_reach:
>             return False
>         max_reach = max(max_reach, i + jump)
>         if max_reach >= len(nums) - 1:
>             return True
>
>     return True
> ```
> **Complexity:** O(n) time, O(1) space

---

## C10: Edit Distance ⭐⭐⭐⭐⭐
**Task:** Minimum operations to convert word1 to word2 (insert, delete, replace).

```python
def min_distance(word1: str, word2: str) -> int:
    pass

# Example:
# min_distance("horse", "ros") → 3
# min_distance("intention", "execution") → 5
```

> [!hint]- 💡 Hint 1 (Low)
> Classic dynamic programming problem.

> [!hint]- 💡 Hint 2 (Mid)
> `dp[i][j]` = min operations to convert word1[0:i] to word2[0:j].

> [!hint]- 💡 Hint 3 (High)
> If chars match: `dp[i][j] = dp[i-1][j-1]`. Else: min of insert, delete, replace.

> [!success]- Solution
> ```python
> def min_distance(word1: str, word2: str) -> int:
>     m, n = len(word1), len(word2)
>     dp = [[0] * (n + 1) for _ in range(m + 1)]
>
>     # Base cases
>     for i in range(m + 1):
>         dp[i][0] = i
>     for j in range(n + 1):
>         dp[0][j] = j
>
>     for i in range(1, m + 1):
>         for j in range(1, n + 1):
>             if word1[i-1] == word2[j-1]:
>                 dp[i][j] = dp[i-1][j-1]
>             else:
>                 dp[i][j] = 1 + min(
>                     dp[i-1][j],      # Delete
>                     dp[i][j-1],      # Insert
>                     dp[i-1][j-1]     # Replace
>                 )
>
>     return dp[m][n]
> ```
> **Complexity:** O(m × n) time and space

---

## 🎯 Algorithm Challenges Complete!

**Skills Practiced:**
- Dynamic Programming (1D and 2D)
- Backtracking
- Greedy Algorithms
- Binary Search variations
- Recursion with memoization

---

## 🏆 All Challenges Complete!

Congratulations on completing all 50 LeetCode-style challenges!

**Summary:**
- Array Challenges: 10 problems
- String Challenges: 10 problems
- Math Challenges: 10 problems
- Data Structure Challenges: 10 problems
- Algorithm Challenges: 10 problems

**Next Steps:**
- Practice on [LeetCode](https://leetcode.com)
- Try [Codewars](https://codewars.com)
- Compete on [HackerRank](https://hackerrank.com)
- Study [[../../04_DSA_Linear/00_Index|Data Structures]]
