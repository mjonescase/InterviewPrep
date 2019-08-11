import sys

from ..Node import Node
from .Color import Color


class NilNode(Node):
    color: Color

    def __init__(self):
        self.key = sys.maxsize
        self.color = Color.BLACK
        self.parent = self
        self.right = self
        self.left = self


NIL_NODE = NilNode()
