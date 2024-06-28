a,b=map(int,input().split())
print(((a-90)*12+b-7)if not(a==90 and b<8 or a<90 or a>101 or a==101 and b>7) else 0)