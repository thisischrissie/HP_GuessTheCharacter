import requests
import random
#later I use random.choice() to select a secret character, which is why random is imported


# Requesting data from the URL
# No API key required 
BASE_URL = "https://hp-api.onrender.com/api/characters"


#data is converted into json() and then assigned a variable
all_characters = requests.get(BASE_URL).json()



#I only want to use certain characters from the data. 
# An empty list is created to store the characters I want
valid_characters = []

#The clue properties I want my selected character to have
clue_properties = ['name', 'gender', 'wizard', 'yearOfBirth', 'ancestry', 'hairColour', 'eyeColour', 'alive', 'species']

#To make sure these properties aren't null or empty
for character in all_characters :
    isCharacterValid = True 

    #if props in each character equal nothing, evaluate to false and break the loop
    for prop in clue_properties: 
        if character[prop] == None or character[prop] == '':
            isCharacterValid = False 
            break 
    #append to character list if the props have the values I need
    if isCharacterValid:
        valid_characters.append(character)



#opens the guess_who.txt file to read
with open('guess_who.txt', 'r') as text_file:
    guess_who = text_file.read()

#function to append any printed output to text file
def get_output(output):

    #print output to the console first
    print(output)

    #opens the guess_who.txt to append the printed output
    guess_who = open('guess_who.txt', 'a')
    guess_who.writelines(output + "\n")

    #closes the file
    guess_who.close()


#get_output() function is called with printed message
get_output("""So you think you know your Harry Potter characters? 
The rules are simple, I will select a character at random and give you up to five clues. You can take a guess each time but if you get it wrong we proceed to the next clue. 
Beware, you ONLY get five clues; the first clue is worth TEN points to your house, the second clue is worth EIGHT points, all the way down to the final clue which is only worth a measley TWO points.""")

#function will take user input to append to the guess_who file
def get_input():

    #wait for user input
    user_response = input()

    #opens text file to append input
    guess_who = open('guess_who.txt', 'a')
    guess_who.writelines(user_response + "\n")

    #close file
    guess_who.close()

    #ensures user response is returned to the console
    return user_response 


#function will get user output and checks if it says 'alohomora' before proceeding. If not, it loops back to repeat the request
def intro():
    start = ''
    while start.lower() != "alohomora":
        get_output("Good luck and type 'ALOHOMORA' to unlock your first clue: ")
        start = get_input()
    return

intro()



#Selects a random character from list
selected_character = random.choice(valid_characters)


#Clues list which will store all the character values I want to use. 
# They are presented to the user as concatenated strings. 
round_clues = [
    #round_clues[0]
    ["I am a man" if selected_character['gender'] == 'male' else "I am a woman", 
    "born in the year " + str(selected_character['yearOfBirth']),
    "and yes, of course, I am a wizard." if selected_character['wizard'] == True else "but I am not a wizard.",
    "Who am I?"
     ],

    #round_clues[1]
    ["They call me a " + selected_character['ancestry'] + " in the wizarding world,", 
    "I belong to the house " + selected_character['house'] + '.' if selected_character['house'] else "I will not tell you what Hogwarts house I belong to; that business is my own.",
    "I could be human, I could also be a " + selected_character['species'] + "." if selected_character['species'] != 'human' else "I'm just a human, all this business being an 'animagus' is simply child's play.",
    "Who am I?"],

    #round_clues[2]
    ["I may have been a Professor at Hogwarts School." if selected_character['hogwartsStaff'] == True else "I am not a Professor at Hogwarts.",
    "Spoiler alert, but by the time the war has ended, I would most likely be dead." if selected_character['alive'] == False else "Spoiler alert, but I do make it out alive to see the end of the war against You-Know-Who.",
    "Who am I?"], 

    #round_clues[3]
    ["My hair is " + selected_character['hairColour'], 
    "and my eyes are " + selected_character['eyeColour'] + ".",
     "In muggle moving pictures, I was portrayed by the actor " + selected_character['actor'] + ".",
     "Who am I?"],

    #round_clues[4] - string slice first and last name
    ["My name backwards is " + selected_character['name'][::-1].lower() + ".", 
    "Who must I be?"
    ]
] 

# function takes user's guess and checks if it matches the mystery character's name. 
# outputs are printed depending on if they got it right or wrong
def evaluate_guess(guess):

    if guess == selected_character['name']:
        get_output("\n CONGRATS! You guessed correctly! \n")
        exit()
    else:
        get_output("\n Unlucky, that is incorrect. Here is your next clue: \n")
        return

#Each clue in each list item is presented to the user. 
clue_1 = " ".join(round_clues[0])
# It waits for user response before moving on to the next clue or finishing the game. 
get_output(clue_1 + "\nTake your guess: ")
first_guess = get_input()
#function called to check if the answer is right
evaluate_guess(first_guess)


clue_2 = " ".join(round_clues[1])
get_output(clue_2 + "\nTake your guess: ")
second_guess = get_input()

evaluate_guess(second_guess)


clue_3 = " ".join(round_clues[2])
get_output(clue_3 + "\nTake your guess: ")
third_guess = get_input()

evaluate_guess(third_guess)


clue_4 = " ".join(round_clues[3])
get_output(clue_4 + "\nTake your guess: ")
fourth_guess = get_input()

evaluate_guess(fourth_guess)


clue_5 = " ".join(round_clues[4])
get_output(clue_5 + "\nTake your final guess: ")
fifth_guess = get_input()

#function runs like evaluate_guess() but the final message is different to indicate the game is over. 
def final_evaluation(guess):
    if guess == selected_character['name']:
        get_output("\n CONGRATS! You guessed correctly! \n")
        exit()
    else:
        get_output("I'm afraid you are out of 'Liquid Luck'. The correct answer is " + selected_character['name'].upper() + ". I hope you will bring more Felix Felicis next time!")
        exit()

final_evaluation(fifth_guess)

