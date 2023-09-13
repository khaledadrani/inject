from pydantic.v1 import BaseSettings


class DummyConfig(BaseSettings):
    HOST: str = "localhost"
    PORT: int = 8700
    ENV: str = "prod"


class DummyDatabase:
    def __init__(self, connection_string: str):
        self.connection_string = connection_string


class DummyRepository:
    def __init__(self, db: DummyDatabase):
        self.db = db


class DummyService:
    def __init__(self, repository: DummyRepository):
        self.repository = repository

    def get_upper_case(self, query: str):
        return self.repository.db.connection_string + ": " + query.upper()


def do_something(db: DummyDatabase):
    return db.connection_string
