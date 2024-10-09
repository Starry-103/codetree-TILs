'''class info:
    def __init__(self, code, score):
        self.code=code
        self.score=score

agents=[info(map(int,input().split()) for _ in range(5)]'''


print(' '.join(sorted([input().split()  for _ in range(5)],key = lambda x: int(x[1]))[0]))