from enum import Enum


class TypeAccess(Enum):
    Admin = "Admin"
    SubAdmin = "Sub_Admin"
    User = "User"

    @classmethod
    def return_types(cls):
        return [f"{cls.Admin}", f"{cls.SubAdmin}", f"{cls.User}"]
