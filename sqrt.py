def mySqrt(self, x):
    """
    :type x: int
    :rtype: int
    """
    if x == 0:
        return 0
    for i in range(1, x + 1):
        n = i * i
        if n == x:
            return i
        elif n > x:
            return i - 1
        else:
            continue