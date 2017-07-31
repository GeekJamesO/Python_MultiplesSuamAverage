"""
Multiples
Part I - Write code that prints all the odd numbers from 1 to 1000. Use the for
loop and don't use a list to do this exercise.
"""

def multiples_I(maxValue):
    print "Write code that prints all the odd numbers from 1 to 1000"
    answerArray = []
    for num in range(1, maxValue + 1):
        if (num % 2 == 1):
            answerArray.append("{0}, ".format(num) )
            # print "  {:,}".format(num)
    answerString = "".join(str(x) for x in answerArray)
    print ( answerString )
    return

multiples_I(1000)


print ""
"""
Part II - Create another program that prints all the multiples
of 5 from 5 to 1,000,000.
"""
def multiplesFromFiveToOneMillion():
    print "Create a program that prints all  multiples of 5 from 5 to 1,000,000."
    for num in range(1, 1000001):
        if (num % 5 == 0):
            print "  {:,}".format(num)
    return

#multiplesFromFiveToOneMillion()
print ""
"""
Sum List
Create a program that prints the sum of all the values in the
list: a = [1, 2, 5, 10, 255, 3]
"""
def SumList(arr) :
    print "Prints the sum of all the values in the list"
    print "  Original list: {0}".format(arr)
    sum = 0
    for x in arr:
        sum += x
    print "  The sum of the values is: {0}".format(sum)
    return

a = [1, 2, 5, 10, 255, 3]
SumList(a)
print " "

"""
Average List
Create a program that prints the average of the values in the
list: a = [1, 2, 5, 10, 255, 3]
"""
def AverageList(arr) :
    print "Create a program that prints the average of the values in the list"
    print "  Original list: {0}".format(arr)
    sum = 0
    for anum in arr:
        sum += anum
    averageOfList = sum / len(arr)
    print "  Sum of values is: {0}  Length of array is {1}".format(sum, len(arr))
    print "  Average of values is: {0}".format(averageOfList)
    return;

a = [1, 2, 5, 10, 255, 3]
AverageList(a)
