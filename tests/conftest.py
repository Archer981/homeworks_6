from pytest_factoryboy import register

from tests.factories import *

pytest_plugins = 'tests.fixtures'

register(AdFactory)
register(CategoryFactory)
register(UserFactory)
