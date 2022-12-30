user = {"username": "jose", "access_level": "guest"}

def get_admin_password():
    return "1234"

print(get_admin_password())

if user["access_level"] == "admin":
    print(get_admin_password())


print(get_admin_password())