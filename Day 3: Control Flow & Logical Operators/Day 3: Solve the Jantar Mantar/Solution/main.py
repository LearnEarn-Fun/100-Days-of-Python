
welcome = """
░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ████████╗░█████╗░
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ╚══██╔══╝██╔══██╗
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ░░░██║░░░██║░░██║
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ░░░██║░░░██║░░██║
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ░░░██║░░░╚█████╔╝
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ░░░╚═╝░░░░╚════╝░
"""

logo = """
    __                       _   __                    
   / / _   _    /7  _   _   / \,' / _   _    /7  _   _ 
n_/ /,'o| / \/7/_7,'o| //7 / \,' /,'o| / \/7/_7,'o| //7
\_,' |_,7/_n_///  |_,7//  /_/ /_/ |_,7/_n_///  |_,7//  
                                                       
                                                                                                                                             
"""

print(welcome)
print(logo)
print("Your mission is to find the way out of Jantar Mantar")
choice1 = input('You just entered Jantar Mantar! Now there are two ways - 1 to the left & 1 to the right. Type L for Left or R for Right \n').lower()
if choice1 == "l":
  choice2 = input('Great! Now there are three ways, which one do you choose? 1, 2 or 3? \n').lower()
  if choice2 == "1":
        print("There is no way out! You lose. Game Over! \n")
  elif choice2 == "2":
    choice3 = input("There are 2 ways! One of them leads to the out! Which do you choose? 1 or 2 \n")
    if choice3 == "1":
        print("You found the way out! You win!")
    elif choice3 == "1":
        print("You lost Your way! You lose. Game Over! \n")
    else:
        print("You entered something invalid")
  elif choice2 == "3":
    print("There is no way out! You lose. Game Over! \n")
  else:
    print("You entered something invalid")
else:
    print("You entered something invalid")
