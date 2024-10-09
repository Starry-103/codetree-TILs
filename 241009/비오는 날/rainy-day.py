'''n=int(input())
class weather():
    def __init__(self, date, yoil, nalssi):
        self.date=date
        self.yoil=yoil
        self.nalssi=nalssi'''



print(' '.join(min([x for x in [input().split() for _ in range(int(input()))] if x[2] == 'Rain'], key=lambda x: x[0])))