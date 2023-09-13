# Inject, a dependency injection framework for Python projects

Read me!

# TODO
* if possible implement cooler getters for providers
```
#caude that is problematic
# def __getattr__(self, item):
    #
    #     def get_attribute_workaround(custom_object, attribute_name):
    #         return getattr(custom_object, attribute_name)
    #
    #     try:
    #         return get_attribute_workaround(self.provide(), item)
    #     except AttributeError as error:
    #         raise ProvideObjectAttributeError(message=str(error)) from error
```