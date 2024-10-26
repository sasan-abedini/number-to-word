# Example usage of the NumberToWords library.
# مثال استفاده از کتابخانه NumberToWords
# NumberToWords kütüphanesinin kullanım örneği

from number_to_words import NumberToWords

# Create an instance of the converter.
# یک نمونه از تبدیل‌گر ایجاد کنید.
# Bir dönüştürücü örneği oluşturun.
converter = NumberToWords()

# English example
# مثال انگلیسی
# İngilizce örneği
number_en = 123
result_en = converter.number_to_words(number_en, "en")
print(f"{number_en} in English: {result_en}")

# Persian (Farsi) example
# مثال فارسی
# Farsça (Persçe) örneği
number_fa = 456
result_fa = converter.number_to_words(number_fa, "fa")
print(f"{number_fa} به حروف فارسی: {result_fa}")

# Turkish example
# مثال ترکی
# Türkçe örneği
number_tr = 789
result_tr = converter.number_to_words(number_tr, "tr")
print(f"{number_tr} Türkçe yazıyla: {result_tr}")

# Example with zero
# مثال برای صفر
# Sıfır için örnek
number_zero = 0
result_zero_en = converter.number_to_words(number_zero, "en")
result_zero_fa = converter.number_to_words(number_zero, "fa")
result_zero_tr = converter.number_to_words(number_zero, "tr")

print(f"0 in English: {result_zero_en}")
print(f"0 به حروف فارسی: {result_zero_fa}")
print(f"0 Türkçe yazıyla: {result_zero_tr}")

# Example with a large number
# مثال برای یک عدد بزرگ
# Büyük bir sayı örneği
number_large = 123456789
result_large_en = converter.number_to_words(number_large, "en")
print(f"{number_large} in English: {result_large_en}")
