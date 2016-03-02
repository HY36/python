# _*_coding:utf-8_*_
def fact(n):
    '''
    >>>fact(0)
    Traceback (most recent call last):
    ...
    ValueError
    >>>fact(10)
    3628800
    >>>fact(5)
    120
    >>>fact(6)
    720
    '''
    if n<1:
        raise ValueError()
    if n==1:
        return 1
    return n*fact(n-1)

if __name__=='__main__':
    import doctest
    doctest.testmod()