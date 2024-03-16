from typing import Generator

import pytest
from fastapi.testclient import TestClient

from adapters.src import Connection, SessionManager, SQLConnection
from api.src.create_app import create_app


@pytest.fixture
def api_client() -> TestClient:
    api = create_app()
    client = TestClient(api)

    return client


@pytest.fixture(autouse=True)
def initialize_session() -> Generator[None, None, None]:
    # The FastAPI's TestClient does not trigger the lifespan events,
    # which means the session initialization and closing in the lifespan
    # function are not being executed during testing. So for that reason,
    # this fixture has been created.
    connection: Connection = SQLConnection()
    SessionManager.initialize_session(connection)
    yield
    SessionManager.close_session()
