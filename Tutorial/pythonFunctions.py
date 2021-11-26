
def tally(nums):
    x = []
    for j in range(0,nums,1):
        myNum = float( input('Enter your number: ') )
        x.append(myNum)
    return x

numNums = int( input('Please input how many numbers: ') )
y = tally(numNums)
print('Your numbers: ', y)


# def tally(x, y):
#     tot     = x + y
#     dif     = x - y
#     prod    = x * y
#     div     = x / y
#     return tot,dif,prod,div



# a = float( input('Please input your first number: ') )
# b = float( input('Please input your second number: ') )

# w,x,y,z = tally(a, b)

# print('Sum is  ', w)
# print('Dif is  ', x)
# print('Prod is ', y)
# print('Div is  ', z)