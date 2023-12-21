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

    for line in lines:
        winning, actual = clean(line)
        actualNumbers = getNums(actual)
        winningNumbers = getNums(winning)

        cardTotal = getTotalWinnings(winningNumbers, actualNumbers)

        if (cardTotal > 0) :
            total += (2 ** (cardTotal - 1))
        
    print(total)




main()