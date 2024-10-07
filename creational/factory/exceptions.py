class SubclassError(Exception):
    """
    Exception raised when a class is not a subclass of another class
    """

    def __init__(self,
                 message: str = "The provided class is not a subclass of the expected class"):
        super().__init__(message)
