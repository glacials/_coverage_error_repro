from .dist import witness 

# Needs to be run to trigger the error, but doesn't matter whether by the test
# runner or another function
def test_func(self):
    pass

# Must be outside of a test function
witness.testify(123)