# flake8_demo.py

# 1. Unused Imports
import math  # Unused import

def test_unused_import():
    assert 1 + 1 == 2

# 2. Line Length
def test_line_length():
    assert "This is a very long line of code that exceeds the maximum allowed line length in most Python style guides." == "too long"

# 3. Improper Indentation
def test_improper_indentation():
        # This line has an extra space for indentation.
    assert 1 + 1 == 2

# 4. Trailing Whitespace
def test_trailing_whitespace():  
    assert 1 + 1 == 2  # This line has trailing whitespace.

# 5. Unreachable Code
def test_unreachable_code():
    assert 1 + 1 == 2
    return
    assert 2 + 2 == 4  # This line is unreachable.

# 6. Syntax Errors
def test_syntax_error()
    assert 1 + 1 == 2  # Missing colon.

# 7. Blank Line Violations



def test_blank_line_violations():  # Extra blank lines at the start
    assert 1 + 1 == 2
