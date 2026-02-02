# Challenge: String Problems 🏆
Notebook: [[12_Challenge_Strings.ipynb]]


> **Difficulty:** ⭐⭐⭐ - ⭐⭐⭐⭐⭐
> **Style:** LeetCode / Codewars
> **Topics:** Strings, Dictionaries, Sliding Window, Two Pointers

---

## C1: Valid Palindrome ⭐⭐
**Task:** Check if a string is a palindrome, considering only alphanumeric characters.

```python
def is_palindrome(s: str) -> bool:
    pass

# Example:
# is_palindrome("A man, a plan, a canal: Panama") → True
# is_palindrome("race a car") → False
# is_palindrome(" ") → True
```

> [!hint]- 💡 Hint 1 (Low)
> First, filter out non-alphanumeric characters.

> [!hint]- 💡 Hint 2 (Mid)
> Convert to lowercase and compare with reversed version.

> [!hint]- 💡 Hint 3 (High)
> Use `isalnum()` to filter, `lower()` to normalize, `[::-1]` to reverse.

> [!success]- Solution
> ```python
> def is_palindrome(s: str) -> bool:
>     cleaned = ''.join(c.lower() for c in s if c.isalnum())
>     return cleaned == cleaned[::-1]
>
> # Two-pointer alternative (O(1) space):
> def is_palindrome_v2(s: str) -> bool:
>     left, right = 0, len(s) - 1
>     while left < right:
>         while left < right and not s[left].isalnum():
>             left += 1
>         while left < right and not s[right].isalnum():
>             right -= 1
>         if s[left].lower() != s[right].lower():
>             return False
>         left += 1
>         right -= 1
>     return True
> ```
> **Complexity:** O(n) time, O(n) or O(1) space

---

## C2: Longest Substring Without Repeating ⭐⭐⭐
**Task:** Find the length of the longest substring without repeating characters.

```python
def length_of_longest_substring(s: str) -> int:
    pass

# Example:
# length_of_longest_substring("abcabcbb") → 3  # "abc"
# length_of_longest_substring("bbbbb") → 1  # "b"
# length_of_longest_substring("pwwkew") → 3  # "wke"
```

> [!hint]- 💡 Hint 1 (Low)
> Use a sliding window approach - expand and contract as needed.

> [!hint]- 💡 Hint 2 (Mid)
> Keep track of character positions in a dictionary.

> [!hint]- 💡 Hint 3 (High)
> When you see a repeat, move left pointer past the previous occurrence.

> [!success]- Solution
> ```python
> def length_of_longest_substring(s: str) -> int:
>     char_index = {}
>     left = max_length = 0
>
>     for right, char in enumerate(s):
>         if char in char_index and char_index[char] >= left:
>             left = char_index[char] + 1
>         char_index[char] = right
>         max_length = max(max_length, right - left + 1)
>
>     return max_length
> ```
> **Complexity:** O(n) time, O(min(n, alphabet)) space

---

## C3: Valid Anagram ⭐⭐
**Task:** Check if two strings are anagrams of each other.

```python
def is_anagram(s: str, t: str) -> bool:
    pass

# Example:
# is_anagram("anagram", "nagaram") → True
# is_anagram("rat", "car") → False
# is_anagram("listen", "silent") → True
```

> [!hint]- 💡 Hint 1 (Low)
> Anagrams have the same characters with the same frequencies.

> [!hint]- 💡 Hint 2 (Mid)
> Count character frequencies for both strings and compare.

> [!hint]- 💡 Hint 3 (High)
> Use `collections.Counter` or a dictionary to count characters.

> [!success]- Solution
> ```python
> from collections import Counter
>
> def is_anagram(s: str, t: str) -> bool:
>     return Counter(s) == Counter(t)
>
> # Without Counter:
> def is_anagram_v2(s: str, t: str) -> bool:
>     if len(s) != len(t):
>         return False
>     count = {}
>     for c in s:
>         count[c] = count.get(c, 0) + 1
>     for c in t:
>         if c not in count:
>             return False
>         count[c] -= 1
>         if count[c] < 0:
>             return False
>     return True
> ```
> **Complexity:** O(n) time, O(1) space (26 letters max)

---

## C4: Group Anagrams ⭐⭐⭐
**Task:** Group words that are anagrams of each other.

```python
def group_anagrams(strs: list) -> list:
    pass

# Example:
# group_anagrams(["eat","tea","tan","ate","nat","bat"])
# → [["eat","tea","ate"], ["tan","nat"], ["bat"]]
```

