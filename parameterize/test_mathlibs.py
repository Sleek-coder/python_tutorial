import mathlibs 

import pytest 

@pytest.mark.parametrize("test_input,expected_output",
                          [
                              (5,25),
                              (9,81),
                              (10,100)
                          ]
                          )
def test_calc_square_(test_input, expected_output):
    
    result = mathlibs.calc_square(test_input)
    assert result == expected_output 
    
