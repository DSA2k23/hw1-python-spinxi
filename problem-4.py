string_roman = "IV"

roman_nishnebi = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#რესულტი დაგვჭირდება ბოლოში
gamotana = 0
#გადავატაროთ სტრინგს
for i in range(len(string_roman)):
    #რომაულ ნიშნებში ვეძებთ სტრინგის ელემენტებს რომელიც დაემთხვევა
    value = roman_nishnebi[string_roman[i]]
    #თუ ბოლოა ნიშანი და თუ მისი მომდევნო ნიშანი მეტია მაშინ გამოვაკლოთ, რადგან ამ
    #შემთხვევაში მივიღებდით IV 6 ამიტომ გამოკლებაა საჭირო
    if i < len(string_roman) - 1 and roman_nishnebi[string_roman[i+1]] > value:
        gamotana -= value
    #სხვა შემთხვევაში მივუმატოთ რესულტატს
    else:
        gamotana += value
        
print(gamotana)
