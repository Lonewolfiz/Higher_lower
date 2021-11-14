import art
import game_data as gd
from replit import clear
import random as rn
print(art.logo)
def random_func():
  return rn.choice(gd.data)
def compare_func(compare_a,compare_b):
  if compare_a>compare_b:
    return 'A'
  else:
    return 'B'  
def final_func(Answer,Guess):
  if Answer==Guess:
    return True
  else:
    return False  
is_game_over=False
count=0
while not is_game_over:
  compare_a=random_func()
  compare_b=random_func()

  print(f"{compare_a['name']} , {compare_a['description']} , {compare_a['country']}")
  print(art.vs)
  print(f"{compare_b['name']} , {compare_b['description']} , {compare_b['country']}")

  Answer=compare_func(compare_a['follower_count'],compare_b['follower_count'])
  Guess=input("Who has more followers? Type 'A' or 'B' : ")

  final_Answer=final_func(Answer,Guess)
  if final_Answer==True:
    count+=1
    clear()
    print(f"You're right. Current Score : {count}")
  else:
    is_game_over=True
    clear()
    print(f"Sorry that's wrong. Final score : {count}")

  