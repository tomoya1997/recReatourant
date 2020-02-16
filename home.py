import package.roboko_package.roboko as Roboko
import package.csv_file.csv as csv_file

roboko = Roboko.Roboko()
csv_file = csv_file.Csv()
# 挨拶
roboko.greet()
# オススメ
if csv_file.exist:
    restaurants = csv_file.populerRestaurants()
    roboko.suggest(restaurants)

# 質問（レストラン）
roboko.ask()
# csvへの書き込み
csv_file.write(roboko.restaurant.capitalize())

# お礼
roboko.toThank()

