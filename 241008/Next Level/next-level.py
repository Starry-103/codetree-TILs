class Account:
    def __init__(self, id='codetree', level='10'):
        self.id=id
        self.level=level

user1=Account()
user2=Account(*input().split())
print("user",user1.id, "lv",user1.level)
print("user",user2.id,"lv",user2.level)