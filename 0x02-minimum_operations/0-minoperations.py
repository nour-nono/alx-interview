#!/usr/bin/python3
"""
module to find the minimum number of operations to reach n from 1
"""
from math import inf

mem = {}


def divisors(n):
	i = 2
	div = []
	while (i*i < n):
		if n % i == 0:
			div.append(i)
			div.append(int(n/i))
		i += 1
	if i*i == n and n % i == 0:
		div.append(i)
	return div


def minOperations(n):
	if not isinstance(n, int) or n <= 1:
		return 0
	if n in mem:
		return mem[n]
	nDiv = divisors(n)
	if len(nDiv) == 0:
		mem[n] = n
		return n
	ans = inf
	tmp = 0
	for x in nDiv:
		tmp = max(tmp, x)
	for x in nDiv:
		ans = min(ans, minOperations(x) + n/x)
	ans = minOperations(tmp) + n/tmp
	ans = int(ans)
	mem[n] = ans
	return ans
