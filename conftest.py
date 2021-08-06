from .dist.witness import Witness

def pytest_collection_modifyitems(items, config):
    w = Witness()
    w.testify()