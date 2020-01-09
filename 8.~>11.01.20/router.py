#!python3
#-*-encoding:utf-8-*-


class Router:
    AVAILABLE_METHODS = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS']

    def __init__(self):
        self.roster ={}
        self.path_roster = set('')

    def __getattr__(self, attr):
        if attr.upper() in self.AVAILABLE_METHODS:
            return lambda path: self.request(attr.upper(), path)
        raise AttributeError(f'method {attr} is not defined for {self}')

    def add_path(self, path, method, func):
        self.path_roster.add(path)
        if (method, path) in self.roster.keys():
            if ((method, path), func) in self.roster.items():
                return f"path {path} alredy associated with method {method}"
            else:
                self.roster.update([((method, path), func)])
                return f'method {method} added for path {path}'
        else:
            self.roster.update([((method, path), func)])
            return f'method {method} added for path {path}'


    def request(self, method, path):
        if (method, path) not in self.roster.keys():
            if path not in self.path_roster:
                return f'Error 404, path {path} not found'
            else:
                return f'Error 405, Method {method} not allowed'
        else:
            func = self.roster[(method, path)]
            return func(path, method)


def my_info(path, method):
    return 200, {"me": "Joanne"}


def update_me(path, method):
    return 200, "OK"


if __name__ == '__main__':
    router = Router()

    print(router.add_path('/me', 'GET', my_info))
    print(router.add_path('/me', 'GET', my_info))
    print(router.add_path('/me', 'PATCH', update_me))


    print(router.request('GET', '/me'))
    print(router.get('/me'))

    print(router.post( '/me'))
    print(router.get('/us'))