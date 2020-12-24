from patterns.fabric_pattern.MilkFabric import CheeseFabric, SourCreameFabric
from patterns.fabric_pattern.Product import Cheese, SourCreame


def get_cheese_list():
    cheese_list = [Cheese(), Cheese(), Cheese()]
    return cheese_list


def test_fabric(monkeypatch):
    cheesefabric = CheeseFabric()
    monkeypatch.setattr(cheesefabric, "deliver", get_cheese_list)
    assert len(cheesefabric.deliver()) == 3
    sourcreamefabric = SourCreameFabric()
    assert type(sourcreamefabric.deliver(2)) == list
    assert len(sourcreamefabric.deliver(2)) == 2
    assert type(sourcreamefabric.deliver(2)[0]) == SourCreame


