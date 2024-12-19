class NotFoundError(Exception):
    def __init__(self, detail):
        self.status_code = 404
        self.detail = detail
        super().__init__(self.detail)


class NotUniqueError(Exception):
    def __init__(self, detail):
        self.status_code = 409
        self.detail = detail
        super().__init__(self.detail)
