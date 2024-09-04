#!/usr/bin/env python3
"""API authentication"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Class for managing authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks if a user is authenticated

        Args:
        path (str): The path to check
        excluded_paths (List[str]): List of paths that do not require
         authentication

        Returns:
            False
        """
        return False

    def authorization_header(self, request=None) -> str:
        """Authorization header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns current user"""
        return None
