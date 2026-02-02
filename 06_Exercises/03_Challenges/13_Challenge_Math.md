# Challenge: Math & Logic Problems 🏆
Notebook: [[13_Challenge_Math.ipynb]]


> **Difficulty:** ⭐⭐⭐ - ⭐⭐⭐⭐⭐
> **Style:** LeetCode / Codewars
> **Topics:** Math, Bit Manipulation, Number Theory, Logic

---

## C1: Reverse Integer ⭐⭐
**Task:** Reverse digits of a 32-bit signed integer. Return 0 if overflow.

```python
def reverse(x: int) -> int:
    pass

# Example:
# reverse(123) → 321
# reverse(-123) → -321
# reverse(120) → 21
```

> [!hint]- 💡 Hint 1 (Low)
> Extract digits one by one using modulo and division.

> [!hint]- 💡 Hint 2 (Mid)
> Build the reversed number by multiplying by 10 and adding digits.

> [!hint]- 💡 Hint 3 (High)
> Check for overflow: result must be in [-2³¹, 2³¹ - 1].

> [!success]- Solution
> ```python
> def reverse(x: int) -> int:
>     sign = -1 if x < 0 else 1
>     x = abs(x)
>     result = 0
>
>     while x:
>         result = result * 10 + x % 10
>         x //= 10
>
>     result *= sign
>     if result < -2**31 or result > 2**31 - 1:
>         return 0
>     return result
> ```
> **Complexity:** O(log n) time, O(1) space

---

## C2: Power of Two ⭐⭐
**Task:** Check if a number is a power of two.

```python
def is_power_of_two(n: int) -> bool:
    pass

# Example:
# is_power_of_two(1) → True  # 2^0
# is_power_of_two(16) → True  # 2^4
# is_power_of_two(3) → False
```

> [!hint]- 💡 Hint 1 (Low)
> Powers of two have only one bit set in binary.

> [!hint]- 💡 Hint 2 (Mid)
> What happens when you subtract 1 from a power of two?

> [!hint]- 💡 Hint 3 (High)
> `n & (n - 1)` clears the lowest set bit. For powers of 2, this gives 0.

> [!success]- Solution
> ```python
> def is_power_of_two(n: int) -> bool:
>     return n > 0 and (n & (n - 1)) == 0
>
> # Alternative without bit manipulation:
> def is_power_of_two_v2(n: int) -> bool:
>     if n <= 0:
>         return False
>     while n > 1:
>         if n % 2 != 0:
>             return False
>         n //= 2
>     return True
> ```
> **Complexity:** O(1) time, O(1) space

---

## C3: Count Primes ⭐⭐⭐
**Task:** Count the number of prime numbers less than n.

```python
def count_primes(n: int) -> int:
    pass

# Example:
# count_primes(10) → 4  # [2, 3, 5, 7]
# count_primes(0) → 0
# count_primes(1) → 0
```

> [!hint]- 💡 Hint 1 (Low)
> Use the Sieve of Eratosthenes algorithm.

> [!hint]- 💡 Hint 2 (Mid)
> Mark all multiples of each prime as non-prime.

> [!hint]- 💡 Hint 3 (High)
> Start marking from p² since smaller multiples are already marked.

> [!success]- Solution
> ```python
> def count_primes(n: int) -> int:
>     if n < 2:
>         return 0
>
>     is_prime = [True] * n
>     is_prime[0] = is_prime[1] = False
>
>     for i in range(2, int(n**0.5) + 1):
>         if is_prime[i]:
>             for j in range(i*i, n, i):
>                 is_prime[j] = False
>
>     return sum(is_prime)
> ```
> **Complexity:** O(n log log n) time, O(n) space

---

## C4: Single Number ⭐⭐
**Task:** Every element appears twice except one. Find it.

```python
def single_number(nums: list) -> int:
    pass

# Example:
# single_number([2, 2, 1]) → 1
# single_number([4, 1, 2, 1, 2]) → 4
```

