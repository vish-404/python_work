# debugging using...

# raise function...
#  can be explaind as "it stop running the code in this function and move 
#  the program execution to the except (to line 27) statement"

def bacon():
    raise Exception("this is a error message")
# bacon()  # to raise exception as default

def boxprint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception("symbol must be a single charcter string")
    if width <= 2:
        raise Exception("width must be greater than 2")
    if height <= 2:
        raise Exception("height must be greater than 2")
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (" " * (width - 2) + symbol))
    print(symbol * width)


for sym, w, h in (('*', 4, 4), ('O', 20, 10), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        boxprint(sym, w, h)
    except Exception as err: 
        print("An Exception happened: " + str(err))

# assert function...

#  A condition (that is, an expression that evaluates to True or False)
#  A string to display when the condition is False

door_status = "open"
assert door_status == 'open', "The door must be open"
# the above assert will let the code pass but

door_status = 'I\'m sorry, Dave. I\'m afraid I can\'t do that.'
# assert door_status == 'open', "The door must be open"
# now the code will generate error telling second string

spotlight = {"ns" : "Yellow", "sw" : "Green" , "se" : "Red" }
assert "Red" in spotlight.values(), "Neither of the lights are red..."