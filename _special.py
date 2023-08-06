#! python3

# The first line of all your Python programs should be a shebang line(starts with #!), which
# tells your computer that you want Python to execute this program with python version 3 ,
# in case if you have multiple version for python

print("Welcome to python world !")

# print special ... use of end to control floo of print [(end = ""), " " can be changed].. 

print("hello", end = '\t')
print("World" + '\n')


# sum() function  cool...
arr = [1, 2 , 3, 4]
print(sum(arr))

# introducing len
name = input("What is your name? ")

if len(name) < 3:
    print("ERROR: No. of min. allowed letters is 3")
elif len(name) > 40:
    print("ERROR:  No. of max. allowed letters is 40")
else:
    print(" Name looks good.")

# mathematical operations and boolian ...
    price = 1000000
    having_good_credit = True

    if having_good_credit:
        down_payment = 0.1 * price
    else:
        down_payment = 0.2 * price

    print(f"Down payment : {down_payment}")
    print(" ")


    has_good_credits = True
    has_criminal_record = True

    if has_good_credits and not has_criminal_record:
        print("Eligible for loan.")
    else:
        print("Not eligible for loan")
        print(" ")


    w = float(input("Weight: "))
    u = input("kg or lbs: ")
    if u.lower() == "kg":
        Wgt = w * 2.2
        print(f"you are {Wgt} lbs")
    elif u.lower() == 'lbs':
        Wgt = w // 2.2
        print(f"you are {Wgt} kg")
        print(" ")

# special string ...
    i = 0
    while i <= 10:
        i = i + 1
        print(" " * (11 - i) + "*" * (2 * i - 1) + " " * (11 - i))

# number game ...  dealling with errors
    import random
    print("choose a number")
    lucky_number = random.randint(1, 9)
    guess_no = 0
    guess_limit = 2
    while guess_no < guess_limit:
        g = int(input("Guess: "))
        guess_no = guess_no + 1
        if g == lucky_number:
            print("You won!")
            break
    else:
        print("Sorry,you loss....")

    print("choose a number")
    l_n1 = random.randint(1, 9)
    l_n2 = random.randint(1, 9)
    g_n = 0
    g_l = 2
    while g_n < g_l:
        try:
            g = int(input("Guess: "))
            g_n = g_n + 1
            if g == l_n1:
                print("You passed level 1,")
                g_n2 = 0
                while g_n2 < g_l:
                    try:
                        g2 = int(input("Guess: "))
                        g_n2 += 1
                        if g2 == l_n2:
                            print("Are you crazy....")
                            print("You won!")
                            break
                        else:
                            print("try again...")
                    except ValueError:
                        print("Stupid,choose a no. ")
            else:
                print("try again...")
        except ValueError:
            print("Stupid,choose a no. ")

    print(f"Sorry,you loss.... !\n Ans were {lucky_number}, {l_n1} , {l_n2}")

# use of for
    p = [10, 20, 30]
    total = 0
    for n in p:
        total = total + n
    print(total)


    for x in range(5):
        for y in range(0, 5):
            print(f"({x}, {y})")


    n = [5, 2, 5, 2, 2]
    for p in n:
        print("x" * p)
    print("")


    n = [8, 2, 8, 2, 8]
    for m in n:
        o = ""
        for x in range(m):
            o += "🎁"
        print(o)

# dealing with lists
    n = ['Prakhar', 'Tanishka', "Ayush"]
    print(n[1])
    print(n[0:])
    print(n[0:2])

    n = [2, 3, 4, 7, 8, 9, 11, 1, 5, 6]
    maximum = n[0]
    for m in n:
        if m > maximum:
            maximum = m
    print(maximum)

    numbers = [2, 3, 3, 2, 5, 7]

    for m in numbers:
        n = numbers[0]
        if m == n:
            numbers.remove(m)
        else:
            n = m
    print(numbers)


    num = [2, 3, 3, 2, 5, 7]
    uniques = []
    for x in num:
        if x not in uniques:
            uniques.append(x)
    print(uniques)

# calculator
    print("One step calculator...")
    try:
        x = int(input("a: "))
        y = int(input("b: "))
        tool = input("+|-|*|/ : ")
        if tool == "+":
            print(x + y)
        elif tool == "-":
            print(x - y)
        elif tool == "*":
            print(x * y)
        elif tool == "/":
            print(x / y)
        else:
            print("ERROR")
        print('Thanks')
    except ValueError:
        print("Letters are not applied for mathematical operations.")
    except ZeroDivisionError:
        print("Zero cannot be used for division.")

