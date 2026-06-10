from pathlib import Path
import time

# ---------------------------------------------------------------
# Load numbers from file
# ---------------------------------------------------------------
def load_numbers(filename):
    path = Path(filename)
    content = path.read_text()
    return [int(line) for line in content.splitlines() if line.strip()]


# ---------------------------------------------------------------
# LINEAR SEARCH
# Checks every number one by one from the start.
# ---------------------------------------------------------------
def linear_search(numbers, target):
    for index, value in enumerate(numbers):
        if value == target:
            return index   # found it
    return -1              # not found


# ---------------------------------------------------------------
# BINARY SEARCH
# Requires a sorted list. Splits the search area in half each step.
# ---------------------------------------------------------------
def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] == target:
            return mid          # found it
        elif numbers[mid] < target:
            left = mid + 1      # target is in the right half
        else:
            right = mid - 1     # target is in the left half

    return -1                   # not found


# ---------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------
def main():
    numbers = load_numbers('large_data.txt')

    print("=" * 55)
    print(f"  Loaded {len(numbers)} sorted numbers from large_data.txt")
    print("=" * 55)

    # We pick the LAST number as the target — this is the
    # WORST CASE for linear search (it has to check every single
    # number before finding it at the very end).
    target = numbers[-1]
    print(f"\n  Target number to find: {target}")
    print(f"  (This is the last number in the list — worst case!)\n")

    # -----------------------------------------------------------
    # Run LINEAR SEARCH and measure time
    # -----------------------------------------------------------
    print("-" * 55)
    print("  LINEAR SEARCH")
    print("-" * 55)

    # Repeat many times so the timer can measure a meaningful gap
    REPEAT = 100_000

    start = time.perf_counter()
    for _ in range(REPEAT):
        result_lin = linear_search(numbers, target)
    end = time.perf_counter()

    lin_time = (end - start) / REPEAT  # average time per search

    if result_lin != -1:
        print(f"  Found {target} at index {result_lin}")
    else:
        print(f"  {target} was NOT found")
    print(f"  Time per search : {lin_time:.8f} seconds")
    print(f"  ({REPEAT:,} runs averaged)\n")

    # -----------------------------------------------------------
    # Run BINARY SEARCH and measure time
    # -----------------------------------------------------------
    print("-" * 55)
    print("  BINARY SEARCH")
    print("-" * 55)

    start = time.perf_counter()
    for _ in range(REPEAT):
        result_bin = binary_search(numbers, target)
    end = time.perf_counter()

    bin_time = (end - start) / REPEAT

    if result_bin != -1:
        print(f"  Found {target} at index {result_bin}")
    else:
        print(f"  {target} was NOT found")
    print(f"  Time per search : {bin_time:.8f} seconds")
    print(f"  ({REPEAT:,} runs averaged)\n")

    # -----------------------------------------------------------
    # Comparison summary
    # -----------------------------------------------------------
    print("=" * 55)
    print("  COMPARISON SUMMARY")
    print("=" * 55)
    print(f"  Linear  : {lin_time:.8f} sec")
    print(f"  Binary  : {bin_time:.8f} sec")

    if bin_time > 0:
        speedup = lin_time / bin_time
        print(f"\n  Binary search was {speedup:.1f}x FASTER than linear search!")

    print("=" * 55)


if __name__ == '__main__':
    main()
