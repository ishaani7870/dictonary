studentlist = {'S 001': ['Math', 'Science'], 'S 002': ['Math', 'English'], 'S 00 3': ['Computer', 'Mathematics']}
for key,vals in studentlist.items():
    studentlist[key.replace('', '')] = studentlist.pop(key)
print(studentlist)
