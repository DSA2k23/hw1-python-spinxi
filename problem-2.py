# def atobitidan_samobiti(num):
#     if num == 0:
#         return '0'
#     else:
#         samobiti = ''
#         while num > 0:
#             #ვიგებთ ნაშთს
#             nashti = num % 3
#             #ვუმატებთ სტრინგად ნაშთს
#             samobiti += str(nashti)
#             #რიცხვი გავყოთ სამზე და ახლა ამ დარჩენილზე იგივე წავიდა სანამ 0 არ უდრის
#             num = num // 3
#         return samobiti
# print(atobitidan_samobiti(int(input())))

def atobitidan_samobiti(num):
    if num == 0:
        return '0'
    else:
        samobiti = ''
        while num > 0:
            #ვიგებთ ნაშთს
            nashti = num % 3
            #ვუმატებთ სტრინგად ნაშთს
            samobiti += str(nashti)
            #რიცხვი გავყოთ სამზე და ახლა ამ დარჩენილზე იგივე წავიდა სანამ 0 არ უდრის
            num = num // 3
        return samobiti[::-1]




num = int(input())

res = atobitidan_samobiti(num)

print(res)
