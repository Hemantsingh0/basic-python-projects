known_users = ["Himanshu","Jyoti","Rishi","Arti","Lalita","Shyam","Dulari"]

print(len(known_users))

while True:
    print("Hi My name is travis")
    name= input("please enter your name:").strip().capitalize()

    if name in known_users:
        print("hello {}.".format(name))
        remove=input("would you like to be removed from the system (Y/N)?:").strip().lower()

        if remove == "y":
            known_users.remove(name)
        elif remove == "n":
            print("it's okay, i am happy to see you")
    else:
       print("Hmm i don't think i have met you yet {}".format(name))
       add_me =input("would you like to be added to the system (Y/N)?:").strip().lower()
       if add_me=="y":
           known_users.append(name)
       elif add_me == "n":
            print("no worries, you can leave immediately!")
           
           
       
