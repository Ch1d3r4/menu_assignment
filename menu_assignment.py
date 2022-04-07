class User():
    first_name = ''
    last_name = ''
    email_address = ''
    phone_number = ''
    gender = ''
    allergies = ''
    user_type = ''

    def __init__(self, first_name, last_name, email_address, phone_number, gender, allergies, user_type):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.phone_number = phone_number
        self.gender = gender
        self.allergies = allergies
        self.user_type = user_type


class Meal():
    name = ''
    allergens = ''
    serving = ''
    image = ''

    def __init__(self, name, allergens, serving, image):
        self.name = name
        self.allergens = allergens
        self.serving = serving
        self.image = image


class Order():
    details = ''
    price = ''

    def __init__(self, details, price):
        self.details = details
        self.price = price


user_eit = User('Zee', 'Sosu', 'zee.sosu@kitchen.org',
                '0500100100', 'male', 'dairy', 'eit')

user_staff = User('Yaa', 'Zazu', 'yaa.zazu@kitchen.org',
                  '0200100100', 'female', 'nuts', 'staff')


new_meal = Meal('creamy chicken pasta',
                'gluten and dairy', 1, 'creamy_pasta.jpg')


new_order = Order('creamy chicken pasta', 10.00)


print(user_staff.first_name)
print(user_eit.first_name)
print(new_meal.name)
print(new_order.price)
