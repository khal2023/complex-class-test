from lib.most_often import *


#add item to list
def test_item_added():
    mo = MostOften(["apple", "pear"])
    mo.add_new("banana")
    assert mo.starting_list == ["apple", "pear", "banana"]

def test_added_int_and_str():
    mo = MostOften([6, "banana", 7, 8, "grape", "eggs"])
    mo.add_new("grape")
    mo.add_new(7)
    assert mo.starting_list == [6, "banana", 7, 8, "grape", "eggs", "grape", 7]

#most often calculation
def test_most_often():
    mo = MostOften(["apple", "apple", "apple", "banana", "dragonfruit"])
    assert mo.get_most_often() == "apple"

def test_most_often_int_and_str():
    mo = MostOften([6, "banana", 7, 8, "grape", "eggs", "grape", 7, 7])
    assert mo.get_most_often() == 7

#clear winner returned
#no clear winner message
def test_all_losers():
    mo = MostOften(["apple", "dragonfruit", "kiwi", "orange"])
    assert mo.get_most_often() == "no clear winner"

def test_no_winner_int_and_str():
    mo = MostOften([6, "banana", 7, 8, "grape", "eggs"])
    assert mo.get_most_often() == "no clear winner"


