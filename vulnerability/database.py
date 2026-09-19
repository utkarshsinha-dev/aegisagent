def get_user(username):
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    return query