# you got some source code and it is throwing some nasty error
# what is happening, how do you solve it?

user_emails = [
    {
        "email": "joe@example.com",
        "birthdaa": "01/01/1900"
    },
    {
        "emaile": "joe@example.com",
        "birthday": "01/01/1900"
    },
    {
        "email": "joe@example.com",
        "birthday": "01/01/1900"
    }
]

#print out the user's birthdays
# real-life example might be to email users if it is their birthday offering a promotion

def get_users():
    return user_emails
def send_user_promotion(user):
    print(user['birthday'], user['email'])


for u in get_users():
    try:
        send_user_promotion(u)
    except KeyError as e:
        print("Data malformed", e)


def create_user(name, email):
    if ('@' in email):
        print("Valid email")
        #user_emails.append({'name': name, 'email': email})
    else:
        raise ValueError(email + " is not a valid email")
    return "new user"

try:

    user1 = create_user("Jon", "jon@email.com")
#this one throws an error
    user2 = create_user("Joe", "joeemail.com")
except ValueError as e:
    print(e)
else:
    print("what happened", user1)
finally:
    print("return to your router")

# Why would you want this in a programming language?