> [!hint]- 💡 Hint 1 (Low)
> Anagrams will have the same sorted characters.

> [!hint]- 💡 Hint 2 (Mid)
> Use sorted characters as a key in a dictionary.

> [!hint]- 💡 Hint 3 (High)
> `tuple(sorted(word))` can be used as a dictionary key.

> [!success]- Solution
> ```python
> from collections import defaultdict
>
> def group_anagrams(strs: list) -> list:
>     groups = defaultdict(list)
>     for word in strs:
>         key = tuple(sorted(word))
>         groups[key].append(word)
>     return list(groups.values())
>
> # Alternative: use character count as key
> def group_anagrams_v2(strs: list) -> list:
>     groups = defaultdict(list)
>     for word in strs:
>         count = [0] * 26
>         for c in word:
>             count[ord(c) - ord('a')] += 1
>         groups[tuple(count)].append(word)
>     return list(groups.values())
> ```
> **Complexity:** O(n × k log k) or O(n × k) time

---

## C5: Longest Palindromic Substring ⭐⭐⭐⭐
**Task:** Find the longest palindromic substring.

```python
def longest_palindrome(s: str) -> str:
    pass

# Example:
# longest_palindrome("babad") → "bab" or "aba"
# longest_palindrome("cbbd") → "bb"
```

> [!hint]- 💡 Hint 1 (Low)
> A palindrome can be expanded from its center.

> [!hint]- 💡 Hint 2 (Mid)
> Try each position as the center and expand outward.

> [!hint]- 💡 Hint 3 (High)
> Handle both odd-length (single center) and even-length (two centers) cases.

> [!success]- Solution
> ```python
> def longest_palindrome(s: str) -> str:
>     def expand(left, right):
>         while left >= 0 and right < len(s) and s[left] == s[right]:
>             left -= 1
>             right += 1
>         return s[left + 1:right]
>
>     result = ""
>     for i in range(len(s)):
>         # Odd length
>         odd = expand(i, i)
>         if len(odd) > len(result):
>             result = odd
>         # Even length
>         even = expand(i, i + 1)
>         if len(even) > len(result):
>             result = even
>
>     return result
> ```
> **Complexity:** O(n²) time, O(1) space

---

## C6: String Compression ⭐⭐
**Task:** Compress a string using counts of repeated characters. Return original if not shorter.

```python
def compress(chars: list) -> int:
    pass

# Example:
# chars = ["a","a","b","b","c","c","c"]
# compress(chars) → 6  # chars becomes ["a","2","b","2","c","3"]
# chars = ["a"] → 1
```

> [!hint]- 💡 Hint 1 (Low)
> Track the current character and its count.

> [!hint]- 💡 Hint 2 (Mid)
> When the character changes, write the count to the array.

> [!hint]- 💡 Hint 3 (High)
> Only write the count if it's greater than 1. Convert count to string for multi-digit.

> [!success]- Solution
> ```python
> def compress(chars: list) -> int:
>     write = 0
>     read = 0
>
>     while read < len(chars):
>         char = chars[read]
>         count = 0
>
>         while read < len(chars) and chars[read] == char:
>             read += 1
>             count += 1
>
>         chars[write] = char
>         write += 1
>
>         if count > 1:
>             for digit in str(count):
>                 chars[write] = digit
>                 write += 1
>
>     return write
> ```
> **Complexity:** O(n) time, O(1) space

---

## C7: Valid Parentheses ⭐⭐
**Task:** Check if brackets are valid and properly closed.

```python
def is_valid(s: str) -> bool:
    pass

# Example:
# is_valid("()[]{}") → True
# is_valid("(]") → False
# is_valid("([)]") → False
# is_valid("{[]}") → True
```

> [!hint]- 💡 Hint 1 (Low)
> Use a stack to track opening brackets.

> [!hint]- 💡 Hint 2 (Mid)
> When you see a closing bracket, check if it matches the top of the stack.

> [!hint]- 💡 Hint 3 (High)
> Use a dictionary to map closing to opening brackets.

> [!success]- Solution
> ```python
> def is_valid(s: str) -> bool:
>     stack = []
>     pairs = {')': '(', ']': '[', '}': '{'}
>
>     for char in s:
>         if char in pairs:  # Closing bracket
>             if not stack or stack[-1] != pairs[char]:
>                 return False
>             stack.pop()
>         else:  # Opening bracket
>             stack.append(char)
>
>     return len(stack) == 0
> ```
> **Complexity:** O(n) time, O(n) space

