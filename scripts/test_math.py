# scripts/test_math.py
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def test_add():
    assert add(2, 3) == 5, "add(2,3) should be 5"
    assert add(0, 0) == 0, "add(0,0) should be 0"
    assert add(-1, 1) == 0, "add(-1,1) should be 0"
    print("✅ test_add passed")

def test_multiply():
    assert multiply(3, 4) == 12, "multiply(3,4) should be 12"
    assert multiply(0, 5) == 0,  "multiply(0,5) should be 0"
    print("✅ test_multiply passed")

if __name__ == "__main__":
    test_add()
    test_multiply()
    print("All tests passed!.")