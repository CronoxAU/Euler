# Solution to Project Euler problem 31 - https://projecteuler.net/problem=31
# How many different ways can £2 be made using any number of coins?

# returns the total value of the supplied coins, where P2 is the number 2 pound coins, P1 one pound, p50 is 50 pence, p20 is 20 pence etc. 
def getTotalFromCoins(nP2, nP1, np50, np20, np10, np5, np2, np1):
    return (nP2 *200) + (nP1 * 100) + (np50 * 50) + (np20 * 20) + (np10 * 10) + (np5 * 5) + (np2 * 2) + np1


# returns the number of different ways to make n pounds, using standard English coins (1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p))
# brute force approch, checking each combination of coins, breaking when the result is higher then the traget value
# the only optimisation is assuming that once we reach the inner most for loop (the one for 1p) there will be a valid combination, where 1p coins is equal to the tagert value - the current test value
# this value si not calculated, with one just being added to the count
# this code is suprisingly quick but horrible to read and maintain. i would like to produce a cleaner version.
def numberOfWaysToMakeNPounds(n):
    count = 0
    iP2 = 0 
    iP1 = 0
    ip50 = 0
    ip20 = 0
    ip10 = 0
    ip5 = 0
    ip2 = 0
    ip1 = 1
    testValue = getTotalFromCoins(iP2,iP1,ip50,ip20,ip10,ip5,ip2,ip1)
    # work in pence it avoid issues with rounding
    nPence = int(n *100)
    # loop through each of the different options, counting up, breaking when we get to a result higher than the target value.
    while testValue <= nPence:
        while testValue <= nPence:
            while testValue <= nPence:
                while testValue <= nPence:
                    while testValue <= nPence:
                        while testValue <= nPence:
                            while testValue <= nPence:
                                if testValue <= nPence:
                                    # when we reach the inner loop we can just add one pence at a time until we reach the nPence
                                    # rather than calculating the number needed, just count this as another combination and move on
                                    #if getTotalFromCoins(iP2,iP1,ip50,ip20,ip10,ip5,ip2,ip1) == nPence:
                                    count += 1
                                ip1 = 0
                                ip2 += 1
                                testValue = getTotalFromCoins(iP2,iP1,ip50,ip20,ip10,ip5,ip2,ip1)
                                if testValue == nPence:
                                    count += 1
                                    break
                            ip2 = 0
                            ip5 += 1
                            testValue = getTotalFromCoins(iP2,iP1,ip50,ip20,ip10,ip5,ip2,ip1)
                            if testValue == nPence:
                                count += 1
                                break
                        ip5 = 0
                        ip10 += 1
                        testValue = getTotalFromCoins(iP2,iP1,ip50,ip20,ip10,ip5,ip2,ip1)
                        if testValue == nPence:
                            count += 1
                            break
                    ip10 = 0
                    ip20 += 1
                    testValue = getTotalFromCoins(iP2,iP1,ip50,ip20,ip10,ip5,ip2,ip1)
                    if testValue == nPence:
                        count += 1
                        break
                ip20 = 0
                ip50 += 1
                testValue = getTotalFromCoins(iP2,iP1,ip50,ip20,ip10,ip5,ip2,ip1)
                if testValue == nPence:
                    count += 1
                    break
            ip50 = 0
            iP1 += 1
            testValue = getTotalFromCoins(iP2,iP1,ip50,ip20,ip10,ip5,ip2,ip1)
            if testValue == nPence:
                count += 1
                break
        iP1 = 0
        iP2 += 1
        testValue = getTotalFromCoins(iP2,iP1,ip50,ip20,ip10,ip5,ip2,ip1)
        if testValue == nPence:
            count += 1
            break
    return count