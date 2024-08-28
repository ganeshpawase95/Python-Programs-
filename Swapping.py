def consicutive_swapping(list):
    for i in range(0, len(list)-1, 2):
        list[i], list[i+1] = list[i+1], list[i]
    return list

print(consicutive_swapping([1,10,45,20,40,12,95]))