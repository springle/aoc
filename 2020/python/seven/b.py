from util import timer

from seven.a import ColorGraph

if __name__ == "__main__":
    with timer():
        color_graph = ColorGraph("input")
        print(color_graph.num_bags_inside(color_graph.gold))
