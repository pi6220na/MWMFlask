class User(object):
    def __init__(self, email=None, confirmed=0, admin=0, first_name=None, last_name=None, user_id=None, db_user=None):
        if db_user is not None:
            """ If creating user from db call unpack tuple """
            if isinstance(db_user, tuple):
                self.user_id = db_user[5]
                self.email = db_user[0]
                self.email_confirmed = db_user[1]
                self.admin = db_user[2]
                self.first_name = db_user[3]
                self.last_name = db_user[4]
            else:
                raise TypeError
        else:
            """ creating user from parameters """
            self.user_id = user_id
            self.email = email
            self.admin = admin
            self.email_confirmed = confirmed
            self.first_name = first_name
            self.last_name = last_name

    def __eq__(self, other):
        """Override the default Equals behavior"""
        return self.user_id == other.user_id \
            and self.email == other.email \
            and self.admin == other.admin \
            and self.email_confirmed == other.email_confirmed \
            and self.first_name == other.first_name \
            and self.last_name == other.last_name

    def is_admin(self):
        if self.admin:
            return True
        else:
            return False

    def is_confirmed(self):
        if self.email_confirmed:
            return True
        else:
            return False
