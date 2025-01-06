# pylint_demo.py

# 1. Unused Variables
def test_unused_variable():
    unused_var = 42  # Unused variable
    assert 1 + 1 == 2

# 2. Missing Docstrings
def test_missing_docstring():
    assert 1 + 1 == 2

# 3. Variable Naming Conventions
def test_variable_naming_conventions():
    BAD_VARIABLE_NAME = 42  # Should be in lowercase.
    assert BAD_VARIABLE_NAME == 42
