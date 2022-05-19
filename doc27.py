student = [{'id': 1, 'success': True, 'name': 'Lary'},{'id': 2, 'success': False, 'name': 'Rabi'},
 {'id': 3, 'success': True, 'name': 'Alex'}]
sum = 0
for i in student:
    sum = i['success']
    sum +=1
print('Count for Success is: ',sum)