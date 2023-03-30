num = 1232
#სევინახოთ ნიშნები და რიცხვები
roman_nishnebi = [
    (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'),
    (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'),
    (5, 'V'), (4, 'IV'), (1, 'I')
]
# აქ შევინახავთ რაც დაეთხვევა ლუპიდან
gamosatani_roman_nishani = ''

for value, key in roman_nishnebi:
    #თუ იყოფა რამდენჯერ ეტევა 
    count = num // value
    #თუ ჩაეტია ერთხელ ან ორჯერ ან ნ ჯერ მაშინ იმდენი სიმბოლო ავიღოთ რამდენჯერაც ჩაეტია
    gamosatani_roman_nishani += key * count
    #თუ ჩაეტია გამოვაკლოთ რიცხვს და დანარჩენზე იგივე გავაკეთოთ
    num -= value * count
print(gamosatani_roman_nishani)
