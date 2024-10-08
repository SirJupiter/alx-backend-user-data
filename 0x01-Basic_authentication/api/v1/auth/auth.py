#!/usr/bin/env python3
"""API authentication"""

from flask import request
from typing import List, TypeVar
import re


class Auth:
    """Class for managing authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks if a user is authenticated

        Args:
        path (str): The path to check
        excluded_paths (List[str]): List of paths that do not require
         authentication
        """
        if path is not None and excluded_paths is not None:
            for exclusion_path in map(lambda x: x.strip(), excluded_paths):
                pattern = ''
                if exclusion_path[-1] == '*':
                    pattern = '{}.*'.format(exclusion_path[0:-1])
                elif exclusion_path[-1] == '/':
                    pattern = '{}/*'.format(exclusion_path[0:-1])
                else:
                    pattern = '{}/*'.format(exclusion_path)
                if re.match(pattern, path):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """Authorization header"""
        if not request:
            return None

        if 'Authorization' not in request.headers:
            return None

        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns current user"""
        return None
