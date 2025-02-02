def name():
    name="Bro code"
    print("My Name is {:10}.nice to meet you".format(name))


def number():
    num=1000.000
    # f refer to how many decimal place should be shown
    print("Value is {:.3f}".format(num))
    print("Value is {:,}".format(num))
    # convert decimal into binary
   #print("Value is {:b}".format(num))

name()
number()