#!/usr/bin/env python3
'''Auth class'''
from flask import request
from typing import List, TypeVar


class Auth():
    """
    Manages API Authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        -  paths
        - excluded_paths
        """
        if path is None:
            return True
        if excluded_paths is None or excluded_paths == []:
            return True
        if not path.endswith("/"):
            path += "/"
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        returns None
        """
        if request is None: 
            return None
        header = request.headers.get('Authorization')
        if header is None:
            return None
        return header

    def current_user(self, request=None) -> TypeVar('User'):
        """
        returns None
        """
        return None
