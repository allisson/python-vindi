import os

import pytest

from vindi.api import get_api_instance


@pytest.fixture
def api():
    return get_api_instance(token=os.getenv('API_TOKEN', ''))
