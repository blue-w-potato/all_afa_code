a = [ "--@--@--@" ,
"@--@--@--",
"-@--@--@-"]

n = int(input())
for i in range(1,1+n):
    print((a[i%3]*n)[:n])