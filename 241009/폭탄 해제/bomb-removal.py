class info():
    def __init__(self, code, color, sec):
        self.code=code
        self.color=color
        self.sec=sec


b1=info(*input().split())
print("code :", b1.code)
print("color :", b1.color)
print("second :",b1.sec)