# game ..
    print(".......I M A G I N A R Y      C A R     G A M E  ........")
    started = False
    while True:
        c = input('>').lower()
        if c == "help":
            print("to start the car: start")
            print("to stop the car: stop ")
            print('quit : to exit')
        elif c == "start":
            if started:
                print("Car is already started.")
            else:
                started = True
                print('car started')
                print("welcome, type stop whenever you want....")
        elif c == "stop":
            if not started:
                print("Car is already stopped.")
                print("This car is not for you...")
            else:
                started = False
                print("car stopped")
                print("Get off...")
        elif c == "having fun":
            print("Yeah, you must.....")
        elif c == "enjoying":
            print("Yeah, you must.....")
        elif c == "pleasure":
            print("Yeah, you must.....")
        elif c == "exit":

            print("See you later.......")
            break
        else:
            print("Sorry,I can't understand")

# this line will be excluded from executing the code because of #
# .... lol..  for leaving comment   bye...

# defining function
    def sqr(digit):
        return digit * digit


    print(sqr(1728))

# defining class
    class Point:
        def __init__(self, x_c, y_c):
            self.x = x_c
            self.y = y_c


    point = Point(10, 20)
    print(point.x, point.y)
    point.x = 20
    print(point.x, point.y)


    class Mammal:
        def walk(self):
            print("walks")


    class Dog(Mammal):
        pass


    class Cat(Mammal):
        pass


    d = Dog()
    d.walk()

# formating string...

    def mutate_string(string, position, character):
        l = list(string)
        l[position] = character
        string = ''.join(l)
        return string

    if __name__ == '__main__':
        s = input()
        i, c = input().split()
        s_new = mutate_string(s, int(i), c)
        print(s_new)



    def mutate_string(string, position, character):
        string = string[:position] + character + string[position + 1:]
        return string

    if __name__ == '__main__':
        s = input()
        i, c = input().split()
        s_new = mutate_string(s, int(i), c)
        print(s_new)

# finding sub_string in string..

    def count_substring(string, sub_string):
        l = list(string)
        c = 0
        for i in range(0, len(string) - len(sub_string) + 1):
            if l[i:i + len(sub_string)] == list(sub_string):
                c = c  + 1
        return c

    if __name__ == '__main__':
        string = input().strip()
        sub_string = input().strip()
        
        count = count_substring(string, sub_string)
        print (count)

# character recognising
    s = input()
    l = list(s)
    print(f"\n\n {', '.join(l)} \n") #joins a list by given character
    print(s.split(l[2])) # splits the string at that char.
    alnum = alpha = dig = upp = low = False
    for i in range(len(s)):
        if l[i].isalnum(): alnum = True
        if l[i].isalpha(): alpha = True
        if l[i].isdigit(): dig = True
        if l[i].isupper(): upp = True
        if l[i].islower(): low = True

    print(f'String has  digit or alphabet -- {alnum}')
    print(f'String has alphabet -- {alpha}')
    print(f'String has digit -- {dig}')
    print(f'String has lowrcase letter -- {low}')
    print(f'String has uppercase letter -- {upp}')

    print(f"string contains only digits -- {s.isdigit()}")
    print(f"string contains only alphabets or digits -- {s.isalnum()}")
    print(f"string contains only upper case letter -- {s.isupper()}")
    print(f"string contains only lower case letter -- {s.islower()}")
    print(f"string is in title form -- {s.istitle()}")
    print(f"string contains only decimals -- {s.isdecimal()}")
    print(f"string contains only spaces\\tabs\\new_line -- {s.isspace()}")

