x = input("Enter a country: ")
country_code = {'india' : '0091',
                'Australia' : '0025',
                'Nepal' : '0097'}
print("Country code for India -")
print(country_code.get(x, 'Not found'))
print("Country code for USA -")
print(country_code.get('USA', 'Not found'))