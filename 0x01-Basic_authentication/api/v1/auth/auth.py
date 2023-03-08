
EBS@IT-PC2 MINGW64 ~
$ ssh 26832540717b@26832540717b.34dca203.alx-cod.online
26832540717b@26832540717b.34dca203.alx-cod.online's password:
root@26832540717b:/# cd alx-backend-user-data
root@26832540717b:/alx-backend-user-data# cd 0x01-Basic_authentication
root@26832540717b:/alx-backend-user-data/0x01-Basic_authentication# cd api/v1
root@26832540717b:/alx-backend-user-data/0x01-Basic_authentication/api/v1# mkdir auth
root@26832540717b:/alx-backend-user-data/0x01-Basic_authentication/api/v1# cd auth
root@26832540717b:/alx-backend-user-data/0x01-Basic_authentication/api/v1/auth# cat>auth.py
#!/usr/bin/env python3
""" Module of Authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Class to manage the API authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method for requiring authentication """
        if path is None or excluded_paths is None or not len(excluded_paths):
            return True
        # Add slash to all cases for consistency
        if path[-1] != '/':
            path += '/'
        if excluded_paths[-1] != '/':
            excluded_paths += '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Method that handles authorization header """
        if request is None:
            return None

        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('User'):
        """ Validates current user """
        return None
