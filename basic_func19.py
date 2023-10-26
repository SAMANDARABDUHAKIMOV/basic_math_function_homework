def main(a, b):
    '''find the absolute value of the difference between a and b. Return it.
    
    Args:
        a (int): a number
        b (int): a number
        
    Returns:
        int: the result.
    '''
    x=a-b
    return abs(x)
a=4
b=11
print(main(a,b))