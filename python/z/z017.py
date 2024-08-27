a = ["西施","貂蟬","王昭君","楊貴妃","馮小憐","蘇妲己","趙飛燕","鄭旦","褒姒","甄宓"]
b = [78, 62, 86, 70, 12, 16, 38, 15, 22, 13]
c = [ [ a[i], b[i] ] for i in range( len(a) )]
for i in sorted( c, key=lambda x:x[1] ):
    print( i[0] )