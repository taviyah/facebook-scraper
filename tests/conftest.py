import pytest


@pytest.fixture(scope="module")
def vcr_cassette_dir(request):
    return "tests/cassettes"
