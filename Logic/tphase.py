#Testing Curl
import pycurl
from ScoreSystem import *

verbose = 0
c = pycurl.Curl()
#Starting Player
pov ='S'
#history
h = '0'
#Dealer
d = '0'
#Vulnerability
v = '0'
#South Hand
s = '0'
#West Hand
w = '0'
#North Hand
n = '0'
#East Hand
e = '0'
#Unknown Opaque Value
o = '0'




c.setopt(c.URL, 'http://gibrest.bridgebase.com/u_bm/robot.php?&pov=S&h=&d=s&v=B&n=kt982.q3.k62.t86&s=aq73.94.ajt983.a&e=j5.jt872.754.972&w=64.ak65.q.kqj543&o=state1&src=eric')
body = c.perform()
c.close()

print(body)

# Test Scoring
if verbose:
    print("\nIf contract level was 3, contract suit was no trump. and 10 tricks were won:")
    print(str(Score.scoregame(3,4,10)) + " points")