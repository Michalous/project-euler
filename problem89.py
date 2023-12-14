with open("0089_roman.txt", "r") as handle:
        data = handle.read()
data = data.split("\n")

class RomanNumerals:
    @staticmethod
    def to_roman(num):
        arab = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        letters = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        string = ""
        for i in range(len(arab)):
            while arab[i] <= num:
                string += letters[i]
                num -= arab[i]
        return string

    @staticmethod
    def from_roman(num):
        arab = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1, 0]
        letters = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I", "Q"]
        result = 0
        num += 'Q'
        a = 0
        while a < len(num) - 1:
            if num[a] + num[a+1] in letters:
                result += arab[letters.index(num[a] + num[a+1])]
                a += 2
            else:
                result += arab[letters.index(num[a])]
                a += 1
        return result

total_old_characters = 0
total_new_characters = 0


for line in data:
    total_old_characters += len(line)
    from_roman = RomanNumerals.from_roman(line)
    to_roman = RomanNumerals.to_roman(from_roman)
    total_new_characters += len(to_roman)
    
print(total_old_characters - total_new_characters) 
    
    
    
    
    