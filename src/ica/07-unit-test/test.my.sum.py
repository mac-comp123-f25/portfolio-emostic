from mysum import sum3

def test_sum3_ints():
    assert sum3([5, 2, 8, -2])==15

def test_sum3_floats():
    assert sum3([3.0,2.0,5.0])==10.0