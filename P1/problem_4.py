class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if not user or not group:
        return False

    users = group.get_users()
    if user in users:

        return True

    else:
        groups = group.get_groups()

        for sgroup in groups:
            check = is_user_in_group(user, sgroup)
            if check is True:
                return True

    return False


print(is_user_in_group("sub_child_user", sub_child))
# True
print(is_user_in_group("sub_child_user", child))
# True
print(is_user_in_group("sub_child_user", parent))
# True
print(is_user_in_group("another_user", parent))
# False
print(is_user_in_group("another_user", child))
# False
print(is_user_in_group("another_user", sub_child))
# False
print(is_user_in_group("", sub_child))
# False
print(is_user_in_group(None, sub_child))
# False
print(is_user_in_group(None, None))
# False








