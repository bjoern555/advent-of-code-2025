# 🎄 Advent of Code 2025 Solutions

![Language](https://img.shields.io/badge/language-Python_3.12-blue)
![Completion](https://img.shields.io/badge/stars-22%2F24-yellow)
![Rank](https://img.shields.io/badge/Uni_Rank-Top_6-orange)

## 📖 About
This repository contains my solutions for **AOC 2025**.
I focused on writing clean code in Python, instead of Java.

**Achievement Unlocked:** I secured a position in the **Top 6** on the ZHAW private leaderboard and improved my Python skills a lot!

## 🧠 Key Learnings
### Strategy
* **Draw Always:** Visualization prevents logic errors.
* **New Datastructures** Used defaultdict or deque
* **String Ops:** Construct and compare full strings rather than iterating chars.
* **Clean Logic:** Leverage `min()` / `max()` to handle boundaries concisely.

### Algorithms
* **Intervals:** Sorting is the prerequisite to efficient solutions.
* **Cyclic Logic:** Modulo (`%`) handles wrapping indices perfectly.
* **Dynamic Programming:** Essential when `OPT(i)` relies on previous states (e.g., Knapsack-style).
* **Pathfinding:** BFS remains the go-to for complex state-space searches.
* **HashMaps:** The default choice for counting and tracking non-unique elements.

## 🏃‍♂️ How to Run
To run a solution, you must navigate into the specific day's directory first.
(This ensures the script can find its local `input.txt` file).

**Example:**
```bash
# 1. Enter the directory
cd 2025/day01

# 2. Run the solution
python day01.py