# Solution to Project Euler problem 31 - https://projecteuler.net/problem=31
# How many different ways can £2 be made using any number of coins?

# returns the total value of the supplied coins, where P2 is the number 2 pound coins, P1 one pound, p50 is 50 pence, p20 is 20 pence etc. 
def getTotalFromCoins(nP2, nP1, np50, np20, np10, np5, np2, np1):
    return (nP2 *200) + (nP1 * 100) + (np50 * 50) + (np20 * 20) + (np10 * 10) + (np5 * 5) + (np2 * 2) + np1



# returns the number of different ways to make n pounds, using standard English coins (1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p))
def numberOfWaysToMakeNPounds(n):
    count = 0
    iP2 = 0 
    iP1 = 0
    ip50 = 0
    ip20 = 0
    ip10 = 0
    ip5 = 0
    ip2 = 0
    ip1 = 0
    # work in pence it avoid issues with rounding
    nPence = int(n *100)
    # loop through each of the different options, counting up, breaking when we get to a result higher than the target value.
    while getTotalFromCoins(iP2,iP1,ip50,ip20,ip10,ip5,ip2,ip1) <= nPence:
        while getTotalFromCoins(iP2,iP1,ip50,ip20,ip10,ip5,ip2,ip1) <= nPence:
            while getTotalFromCoins(iP2,iP1,ip50,ip20,ip10,ip5,ip2,ip1) <= nPence:
                while getTotalFromCoins(iP2,iP1,ip50,ip20,ip10,ip5,ip2,ip1) <= nPence:
                    while getTotalFromCoins(iP2,iP1,ip50,ip20,ip10,ip5,ip2,ip1) <= nPence:
                        while getTotalFromCoins(iP2,iP1,ip50,ip20,ip10,ip5,ip2,ip1) <= nPence:
                            while getTotalFromCoins(iP2,iP1,ip50,ip20,ip10,ip5,ip2,ip1) <= nPence:
                                while getTotalFromCoins(iP2,iP1,ip50,ip20,ip10,ip5,ip2,ip1) <= nPence:
                                    if getTotalFromCoins(iP2,iP1,ip50,ip20,ip10,ip5,ip2,ip1) == nPence:
                                        count += 1
                                    ip1 += 1
                                ip1 = 0
                                ip2 += 1
                            ip2 = 0
                            ip5 += 1
                        ip5 = 0
                        ip10 += 1
                    ip10 = 0
                    ip20 += 1
                ip20 = 0
                ip50 += 1
            ip50 = 0
            iP1 += 1
        iP1 = 0
        iP2 += 1
    return count