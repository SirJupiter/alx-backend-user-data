#!/usr/bin/env python3
"""File contains class BasicAuth"""

from api.v1.auth.auth import Auth
import base64


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

        # if not type(base64_authorization_header) is str:
        #     return None

        try:
            decoded_str = base64.b64decode(base64_authorization_header).decode('utf-8')
            return decoded_str
        except Exception:
            return None
