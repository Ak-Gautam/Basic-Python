#This function is to decide the winner 
def result(y) :
    flag = False
    if [y.get(1), y.get(2), y.get(3)] == [p1, p1, p1]:
        flag = True
        print("Player1 wins")
    elif [y.get(4), y.get(5), y.get(6)] == [p1, p1, p1]:
        flag = True
        print("Player1 wins")
    elif [y.get(1), y.get(4), y.get(7)] == [p1, p1, p1]:
        flag = True
        print("Player1 wins")
    elif [y.get(7), y.get(8), y.get(9)] == [p1, p1, p1]:
        flag = True
        print("Player1 wins")
    elif [y.get(2), y.get(5), y.get(8)] == [p1, p1, p1]:
        flag = True
        print("Player1 wins")
    elif [y.get(3), y.get(6), y.get(9)] == [p1, p1, p1]:
        flag = True
        print("Player1 wins")
    elif [y.get(1), y.get(5), y.get(9)] == [p1, p1, p1]:
        flag = True
        print("Player1 wins")
    elif [y.get(3), y.get(5), y.get(7)] == [p1, p1, p1]:
        flag = True
        print("Player1 wins")
    elif [y.get(1), y.get(2), y.get(3)] == [p2, p2, p2]:
        flag = True
        print("Player2 wins")
    elif [y.get(4), y.get(5), y.get(6)] == [p2, p2, p2]:
        flag = True
        print("Player2 wins")
    elif [y.get(7), y.get(8), y.get(9)] == [p2, p2, p2]:
        flag = True
        print("Player2 wins")
    elif [y.get(1), y.get(4), y.get(7)] == [p2, p2, p2]:
        flag = True
        print("Player2 wins")
    elif [y.get(2), y.get(5), y.get(8)] == [p2, p2, p2]:
        flag = True
        print("Player2 wins")
    elif [y.get(3), y.get(6), y.get(9)] == [p2, p2, p2]:
        flag = True
        print("Player2 wins")
    elif [y.get(1), y.get(5), y.get(9)] == [p2, p2, p2]:
        flag = True
        print("Player2 wins")
    elif [y.get(3), y.get(5), y.get(7)] == [p2, p2, p2]:
        flag = True
        print("Player2 wins")
    return flag

#Declaring the dict and creating the "graphical" formal of the game

pos = {1: '-', 2: '-', 3: '-', 4: '-', 5: '-', 6: '-', 7: '-', 8: '-', 9: '-'}

print("", pos[1]+ "  | "+pos[2]+ " |  "+pos[3]+ "\n",
      "------------\n",
     pos[4]+ "  | "+pos[5]+ " |  "+pos[6]+ "\n",
      "------------\n",
     pos[7]+"  | "+pos[8]+" |  "+pos[9]+"\n")

#A simple Toss and player selection

import random
z = input("Press any key to toss")
toss = random.randint(0, 1)
toss = 'Head' if toss == 0 else 'Tail'
print(toss)

p1 = input("player one sign (x/o)\n")
p2 = 'o' if p1 == 'x' else 'x'
print("\nPlayer1 "+p1,
     "Player2 "+p2)

print("player1 Choose location 1 ,2 ,3\n\t\t\t4, 5, 6\n\t\t\t...\n")

#Actual program running the game

use = [0]            #A little feature to not use the used spot
for i in range(0, 5):
    if i == 5:
        break
    loc1 = int(input("Player1 enter the location\n"))
    if loc1 in use:                                        #This line ensures single use
        print("Location taken. Enter Another location\n")
        continue
    use.append(loc1)
    pos[loc1] = p1
    print("", pos[1]+ "  | "+pos[2]+" |  "+pos[3]+"\n",
          "------------\n",
         pos[4]+"  | "+pos[5]+" |  "+pos[6]+"\n",
          "------------\n",
         pos[7]+"  | "+pos[8]+" |  "+pos[9]+"\n")
    f = result(pos)
    if f == True:
        break
    if i == 4:
        continue
    loc2 = int(input("Player2 enter the location\n"))
    if loc2 in use:
        print("Location taken. Enter Another location\n")
        loc2 = int(input(" Player2 Enter a valid position\n"))   # Ugly approach but could not figure out better way 
        if loc2 in use:
            print("Start again\n")
            break
    use.append(loc2)
    pos[loc2] = p2
    print("", pos[1]+ "  | "+pos[2]+" |  "+pos[3]+"\n",
          "------------\n",
         pos[4]+"  | "+pos[5]+" |  "+pos[6]+"\n",
          "------------\n",
         pos[7]+"  | "+pos[8]+" |  "+pos[9]+"\n")
    f = result(pos)
    if f == True :
        break
print("Game Over")
