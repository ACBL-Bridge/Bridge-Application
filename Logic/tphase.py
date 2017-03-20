#Testing Curl
import pycurl
from ScoreSystem import *
from io import BytesIO

verbose = 0
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
s = ''
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



strr = "TEST"

print(strr[-2:])


#buffer = BytesIO()
#c.setopt(c.URL, 'http://gibrest.bridgebase.com/u_bm/robot.php?&pov=S&h=&d=s&v=B&n=kt982.q3.k62.t86&s=aq73.94.ajt983.a&e=j5.jt872.754.972&w=64.ak65.q.kqj543&o=state1&src=eric')
#c.setopt(c.WRITEDATA, buffer)
#c.perform()
#c.close()

#buffer = str(buffer.getvalue())

#mylst = buffer.split()
#print(mylst)

# Test Scoring
if verbose:
    print("\nIf contract level was 3, contract suit was no trump. and 10 tricks were won:")
    print(str(Score.scoregame(3,4,10)) + " points")