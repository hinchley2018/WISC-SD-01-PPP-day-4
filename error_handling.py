# you got some source code and it is throwing some nasty error
# what is happening, how do you solve it?

user_emails = [
    {
        "email": "joe@example.com",
        "birthdaa": "01/01/1900"
    },
    {
        "email": "joe@example.com",
        "birthday": "01/01/1900"
    },
    {
        "email": "joe@example.com",
        "birthdya": "01/01/1900"
    }
]

#print out the user's birthdays
# real-life example might be to email users if it is their birthday offering a promotion
for u in user_emails:
    print(u['birthday'])
