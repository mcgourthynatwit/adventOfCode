
def clean(lines):
    parts = lines.split(":", 1)
    info = parts[1].strip()
    return info
    
def getNums(line):
    
    val = ""
    
    for c in line:
        if c.isdigit():
            val = val + c
    
    return int(val)

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

    time = getNums(timeArr)
    dis = getNums(disArr)

    ways = getRecord(time, dis)
    print(ways)    


main()


