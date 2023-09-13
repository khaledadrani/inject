class Injector:
    """
    Declarative Injector
    """

    def __add_components(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        setattr(self, 'providers', tuple(kwargs.keys()))

    def __new__(cls, *args, **kwargs):
        instance = object.__new__(cls)
        data = instance.__extract_attributes()
        instance.__add_components(**data)
        return instance

    def __extract_attributes(self):
        members = [attr for attr in dir(self) if not attr.startswith("__")]
        return {k: v for k, v in dict(vars(self.__class__)).items() if k in members}
