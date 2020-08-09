from sandbox import add

def test_1_plus_2_equal_3_ok():
    a = 1
    b = 2
    c = add(a, b)
    assert c == 3

def test_5_plus_3_equal_9_fail():
    a = 5
    b = 3
    c = add(a, b)
    assert c != 9 
