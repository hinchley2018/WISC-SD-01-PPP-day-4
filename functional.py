area = lambda length, width: length * width
users = [
    {
        "name": "jonathon"
        "age": 23
    },
    {
        "name": "joe"
        "age": 18
    }
]

# list comprehension to generate a list
user_names = [u['email'] for u in users]

#equivalent code to do the same
user_names = []
for (u in users):
    user_names.append(u['name'])

#set comprehensions can have conditionals at end
users_under_twenty_one = {u['name'] for u in users if u['age'] < 21}


users_under_twenty_one = {u['name'] for num in numbers}



# Activity on functional programming
#https://digitalskills.instructure.com/courses/4079/pages/python-tricks-practice-ppp-4-functional-programming-in-python-2?module_item_id=548810

#1
grades = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
sorted_grades = sorted(grades, key = lambda x: x[1])
print(sorted_grades)

#2
cubes = [num ** 3 for num in [3,6,9,2]]
print(cubes)

#3
even_odd = lambda n: x % 2 == 0
evens = [even_odd(num) for num in [3,6,9,2]]
print(evens)


#4 
[i for i in range(1,101)]

#5
{word: len(word) for word in sent.split()}