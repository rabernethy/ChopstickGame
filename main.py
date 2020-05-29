# hand game
    #Moves: Attack, Split
        # Attack [You] [Them] (acceptable args for "You" and "Them" are 'L' and 'R')
        # Split
cpuLeft = cpuRight = humanLeft = humanRight = 1

# game loop:
while True:
    print("CPU: ", cpuLeft, " ", cpuRight)
    print("You: ", humanLeft, " ", humanRight)
    
    # Player Move
    while True:
        move = input("Enter A Move: ")
        if move.startswith('Attack' or 'attack'):
            # Player attacks with Left Hand
            if move[7:8] is 'L' or 'l':
                if move[9:10] is 'L' or 'l':
                    cpuLeft += humanLeft
                    break
                if move[9:10] is 'R' or 'r':
                    cpuRight += humanLeft
                    break
            # Player Attacks with Right Hand    
            if move[7:8] is 'R' or 'r':
                if move[9:10] is 'L' or 'l':
                    cpuLeft += humanRight
                    break
                if move[9:10] is 'R' or 'r':
                    cpuRight += humanLeft
                    break
        if (move.startswith('Split' or 'split') and (humanLeft != humanRight) and (humanLeft or humanRight == 2) or (humanLeft or humanRight == 4)):
            if (humanLeft or humanRight) == 2:
                humanLeft = humanRight = 1
                break
            if (humanLeft or humanRight) == 4:
                humanLeft = humanRight = 2
                break
        if(move.startswith('Help' or 'help')):
            print("\nAttack [Your hand] [CPU hand] (\"Your hand\" and \"CPU hand\" can take the arguments 'L' or 'R')")
            print("Splice")
    
    # CPU Clean Up:
    if cpuLeft >= 5:
        cpuLeft = 0
    if cpuRight >= 5:
        cpuRight = 0
    
    print("CPU: ", cpuLeft, " ", cpuRight)
    print("You: ", humanLeft, " ", humanRight)
    
    # CPU Move:
        # Attack To Kill:
    if humanRight + cpuRight >= 5:
        humanRight += cpuRight
        print("CPU Attack R R")
    elif humanRight + cpuLeft >= 5:
        humanRight += cpuLeft
        print("CPU Attack L R")
    elif humanLeft + cpuRight >= 5:
        humanLeft += cpuRight
        print("CPU Attack R L")
    elif humanLeft + cpuLeft >= 5:
        humanLeft += cpuLeft
        print("CPU Attack L L")
        
        # Split:
    elif ((cpuLeft != cpuRight) and ((cpuLeft or cpuRight) == 0) and ((cpuLeft or cpuRight) == 2) or ((cpuLeft or cpuRight) == 4)):
        if (cpuLeft or cpuRight) == 2:
            cpuLeft = cpuRight = 1
        if(cpuLeft or cpuRight) == 4:
            cpuLeft = cpuRight = 2
        print("CPU Split")
        
        # Attack Normal:
    elif cpuLeft > cpuRight:
        if humanLeft > humanRight:
            humanLeft += cpuLeft
            print("CPU Attack L L")
        else:
            humanRight += cpuLeft
            print("CPU Attack L R")
    else:
        if humanLeft > humanRight:
            humanLeft += cpuRight
            print("CPU Attack R L")
        else:
            humanRight += cpuRight
            print("CPU Attack R R")
        
    # Human Clean Up:
    if humanLeft >= 5:
        humanLeft = 0
    if humanRight >= 5:
        humanRight = 0
        
    # Game Clean Up:
        if (humanLeft and humanRight) == 0:
            print("Sorry, you lost.")
            break
        if (cpuLeft and cpuRight) == 0:
            print("Congrats, you won!")
            break
