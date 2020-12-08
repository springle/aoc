import re

from collections import defaultdict
from functools import lru_cache

from util import timer


class ColorGraph:
    rule_pattern = re.compile(r"^(.*?) bags contain (.*?).$")
    clause_pattern = re.compile(r"^(\d+) (.*?) bags?")
    gold = "shiny gold"

    def __init__(self, path: str):
        self.graph = defaultdict(dict)
        with open(path) as file:
            for line in file:
                color, rule = re.match(self.rule_pattern, line.strip()).groups()
                for clause in rule.split(", "):
                    try:
                        quantity, contained_color = re.match(self.clause_pattern, clause).groups()
                        self.graph[color][contained_color] = int(quantity)
                    except AttributeError:
                        pass

    @lru_cache
    def num_bags_inside(self, color: str) -> int:
        if color not in self.graph:
            return 0

        total = 0
        for contained_color, multiplier in self.graph[color].items():
            total += multiplier + multiplier * self.num_bags_inside(contained_color)

        return total

    @lru_cache
    def contains_gold(self, color: str) -> bool:
        if color in self.graph.keys():
            for contained_color in self.graph[color].keys():
                if contained_color == self.gold or self.contains_gold(contained_color):
                    return True

        return False


if __name__ == "__main__":
    with timer():
        color_graph, total = ColorGraph("input"), 0
        for color in color_graph.graph.keys():
            if color_graph.contains_gold(color):
                total += 1

        print(total)
