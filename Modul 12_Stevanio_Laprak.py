import pandas as pd

# Baca file CSV
data = pd.read_csv('Negara.csv')

# Membuat DataFrame dari data yang dibaca
df = pd.DataFrame(data)

# Hitung rata-rata (mean) berdasarkan kolom 'Benua' untuk 'Luas' dan 'Populasi'
mean = df.groupby('Benua')[['Luas', 'Populasi']].mean()

# Hitung standar deviasi (std) berdasarkan kolom 'Benua' untuk 'Populasi'
std = df.groupby('Benua')[['Luas','Populasi']].std()

# Menampilkan DataFrame, mean, dan std
print(df)
print(mean)
print(std)

mean.to_csv('Negaramean.csv')
std.to_csv('NegaraStd.csv')