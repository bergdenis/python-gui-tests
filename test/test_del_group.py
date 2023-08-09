from model.group import Group
import random


def test_del_group(app):
    if len(app.groups.get_group_list()) == 1:
        app.groups.add_new_group(Group(name="Temp_group"))
    old_list = app.groups.get_group_list()
    index = random.choice(range(len(old_list)))
    app.groups.del_group_by_index(index)
    new_list = app.groups.get_group_list()
    old_list.pop(index)
    assert sorted(old_list) == sorted(new_list)