---

## C8: Minimum Window Substring ⭐⭐⭐⭐⭐
**Task:** Find minimum window in s containing all characters of t.

```python
def min_window(s: str, t: str) -> str:
    pass

# Example:
# min_window("ADOBECODEBANC", "ABC") → "BANC"
# min_window("a", "a") → "a"
# min_window("a", "aa") → ""
```

> [!hint]- 💡 Hint 1 (Low)
> Use sliding window with two pointers.

> [!hint]- 💡 Hint 2 (Mid)
> Expand right to include all chars, then shrink left to minimize.

> [!hint]- 💡 Hint 3 (High)
> Track how many required characters are satisfied with a counter.

> [!success]- Solution
> ```python
> from collections import Counter
>
> def min_window(s: str, t: str) -> str:
>     if not s or not t:
>         return ""
>
>     need = Counter(t)
>     required = len(need)
>     formed = 0
>     window = {}
>
>     left = 0
>     min_len = float('inf')
>     result = ""
>
>     for right, char in enumerate(s):
>         window[char] = window.get(char, 0) + 1
>
>         if char in need and window[char] == need[char]:
>             formed += 1
>
>         while formed == required:
>             if right - left + 1 < min_len:
>                 min_len = right - left + 1
>                 result = s[left:right + 1]
>
>             left_char = s[left]
>             window[left_char] -= 1
>             if left_char in need and window[left_char] < need[left_char]:
>                 formed -= 1
>             left += 1
>
>     return result
> ```
> **Complexity:** O(s + t) time, O(s + t) space

---

## C9: Decode String ⭐⭐⭐
**Task:** Decode an encoded string like "3[a2[c]]" → "accaccacc".

```python
def decode_string(s: str) -> str:
    pass

# Example:
# decode_string("3[a]2[bc]") → "aaabcbc"
# decode_string("3[a2[c]]") → "accaccacc"
# decode_string("2[abc]3[cd]ef") → "abcabccdcdcdef"
```

> [!hint]- 💡 Hint 1 (Low)
> Use a stack to handle nested brackets.

> [!hint]- 💡 Hint 2 (Mid)
> Push current string and count when you see '[', pop and multiply when you see ']'.

> [!hint]- 💡 Hint 3 (High)
> Maintain current_string and current_num, use stack for nested contexts.

> [!success]- Solution
> ```python
> def decode_string(s: str) -> str:
>     stack = []
>     current_string = ""
>     current_num = 0
>
>     for char in s:
>         if char.isdigit():
>             current_num = current_num * 10 + int(char)
>         elif char == '[':
>             stack.append((current_string, current_num))
>             current_string = ""
>             current_num = 0
>         elif char == ']':
>             prev_string, num = stack.pop()
>             current_string = prev_string + current_string * num
>         else:
>             current_string += char
>
>     return current_string
> ```
> **Complexity:** O(n × max_k) time, O(n) space

---

## C10: Longest Common Prefix ⭐⭐
**Task:** Find the longest common prefix among an array of strings.

```python
def longest_common_prefix(strs: list) -> str:
    pass

# Example:
# longest_common_prefix(["flower","flow","flight"]) → "fl"
# longest_common_prefix(["dog","racecar","car"]) → ""
```

> [!hint]- 💡 Hint 1 (Low)
> The common prefix can't be longer than the shortest string.

> [!hint]- 💡 Hint 2 (Mid)
> Compare characters at each position across all strings.

> [!hint]- 💡 Hint 3 (High)
> Use `zip(*strs)` to iterate through character positions together.

> [!success]- Solution
> ```python
> def longest_common_prefix(strs: list) -> str:
>     if not strs:
>         return ""
>
>     prefix = []
>     for chars in zip(*strs):
>         if len(set(chars)) == 1:
>             prefix.append(chars[0])
>         else:
>             break
>
>     return ''.join(prefix)
>
> # Alternative: compare with first string
> def longest_common_prefix_v2(strs: list) -> str:
>     if not strs:
>         return ""
>     prefix = strs[0]
>     for s in strs[1:]:
>         while not s.startswith(prefix):
>             prefix = prefix[:-1]
>             if not prefix:
>                 return ""
>     return prefix
> ```
> **Complexity:** O(n × m) where m = shortest string length

---

## 🎯 String Challenges Complete!

**Skills Practiced:**
- Sliding Window
- Two Pointers
- Stack-based parsing
- Character counting
- String manipulation

**Next Challenge:** [[13_Challenge_Math|Math & Logic Challenges]]
