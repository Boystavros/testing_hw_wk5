### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    #Must have double equal signs to test equality
    if card.value = 1:
      return True
    #missing colon after else
    else
      return False
   
  #dif should be def to define function
  #card1 and card2 should be comma seperated
  dif highest_card(self, card1 card2):
  #statement block not indented
  if card1.value > card2.value:
    #card is an undefined variable, should be card1
    return card
  else:
    return card2
  #no return statement if cards have equal value

#whole function needs to be indented, otherwise is not a method of CardGame class
def cards_total(self, cards):
  #total value not initialised
  total
  for card in cards:
    total += card.value
    #total is an int so cannot be concatenated with the string
    #return statement is inside loop, but should be outside
    return "You have a total of" + total
  
```
