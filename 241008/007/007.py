class Info:
    def __init__(self, code, loc, time):
        self.code=code
        self.loc=loc
        self.time=time

inf1=Info(*input().split())
print("secret code :", inf1.code)
print("meeting point :", inf1.loc)
print("time :", inf1.time)