"""
There are N strings. Each string's length is no more than 20 characters. There
are also Q queries. For each query, you are given a string, and you need to find
out how many times this string occurred previously.

Input Format
The first line contains N, the number of strings.
The next N lines each contain a string.
The N + 2nd line contains Q, the number of queries.
The following Q lines each contain a query string.

Sample Input
4
aba
baba
aba
xzxb
3
aba
xzxb
ab

Sample Output
2
1
0
"""

n = int(raw_input().rstrip())
n_strings = {}
for i in range(n):
    string = raw_input().rstrip()
    if string not in n_strings:
        n_strings[string] = 0
    n_strings[string] += 1

q = int(raw_input().rstrip())
queries = []
for i in range(q):
    query = raw_input().rstrip()
    queries.append(query)

for query in queries:
    print n_strings.get(query, 0)
