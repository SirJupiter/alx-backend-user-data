#!/usr/bin/env python3
"""Salted hash"""

import bcrypt
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """Hash a password with salt"""
    return bcrypt.hashpw(password.encode(encoding='utf-8'), bcrypt.gensalt())


class Auth:
    """auth class to interact with the authentication database"""
    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers user"""

        hashed_password = _hash_password(password)
        user = self._db.find_user_by(email=email)

        if user:
            raise ValueError('User {} already exists'.format(email))

        return self._db.add_user(email, hashed_password)
