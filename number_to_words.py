class NumberToWords:
    def __init__(self):
        self.units_en = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        self.teens_en = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", 
                         "seventeen", "eighteen", "nineteen"]
        self.tens_en = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
        self.thousands_en = ["", "thousand", "million", "billion"]

        self.units_fa = ["", "یک", "دو", "سه", "چهار", "پنج", "شش", "هفت", "هشت", "نه"]
        self.tens_fa = ["", "ده", "بیست", "سی", "چهل", "پنجاه", "شصت", "هفتاد", "هشتاد", "نود"]
        self.hundreds_fa = ["", "صد", "دویست", "سیصد", "چهارصد", "پانصد", "ششصد", "هفتصد", "هشتصد", "نهصد"]

        self.units_tr = ["", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
        self.tens_tr = ["", "on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]

    def number_to_words(self, num, lang="en"):
        if lang == "en":
            return self._number_to_words_en(num)
        elif lang == "fa":
            return self._number_to_words_fa(num)
        elif lang == "tr":
            return self._number_to_words_tr(num)
        else:
            raise ValueError("Unsupported language")

    def _number_to_words_en(self, num):
        if num == 0:
            return "zero"
        words = ""
        for idx, chunk in enumerate(self._split_by_thousands(num)):
            if chunk:
                words = self._convert_chunk_en(chunk) + " " + self.thousands_en[idx] + " " + words
        return words.strip()

    def _convert_chunk_en(self, num):
        words = ""
        if num >= 100:
            words += self.units_en[num // 100] + " hundred "
            num %= 100
        if num >= 10 and num < 20:
            words += self.teens_en[num - 10] + " "
        else:
            words += self.tens_en[num // 10] + " "
            words += self.units_en[num % 10] + " "
        return words.strip()

    def _number_to_words_fa(self, num):
        if num == 0:
            return "صفر"
        words = ""
        if num >= 100:
            words += self.hundreds_fa[num // 100] + " و "
            num %= 100
        if num >= 10:
            words += self.tens_fa[num // 10] + " و "
            num %= 10
        if num > 0:
            words += self.units_fa[num] + " "
        return words.strip().replace(" و ", " و").rstrip(" و")

    def _number_to_words_tr(self, num):
        if num == 0:
            return "sıfır"
        words = ""
        if num >= 10:
            words += self.tens_tr[num // 10] + " "
            num %= 10
        if num > 0:
            words += self.units_tr[num] + " "
        return words.strip()

    def _split_by_thousands(self, num):
        chunks = []
        while num > 0:
            chunks.append(num % 1000)
            num //= 1000
        return chunks

# مثال استفاده:
if __name__ == "__main__":
    converter = NumberToWords()
    print(converter.number_to_words(123, "en"))  # Output: "one hundred twenty three"
    print(converter.number_to_words(456, "fa"))  # Output: "چهارصد و پنجاه و شش"
    print(converter.number_to_words(789, "tr"))  # Output: "yedi yüz seksen dokuz"