> [!hint]- 💡 Hint 1 (Low)
> XOR has a special property with duplicates.

> [!hint]- 💡 Hint 2 (Mid)
> `a ^ a = 0` and `a ^ 0 = a`.

> [!hint]- 💡 Hint 3 (High)
> XOR all numbers together - pairs cancel out.

> [!success]- Solution
> ```python
> def single_number(nums: list) -> int:
>     result = 0
>     for num in nums:
>         result ^= num
>     return result
>
> # One-liner with reduce:
> from functools import reduce
> def single_number_v2(nums: list) -> int:
>     return reduce(lambda x, y: x ^ y, nums)
> ```
> **Complexity:** O(n) time, O(1) space

---

## C5: Happy Number ⭐⭐
**Task:** A happy number eventually reaches 1 when replacing with sum of squares of digits.

```python
def is_happy(n: int) -> bool:
    pass

# Example:
# is_happy(19) → True  # 1² + 9² = 82 → 64 + 4 = 68 → ... → 1
# is_happy(2) → False
```

> [!hint]- 💡 Hint 1 (Low)
> Either it reaches 1 or it enters a cycle.

> [!hint]- 💡 Hint 2 (Mid)
> Use a set to detect cycles, or Floyd's algorithm.

> [!hint]- 💡 Hint 3 (High)
> Sum of digit squares: `sum(int(d)**2 for d in str(n))`

> [!success]- Solution
> ```python
> def is_happy(n: int) -> bool:
>     def get_next(num):
>         return sum(int(d)**2 for d in str(num))
>
>     seen = set()
>     while n != 1 and n not in seen:
>         seen.add(n)
>         n = get_next(n)
>
>     return n == 1
>
> # Floyd's cycle detection (O(1) space):
> def is_happy_v2(n: int) -> bool:
>     def get_next(num):
>         return sum(int(d)**2 for d in str(num))
>
>     slow = n
>     fast = get_next(n)
>     while fast != 1 and slow != fast:
>         slow = get_next(slow)
>         fast = get_next(get_next(fast))
>
>     return fast == 1
> ```
> **Complexity:** O(log n) time, O(log n) or O(1) space

---

## C6: Missing Number ⭐⭐
**Task:** Find the missing number in [0, n] range.

```python
def missing_number(nums: list) -> int:
    pass

# Example:
# missing_number([3, 0, 1]) → 2
# missing_number([0, 1]) → 2
# missing_number([9,6,4,2,3,5,7,0,1]) → 8
```

> [!hint]- 💡 Hint 1 (Low)
> Sum of 0 to n is n*(n+1)/2.

> [!hint]- 💡 Hint 2 (Mid)
> Subtract actual sum from expected sum.

> [!hint]- 💡 Hint 3 (High)
> Or use XOR: `0^1^2^...^n ^ nums[0]^nums[1]^...` leaves missing.

> [!success]- Solution
> ```python
> def missing_number(nums: list) -> int:
>     n = len(nums)
>     expected = n * (n + 1) // 2
>     actual = sum(nums)
>     return expected - actual
>
> # XOR solution:
> def missing_number_v2(nums: list) -> int:
>     result = len(nums)
>     for i, num in enumerate(nums):
>         result ^= i ^ num
>     return result
> ```
> **Complexity:** O(n) time, O(1) space

---

## C7: Pow(x, n) ⭐⭐⭐
**Task:** Implement power function efficiently.

```python
def my_pow(x: float, n: int) -> float:
    pass

# Example:
# my_pow(2.0, 10) → 1024.0
# my_pow(2.1, 3) → 9.261
# my_pow(2.0, -2) → 0.25
```

> [!hint]- 💡 Hint 1 (Low)
> Use binary exponentiation - square when possible.

> [!hint]- 💡 Hint 2 (Mid)
> x^n = (x^(n/2))^2 for even n, x * x^(n-1) for odd n.

