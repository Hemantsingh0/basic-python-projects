#random module gives random number between two digits
import random

#initially the health is reserved at 50
health= 50

#from difficulty function, we can set difficulty level from 1 to 3
difficulty = 2

#potion health random no. b/w 25 and 50 divided by difficulty level and by casting it is also defined as int type data
potion_health= int(random.randint(25,50) / difficulty)

#health is now sum of original health + potion_health
health = (health + potion_health)

#now we print value of health 
print(health)
