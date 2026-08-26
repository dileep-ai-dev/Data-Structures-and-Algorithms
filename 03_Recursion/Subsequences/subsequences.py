# Generate all subsequences using Include / Exclude pattern

def generate_subsequences(arr, index, current, result):

    # Base Case
    if index == len(arr):
        result.append(current.copy())
        return

    # Include
    current.append(arr[index])
    generate_subsequences(arr, index + 1, current, result)

    # Backtrack
    current.pop()

    # Exclude
    generate_subsequences(arr, index + 1, current, result)


arr = [1, 2, 3]

result = []

generate_subsequences(arr, 0, [], result)

print("All Subsequences:")

for subsequence in result:
    print(subsequence)