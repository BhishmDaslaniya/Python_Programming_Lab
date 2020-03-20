# [17CE023] Bhishm Daslaniya

'''
Algorithm!
--> Build a list of tuples such that the string "aaabbc" can be squashed down to [("a", 3), ("b", 2), ("c", 1)]
--> Add to answer all combinations of substrings from these tuples which would represent palindromes which have all same letters
--> traverse this list to specifically find the second case mentioned in probelm
'''

def substrCount(n, s):
    l = []
    count = 0
    current = None
 
    for i in range(n):
        if s[i] == current:
            count += 1
        else:
            if current is not None:
                l.append((current, count))
            current = s[i]
            count = 1
    l.append((current, count))

    # print(l)
    
    ans = 0
		
    for i in l:
        ans += (i[1] * (i[1] + 1)) // 2

    for i in range(1, len(l) - 1):
        if l[i - 1][0] == l[i + 1][0] and l[i][1] == 1:
            ans += min(l[i - 1][1], l[i + 1][1])

    return ans

if __name__ == '__main__':
    n = int(input())
    s = input()
    result = substrCount(n,s)
    print(result)