def solve() -> int:
    with open("input.txt", "r") as file:
        lines = file.readlines()

    nums = {'zero':0,'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
            'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    total = 0

    for line in lines:
        combined = [] 

        for i, char in enumerate(line):
            for key, word in enumerate(nums):
                if word in line[i:i+len(word)]:
                    combined.append(str(nums[word]))
            if char.isdigit():
                combined.append(char)

        if combined:
            total += int(combined[0] + combined[-1])

    return total

print(solve())