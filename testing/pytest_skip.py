import pytest
import sys

def test_simple_skip():
	if sys.platform != "fakeos":
		pytest.skip("Test only works on fakeOs")
	fakeos.do_something_fake()
	assert fakeos.did_nont_happen