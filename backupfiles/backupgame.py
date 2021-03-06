#!/usr/bin/env python3
import time as t
import battleengine as b
import colors as c
import classes as cl
import town
import load

logo='''
 _______  _        _______           _______ 
(  ___  )( \      (  ____ )|\     /|(  ___  )
| (   ) || (      | (    )|| )   ( || (   ) |
| (___) || |      | (____)|| (___) || (___) |
|  ___  || |      |  _____)|  ___  ||  ___  |
| (   ) || |      | (      | (   ) || (   ) |
| )   ( || (____/\| )      | )   ( || )   ( |
|/     \|(_______/|/       |/     \||/     \|
                                             
 _______           _______  _______ _________
(  ___  )|\     /|(  ____ \(  ____ \\__   __/
| (   ) || )   ( || (    \/| (    \/   ) (   
| |   | || |   | || (__    | (_____    | |   
| |   | || |   | ||  __)   (_____  )   | |   
| | /\| || |   | || (            ) |   | |   
| (_\ \ || (___) || (____/\/\____) |   | |   
(____\/_)(_______)(_______/\_______)   )_(   
'''
def run():
    print(c.clear)
    print(c.yellow+str("Hello! And welcome to...."))
    t.sleep(1)
    print(c.random_color()+logo)
    t.sleep(1)
    print()
    print()
    neworload()

def neworload():
    qws=input(c.yellow+"Do you want to start a new game? Or load a save file?"+c.reset+" (1), (2)"+c.violet).strip()
    if qws=="1":
        qwa=input(c.yellow+"Are you sure? Any old save file will be deleted."+c.reset+" (Y/N)"+c.violet).strip().lower()
        if qwa=="y":
            nameask()
        elif qwa=="n":
            neworload()
        else:
            neworload()
    elif qws=="2":
        print(c.yellow+"Okay! Here's your stats.")
        load.load_game()
        cl.show_player()
        qwz=input(c.yellow+"Are you sure you want to load this?"+c.reset+" (Y/N)"+c.violet).strip().lower()
        if qwz=="y":
            town.hub()
        if qwz=="n":
            neworload()
    else:
        print(c.yellow+"I don't understand... type 1 for a save file, and 2 for loading a game.")
        neworload()

def nameask():
    name_question=input(c.yellow+"What is your name? "+c.reset+ ">>>"+c.violet).strip().title()
    if name_question=="Jaja"or"Jajaio":
        print("*insert funny easter egg here*")
    else:
        confirm=input(c.yellow+"Oh, so your name is "+c.blue+name_question+c.yellow+"?"+c.reset+"(Y/N) >>>"+c.violet).strip().lower()
        if confirm=="y":
            cl.Player.name=name_question
            input(c.yellow+"Okay "+c.blue+cl.Player.name+c.yellow+", your adventure is about to start. Press enter to start!")
            print("to be continued")
        elif confirm=="n":
            nameask()

if __name__=='__main__':
    run()
