#!/usr/bin/env python3
"""Salted hash"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4


def _hash_password(password: str) -> bytes:
    """Hash a password with salt"""
    return bcrypt.hashpw(password.encode(encoding='utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """Generate a random UUID"""
    return str(uuid4())


class Auth:
    """auth class to interact with the authentication database"""
    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers user"""

        hashed_password = _hash_password(password)

        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            return self._db.add_user(email, hashed_password)

        raise ValueError('User {} already exists'.format(email))

    def valid_login(self, email: str, password: str) -> bool:
        """Validates user login"""

        try:
            user = self._db.find_user_by(email=email)

            return bcrypt.checkpw(
                password.encode(encoding='utf-8'), user.hashed_password)

        except NoResultFound:
            return False
