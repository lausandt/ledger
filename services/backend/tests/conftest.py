from typing import Generator

from fastapi.testclient import TestClient

from pytest import fixture

from src.main import app as _app


@fixture(scope='module')
def client() -> Generator:
    with TestClient(_app) as client:
        yield client
