list1 = [12, 34, 56, 75, 77, 88, '123', "umer"]
list2 = [34, 54, 56, 44, 75, 77, 89, 123]
uncommon_ele = []


str_list1 = []
i = 0
while i < len(list1):
    str_list1.append(str(list1[i]))
    i += 1


str_list2 = []
k = 0
while k < len(list2):
    str_list2.append(str(list2[k]))
    k += 1


i = 0
while i < len(str_list1):
    j = 0
    found = False
    while j < len(str_list2):
        if str_list1[i] == str_list2[j]:
            found = True
            break
        j += 1
    if not found:
        uncommon_ele.append(list1[i])
    i += 1

k = 0
while k < len(str_list2):
    l = 0
    found = False
    while l < len(str_list1):
        if str_list2[k] == str_list1[l]:
            found = True
            break
        l += 1
    if not found:
        uncommon_ele.append(list2[k])
    k += 1

print("Uncommon elements from both lists are:", uncommon_ele)