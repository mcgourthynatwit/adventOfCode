def clean(line):
    line = line.split(":")
    line = line[1].split("|")
    return line[0], line[1]

def getNums(numbers):
    retNums = []
    num = ""
    
    for c in numbers:
        if c == " ":
            if num:
                retNums.append(int(num))
                num = ""
        else:
            num = num + c

    # Add the end character
    if num != "":
        retNums.append(int(num))
    return retNums

def getTotalWinnings(winningNumbers, actualNumbers):
    total = 0
    for nums in actualNumbers:
        if nums in winningNumbers:
            total += 1
    return total

def main():
    file = open("Day4/input.txt")

    lines = file.readlines()
    total = 0
    n = 6
    scratch_arr = [1] * 206
    idx = 0 

    for line in lines:
        winning, actual = clean(line)
        actualNumbers = getNums(actual)
        winningNumbers = getNums(winning)

        cardTotal = getTotalWinnings(winningNumbers, actualNumbers)
        matches = 0

        print(cardTotal)

        for cards in range(1, cardTotal + 1):
            newIdx = idx + cards
            scratch_arr[idx + cards] += scratch_arr[idx]
        idx += 1        
        print(sum(scratch_arr))

main()