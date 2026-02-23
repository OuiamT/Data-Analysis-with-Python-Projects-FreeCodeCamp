# Mean-Variance-Standard Deviation Calculator:

## 📋 Overview:
This project takes **9 digits** as input, reshapes them into a **3×3 NumPy matrix**, and calculates the following statistics along both axes and for the flattened matrix:
- Mean
- Variance
- Standard Deviation
- Maximum
- Minimum
- Sum

## 📊 Output Format:

The result is a dictionary where each key maps to a list of three elements:
```
[columns, rows, flattened]
```

### Example:

**Input:** `123456789`

**Matrix:**
```
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
```

**Output:**
```python
{
  'mean':               [[4.0, 5.0, 6.0], [2.0, 5.0, 8.0], 5.0],
  'variance':           [[6.0, 6.0, 6.0], [0.67, 0.67, 0.67], 6.67],
  'standard deviation': [[2.45, 2.45, 2.45], [0.82, 0.82, 0.82], 2.58],
  'max':                [[7, 8, 9], [3, 6, 9], 9],
  'min':                [[1, 2, 3], [1, 4, 7], 1],
  'sum':                [[12, 15, 18], [6, 15, 24], 45]
}
```

## ⚙️ How It Works:

| Function | Description |
|---|---|
| `calculate(list_of_nine_numbers)` | Reshapes the input list into a 3×3 matrix and returns all statistics |
| `calculate_var(my_list, var)` | Computes a specific statistic along axis 0, axis 1, and flattened |

The script uses a `while` loop for user input with validation. There are two approaches to enforce exactly 9 digits:

**Approach 1 — Regex:**
```
if re.search(r"^\d{9}$", nine_numbers):
    print(calculate(list(map(lambda x: int(x), list(nine_numbers)))))
```
`re.search()` scans the string for any 9 consecutive digits. Note that `list(nine_numbers)` is needed inside `map()` to split the string into individual characters before converting each to an integer.

**Approach 2 — `len()`:**
```
nine_numbers = list(input("Enter nine numbers:"))   # cast to list

if len(nine_numbers) == 9:
    print(calculate(list(map(lambda x: int(x), nine_numbers))))
```
Here, the input string is cast to a `list` immediately, so each character becomes an element. The `len()` check then confirms there are exactly 9 elements, and the `list()` call inside `map()` is no longer needed since `nine_numbers` is already a list.

## ⚠️ Input Constraints:

- Input must be exactly 9 digits
- No spaces, commas, or other separators

## 🗂️ Project Structure:

```
.
├── main.py       # Main script with calculate() and calculate_var() functions
└── README.md     # Project documentation
```