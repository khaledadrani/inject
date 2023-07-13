from functools import partial

from inject.providers import SingletonProvider, Provider
from tests.conftest import DummyDatabase


class TestSingletonProvider:
    def setup_method(self):
        self.object_to_provide = DummyDatabase
        self.construct_args = {"connection_string": "db_url"}
        self.create_provide_object = partial(SingletonProvider, self.object_to_provide, **self.construct_args)

    def test_singleton_provide(self):
        provider = self.create_provide_object()

        first_object = provider()
        second_object = provider()

        assert id(first_object) == id(second_object)