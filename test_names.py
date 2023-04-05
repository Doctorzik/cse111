from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest


def test_make_full_name():

  full = make_full_name("jeremiah", "gabriel")
  assert isinstance(full, str)

  #Call the make_full_name with assert to test the
  #  funtion
  assert make_full_name("jeremiah","gabriel") == "jeremiah;gabriel"
  assert make_full_name("togbaturi", "gabriel") == "togbaturi;gabriel"

def test_extract_family_name(full):
  family = full.index(";")



def test_extract_given_name():
 pytest.main(["-v", "--tb=line", "-rN", __file__])
