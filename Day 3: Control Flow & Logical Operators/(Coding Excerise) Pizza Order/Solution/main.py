welcome = """
░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ████████╗░█████╗░
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ╚══██╔══╝██╔══██╗
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ░░░██║░░░██║░░██║
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ░░░██║░░░██║░░██║
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ░░░██║░░░╚█████╔╝
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ░░░╚═╝░░░░╚════╝░
"""

logo = """
 +-+-+-+-+-+-+ +-+-+-+-+-+ +-+-+-+-+-+
 |P|y|t|h|o|n| |P|i|z|z|a| |O|r|d|e|r|
 +-+-+-+-+-+-+ +-+-+-+-+-+ +-+-+-+-+-+
"""

print(welcome)
print(logo)
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

detailed_bill = ""

bill = 0
if size == "S":
  bill = 20
  detailed_bill += "Small Pizza: $20"

if size == "M":
  bill = 25
  detailed_bill += "Medium Pizza: $25"
 
if size == "L":
  bill = 30
  detailed_bill += "Large Pizza: $30"

if add_pepperoni == "Y":
  if size == "S":
    bill += 4
    detailed_bill += "\nPepperoni for Small Pizza: $4"
  else:
    bill += 6
    detailed_bill += "\nPepperoni for Medium or Large Pizza: $6"

if extra_cheese == "Y":
    bill += 2
    detailed_bill += "\nExtra Cheese: $2"
print(f"Your bill is ${bill} \n----------------------- \n{detailed_bill}")
