import hashlib
import os
import re
from typing import Dict

from pydantic import ValidationError
from sqlalchemy.orm import Session

from repositories.UserRepository import UserRepository


class UserAuthentication:
    is_login: bool = False
    login: str = "Login"
    session: Session
    permissions: Dict = {}

    @classmethod
    async def check(cls, login_, password_):
        repo: UserRepository = UserRepository()
        base = await repo.get_by_email(login_)
        hash_salt, hash_pw = base.entity['entity_'].password.get_secret_value().split(':')
        salt = bytes.fromhex(hash_salt)
        pwd_2 = cls.cript_password(password_, salt)
        if cls.check_pwd(pwd_2, base, login_):
            cls.is_login = False
            raise ValidationError("Login Incorreto")
        cls.is_login = True
        cls.login = base.entity['entity_'].login
        cls.permissions = cls.give_permissions(base)

    @classmethod
    def check_pwd(cls, password_, base, login_) -> bool:
        return True if (
                password_ is not None
                and login_ is not None
                and base.entity is not None
                and password_ != base.entity['entity_'].password.get_secret_value()
        ) else False

    @classmethod
    async def create_user(cls, login_, password_):
        repo: UserRepository = UserRepository()
        base = await repo.get_by_email(login_)
        if cls.check_pwd(password_, base, login_):
            cls.is_login = False
            raise ValidationError("Login Incorreto")
        cls.is_login = True
        cls.login = base.entity['entity_'].login
        cls.permissions = cls.give_permissions(base)

    @classmethod
    def give_permissions(cls, base):
        roles: Dict = {
            "Admin": {
                "User": ["Create", "Read", "Update", "Delete"],
                "stock": ["Create", "Read", "Update", "Delete"],
                "supplier": ["Create", "Read", "Update", "Delete"],
                "product": ["Create", "Read", "Update", "Delete"],
            },
            "Sub_Admin": {
                "User": [],
                "stock": ["Create", "Read", "Update"],
                "supplier": ["Create", "Read", "Update"],
                "product": ["Create", "Read", "Update"],
            },
            "User": {
                "User": [],
                "stock": ["Read"],
                "supplier": ["Read"],
                "product": ["Read"],
            },
        }
        return roles[f"{base.entity['entity_'].typeAccess.value}"]

    @classmethod
    def validate_password(cls, password):
        pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[!@+$%&#/€?*.-])[a-zA-Z\d!@+$%&#/€?*.-]{8,16}$'

        if re.match(pattern, password):
            return True
        else:
            return False

    @classmethod
    def cript_password(cls, password, salt=os.urandom(16)):
        salt_hex = salt.hex()
        password_hash = hashlib.pbkdf2_hmac(
            'sha256', password.encode('UTF-8'), salt, 100000)
        return f'{salt_hex}:{password_hash.hex()}'

    @classmethod
    def user_logout(cls):
        cls.is_login = False
        cls.is_login: bool = False
        cls.login: str = "Login"
        cls.session: Session
        cls.permissions: Dict = {}
