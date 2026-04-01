import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9]+@[a-z]+\.[a-z]+$'
    return re.match(pattern, email)

def validate_userid(uid):
    pattern = r'^[A-Za-z0-9]{4,10}$'
    return re.match(pattern, uid)