author="jajaio"
'''TODO
Make advanced player classes
More monsters?
'''

class Thing():
	hp=None #Health
	agi=None #Agility
	deff=None #Defence
	att=None #Attack
	mp=None #Magic Power (Ammount of times you can heal)

class Player(Thing):
    gold=None
    name="Test Name"

class Foe(Thing):
	pass
#Basic Player Classes, the player will get to choose at the start of the game what class they want.
class Rogue(Player):
	hp=50
	agi=70
	deff=3
	att=20
	mp=1
class Sellsword(Player):
	hp=65
	agi=45
	deff=5
	att=30
	mp=0
class Cleric(Player):
	hp=40
	agi=65
	deff=3
	att=25
	mp=4
#Lost is the default class, gotta make the player something!
class Lost(Player):
	hp=30
	agi=30
	deff=1
	att=20
	mp=1
Player=Lost
#Basic Monster Classes.
class Slime(Foe):
	hp=20
	agi=15
	att=10
	deff=0
	mp=0
Foe=Slime
class Bandit(Foe):
	hp=60
	agi=40
	att=20
	deff=2
	mp=1
class Zombie(Foe):
	hp=55
	agi=10
	att=15
	deff=1
	mp=0
class Skeleton(Foe):
	hp=40
	agi=50
	att=25
	deff=2
	mp=1
class Goblin(Foe):
	hp=75
	agi=20
	att=15
	mp=0
	deff=1
def show_cleric():
	tebt='''
	Cleric Stats:
	Health: {c.hp}
	Agility: {c.agi}
	Attack: {c.att}
	Defence: {c.deff}	
	Magic: {c.mp}
	'''
	print(tebt.format(c=Cleric()))
def show_rogue():
	text='''
	Rogue Stats:
	Health: {r.hp}
	Agility: {r.agi}
	Attack: {r.att}
	Defence: {r.deff}
	Magic: {r.mp}
	'''
	print(text.format(r=Rogue()))

def show_sellsword():
	tezt='''
	Sellsword Stats:
	Health: {s.hp}
	Agility: {s.agi}
	Attack: {s.att}
	Defence: {s.deff}
	Magic: {s.mp}
	'''
	print(tezt.format(s=Sellsword()))

def show_player():
    yext='''
    Player Stats:
    Health: {p.hp}
    Agility: {p.agi}
    Attack: {p.agi}
    Defence: {p.deff}
    Magic: {p.mp}
    '''
    print(yext.format(p=Player()))

if __name__=='__main__':
    show_rogue()
    show_sellsword()
    show_cleric()
    show_player()

