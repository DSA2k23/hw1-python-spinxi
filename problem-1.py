# def sheamowme(arr):
#     #მთლიანი ჯამი
#     total_sum = 0
#     #მარცხენა ჯამი
#     left_sum = 0
#     #გავიგოთ მთლიანი ჯამი
#     for i in range(len(arr)):
#         total_sum += arr[i]
#     #გავიგოთ მარცხენას ჯამი ტოლია თუარა მთლიანს გამოკლებული მარცხენა და ელემენტი რომელზეც ვართ
#     for i in range(len(arr)):
#         #თუ უდრის ეგაა
#         if left_sum == total_sum - left_sum - arr[i]:
#             return f"YES SIR WE HAVE NUMBER:INDEX ==> {arr[i]}:{i}"
#         #თუ იფში არ შევა დავამატოთ მარცხენას ყველა ელემენტი
#         left_sum += arr[i]
#     #თუ არა არა
#     return "NO"

# print(sheamowme(arr=[1, 2, 5, 3]))


def sheamowme(arr):
    #მთლიანი ჯამი
    total_sum = 0
    #მარცხენა ჯამი
    left_sum = 0
    #გავიგოთ მთლიანი ჯამი
    for i in range(len(arr)):
        total_sum += arr[i]
    #გავიგოთ მარცხენას ჯამი ტოლია თუარა მთლიანს გამოკლებული მარცხენა და ელემენტი რომელზეც ვართ
    for i in range(len(arr)):
        #თუ უდრის ეგაა
        if left_sum == total_sum - left_sum - arr[i]:
            return f"YES SIR WE HAVE NUMBER:INDEX ==> {arr[i]}:{i}"
        #თუ იფში არ შევა დავამატოთ მარცხენას ყველა ელემენტი
        left_sum += arr[i]
    #თუ არა არა
    return "NO"


arr_nums = (input("შემოიტანე მასივი: "))
arr = []

elements = arr_nums.split(' ')
for element in elements:
    arr.append(int(element))
res = sheamowme(arr)
print(res)



