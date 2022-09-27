films={
    "Kabir Singh":[3,4],
    "Raaz":[15,4],
    "Brahmastra":[12,9],
    "Ghost Rider":[20,1],
    }

while True:
    choice=input("which movie you want to see:?").strip().title()

    if choice in films:
        age=int(input("how old are you?:").strip())

        #check user age

        if age >= films[choice][0]:
            #check enough seats are available or not
           num_seats = films[choice][1]

           if num_seats > 0:
              print("enjoy the film")
              films[choice][1]=films[choice][1]-1
           else: 
                print("sorry.. we are sold out")
        else: 
            print("you are too young to see that film")
    else:
        print("sorry, we don't have that film...")
