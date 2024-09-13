#!/usr/bin/env python3
"""Salted hash"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """Hash a password with salt"""
    return bcrypt.hashpw(password.encode(encoding='utf-8'), bcrypt.gensalt())
