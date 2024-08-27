import codecs
import sys

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

a = ["西施","貂蟬","王昭君","楊貴妃","馮小憐","蘇妲己","趙飛燕","鄭旦","褒姒","甄宓"]
b = input()
if b in a:
    print(a.index(b))
else:
    print("找不到")