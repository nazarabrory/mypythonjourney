import random

print("H A N G M A N")
menu = input('Type "play" to play the game, "exit" to quit:', )
if menu == "play":
    word = ['python', 'java', 'kotlin', 'javascript']
    random_word = random.choice(word)
    # print(f"Your word is: {random_word}")

    list_of_word = []
    for q in random_word:
        list_of_word.append(q)

    default_answer = ""
    list_of_answer = []
    for e in list_of_word:
        list_of_answer.append("-")
    for tt in list_of_answer:
        default_answer = default_answer + tt


    set_of_word = set(list_of_word)

    characters = "qwertyuiopasdfghjklzxcvbnm"
    list_of_guess = []
    chances = 8
    answer = default_answer
    #print(answer)
    answer = ""
    while chances != 0:
        print()
        print(answer.join(list_of_answer))
        guess = input("Input a letter: ", )

        if len(guess) > 1:
            print("You should input a single letter")
        elif guess not in characters:
            print("It is not an ASCII lowercase letter")
        elif guess in list_of_guess:
            print("You already typed this letter")
        elif guess in set_of_word:
            for p in range(0, len(list_of_word)):
                if guess == list_of_word[p]:
                    list_of_answer[p] = guess
#        print(answer.join(list_of_answer))
            if "-" not in list_of_answer:
                print("You survived!")
                break
        else:
            print("No such letter in the word")
 #       print(answer.join(list_of_answer))
            chances = chances - 1
        list_of_guess.append(guess)
    else:
        print("You are hanged!")
    menu = input('Type "play" to play the game, "exit" to quit:', )
elif menu == "exit":
    exit()
else:
    menu = input('Type "play" to play the game, "exit" to quit:', )
