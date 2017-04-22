"""Bunch of tools helpful for working with vk api"""
import requests

api_url = 'https://api.vk.com/method/{method_name}?{parameters}&access_token={access_token}'
auth_url = 'https://oauth.vk.com/authorize?client_id={app_id}&scope={scope}&redirect_uri=http://oauth.vk.com/blank.html&display=page&response_type=token'


class VkAPI:
    """The most basic vk API wrapper.

    Usage:
        VkAPI(access_token).method_name(method_argument_name=method_argument_value) -> parsed response json

    Examples:
        vk = VkAPI('face123456789')
        vk.getProfiles(uid=1)
        vk.users.search(q='Vasya Babich')

    Args:
        access_token (str): vk application access token

    Attributes:
        access_token (str): vk application access token
    """

    def __init__(self, access_token):
        self.access_token = access_token

    def __getattr__(self, method_name):
        return Request(method_name, self.access_token)

    def __call__(self, method_name, **method_args):
        return getattr(self, method_name)(**method_args)


class Request:
    """Request handler for VkAPI

    Args:
        method_name: name of vk API method to be called
        access_token: vk application access token

    Attributes:
        method_name: name of vk API method to be called
        access_token: vk application access token
    """

    def __init__(self, method_name, access_token):
        self.method_name = method_name
        self.access_token = access_token

    def __getattr__(self, method_name):
        return Request(self.method_name + '.' + method_name, self.access_token)

    def __call__(self, **method_args):
        data = requests.get(self.format_url(**method_args))
        return data.json()

    def format_url(self, **method_args):
        """Formats url for vk api. E.g https://api.vk.com/method/getProfiles?uid=1&access_token=face123456789

        Args:
            method_args (dict): dictionary containing method arguments name:value pair
        """
        return api_url.format(method_name=self.method_name, parameters=Request.format_parameters(method_args),
                              access_token=self.access_token)

    @staticmethod
    def format_parameters(method_args):
        """Formats method arguments for request url

        Args:
            method_args (dict): method arguments
        """
        if len(method_args) > 0:
            return ('{}={},'.format(*method_args.popitem()) + Request.format_parameters(method_args)).rstrip(',')
        else:
            return ''

    @staticmethod
    def format_scope(scope):
        """Formats scope arguments for auth url

        Args:
            scope (list): requested scope list
        """
        if len(scope) > 0:
            return ('{},'.format(scope.pop()) + Request.format_scope(scope)).rstrip(',')
        else:
            return ''

    @staticmethod
    def generate_auth_token_url(app_id, scope):
        """Generates url to get auth token for application

        Args:
            app_id (int): vk application id
            scope (list): requested scope list
        """
        return auth_url.format(app_id=app_id, scope=Request.format_scope(scope))

if __name__ == '__main__':
    pass
