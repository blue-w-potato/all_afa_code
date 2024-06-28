n=[eval(input()) for i in range(5)]
print(*n)
print(f'''Sum = {sum(n):.1f}
Average = {sum(n)/5:.1f}
''')