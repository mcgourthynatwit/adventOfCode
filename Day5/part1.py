def clean(lines):
    parts = lines.split(":", 1)
    info = parts[1].strip()

    return info
    
def getNums(line):
    retArr = []
    val = ""
    
    for c in line:
        if c.isdigit():
            val = val + c
        elif val != "":
            retArr.append(int(val))
            val = ""
        else:
            val = ""
    retArr.append(int(val))
    return retArr

def getRecord(time, dis):
    held = 0
    ways = 0
    while time > 0 :
        if ( time * held ) > dis:
            ways += 1
        time -= 1
        held += 1
    return ways
   
def main():
    text = open("Day5/input.txt")

    lines = text.readlines()

    timeArr = clean(lines[0])
    disArr = clean(lines[1])

    timeArr = getNums(timeArr)
    disArr = getNums(disArr)

    print(timeArr)
    print(disArr)
    
    total = 0
    
    for vals in range(len(timeArr)):
        ways = getRecord(timeArr[vals], disArr[vals])
        if total == 0:
            total = ways
        else:
            total *= ways
    print(total)
    


main()


