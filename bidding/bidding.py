from art import logo

def confirmation():
  person = {}
  name = input("what's your name?")
  bid = int(input("What's your bid? $"))
  person [name] = bid
  
  confirm = input("Are there any other bidders? ")
  if (confirm.lower == "yes"):
    confirmation()

  biggest = 0
  owner = ""
  for k in person:
    if (person[k] > biggest):
      biggest = person[k]
      owner = k
      
  print(f'the winner is {owner} and the bid is {biggest}')
  
print(logo)
confirmation()
