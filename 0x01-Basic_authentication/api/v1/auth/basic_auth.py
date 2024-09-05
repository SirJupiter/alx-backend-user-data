#!/usr/bin/env python3
"""File contains class BasicAuth"""

from api.v1.auth.auth import Auth


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