> [!hint]- 💡 Hint 3 (High)
> Handle negative n by computing 1/x^(-n).

> [!success]- Solution
> ```python
> def my_pow(x: float, n: int) -> float:
>     if n == 0:
>         return 1
>     if n < 0:
>         x = 1 / x
>         n = -n
>
>     result = 1
>     while n:
>         if n % 2:
>             result *= x
>         x *= x
>         n //= 2
>
>     return result
> ```
> **Complexity:** O(log n) time, O(1) space

---

## C8: Sqrt(x) ⭐⭐
**Task:** Compute integer square root without using built-in sqrt.

```python
def my_sqrt(x: int) -> int:
    pass

# Example:
# my_sqrt(4) → 2
# my_sqrt(8) → 2  # sqrt(8) = 2.828..., truncated
```

> [!hint]- 💡 Hint 1 (Low)
> Use binary search between 0 and x.

> [!hint]- 💡 Hint 2 (Mid)
> If mid² <= x, the answer is at least mid.

> [!hint]- 💡 Hint 3 (High)
> Search for largest mid where mid² <= x.

> [!success]- Solution
> ```python
> def my_sqrt(x: int) -> int:
>     if x < 2:
>         return x
>
>     left, right = 1, x // 2
>     while left <= right:
>         mid = (left + right) // 2
>         sq = mid * mid
>         if sq == x:
>             return mid
>         elif sq < x:
>             left = mid + 1
>         else:
>             right = mid - 1
>
>     return right
> ```
> **Complexity:** O(log n) time, O(1) space

---

## C9: Number of 1 Bits ⭐⭐
**Task:** Count the number of 1 bits (Hamming weight).

```python
def hamming_weight(n: int) -> int:
    pass

# Example:
# hamming_weight(11) → 3  # binary: 1011
# hamming_weight(128) → 1  # binary: 10000000
```

> [!hint]- 💡 Hint 1 (Low)
> Check each bit by using AND with 1.

> [!hint]- 💡 Hint 2 (Mid)
> `n & (n-1)` removes the lowest set bit.

> [!hint]- 💡 Hint 3 (High)
> Keep removing lowest bits and count iterations.

> [!success]- Solution
> ```python
> def hamming_weight(n: int) -> int:
>     count = 0
>     while n:
>         n &= n - 1  # Remove lowest set bit
>         count += 1
>     return count
>
> # Alternative:
> def hamming_weight_v2(n: int) -> int:
>     return bin(n).count('1')
> ```
> **Complexity:** O(k) where k = number of 1 bits

---

## C10: Roman to Integer ⭐⭐
**Task:** Convert Roman numeral to integer.

```python
def roman_to_int(s: str) -> int:
    pass

# Example:
# roman_to_int("III") → 3
# roman_to_int("IV") → 4
# roman_to_int("MCMXCIV") → 1994
```

> [!hint]- 💡 Hint 1 (Low)
> Map each Roman numeral to its value.

> [!hint]- 💡 Hint 2 (Mid)
> Subtraction cases: smaller value before larger (IV = 4, not 6).

> [!hint]- 💡 Hint 3 (High)
> If current < next, subtract; otherwise add.

> [!success]- Solution
> ```python
> def roman_to_int(s: str) -> int:
>     values = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
>               'C': 100, 'D': 500, 'M': 1000}
>
>     result = 0
>     for i in range(len(s)):
>         if i < len(s) - 1 and values[s[i]] < values[s[i+1]]:
>             result -= values[s[i]]
>         else:
>             result += values[s[i]]
>
>     return result
> ```
> **Complexity:** O(n) time, O(1) space

---

## 🎯 Math Challenges Complete!

**Skills Practiced:**
- Bit manipulation
- Number theory
- Binary search
- Mathematical optimization
- Fast exponentiation

**Next Challenge:** [[14_Challenge_DataStructures|Data Structure Challenges]]
