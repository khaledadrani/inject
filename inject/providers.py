# dependency injector with Composition
from functools import partial


class Provider:
    def __init__(self, object_class, **kwargs):
        self.object_class = object_class
        self.arguments = kwargs

        self.dependencies = {k: v for k, v in self.arguments.items() if isinstance(v, Provider)}

        self._provide = partial(self.object_class, **self.arguments)

    def __str__(self):
        return "object"

    def provide(self):
        resolved = {k: v.provide() for k, v in self.dependencies.items()}
        resolved_provide = partial(self._provide, **resolved)
        print('created an object! ', str(self.__class__))
        return resolved_provide()

    def __call__(self):
        return self.provide()

    def __getattr__(self, item):
        def get_attribute_workaround(custom_object, attribute_name):
            return getattr(custom_object, attribute_name)

        return get_attribute_workaround(self.provide(), item)


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
