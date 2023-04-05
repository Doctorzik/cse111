import pytest

from quiz import get_percentage, get_accolade


def test_get_accolade():

  accolade = get_accolade(50)

  assert accolade == "Well done! you did a great Job"

  accolade = get_accolade(40)

  assert accolade == "Please Try Harder Next time"


def test_get_percentage():
  percent = get_percentage(1, 1)

  assert percent == 100 
  

  percent = get_percentage(5, 10)

  assert percent == 50


pytest.main(["-v", "--tb=line", "-rN", __file__])
