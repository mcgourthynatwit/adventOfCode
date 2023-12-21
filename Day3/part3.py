def main():
    file = open("Day3/testInput.txt")
    lines = file.readlines()
    for line in lines:
        print(line)

main()

def getCoords(txt):
    idx = 0
    num_arr = []
    dig_arr = []
    nums = []
    for c in txt:
        if c is '.':
            idx += 1
            continue
        elif c.isDigit():
            num_arr.push(idx)
        else:

def getDiagonal(arr):
