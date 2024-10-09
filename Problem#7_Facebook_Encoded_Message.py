"""
# Problem 7 - Facebook - Encoded Message - Medium

This problem was asked by Facebook.
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
You can assume that the messages are decodable. For example, '001' is not allowed.
"""
# a,b,c,d,e,f,g,h,i,j
# k.l.m,n,o,p,q,r,s,t
# u,v,w,x,y,z

# example num = 1984 - aihd, shd
# num = 7123 - gabc, glc, gaw

import random


def main(input_str: str):
    res = 1
    for i in range(len(input_str) - 1):
        if int(input_str[i:i + 2]) < 27:
            # if two consecutive numbers are less than 27 then they can be interpreted as a different letter
            # print(input_str[i:i+2])
            res += 1
    return res


if __name__ == '__main__':
    test1 = '111'
    test2 = '7123'
    test3 = '1984'
    print(f"The number is {test1} and the number of ways to decode it are: {main(test1)}")
    print(f"The number is {test2} and the number of ways to decode it are: {main(test2)}")
    print(f"The number is {test3} and the number of ways to decode it are: {main(test3)}")
    print("\nRandom tests below:")
    for i in range(5):
        random_test = str(random.randint(0, 100000))
        print(f"The number is {random_test} and the number of ways to decode it are: {main(random_test)}")
