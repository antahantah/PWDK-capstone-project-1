from config.setting import PROD_PATH
from scripts.extract import ekstrak_csv
from scripts.transform import transform_fit

# Command Extract CSV
prod_df = ekstrak_csv(PROD_PATH)
# print(prod_df.head(15))

afterTransform = transform_fit(prod_df)
# print(afterTransform.head(15))

checkDataTypes = afterTransform.dtypes
print(f"\n\n Jenis-jenis tipe data:\n{checkDataTypes}")

# print(afterTransform.iloc[200:215][['ratings','no_of_ratings','currency','final_price']])

print(afterTransform.iloc[201:215])



# ---- DATA DEMOGRAPHIC RATING

print("\n\n Rating product")
rating_prod = afterTransform['ratings']
print(rating_prod)

print("\n\nRating yang tidak terisi (N/A) adalah: ")
print(afterTransform['ratings'].isnull().sum())

print("\n\nData aggregation pada Rating")
print(rating_prod.agg(['count', 'min', 'max', 'mean', 'median']))


# ---- DATA DEMOGRAPHIC No OF RATING

print("\n\nJumlah Rating")
no_rating = afterTransform['no_of_ratings']
print(no_rating)

print("\n\nRating yang tidak terisi (N/A) adalah: ")
print(afterTransform['no_of_ratings'].isnull().sum())

print("\n\nRating yang lebih dari 1000 pengisian: ")
rating_more_1000 = afterTransform[afterTransform['no_of_ratings'] >= 1000]
print(rating_more_1000)

print("\n\nRating yang lebih dari 100 pengisian dan 4 keatas: ")
rating_big_better = afterTransform[(afterTransform['no_of_ratings'] > 100) & (afterTransform['ratings'] >= 4)]
print(rating_big_better)

print("\n\nBerapa banyak produk yang memiliki rating 4 ke atas dan rincian per desimal")
rating_great = afterTransform[afterTransform['ratings'] >= 4.0 ]['ratings'].value_counts()
print(rating_great)

# ---- DATA DEMOGRAPHIC ACTUAL PRICE
print("\n\nHarga Asli")
real_price = afterTransform['actual_price']
print(real_price)

print("\n\nHarga yang tidak diisi (N/A) adalah: ")
print(afterTransform['actual_price'].isnull().sum())

print("\n\nHarga actual yang paling mahal: ")
high_price = afterTransform.sort_values(by='actual_price', ascending=False)
print(high_price.head(15))


# ---- DATA DEMOGRAPHIC DISCOUNT PRICE AND FINAL PRICE
print("\n\nHarga Diskon")
diskon_price = afterTransform['discount_price']
print(diskon_price)

print("\n\nBarang yang tidak didiskon (N/A) adalah: ")
print(afterTransform['discount_price'].isnull().sum())

print("\n\npotongan diskon paling besar: ")
big_cut = afterTransform.sort_values(by='discount_percent(%)', ascending=False)
print(big_cut.head(15))

print("\n\nData aggregation pada Final Price")
true_true = afterTransform['final_price']
print(true_true.agg(['count', 'min', 'max', 'mean', 'median']))

print("\n\nProduct yang tidak didiskon")
no_diskon = afterTransform[((afterTransform['discount_price'].isnull()) & (afterTransform['actual_price'].notnull()))]
print(no_diskon.shape[0])

print("\n\nberapa banyak row dan columns: ")
print(afterTransform.shape) 

