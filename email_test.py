email1 = 'pawel.rubach@sgh.waw.pl'
email2 = '@sgh.waw.pl'
email3 = 'pawel@pl'
email4 = 'pawel@'
email5 = 'pawel@edeh.'
email6 = 'pawel@.pl'

email_list = [email1, email2, email3, email4, email5, email6]

#TODO create a function that will test if the email is valid
def validate_email(email):
    #if email[-1] == '.' or email[-1] == '@':
    if email[-1] in ['.', '@']:
        return False
    #email[-1]
    #....
    return True

#print(email6[-1])

for em in email_list:
    print('{}: {}'.format(em, validate_email(em)))

#print(validate_email(email1))