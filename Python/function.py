# def greet(person):
#     return f'Hello there, {person}'

# def greet(person):
#     print(f'Hello there, {person}')

# def three_things(a,b,c):
#     print('high')

# def send_email(to_email, from_email, subject, body):
#     email = f'''
#         to:{to_email}
#         from:{from_email}
#         subject:{subject}
#         ------------------------
#         body:{body}
#     '''
#     print(email)

# send_email(subject='stuff', to_email='nick@night.com', body='bin bong donkey kong', from_email='yo@mam.com')

# def power(num, power=2):
#     return num**power

def send_email(to_email, from_email, subject, body):
    '''This is a docstring.  This is what appears if you run the help function for this function'''

    email = f'''
        to:{to_email}
        from:{from_email}
        subject:{subject}
        ------------------------
        body:{body}
    '''
    print(email)