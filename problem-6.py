# def sheamowme(arr, target):
#     count = 0
#     meore_arr = []
#     for num in arr:
#         #გავიგოთ სხვაობა ტარგეტისა და მოცემულ ელემენტის
#         #თუ მათი სხვაობა იქნება ერეიში ესეიგი ეგეთი წყვილი არსებობს
#         #და დავამატოთ ყველა არსებობაზე ქაუნთს
#         difference  = target - num
#         if difference in meore_arr:
#             count += 1
#         meore_arr.append(num)
#     return count
# n = int(input())
# print(sheamowme(list(map(int, input().split())), int(input())))


def sheamowme(arr, target):
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == target:
                count += 1
    return count
n = int(input())
print(sheamowme(list(map(int, input().split())), int(input())))

