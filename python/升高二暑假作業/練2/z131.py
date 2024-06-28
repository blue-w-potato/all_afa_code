n=input()
try:
    n=int(n)
    print(n,'is a number.')
except:
    if 65<=ord(n.upper())<=65+25:
        print(n,'is an alphabet.')
    else:
        print(n,'is a symbol.')