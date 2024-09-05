#!/usr/bin/env python3
"""File contains class BasicAuth"""

from api.v1.auth.auth import Auth
import base64
from typing import TypeVar, Tuple
from models.user import User


class BasicAuth(Auth):
    """BasicAuth class"""
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """Extracts base64 encoded string from authorization header"""
        if not authorization_header or not type(authorization_header) is str:
            return None

        if authorization_header[0:6] != 'Basic ':
            return None

        base64_str = authorization_header.split(' ')[1]
        return base64_str

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Decodes base64 string"""
        if not base64_authorization_header:
            return None

        if not type(base64_authorization_header) is str:
            return None

        try:
            decoded_str = base64.b64decode(
                base64_authorization_header).decode('utf-8')
            return decoded_str
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> Tuple[str, str]:
        """extracing data"""
        if decoded_base64_authorization_header is None:
            return (None, None)

        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)

        if ":" not in decoded_base64_authorization_header:
            return (None, None)

        username, password = decoded_base64_authorization_header.split(":")
        return (username, password)

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """Returns User object or None if not found"""
        if (user_email is None
                or not isinstance(user_email, str)):
            return None

        if (user_pwd is None
                or not isinstance(user_pwd, str)):
            return None

        user_list = User.all()
        if not user_list:
            return None
        valid_user = None

        for user in user_list:
            if user.email == user_email:
                valid_user = user

        if valid_user is None:
            return None

        if not valid_user.is_valid_password(user_pwd):
            return None

        return valid_user

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieves the user from a request.
        """
        auth_header = self.authorization_header(request)
        b64_auth_token = self.extract_base64_authorization_header(auth_header)
        auth_token = self.decode_base64_authorization_header(b64_auth_token)
        email, password = self.extract_user_credentials(auth_token)
        return self.user_object_from_credentials(email, password)
