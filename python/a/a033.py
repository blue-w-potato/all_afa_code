a=input()
print(f'|{a[len(a)-4 if len(a)>4 else -4:]:_>8}|')