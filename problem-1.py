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
#             return "YES"
#         #თუ იფში არ შევა დავამატოთ მარცხენას ყველა ელემენტი
#         left_sum += arr[i]
#     #თუ არა არა
#     return "NO"

# print(sheamowme(arr=[1, 2, 5, 3]))


def sheamowme(arr):
    if(len(arr) >=3):
        #მთლიანი ჯამი
        total_sum = 0
        #მარცხენა ჯამი
        left_sum = 0
        #გავიგოთ მთლიანი ჯამი
        for i in range(len(arr)):
            total_sum += int(arr[i])
        #გავიგოთ მარცხენას ჯამი ტოლია თუარა მთლიანს გამოკლებული მარცხენა და ელემენტი რომელზეც ვართ
        for i in range(len(arr)):
            #თუ უდრის ეგაა
            if left_sum == total_sum - left_sum - int(arr[i]):
                return f"YES"
            #თუ იფში არ შევა დავამატოთ მარცხენას ყველა ელემენტი
            left_sum += int(arr[i])
        #თუ არა არა
        return "NO"
    elif(len(arr) == 1):
        return "YES"
    else:
        return "NO"

n = int(input())
arr = list(map(int, input().split()))
res = sheamowme(arr)
print(res)


