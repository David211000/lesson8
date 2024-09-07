first=int(input())
second=int(input())
third=int(input())
if first==second==third:
    print(3)
elif first==second!=third or first!=second==third or third==first!=second:
    print(2)
else:
    print(0)