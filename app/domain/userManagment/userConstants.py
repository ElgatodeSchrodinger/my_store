import enum

class UserRoles(enum.Enum):

    admin = 'admin'
    anonymous = 'anonymous'

    def __str__(self):
        return self.value