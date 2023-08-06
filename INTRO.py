print("Hi, there")
name = input('What is your full name? ')
n = name[0:4]
print('Hi ' + name.lower())
ay = input("What is your birth year? ")
p = input("your phone no. , Please: ")
dig_mapping = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}
output = ""
for ch in p:
    output += dig_mapping.get(ch, ch + " > !") + " "
print(output)
print("")
ff = input('Which food is your favourite ? ')
print("LOL")
print("")

temperature = int(input("What is the temperature today? "))
if temperature > 24:
    print("It is a hot day.")
elif temperature < 16:
    print("It is a cold day.")
else:
    print("It's a normal day.")
print("Thank you..")
print(" ")

zs = input('So,what is your zodiac sign? ')
print('Wow!,' + zs + " ,That's cool")

print("So,First name: " + name.split(' ')[0])
print('And last name: ' + name.split(" ")[-1])


def function(first_name, last_name):
    print(f"THIS IS HOW TO USE FUNCTION IN PYTHON..")
    print("next two lines are considered..")
    print(f"you got that,{first_name} {last_name}")


print("Hi there!")
function(name.split(' ')[0], name.split(" ")[-1])


cy = input("Which year is going on? ")
age = int(cy) - int(ay)

wkg = input("then,your weight in kg: ")
wg = float(wkg) * 1000
motto = input("what do you want to become? ")

print(" L  O  L  ")
print('NOTICE FOR EVERYONE ')
print(' A load on earth named  ' + name + '[' + zs + '],Having Age ' + str(age) + " likes " + ff + ".")
print(f"Anyhow {name} got " + str(wg) + " grams weight because of " + ff +
      '.And want to become ' + motto)
print(name[0:4] + ", your this name will be consider further")
print("")

print(f"You will be shocked by knowing that your name consists of  {len(name)}  letters")

def print_rangoli(size):
    dit = {
        0 : 'a',1 : 'b',2 : 'c',3 : 'd',4 : 'e',5 : 'f',6 : 'g',
        7 : 'h',8 : 'i',9 : 'j',10 : 'k',11 : 'l',12 : 'm',
        13 : 'n',14 : 'o',15 : 'p',16 : 'q',17 : 'r',18 : 's',
        19 : 't',20 : 'u',21 : 'v',22 : 'w',23 : 'x',24 : 'y',25 : 'z',
    }

    l = []
    for i in range(0, size + 1, 1):
        s = []
        for j in  range(0, i + 1, 1):
            s.append(dit[size -j])
        for j in  range(i, 0 ,  -1):
            s.append(dit[size - j  + 1])
        l.append('-'.join(s).center(4 * size + 1, '-'))
    for i in range(size - 1 , -1 , -1):
        s = []
        for j in  range(0, i + 1, 1):
            s.append(dit[size -j])
        for j in  range(i, 0 ,  -1):
            s.append(dit[size - j  + 1])
        l.append('-'.join(s).center(4 * size + 1, '-'))
    print('\n'.join(l))

if __name__ == '__main__':
    n = int(input('give a number : '))
    print_rangoli(n - 1)

"""The if __name__ == "__main__": block in Python is used to control the execution of code
 when a script is run as the main program versus when it is imported as a module in another
 script. It serves as a conditional statement that allows specific code to run only when the
 script is executed directly, not when it is imported as a module.
"""