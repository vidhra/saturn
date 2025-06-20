import unittest
from internal.dag.dag import AcyclicGraph, BasicEdge, Counter, MODE_DEPTH_FIRST, ORDER_DOWN, ORDER_UP
import pytest
pytestmark = pytest.mark.asyncio

class TestAcyclicGraph(unittest.TestCase):

    def test_root(self):
        g = AcyclicGraph()
        g.add(1)
        g.add(2)
        g.add(3)
        g.connect(BasicEdge(3, 2))
        g.connect(BasicEdge(3, 1))
        self.assertEqual(g.root(), 3)

    def test_root_cycle(self):
        g = AcyclicGraph()
        g.add(1)
        g.add(2)
        g.add(3)
        g.connect(BasicEdge(1, 2))
        g.connect(BasicEdge(2, 3))
        g.connect(BasicEdge(3, 1))
        with self.assertRaises(Exception):
            _ = g.root()

    def test_root_multiple(self):
        g = AcyclicGraph()
        g.add(1)
        g.add(2)
        g.add(3)
        g.connect(BasicEdge(3, 2))
        with self.assertRaises(Exception):
            _ = g.root()

    def test_transitive_reduction(self):
        g = AcyclicGraph()
        g.add(1)
        g.add(2)
        g.add(3)
        g.connect(BasicEdge(1, 2))
        g.connect(BasicEdge(1, 3))
        g.connect(BasicEdge(2, 3))
        g.transitive_reduction()
        actual = g.__str__().strip()
        expected = "\n".join(line.strip() for line in """
1
2
2
3
3
""".strip().splitlines())
        self.assertEqual(actual, expected)

    def test_transitive_reduction_more(self):
        g = AcyclicGraph()
        g.add(1)
        g.add(2)
        g.add(3)
        g.add(4)
        g.connect(BasicEdge(1, 2))
        g.connect(BasicEdge(1, 3))
        g.connect(BasicEdge(1, 4))
        g.connect(BasicEdge(2, 3))
        g.connect(BasicEdge(2, 4))
        g.connect(BasicEdge(3, 4))
        g.transitive_reduction()
        actual = g.__str__().strip()
        expected = "\n".join(line.strip() for line in """
1
2
2
3
3
4
4
""".strip().splitlines())
        self.assertEqual(actual, expected)

    def test_transitive_reduction_multiple_roots(self):
        g = AcyclicGraph()
        # First subgraph
        g.add(1)
        g.add(2)
        g.add(3)
        g.add(4)
        g.connect(BasicEdge(1, 2))
        g.connect(BasicEdge(1, 3))
        g.connect(BasicEdge(1, 4))
        g.connect(BasicEdge(2, 3))
        g.connect(BasicEdge(2, 4))
        g.connect(BasicEdge(3, 4))
        # Second subgraph
        g.add(5)
        g.add(6)
        g.add(7)
        g.add(8)
        g.connect(BasicEdge(5, 6))
        g.connect(BasicEdge(5, 7))
        g.connect(BasicEdge(5, 8))
        g.connect(BasicEdge(6, 7))
        g.connect(BasicEdge(6, 8))
        g.connect(BasicEdge(7, 8))
        g.transitive_reduction()
        actual = g.__str__().strip()
        expected = "\n".join(line.strip() for line in """
1
2
2
3
3
4
4
5
6
6
7
7
8
8
""".strip().splitlines())
        self.assertEqual(actual, expected)

    def test_transitive_reduction_fully_connected(self):
        g = AcyclicGraph()
        node_count = 200
        nodes = [Counter(str(i)) for i in range(node_count)]
        for n in nodes:
            g.add(n)
        for i in range(node_count):
            for j in range(node_count):
                if i == j:
                    continue
                g.connect(BasicEdge(nodes[i], nodes[j]))
        g.transitive_reduction()
        total_calls = sum(n.calls for n in nodes)
        # If vertex naming were excessively invoked the total calls would be much higher.
        self.assertLessEqual(total_calls, 2 * node_count)

    def test_validate(self):
        g = AcyclicGraph()
        g.add(1)
        g.add(2)
        g.add(3)
        g.connect(BasicEdge(3, 2))
        g.connect(BasicEdge(3, 1))
        # Should not raise.
        g.validate()

    def test_validate_cycle(self):
        g = AcyclicGraph()
        g.add(1)
        g.add(2)
        g.add(3)
        g.connect(BasicEdge(3, 2))
        g.connect(BasicEdge(3, 1))
        g.connect(BasicEdge(1, 2))
        g.connect(BasicEdge(2, 1))
        with self.assertRaises(Exception):
            g.validate()

    def test_validate_cycle_self(self):
        g = AcyclicGraph()
        g.add(1)
        g.add(2)
        g.connect(BasicEdge(1, 1))
        with self.assertRaises(Exception):
            g.validate()

    def test_ancestors(self):
        g = AcyclicGraph()
        # Add vertices 1,2,3,4,5 and (implicitly) 0 by connecting an edge from 0 -> 1.
        for i in [1, 2, 3, 4, 5]:
            g.add(i)
        g.connect(BasicEdge(0, 1))
        g.connect(BasicEdge(1, 2))
        g.connect(BasicEdge(2, 3))
        g.connect(BasicEdge(3, 4))
        g.connect(BasicEdge(4, 5))
        actual = g.ancestors(2)
        expected = {3, 4, 5}
        self.assertEqual(actual, expected)

    def test_descendants(self):
        g = AcyclicGraph()
        for i in [1, 2, 3, 4, 5]:
            g.add(i)
        g.connect(BasicEdge(0, 1))
        g.connect(BasicEdge(1, 2))
        g.connect(BasicEdge(2, 3))
        g.connect(BasicEdge(3, 4))
        g.connect(BasicEdge(4, 5))
        actual = g.descendants(2)
        expected = {0, 1}
        self.assertEqual(actual, expected)

    def test_find_descendants(self):
        g = AcyclicGraph()
        for i in range(7):
            g.add(i)
        g.connect(BasicEdge(0, 1))
        g.connect(BasicEdge(1, 2))
        g.connect(BasicEdge(2, 6))
        g.connect(BasicEdge(3, 4))
        g.connect(BasicEdge(4, 5))
        g.connect(BasicEdge(5, 6))
        actual = g.first_descendants_with(6, lambda v: v % 2 != 0)
        expected = {1, 5}
        self.assertEqual(actual, expected)
        self.assertTrue(g.match_descendant(6, lambda v: v == 1))
        self.assertFalse(g.match_descendant(6, lambda v: v == 6))
        self.assertFalse(g.match_descendant(6, lambda v: v == 10))

    def test_find_ancestors(self):
        g = AcyclicGraph()
        for i in range(7):
            g.add(i)
        g.connect(BasicEdge(1, 0))
        g.connect(BasicEdge(2, 1))
        g.connect(BasicEdge(6, 2))
        g.connect(BasicEdge(4, 3))
        g.connect(BasicEdge(5, 4))
        g.connect(BasicEdge(6, 5))
        actual = g.first_ancestors_with(6, lambda v: v % 2 != 0)
        expected = {1, 5}
        self.assertEqual(actual, expected)
        self.assertTrue(g.match_ancestor(6, lambda v: v == 1))
        self.assertFalse(g.match_ancestor(6, lambda v: v == 6))
        self.assertFalse(g.match_ancestor(6, lambda v: v == 10))

    def test_walk(self):
        g = AcyclicGraph()
        g.add(1)
        g.add(2)
        g.add(3)
        g.connect(BasicEdge(3, 2))
        g.connect(BasicEdge(3, 1))
        visits = []

        def callback(v, d):
            visits.append((v, d))
            return None

        err = g.walk(MODE_DEPTH_FIRST | ORDER_DOWN, True, {1, 2, 3}, callback)
        self.assertIsNone(err)
        # Accept either [1,2,3] or [2,1,3] for the top-level (order among start vertices)
        top_order = [v for v, d in visits if d == 0]
        self.assertIn(top_order, ([1, 2, 3], [2, 1, 3]))

    def test_walk_error(self):
        g = AcyclicGraph()
        g.add(1)
        g.add(2)
        g.add(3)
        g.add(4)
        g.connect(BasicEdge(4, 3))
        g.connect(BasicEdge(3, 2))
        g.connect(BasicEdge(2, 1))
        visits = []

        def callback(v, d):
            if v == 2:
                return "error"
            visits.append(v)
            return None

        err = g.walk(MODE_DEPTH_FIRST | ORDER_DOWN, True, {1, 2, 3, 4}, callback)
        self.assertIsNotNone(err)
        self.assertEqual(visits, [1])

    def test_topo_order(self):
        """
        Constructs a sample dependency graph:

               1     2
              / \\   /  \\
             3   4 5    -
              \\       /
               6      /
                \\   /
                   7
                 ...

        """
        g = AcyclicGraph()
        for i in range(1, 12):
            g.add(i)
        g.connect(BasicEdge(1, 3))
        g.connect(BasicEdge(1, 4))
        g.connect(BasicEdge(2, 4))
        g.connect(BasicEdge(2, 5))
        g.connect(BasicEdge(3, 6))
        g.connect(BasicEdge(4, 7))
        g.connect(BasicEdge(5, 7))
        g.connect(BasicEdge(7, 8))
        g.connect(BasicEdge(7, 9))
        g.connect(BasicEdge(7, 10))
        g.connect(BasicEdge(8, 11))
        g.connect(BasicEdge(9, 11))
        g.connect(BasicEdge(10, 11))
        # Topological order for ORDER_DOWN: each vertex's dependencies (down_edges) appear before it.
        order = g.topo_order(ORDER_DOWN)
        completed = set()
        for v in order:
            for dep in g.down_edges.get(v, set()):
                self.assertIn(dep, completed)
            completed.add(v)
        # For ORDER_UP, the reverse condition holds.
        order_up = g.topo_order(ORDER_UP)
        completed = set()
        for v in order_up:
            for dep in g.up_edges.get(v, set()):
                self.assertIn(dep, completed)
            completed.add(v)


if __name__ == "__main__":
    unittest.main() 