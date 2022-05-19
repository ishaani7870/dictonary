l = [{"V":"S001"},
     {"V": "S002"}, 
     {"VI": "S001"},
     {"VI": "S005"}, 
     {"VII":"S005"}, 
     {"V":"S009"},
     {"VIII":"S007"}]
a=set(val for i in l for val in i.values())
print(a)