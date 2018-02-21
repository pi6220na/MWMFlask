class User(object):
    def __init__(self, email, confirmed, first_name, last_name, user_id):
        self.user_id = user_id
        self.email = email
        self.email_confirmed = confirmed
        self.first_name = first_name
        self.last_name = last_name
