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

        for s in sets:
            red_count = 0
            green_count = 0
            blue_count = 0

            pairs = split(s.strip())
            
            for number, color in pairs:
                if color == "red":
                    red_count += int(number)
                elif color == "blue":
                    blue_count += int(number)
                elif color == "green":
                    green_count += int(number)

            if red_count <= 12 and blue_count <= 14 and green_count <= 13:
                continue
            else:
                valid = False
                break
        if valid is True:
            
            total += int(ID)             
       
    print(total)
             



main()