from faker import Faker

fake = Faker()

def generate_user():
    return {
        "name": fake.name(),
        "email": fake.email(),
        "address": fake.address()
    }

def generate_bulk_users(count=10):
    return [generate_user() for _ in range(count)]

if __name__ == "__main__":
    users = generate_bulk_users(5)
    for user in users:
        print(user)
