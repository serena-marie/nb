# 01
Have a file of strings, want to return a list that contains one of each duplicate string, where characters might be in a diff order

i.e
```
dkjs
gjfo
skdj
abfc
```
Output would be 
['dkjs']

How would I accomplish this in JS?
- Iterate through entire file, sorting each string, alphabetically, store in data structure
- Iterate through data structure if it doesn't exist, push, otherwise continue.

Could I do this any differently in Python?
- Create a list of dicts. Each dict is a frequency dict. Compare each word.

Would be O(n), but I wonder if there's a quicker way. 

> How does this compare to the problem of counting the number of occurrences of letters in a string? How will you know if a word has been seen before, if the letters are all jumbled the next time you see it? What control structures (if statements, for loops) will you need to use to solve this problem?

