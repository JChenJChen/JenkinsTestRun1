import testFile
import pytest
import sys

# @pytest.mark.skip(sys.version_info > (3,5), reason = "skipping")
def test_calc_total():
	total = testFile.calc_total(4,5)
	assert total == 10
	print("test_calc_total passed")

def test_calc_multiply():
	result = testFile.calc_multiply(10,3)
	assert result == 30
	print ("test_calc_multiply passed")