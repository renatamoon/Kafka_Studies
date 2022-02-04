from faker import Faker
# the fake module is only to create a name, user, address and also a name

fake = Faker()

def get_registered_user():
    return {
        'name': fake.name(),
        'address': fake.address(),
        'created_at': fake.year()
    }


# here we'll put the code to run
if __name__ == '__main__':
    print(get_registered_user())