from functools import partial

from inject.exceptions import ProvideObjectError


class Provider(type):
    def __setitem__(self, key, value):
        self.__dict__[key] = value


class FactoryProvider:
    def __init__(self, object_class, **kwargs):
        self.object_class = object_class
        self.arguments = kwargs

        self.dependencies = {k: v for k, v in self.arguments.items() if isinstance(v, Provider)}

        self._provide = partial(self.object_class, **self.arguments)

    def __str__(self):
        return f"Provider<{self.object_class.__class__}>"

    def provide(self) -> object:
        resolved = {k: v.provide() for k, v in self.dependencies.items()}
        resolved_provide = partial(self._provide, **resolved)
        try:
            return resolved_provide()
        except TypeError as error:
            raise ProvideObjectError(message=str(error)) from error

    def __call__(self) -> object:
        return self.provide()


class SingletonProvider(FactoryProvider):
    def __init__(self, object_class, **kwargs):
        super().__init__(object_class, **kwargs)
        self._instance = None

    def provide(self) -> object:
        if self._instance is None:
            resolved = {k: v.provide() for k, v in self.dependencies.items()}
            resolved_provide = partial(self._provide, **resolved)
            self._instance = resolved_provide()
        return self._instance
