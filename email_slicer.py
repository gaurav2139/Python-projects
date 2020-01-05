email = input("Enter your Email ID:")
user_name = email[:email.index("@")]
domain_name = email[email.index("@")+1:]
result = "Your username is Email is {}, Your username is {}, Your doamin name is {}".format(email,user_name,domain)
print(result)