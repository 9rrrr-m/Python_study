# 1
import diablo2

jane = diablo2.Amazon()
mary = diablo2.Amazon()

print(jane.strength)
print(jane.attack())

eve = diablo2.Amazon()
eve.exercise()
print(eve.strength)

# 2
from diablo2 import *

jane = Amazon()
mary = Amazon()

print(jane.strength)
print(jane.attack())

eve = Amazon()
eve.exercise()
print(eve.strength)

# 3
from diablo2 import Amazon

jane = Amazon()
mary = Amazon()

print(jane.strength)
print(jane.attack())

eve = Amazon()
eve.exercise()
print(eve.strength)
