def sheamowme(target, arr):
    count = 0
    meore_arr = []
    for num in arr:
        #გავიგოთ სხვაობა ტარგეტისა და მოცემულ ელემენტის
        #თუ მათი სხვაობა იქნება ერეიში ესეიგი ეგეთი წყვილი არსებობს
        #და დავამატოთ ყველა არსებობაზე ქაუნთს
        difference  = target - num
        if difference in meore_arr:
            count += 1
        meore_arr.append(num)
    return count
print(sheamowme(6,arr=[1, 7,  7, -1, 5]))
