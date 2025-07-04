# age = int(input('age: '))

# if age < 18 :
#     print('you are young') #indentation is important
# elif age > 18 and age < 30 :
#     print('you are normal age')
# else :
#     print('you are old')

# tired = input('are u tired? "y/n"')
# if tired == 'y' :
#     print('rest well')
# elif tired == 'n' :
#     print('go back to work')
# else :
#     print('please enter y or n')


#homework
username = input('User Name : ')
password = input('Password : ')

# if username == "Yu" and password == "yu" :
#     print("Log in Success")
# else :
#     print("Log in Fail")

if username == "Yu" and password == "yu" :
    print("Log in Success")
elif username == "Yu" :
    print("Your password is wrong")
elif password == "yu" :
    print("Your username or password is wrong")
else :
    print("Log in Fail")