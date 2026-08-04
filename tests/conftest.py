from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import INITIAL_ACTIVITIES, activities, app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    activities.clear()
    activities.update(deepcopy(INITIAL_ACTIVITIES))
    yield
