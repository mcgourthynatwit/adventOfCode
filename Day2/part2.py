def clean(line):
    line = line.replace("," , "")
    parts = line.split(":", 1)
    ID = parts[0].strip().split()[1]
    line = parts[1].strip()

    return line, ID

def split(line):    
    pairs = []
    parts = line.split()

    for i in range(0, len(parts), 2):
        number = parts[i]
        color = parts[i + 1]
        pairs.append((number, color))
    
    return pairs 
def main():
    file = open("Day2/input.txt")
    total = 0

    lines = file.readlines()
    for line in lines:
        
        # clean input
        line, ID =  clean(line)
        sets = line.split(";")

        # split lines
        valid = True 
        red_count = 0
        green_count = 0
        blue_count = 0
        for s in sets:


            pairs = split(s.strip())
            
            for number, color in pairs:
                if color == "red" and int(number) > red_count:
                    red_count = int(number)
                elif color == "blue" and int(number) > blue_count :
                    blue_count = int(number)
                elif color == "green" and int(number) > green_count:
                    green_count = int(number)
        total += (blue_count * red_count * green_count)    
        print('for line', line ,' the total is ', total, red_count, green_count, blue_count)
       
       
    print(total)
             



main()