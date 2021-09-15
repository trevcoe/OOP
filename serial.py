"""Python serial number generator."""


class SerialGenerator:
    def init(num, start=0):
        num.start = num.next = start

    def rep(num):
        return f"<SerialGenerator start ={num.start} next={num.next}>"

    def generate(num):
        num.next += 1
        return num.next -1

    def reset(num):
        num.next = num.start
        


    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

