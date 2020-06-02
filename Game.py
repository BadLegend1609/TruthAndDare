###     MAKING TRUTH AND DARE    ###
#importing data

import string
import Truth_and_dare_dictionary
import random
### Greeting the user and instructions###
print("\nWELCOME TO THE GAME!!! YOU'RE PLAYING TRUTH AND DARE NOW.....")
name=str(input("NICK: Hi, I'm Nick, your host for this game. May I know your name?\nEnter Your First Name: "))
name=name.capitalize()
name=name.lstrip()
print("\n\n\nSo... um.., Hi ",name,"! :) Before you move into the game, lets go through the rules once. It's simple AF. And once you're done, we can proceed to the game. ^o^")
print("\nHere are the most simple rules:-\ni] Each round has as many questions as you want.\nii]You can end the game once the number of questions are answered.\nHope you ejnoy the game. OwO\n\nWanna Start it now???")
trash_input=input("\nYOU: ")
### GAME BLOCK BEGIN###
def game():
    qns=0
    times=int(input("Nick: How many questions do you want to play???"+name+"?\nYOU:"))
    print("\n\n")
    global trash_input
    while qns<times:
        #questions
        t_or_d=input(random.choice(Truth_and_dare_dictionary.starting_questions))
        print("\n")
        ###remove whitespace and lowercase from the imput###
        t_or_d = t_or_d.lower()
        ### Processing the data and interactions ###
        def mid_game_function():
            trash_input=input("YOU:")
            if t_or_d=="truth" or t_or_d=="t":
                print("Nick: "+random.choice(Truth_and_dare_dictionary.truth_replies),"\n\n")
            elif t_or_d=="dare" or t_or_d=="d":
                print("Nick: "+random.choice(Truth_and_dare_dictionary.dare_replies),"\n\n")
        if t_or_d=="truth" or t_or_d=="t":
            print("Nick: "+random.choice(Truth_and_dare_dictionary.truth))
            mid_game_function()
            qns+=1
        elif t_or_d=="dare" or t_or_d=="d":
            print("Nick: "+random.choice(Truth_and_dare_dictionary.dare))
            mid_game_function()
            qns+=1
        else:
            print("Nick: I can't undersatand what you said...This round is over for your mistype.I undserstand only the 'truth and dare' game... nothing else.")
            qns+=times
### GAME BLOCK ENDS###
#Runing the game
game()
#if the user wants to play it again or add extra questions
def end_game():
    eq_ask=input("The round has ended.Do you have any questions in mind that you may like to add?   (Answer with Y/y or N/n only)?\nYOU: ")
    eq_ask=eq_ask.capitalize()
    eq_ask=eq_ask.lstrip()
    print("\n\n")
    if eq_ask=="Y":
        tord=input("Is it truth or dare?\nYOU: ")
        print("\n")
        tord = tord.lower()
        tord=tord.lstrip()
        if tord=="truth" or tord=="t":
            qnt=str(input("Nick:Write the question for me so that I can add it.\nYOU: "))
            print("Nick:Question added succesfully.")
            Truth_and_dare_dictionary.truth.append(qnt)
            again()
        elif tord=="dare" or tord=="d":
            qnd=str(input("Nick:Write the question for me so that I can add it.\nYOU: "))
            print("Nick:Question added succesfully.")
            Truth_and_dare_dictionary.dare.append(qnd)
            again()
        elif tord!="t" and tord!="d" and tord!="truth" and tord!="dare":
            print("Nick: I can't undersatand what you said...")
            end_game()  
    elif eq_ask=="N":
        print("Nick:Okay,np.... ^u^\n")
        again()
    else:
        print("Answer only in y/Y or n/N\n\n")
def again():
    a=input("Nick:Hope you liked it lmao... Wanna play it again  (Answer with Y/y or N/n only)?\nYOU: ")
    a=a.capitalize()
    a=a.lstrip()
    print("\n\n")
    if a=="Y":
        game()
    elif a=="N":
        print("Thanks for playing. See you soon..")
    else:
        print("Answer only in y/Y or n/N\n\n")
        again()
end_game()
###         END GAME        ###