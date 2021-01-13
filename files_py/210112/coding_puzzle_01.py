def int_addition(num):

    '''
    A function that returns the sum of all integers from 0 to input.
    '''

    # if input is not integer, function returns 0
    if type(num) != int:
        print('Wrong input... BYE!')
        return 0

    # otherwise, create range from 0 to num
    # keep running total (sum) and add each element of range to sum using for loop
    else:
        range_list = range(num + 1)
        sum = 0
        for i in range_list:
            sum = sum + i
        return sum