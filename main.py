import random
import replit
from art import logo

def deal(selections):
  card = random.choice(selections)
  return card


def aceDrawn(cards):
  for card in cards:
    if 11 in cards and sum(cards) > 21:
      cards[cards.index(11)] = 1


def black_jack(cards):
  if 10 in cards and 11 in cards:
    return True
  else:
    return False


def calculate(cards):
  cardSum = sum(cards)
  return cardSum


def check(user, comp):
  if user == "BlackJack":
    print("You win")
  elif comp == "BlackJack":
    print("You lose")
  if user == "loss":
    print("You lose!")
  elif comp == "loss":
    print("You win!")
  elif user > comp:
    print("You win!")
  elif user < comp:
    print("You lose!")
  else:
    print("Draw!")


def BlackJack():
  gameOn = True
  print(logo)
  card_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
  user_cards = []
  cpu = []
  user_cards.append(deal(card_list))
  cpu.append(deal(card_list))
  cpu = []
  while gameOn:
    user_cards.append(deal(card_list))
    cpu.append(deal(card_list))
    aceDrawn(cpu)
    aceDrawn(user_cards)
    bj_user = black_jack(user_cards)
    bj_cpu = black_jack(cpu)
    if bj_user:
      user_total = "BlackJack"
      print("BlackJack! You win")
    else:
      user_total = calculate(user_cards)
      if user_total > 21:
        gameOn = False
        print("You lose!")
      if bj_cpu:
        cpu_total = "BlackJack"
        print("Computer has BlackJack, You lose")
        gameOn = False
      else:
        cpu_total = calculate(cpu)
    print(f"User Cards: {user_cards}")
    print(f"Total: {user_total}")
    print(f"Computer's cards: {cpu[0]}")
    

    if gameOn:
      again = input("Would you like to draw another card? (Y/N)").lower()
      if again == "n":
        while calculate(cpu) < 17:
          cpu.append(deal(card_list))
          aceDrawn(cpu)
        cpu_total = calculate(cpu)
        check(user_total, cpu_total)
        print(f"final hand user: {user_cards}")
        print(f"final hand cpu: {cpu}")
        gameOn = False

    if gameOn == False:
      play_again = input("Would you like to play again? (Y/N)").lower()
      if play_again == "y":
        replit.clear()
        BlackJack()
BlackJack()