class NegativeException(Exception):
    """Raised if a value is below 0"""

    def __init__(self, number: float, error_code: int):
        self.number = number
        self.error_code = error_code
        super().__init__(
            f"{self.number} is less than 0 (ERROR_CODE: {self.error_code})",
            self.number,
            self.error_code,
        )

    def __str__(self):
        return f"{self.number} is less than 0 (ERROR_CODE: {self.error_code})"

    def __reduce__(
        self,
    ):  # to give the class some instructions on how to deserialize it
        return NegativeException, (self.number, self.error_code)

    def custom_method(self):
        print((self.number, self.error_code), "were used by the custom method")


# raise NegativeException(-2, 999)

try:
    raise NegativeException(-2, 999)
except NegativeException as err:
    print(err)
    print(err.error_code)
    print(err.args)

    err.custom_method()
