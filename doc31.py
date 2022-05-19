student_list = {'S 001': ['Math', 'Science'], 'S 002': ['Math', 'English']}
for key,values in list(student_list.items()):
    word = ""
for i in key:
    if i != " ":
        word += i
print(word)
student_list[word] = student_list.pop(key)
print(student_list)


input = {'S 001': ['Math', 'Science'], 'S 002': ['Math', 'English']}
output = { key.replace(" ", "") :value for key, value in input.items() }
print(output)