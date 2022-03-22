#special function package of scipy - permutation and combination
'''comb(N, k, exact=False, repetition=False)
    The number of combinations of N things taken k at a time.

    This is often expressed as "N choose k".

    Parameters
    ----------
    N : int, ndarray
        Number of things.
    k : int, ndarray
        Number of elements taken.
    exact : bool, optional
        If `exact` is False, then floating point precision is used, otherwise
        exact long integer is computed.
    repetition : bool, optional
        If `repetition` is True, then the number of combinations with
        repetition is computed.
'''
from scipy.special import comb,perm
help(comb)
com = comb(5,2,exact = False, repetition = True)
print(com)
per = perm(5,2,exact = True)
print(per)
