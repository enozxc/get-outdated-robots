from operator import index
def get_outdated_robots(robots: list, new_version: int) -> list:
    return [
        index for index, robot in enumerate(robots) if robot["core_version"] < new_version
    ]

robots = [
    {"core_version": 9},
    {"core_version": 13},
    {"core_version": 16},
    {"core_version": 9},
    {"core_version": 14},
]

new_version = 10
get_outdated_robots([
    {"core_version": 9},
    {"core_version": 13},
    {"core_version": 16},
    {"core_version": 9},
    {"core_version": 14},
], 10)