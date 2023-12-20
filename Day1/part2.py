strToNum = {
    "one" : "1",
    "two" : "2",
    "three" : "3",
    "four" : "4",
    "five" : "5",
    "six" : "6",
    "seven" : "7",
    "eight" : "8",
    "nine" : "9",
}
def getFirstNum(inputString) :
    concatString = ""
    val = None
    for c in inputString:
        if c.isdigit():
            return c
        concatString = concatString + c
        for key in strToNum:
            if key in concatString:
                return strToNum[key]

        
def getSecondNum(inputString) :
    concatString = ""
    val = None
    for c in reversed(inputString):
        if c.isdigit():
            return c
        concatString = c + concatString
    
        for key in strToNum:
            if key in concatString:
                return strToNum[key]

def main() :
    
    file = open("Day1/input.txt")
    total = 0

    lines = file.readlines()
    for line in lines:
        text = line.strip()
        first = getFirstNum(text)
        second = getSecondNum(text)
        print("The text is ", text, " the nums are ", first, second)
        val = first + second
        total += int(val)
    print(total)

main()



