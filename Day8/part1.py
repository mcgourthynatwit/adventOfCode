network = {}

def clean(line):
    element = line.split(" = ", 1)
    rem = element[1]

    rem = rem.replace('(', '') 
    rem = rem.replace(')', '')
    rem = rem.replace(',', '')

    instructions = rem.split(" ", 1)
    
    return element[0].strip(), instructions[0].strip(), instructions[1].strip()

def main():
    steps = "LRLRLRRLRRLRLRRRLRRLRLRRLLLRRRLRRRLLRRLRRRLRRRLRRLRRLRRRLRRLRLRLRRRLRRLRRLLRRRLLRLRRRLRRRLRRLRRRLRRLLRLLRRRLRRLRLRRRLRLRLRRRLLRLRRLLRRRLRRRLRLRRLLRRLRLRRLRRRLRLLRRRLRRRLLRLLRLLRRRLRLRLRLRLRRLRRLRLRRRLLLRLLRRRLRRLLRLRLRRRLLRLRRRLLRRLRRLRLRLRLRRLRRLRRRLRRRLRRLRRLRRRLRLRRRLRLRRRR"

    file = open("input.txt")
    lines = file.readlines()

    for line in lines:
        el, l, r = clean(line)
        network[el] = [l, r]

    current = "AAA"
    count = 0
    
    while current != "ZZZ":
        if steps[0] == "L":
            current = network[current][0]
        else:
            current = network[current][1]

        steps = steps[1:] + steps[0]
        count += 1
    print(count)
        

main()
    
