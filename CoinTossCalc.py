'''
Author: Avery Wittmer
Date: 17 April, 2019
Description: A simple calculator for finding the probability of flipping k heads
in a span of n coin flips.
'''
def Flip(N, K):
    if N < K:
        P = 0
    elif N == K:
        P = .5**K
    else:
        P1 = Flip(N-1, K)
        P2 = Flip(N-K, K)
        P = P1 + (1 - P2) * .5**(K+1)
    return P



def main():
    print("Welcome to the best coin flip sim in the universe! (Don\'t quote me on that)")
    n = int(input("Enter number of flips:"))
    k = int(input("Enter the number of heads in a row:"))

    if k > n:
        print("Enter a value of k that's bigger than n, otherwise the probability is zero.")
    else:
        Prob = 0
        for flips in range(n+1):
            Prob = Flip(flips, k)

        print('Probability of %s heads in a row over %s flips is %s' %(k, n, Prob))


if __name__ == '__main__':
    main()
