import functools

user = {"username": "jose", "access_level": "guest"}

def make_secure(func):
    @functools.wraps(func)
    def secure_function(panel):
        if user["access_level"] == "admin":
            return func(panel)
        else:
            return f"No admin permissions for {user['username']}."

    return secure_function