from replit import clear
from art import logo

print(logo)
print("Welcome to Secret auction program")
dict = {}
condition = True
while condition:
  name = input("Enter your name\n")
  bid = int(input("Whats your bid?\n"))
  choice = input("are there any other bidders? type 'yes' or 'no'\n")
  dict[name] = bid

  if choice == "yes":
    clear()
  else:
    max = 0
    winner = ""
    for i in dict:
      if dict[i] > max:
        max = dict[i]
        winner = i
    print(f"the highest bid by {winner} is {max}")
    condition = False
