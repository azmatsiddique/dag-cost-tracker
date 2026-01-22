import pytest
import os
from dag_cost_tracker.db import init_db, get_session
from dag_cost_tracker.models import Base

@pytest.fixture
def test_db_path(tmp_path):
    return str(tmp_path / "test_dag_cost.db")

@pytest.fixture
def session(test_db_path):
    engine = init_db(test_db_path)
    Session = get_session(test_db_path)
    session = Session()
    yield session
    session.close()
    if os.path.exists(test_db_path):
        os.remove(test_db_path)
