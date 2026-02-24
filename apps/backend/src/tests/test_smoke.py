import pytest


@pytest.mark.django_db
def test_db_smoke():
    assert True
