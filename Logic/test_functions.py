#Testing Curl and other python properties
import pycurl
from score_game import *
from players import *
from simple_deck import *
from card_sort import *
from io import BytesIO
from verbose import *



examp = ['a','b']
elst = ['b','u','r',['a','b']]
if examp in elst:
    print('FOUND')










"""
gamedeck = BDeck()
gamedeck.shuffle()

playerlst = []
for i in range(4):
    playerlst.append(Player())
    playerlst[i].designation = i
    playerlst[i].collecthand(CardSort.csort(gamedeck.givehand()))
if verbose:
    print(playerlst[0].checkhand() + "\n")


playerlst[0].hand[0] = Card(14,2)
playerlst[0].hand[1] = Card(13,2)
playerlst[0].hand[2] = Card(12,2)
playerlst[0].hand[3] = Card(11,2)
playerlst[0].hand[4] = Card(10,2)
playerlst[0].hand[5] = Card(14,0)
playerlst[0].hand[6] = Card(13,0)
playerlst[0].hand[7] = Card(12,0)
playerlst[0].hand[8] = Card(11,0)
playerlst[0].hand[9] = Card(10,0)
playerlst[0].hand[10] = Card(9,0)
playerlst[0].hand[11] = Card(8,0)
playerlst[0].hand[12] = Card(7,0)

c = pycurl.Curl()
#Current Player
pov ='S'
#history
h = ''
#Dealer
d = 'e'
#Vulnerability
v = 'B'
#South Hand
s = playerlst[0].apihand()
#West Hand
w = ''
#North Hand
n = ''
#East Hand
e = ''
#Unknown Opaque Value
o = 'state1'
#Eric Source
src = 'eric'


print(s)

buffer = BytesIO()
c.setopt(c.URL, 'http://gibrest.bridgebase.com/u_bm/robot.php?&pov=S&h=&d=s&v=B&n=kt982.q3.k62.t86&s=aq73.94.ajt983.a&e=j5.jt872.754.972&w=64.ak65.q.kqj543&o=state1&src=eric')
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()

buffer = str(buffer.getvalue())

mylst = buffer.split()
print(mylst)
"""
# Test Scoring
#if verbose:
#    print("\nIf contract level was 3, contract suit was no trump. and 10 tricks were won:")
#    print(str(Score.scoregame(3,4,10)) + " points")