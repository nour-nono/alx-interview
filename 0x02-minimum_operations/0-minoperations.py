#!/usr/bin/python3
"""
module to find the minimum number of operations to reach n from 1
"""

# from math import inf
# mem = {}
# def divisors(n):
# 	i = 2
# 	div = []
# 	while (i*i < n):
# 		if n % i == 0:
# 			div.append(i)
# 			div.append(int(n/i))
# 		i += 1
# 	if i*i == n and n % i == 0:
# 		div.append(i)
# 	return div
# def minOperations(n):
# 	if not isinstance(n, int) or n <= 1:
# 		return 0
# 	if n in mem:
# 		return mem[n]
# 	n_div = divisors(n)
# 	if len(n_div) == 0:
# 		mem[n] = n
# 		return n
# 	ans = inf
# 	tmp = 0
# 	for x in n_div:
# 		tmp = max(tmp, x)
# 	for x in n_div:
# 		ans = min(ans, minOperations(x) + n/x)
# 	ans = minOperations(tmp) + n/tmp
# 	ans = int(ans)
# 	mem[n] = ans
# 	return and


def prime_factorization(n):
    i = 2
    div_and_powers = {}
    while(i*i <= n):
        power = 0
        while n%i == 0:
            power += 1
            n = n//i
        if power:
            div_and_powers[i] = power
        i+=1
    if n > 1:
        div_and_powers[n] = 1
    return div_and_powers


def minOperations(n):
    """
    this function returns the minimum number of operations to reach n from 1
    params:
        n: int
    return:
        int
    """
    if not isinstance(n, int) or n <= 1:
        return 0
    prime_facrors = prime_factorization(n)
    ans = 0
    for x in prime_facrors:
        ans += prime_facrors[x] * x
    return ans
    
