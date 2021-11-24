#Set all values for movie title, year and a fun fact
title = ['Matrix', 'Blade Runner 2049', 'Pulp Fiction', 'The Fast and the Furious', 'Spider Man: Into the Spider-Verse', 'Creep 2', 'The Book of Life', 'Coco', 'Don\'t Breath 2', 'I am Legend']
year = ['1999', '2017', '1994', '2001', '2018', '2017', '2014', '2017', '2021', '2007']
fun_fact = ['Was originally a graphic novel', 'The original cut of the movie was 4 hours long', 'A quarter pounder with cheese is called a Royale with cheese in France', 'Vin Diesel broke a stuntman\'s nose', 'Stan Lee can be seen standing on a train in one of the movie\'s subways', 'Mark Duplass messed up while trimming his beard, resulting in a noticeable patch of bare skin. An explanation was invented for his character', 'The main character sang a cover of Creep by Radiohead', 'Coco is more popular in China than in the US', 'This movie takes place 8 years after the first film', 'The flashback scene involving the collapse of the Brooklyn Bridge cost $5 million']

#Runs loop if user chooses 'y'
user_continue = "y"
while user_continue == 'y':
    #Print out each title and where it is in the list
    for i in range(len(title)):
        print(i+1, title[i])
    print((len(title)+1), "Add a new movie")
    user_choice = int(input("Which movie would you like to learn about? "))

    #In the case that the user chooses to add a new movie
    if user_choice == len(title)+1:
        title.insert(len(title), input("What is the title of the new movie?"))
        year.insert(len(year), int(input("What is the year of the new movie?")))
        fun_fact.insert(len(fun_fact), input("What is the fun fact about the new movie?"))
        print("Thank you for adding the new movie")
    else:
        print('Invalid Input')
        break

    #Prints the details of the movie the user chose
    print(title[user_choice-1])
    print(year[user_choice-1])
    print(fun_fact[user_choice-1])
    user_continue = input("Would you like to learn about another movie? (y/n)")
    if user_continue == 'n':
        print("Thank you for using the program")
        break
    else:
        continue
