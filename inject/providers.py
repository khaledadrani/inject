# dependency injector with Composition
from functools import partial

from inject.exceptions import ProvideObjectError, ProvideObjectAttributeError


class Provider:
    def __init__(self, object_class, **kwargs):
        self.object_class = object_class
        self.arguments = kwargs

        self.dependencies = {k: v for k, v in self.arguments.items() if isinstance(v, Provider)}

        self._provide = partial(self.object_class, **self.arguments)

    def __str__(self):
        return f"Provider<{self.object_class.__class__}>"

    def provide(self):
        resolved = {k: v.provide() for k, v in self.dependencies.items()}
        resolved_provide = partial(self._provide, **resolved)
        try:
            provided = resolved_provide()
            print('created an object! ', str(self.__class__))
            return provided
        except TypeError as error:
            raise ProvideObjectError(message=str(error)) from error

    def __call__(self):
        return self.provide()

    def __getattr__(self, item):
        def get_attribute_workaround(custom_object, attribute_name):
            return getattr(custom_object, attribute_name)
        try:
            return get_attribute_workaround(self.provide(), item)
        except AttributeError as error:
            raise ProvideObjectAttributeError(message=str(error)) from error


class SingletonProvider(Provider):
    def __init__(self, object_class, **kwargs):
        super().__init__(object_class, **kwargs)
        self._instance = None

    def provide(self):
        if self._instance is None:
            resolved = {k: v.provide() for k, v in self.dependencies.items()}
            resolved_provide = partial(self._provide, **resolved)
            self._instance = resolved_provide()
            print('creating for the first time!', str(self.__class__))
        return self._instance
