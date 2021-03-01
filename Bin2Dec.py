'''
allows the user to enter strings of up to 8 binary digits, 0's and 1's, in any sequence and then
displays its decimal equivalent.

Conditions:
- Arrays may not be used to contain the binary digits entered by the user;
- Determining the decimal equivalent of a particular binary digit in the sequence must be calculated using
a single mathematical function, for example the natural logarithm. It's up to you to figure out which
function to use.

'''

def bin2dec (number):
    import math
    istring = str(number)

    power = len(istring) - 1
    result = 0
    for digit in range(len(istring)):
        result += math.pow(2 * (int(istring[digit])), power)
        power -= 1

    return result

number = input("Please, digit an binary number up to 8 digits: ")

print(bin2dec(number))







