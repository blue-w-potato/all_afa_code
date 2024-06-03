a=input()
print('|____' + '_'*( 4-len(a) if len(a)<4 else 0 ) + a[-4 if len(a)>4 else 0: ] + '|')