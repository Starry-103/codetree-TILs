from datetime import date
m1, d1, m2, d2=map(int,input().split())
A=input()
result=0
start_date=date(2011, m1, d1)
end_date=date(2011,m2,d2)
days_between=(end_date-start_date).days
dow=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
result+=days_between//7
if dow.index(A)<=days_between%7:
    result+=1
print(result+1)