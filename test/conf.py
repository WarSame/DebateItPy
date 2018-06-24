import debateit
from app import initialize_db
import pytest


@pytest.fixture
def client():
    debateit.app.config["SECRET_KEY"] = "this"
    debateit.app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://pguser:pguser@db:5432/debateit"
    debateit.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    debateit.app.config["TESTING"] = True
    client = debateit.app.test_client()
    with debateit.app.app_context():
        initialize_db()
    yield client
