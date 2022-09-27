from random import choice

questions=["why shit happens?","what can we do in headache?","when will we die?"]

questions=choice(questions)
answer=input(questions).lower()
while answer != "shut up":
    answer=input("but why?:").lower()
else:
    print("oh...okk")  
