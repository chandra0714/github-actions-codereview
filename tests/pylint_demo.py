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

# 4. Too Many Arguments
def function_with_too_many_args(a, b, c, d, e, f):  # Too many arguments
    return a + b + c + d + e + f

def test_too_many_arguments():
    assert function_with_too_many_args(1, 2, 3, 4, 5, 6) == 21

# 5. Too Many Local Variables
def test_too_many_local_variables():
    a, b, c, d, e, f, g, h, i, j, k, l, m, n, o = range(15)  # Too many local variables
    assert a + b == 1

# 6. Cyclomatic Complexity
def test_cyclomatic_complexity(x):
    if x > 0:
        if x % 2 == 0:
            return "Even"
        else:
            return "Odd"
    elif x == 0:
        return "Zero"
    else:
        return "Negative"  # High cyclomatic complexity.

# 7. Missing Return Statements
def function_with_missing_return():
    if True:
        return 42

def test_missing_return():
    assert function_with_missing_return() == 42

# 8. Dangerous Default Values
def function_with_mutable_default(x=[]):  # Mutable default argument
    x.append(42)
    return x

def test_dangerous_default_values():
    result = function_with_mutable_default()
    assert result == [42]
