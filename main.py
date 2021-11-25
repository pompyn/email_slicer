
email = input('Enter your email address: ')
user = email[:email.index('@')]
domain_index = email.index("@")
domain_loc = domain_index + 1
domain = email[domain_loc:]

print(f'Your user name is {user}')
print(f' Your domain name is {domain}')
