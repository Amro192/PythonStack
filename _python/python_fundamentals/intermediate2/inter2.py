# x = [ [5,2,3], [10,8,9] ] 
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# x[1][0] = 15
# print(x)

# students[0]['last_name']= 'Brayant'
# print(students)

# sports_directory['soccer'][1]= "Andreas"
# print(sports_directory)

# z[0]['y']=30
# print(z)



students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# def iterateDictionary(students):
#     for student in students:
#         # for key, value in student.items():
#         #     print(f"{key}, - {value}", end=", ")
#         # print("") //another solution
#         print(f"first name - {student['first_name']}, last name - {student['last_name']}")
# iterateDictionary(students) 


# def iterateDictionary(key_name, students):
#     for student in students:
#         print(student[key_name])
# iterateDictionary('first_name',students) 



dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printdojo(dojo):
    counter=0
    for key, values in dojo.items():
        for value in values:
            counter+=1
        print(f"{counter} {key}")    
        print(values)
printdojo(dojo)
