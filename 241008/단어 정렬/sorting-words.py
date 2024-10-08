n=int(input())
wordlist=[]
for _ in range(n):
    wordlist.append(input())
    
wordlist.sort()

for i in wordlist:
    print(i)