# adjusting string ....
    #adding specific char ....
    s = int(input())

    for i in range(1, s + 1):
        print(('H' * (2 * i - 1)).center(2 * s - 1, ' '))
    for i in range(0, s + 1):
        print(((' ' * 3 * s).center(5 * s, 'H')).center(6 * s - 1, ' '))
    for i in range(0, s // 2 + 1):
        print(('H' * 5 * s).center(6 * s - 1, ' '))
    for i in range(0, s + 1):
        print(((' ' * 3 * s).center(5 * s, 'H')).center(6 * s - 1, ' '))
    for i in range(1, s + 1):
        i = s - i + 1
        print((('H' * (2 * i - 1)).center(2 * s - 1, ' ')).rjust(6 * s - 1, ' '))

    # removing extra character .. striping..

    s = '**     Hi, I am the devil !####*****'
    print(s + 'char count -- ' + str(len(s)))
    print(s.strip('*') + '       char count -- '+ str(len(s.strip('*'))))
    print(s.strip('*').lstrip() + '      char count -- '+ str(len(s.strip('*').lstrip())))
    print(s.strip('*').lstrip().rstrip('#') + '      char count -- '+ str(len(s.strip('*').lstrip().rstrip('#'))))

    # removing chars...
    
    spam = 'SpamSpamBaconSpamEggsSpamSpam' 
    print(spam.strip('ampS')) #removes 'S','a','p','m' indivisually from start and end

# breaking string .... 

    import textwrap
    def wrap(lst, max_width):
        l = len(lst)
        l = l + ( l // max_width) + 1 
        
        for i in range(l):
            if i % (max_width + 1) == 0:
                lst = lst[: i] + '\n' + lst[i:]
        lst = lst[1:]
        return lst

        # for i in range(0, l, max_width + 1):
        #         lst = lst[: i] + '\n' + lst[i:]
        # lst = lst[1:]
        # return lst

    if __name__ == '__main__':
        string, max_width = input(), int(input())
        result = wrap(string, max_width)
        print (result)

# string special .. splitig ... finding int..
    s = input("Give two integers ... ")
    l = s.split(" ")
    x = int(l[0])  
    y = int(l[-1])  

    for i in range(x // 2):
        print(('.|.' * (2 * i + 1)).center(y , '-'))

    print('WELCOME'.center(y, '-'))

    for i in range(x // 2):
        i = x // 2 - i -1
        print(('.|.' * (2 * i + 1)).center(y , '-'))
 
# using random to get random digit  and  making dictionaries ....

    import  random

    def dig(r):
        output = ""
        dig_mapping = {
            "0" : "It is certain !",
            "1" : "Good effort!" ,
            "2" : "Try again!",
            "3" : "Good!",
            "4" : "Need more effort!",
            "5" : "Once more !",
            "6" : "Close enough",
            "7" : "Bravo!",
            "8" : "Give  a little more!",
            "9" : "Here we go!"
        }
        output = dig_mapping.get(r, r + " > !")
        return output

    r = str(random.randint(0, 9))
    print(dig(r))

# dict. in detail. .... .
    import pprint  # to use pprint.pprint() specialy for printing nested dict. or looped dict.
    marks = { 'sameer' : 50,
            'piyush' : 45,
            'yash'   : 39,
            'priyanshu' : 44 }
    x = True
    while x:
        name = input('who\'s marks (leave blank to exit): ')
        if name == '':
            x = False
        
        else:
            if name in marks:
                print(f'{name}\'s  marks are {marks[name]}')
            else:
                print("I have no idea about that...")
                marks[name] = int(input("Do you know his\her marks: "))
                print("Datasheet updated:")

    for i in marks.keys():
        print(i)
    print(marks.keys())
    print('\n')
    for i in marks.values():
        print(i)
    print(marks.values())
    print('\n')

    for i in marks.items():
        print(i)
    print(marks.items())
    print('\n')

    for i in marks.keys():
        print(f'{i} \t\t {marks[i]}')

    print('\n')
    marks.setdefault('mohit', 40)
    print(marks.items())
    marks.setdefault('mohit', 42)  # doesn't alter the value
    print(marks.items())
    marks['mohit'] = 41 # alters the value..
    print(marks.items()) 

    pprint.pprint(marks) # to get arranged dict. values

# one more game using array ...

    def game_status():
        print(f'\n {game[0][0]} | {game[0][1]} | {game[0][2]}')
        print(f' --+---+--')
        print(f' {game[1][0]} | {game[1][1]} | {game[1][2]}')
        print(f' --+---+--')
        print(f' {game[2][0]} | {game[2][1]} | {game[2][2]}\n')


    print('Welcome to game!!  \n need 2 players ..\nfirst one is "#" \nsecond one is "O"\nTo exit "0"')

    x, y = True, True
    p1, p2 = 0, 0
    while x:
        game = [['-', '-', '-'],
                ['-', '-', '-'],
                ['-', '-', '-']]
        game_status()
        i = 0
        while y:
            if i % 2 == 0:
                print("1st players choice")
                z = True
                while z:
                    try:
                        p, q = int(input('Row(0 < X <= 3):   ')), int(input('Colomn(0 < X <= 3): '))
                        if p in range(1, 4) and q in range(1, 4):
                            if game[p - 1][q - 1] == '-':
                                game[p - 1][q - 1] = '#'
                                z = False
                            else:
                                print("Choose diff place!")
                        elif p == 0 or q == 0:
                            print("Player 1 has taken his steps back!")
                            p1 -= 1
                            z = False
                            y = False
                    except ValueError:
                        print("Don't be kid anymore!")
                    
            elif i % 2 == 1:
                print("2nd players choice")
                z = True
                while z:
                    try:
                        p, q = int(input('Row(0 < X <= 3):   ')), int(input('Colomn(0 < X <= 3): '))
                        if p in range(1, 4) and q in range(1, 4):
                            if game[p - 1][q - 1] == '-':
                                game[p - 1][q - 1] = 'O'
                                z = False
                            else:
                                print("Choose diff place!")
                        elif p == 0 or q == 0:
                            print("Player 2 has taken his steps back!")
                            p2 -= 1
                            z = False
                            y = False
                    except ValueError:
                        print("Don't be kid anymore!")
            i += 1
            game_status()
            
            for j in range(0, 3):
                if '-' not in game[j]:
                    b = False
                else:
                    b = True
                    continue
            if b == False:
                print("This one got draw!")
                y = False

            for j in range(0, 3):
                if game[j][0] == game[j][1] == game[j][2] == '#':
                    print("1st player has won!")
                    p1 += 1
                    y = False
                elif game[0][j] == game[1][j] == game[2][j] == '#':
                    print("1st player has won!")
                    p1 += 1
                    y = False
                elif game[0][j] == game[1][j] == game[2][j] == 'O':
                    print("2nd player has won!")
                    p2 += 1
                    y = False
                elif game[j][0] == game[j][1] == game[j][2] == 'O':
                    print("2nd player has won!")
                    p2 += 1
                    y = False
            if game[0][0] == game[1][1] == game[2][2] == '#':
                print("1st player has won!")
                p1 += 1
                y = False
            elif game[0][0] == game[1][1] == game[2][2] == 'O':
                print("1st player has won!")
                p1 += 1
                y = False

        print(f'Player 1 scored -- {p1}\nPlayer 2 scored -- {p2}')
        b = True
        while b:
            a = input("Do you want to play more: (y/n)")
            try:
                if a.lower() == "y":
                    print("Here we go..!")
                    y = True
                    b = False
                elif a.lower() == "n":
                    print("Okay")
                    b = False
                    x = False
                else :
                    print("Give appropriate answer!")
            except ValueError:
                print("Give appropriate answer!")
        print("Thanks!")
    print("See you later! :)")

# copy() paste() using python ....

    import pyperclip
    #pyperclip.copy('hello!')
    print(pyperclip.paste())

# changing decimals to othre base number..
    def decimal_all(num, base):
        l = []
        
        while num != 0:
            a = num % base
            dic = {
                1 : '1', 5: '5', 9: '9', 13: 'D',
                2 : '2', 6: '6', 10: 'A', 14: 'E',
                3 : '3', 7: '7', 11 : 'B', 15: 'F',
                4 : '4', 8: '8', 12 : 'C', 

            }
            l.append(dic[a])
            num //= base      
        for i in range((len(l) // 2)):
            l[i], l[len(l) - 1 - i] = l[len(l) - 1 - i], l[i]
        return ''.join(l)
    a, b = int(input("Number: ")), int(input("Base:(<16) "))

    print(decimal_all(a, b))

# this is how to colour of output of particular print()
    print("\033[90m {}\033[00m".format('grey'))
    print("\033[91m {}\033[00m".format('RED'))
    print("\033[92m {}\033[00m".format('green'))
    print("\033[93m {}\033[00m".format('yellow'))
    print("\033[94m {}\033[00m".format('blue'))
    print("\033[95m {}\033[00m".format('purple'))
    print("\033[96m {}\033[00m".format('cyan'))

# take input as complex no.

    l = complex(input()) 
    print(l)   
    
# how to generate sound 

    import winsound
    frequency = 2500
    duration = 3000  # in miliseconds
    winsound.Beep(frequency, duration)
    for i in range(1000, 20000, 100):
        winsound.Beep(i, 1000)
        
# this is how to  use shelves to store data ...
    import shelve
    self =  shelve.open("mydata")
    fam = ["Me", "Papa", "Maa", "Brother", "Sister"]
    self["family"] = fam
    print(type(self))
    self.close()

# how to copy excuted messange in a particular file..
    import traceback,  time, os

    try:
        raise Exception("this is a error message...")
    except:
        errorFile = open('D:\\vish\\errorInfo.txt', 'w')
        errorFile.write(traceback.format_exc())
        errorFile.close()
        print('The traceback info was written to errorInfo.txt.')

    time.sleep(10)
    os.unlink('D:\\vish\\errorInfo.txt')

# iter function...
    # iter function
    x = "Prakhar"
    y = iter(x)
    print(next(y))
    print(next(y))
    print(next(y))
    print(next(y))
    print(next(y))
    print(next(y))
    print(next(y))

    class counting():
        def __iter__(self):
            self.a = 1
            return self
        def __next__(self):
            if self.a <= 20:
                x = self.a
                self.a += 1
                return x  
            else:
                raise StopIteration  # to stop iteration

    new = counting()
    x = iter(new)

    for i in x:
        print(i)

# format function...
    # addinng a place holder in a string...
    #using formate function

    num1 = 25
    msg = "Hey there {} how are you"
    print(msg.format(num1))


    msg2 = "Hey there {:.2f} how are you"
    print(msg2.format(num1))

    num = 24943.22342
    msg = "Hey there {}, how is your life going!!"
    print(msg.format(num))

    msg2 = "Hey there {:.3f}, how is your life going!!"
    print(msg2.format(num))

    st = "Prakhar"
    print(msg.format(st))

    msg3 = "Order for {} , order no. {} costs {:.2f} ruppies"
    print(msg3.format(st, num1, num))

    msg3 = "The name is {1}. {1} has ordered the item no. {0} cost for {2:.2f}"
    print(msg3.format(num1, st, num))

    msg3 =  "this car is {car} model {model}"
    print(msg3.format(car = "volvo", model = "S10"), "\n")

    # using generators to generate a iterable function

    def items():
        print("Frist")
        yield 15  # returns a value without terminating the function unlike "return"

        print("mid")
        yield 25 

        print("Last")
        yield 30

    new = items()
    print(next(new))
    print(next(new), "\n")
    #print(next(new))

    def num2(n):
        for i in range(n):
            yield(i)
    n = num2(5)
    print(next(n))
    print(next(n))
    print(next(n))
    print(next(n))
    print(next(n))

    def sqr(n2):
        for i in range(n2):
            yield i * i

    new = sqr(5)
    for sq in new:
        print(sq)

    # or just do this
    new = sqr(5) 
    while True:
        try:
            print("the square is : ", next(new))
        except StopIteration:
            break

    new = ( i * i for i in range(5))
    for i in new:
        print(i)

# math and statistics module. ... 
    import math , statistics 
    # use python docs for more
    print(math.pi)
    print(math.e)
    print(math.radians(60))
    print(math.degrees(1))
    print(math.sin(1))  # use in radians 
    print(math.log(11), math.log10(10), math.log1p(10))
    print(math.exp(1), math.pow(2, 10))
    print(math.sqrt(20), math.ceil(5.5), math.floor(5.5))

    print(statistics.mean([2, 3, 4, 5, 6, 5, 6, 7, 6, 7]))
    print(statistics.median([2, 3, 4, 5, 6, 5, 6, 7, 6, 7]))
    print(statistics.mode([2, 3, 4, 5, 6, 5, 6, 7, 6, 7]))

# random module...
    import random
    print(random.random())
    print(random.random())
    print(random.random(), "\n")
    print(random.randint(1, 50))
    print(random.randint(1, 50))
    print(random.randint(1, 50), "\n")
    print(random.randrange(1, 10))
    print(random.randrange(1, 10))
    print(random.randrange(1, 10), "\n")
    print(random.randrange(1, 10, 2))
    print(random.randrange(1, 10, 2))
    print(random.randrange(1, 10, 2), "\n")
    print(random.choice("Python"))
    print(random.choice("Python"))
    print(random.choice("Python"), "\n")

# this is how to deal with page ...
    import pyautogui as pg

    import time

    time.sleep(10)
    for i in range (100):
        pg.write("GOLU")
        pg.press("Enter")
