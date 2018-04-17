from __future__ import division

users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}
]

friendships = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (5, 7),
    (6, 8),
    (7, 8),
    (8, 9)
]


def make_friends():
    for user in users:
        user['friends'] = []

    for i, j in friendships:
        first_friend = next(user for user in users if user["id"] == i)
        second_friend = next(user for user in users if user["id"] == j)

        first_friend['friends'].append(second_friend)
        second_friend['friends'].append(first_friend)


def number_of_friends(user):
    return len(user['friends'])


if __name__ == "__main__":
    make_friends()
    total_connections = sum(number_of_friends(user) for user in users)
    num_users = len(users)
    print("Average friends: {}".format(total_connections / num_users))
