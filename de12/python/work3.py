name="kazuto"
waist=77
age=19

print(name, "さんは腹囲", waist, "cmで年齢は",age, "才ですね。")


if waist>=77 and age>=19:#この部分が変更されました
    print(name,"さん、内臓脂肪蓄積注意です")
else:
    print(name,"さん、腹囲は問題ありません")


name=input("名前を教えてください")
waist=input("胸囲は?")
age=input("年齢は?")

print(name, "さんは腹囲", waist, "cmで年齢は",age, "才ですね。")

#ここが修正されています
if waist>=77 and age>=19:
    print(name,"さん、内臓脂肪蓄積注意です")
else:
    print(name,"さん、腹囲は問題ありません")
