#!python3
#-*-encoding:utf-8-*-


class Router:

    def __init__(self):
        self.roster = {}
        
    def add_path(self, path, method, func):
        self.path = path
        self.method = method
        if method not in self.roster:
            self.roster[self.method] = (self.path, func)

    def request(self, method, path):
        for el, value in self.roster.items():
            if el.lower() == method.lower():
                current_path, func = value
                if current_path == path:
                    return func(path, method)
                else:
                    return 404, "Error 404: Not Found"
        else:
            return 405, "Error 405: Method Not Allowed"


    def get(self, path):
        return self.request(self.get.__name__, path)

    def post(self, path):
        return self.request(self.get.__name__, path)

    def put(self, path):
        return self.request(self.get.__name__, path)

    def patch(self, path):
        return self.request(self.get.__name__, path)

    def delete(self, path):
        return self.request(self.get.__name__, path)

    def options(self, path):
        return self.request(self.get.__name__, path)


def my_info(path, method):
        return 200, {"me": "Joanne"}

def update_me(path, method):
        return 200, "OK"


if __name__ == '__main__':
    router = Router()
    router.add_path("/me", "GET", my_info)
    router.add_path("/me", "POST", update_me)
    router.add_path("/me", "PUT", update_me)
    router.add_path("/me", "PATCH", update_me)
    router.add_path("/me", "DELETE", update_me)
    router.add_path("/me", "GET", my_info)
    router.add_path("/me", "OPTIONS", my_info)

    print(router.roster)

    print(router.get("/me"))
    print(router.post("/me"))
    print(router.get("/us"))
    print(router.put("/me"))
    print(router.patch("/me"))
    print(router.delete("/local"))
    print(router.options("/me"))