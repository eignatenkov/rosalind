__author__ = 'egor'
# Problem
#
# A partial permutation is an ordering of only k objects taken from a collection containing n objects (i.e., k≤n). For example, one partial permutation of three of the first eight positive integers is given by (5,7,2).
#
# The statistic P(n,k) counts the total number of partial permutations of k objects that can be formed from a collection of n objects. Note that P(n,n) is just the number of permutations of n objects, which we found to be equal to n!=n(n−1)(n−2)⋯(3)(2) in “Enumerating Gene Orders”.
#
# Given: Positive integers n and k such that 100≥n>0 and 10≥k>0.
#
# Return: The total number of partial permutations P(n,k), modulo 1,000,000.
#
# Sample Dataset
#
# 21 7
#
# Sample Output
#
# 51200

with open("/home/egor/Загрузки/rosalind_pper.txt","r") as f:
    coeffs=[int(x) for x in f.readline().strip().split(' ')]

def p(n,k):
    import math
    return math.factorial(n)/math.factorial(n-k) % 1000000

print(p(coeffs[0],coeffs[1]))