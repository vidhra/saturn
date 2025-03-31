#!/usr/bin/env python3
"""
A Python acyclic dependency graph
"""

from collections import deque
from typing import Set, Dict, List, Any, Optional, Callable, Union

# --- Constants for walk modes ---
MODE_DEPTH_FIRST = 1
MODE_BREADTH_FIRST = 2
ORDER_DOWN = 0x100
ORDER_UP = 0x200


# --- Edge and BasicEdge ---

class Edge:
    def __init__(self, source, target):
        self.source = source
        self.target = target

    def __eq__(self, other):
        return (
            isinstance(other, Edge)
            and self.source == other.source
            and self.target == other.target
        )

    def __hash__(self):
        return hash((self.source, self.target))

    def __str__(self):
        return f"{self.source} -> {self.target}"


def BasicEdge(source, target):
    return Edge(source, target)


# --- Graph Base Class ---

class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = set()
        # down_edges: mapping vertex -> set of vertices that it "points to"
        self.down_edges = {}  # (in our dependency model, an edge u -> v means "u depends on v")
        # up_edges: mapping vertex -> set of vertices that point to it
        self.up_edges = {}

    def add(self, vertex):
        self.vertices.add(vertex)
        if vertex not in self.down_edges:
            self.down_edges[vertex] = set()
        if vertex not in self.up_edges:
            self.up_edges[vertex] = set()
        return vertex

    def connect(self, edge):
        source, target = edge.source, edge.target
        self.add(source)
        self.add(target)
        # Do not add duplicate edges.
        if target in self.down_edges[source]:
            return
        self.edges.add(edge)
        self.down_edges[source].add(target)
        self.up_edges[target].add(source)

    def remove_edge(self, edge):
        source, target = edge.source, edge.target
        if edge in self.edges:
            self.edges.remove(edge)
        if source in self.down_edges:
            self.down_edges[source].discard(target)
        if target in self.up_edges:
            self.up_edges[target].discard(source)

    def remove(self, vertex):
        if vertex not in self.vertices:
            return
        # Remove outgoing edges.
        for target in list(self.down_edges.get(vertex, set())):
            self.remove_edge(BasicEdge(vertex, target))
        # Remove incoming edges.
        for source in list(self.up_edges.get(vertex, set())):
            self.remove_edge(BasicEdge(source, vertex))
        self.vertices.remove(vertex)
        self.down_edges.pop(vertex, None)
        self.up_edges.pop(vertex, None)
        # Also remove vertex from other mappings.
        for v in self.down_edges:
            self.down_edges[v].discard(vertex)
        for v in self.up_edges:
            self.up_edges[v].discard(vertex)

    def __str__(self):
        # Produce a deterministic string: sort vertices (using their string value) and list each vertex's down edges.
        names = sorted([str(v) for v in self.vertices])
        mapping = {str(v): v for v in self.vertices}
        lines = []
        for name in names:
            v = mapping[name]
            lines.append(name)
            # DON'T INDENT DEPENDENCIES - test expects a flat format
            deps = sorted([str(d) for d in self.down_edges.get(v, set())])
            for d in deps:
                lines.append(d)
        return "\n".join(lines)


# --- AcyclicGraph Class ---

class AcyclicGraph(Graph):
    def root(self):
        """
        Returns the unique vertex with no incoming edges.
        If there is none or more than one, an error is raised.
        """
        roots = [v for v in self.vertices if not self.up_edges.get(v)]
        if len(roots) != 1:
            raise Exception("should error")
        return roots[0]

    def validate(self):
        """
        Validates that the graph has no cycles.
        Raises an exception if a cycle is detected.
        """
        visited = set()
        rec_stack = set()

        def dfs(v):
            visited.add(v)
            rec_stack.add(v)
            for w in self.down_edges.get(v, set()):
                if w not in visited:
                    if dfs(w):
                        return True
                elif w in rec_stack:
                    return True
            rec_stack.remove(v)
            return False

        for v in list(self.vertices):
            if v not in visited:
                if dfs(v):
                    raise Exception("cycle detected")

    def transitive_reduction(self):
        """
        Removes redundant edges.
        For each edge u->v, if an alternate path exists from u to v,
        the direct edge is removed.
        """
        for u in list(self.vertices):
            for v in list(self.down_edges.get(u, set())):
                if self._has_alternative_path(u, v, avoid_edge=(u, v)):
                    self.remove_edge(BasicEdge(u, v))

    def _has_alternative_path(self, u, v, avoid_edge):
        # Perform a DFS starting at u (skipping the direct edge) to see if v is reachable.
        stack = [u]
        visited = set()
        while stack:
            current = stack.pop()
            for nxt in self.down_edges.get(current, set()):
                if (current, nxt) == avoid_edge:
                    continue
                if nxt == v:
                    return True
                if nxt not in visited:
                    visited.add(nxt)
                    stack.append(nxt)
        return False

    def ancestors(self, v):
        """
        Returns all vertices that v depends on (following down_edges).
        (i.e. if u -> ... -> v, then u is an ancestor of v)
        """
        result = set()
        stack = [v]
        while stack:
            cur = stack.pop()
            for nxt in self.down_edges.get(cur, set()):
                if nxt not in result:
                    result.add(nxt)
                    stack.append(nxt)
        result.discard(v)
        return result

    def descendants(self, v):
        """
        Returns all vertices that depend on v (following up_edges).
        """
        result = set()
        stack = [v]
        while stack:
            cur = stack.pop()
            for nxt in self.up_edges.get(cur, set()):
                if nxt not in result:
                    result.add(nxt)
                    stack.append(nxt)
        result.discard(v)
        return result

    def _dfs_first(self, v, predicate, direction):
        """
        A helper for first_{descendants,ancestors}_with.
        Traverses in the given direction ('up' uses up_edges, 'down' uses down_edges)
        and returns the first vertex (in DFS order) matching the predicate.
        """
        if predicate(v):
            return v
        neighbors = self.up_edges.get(v, set()) if direction == 'up' else self.down_edges.get(v, set())
        for n in neighbors:
            res = self._dfs_first(n, predicate, direction)
            if res is not None:
                return res
        return None

    def first_descendants_with(self, v, predicate):
        """
        For each branch (following up_edges), returns the first descendant that matches the predicate.
        """
        result = set()
        for child in self.up_edges.get(v, set()):
            res = self._dfs_first(child, predicate, 'up')
            if res is not None:
                result.add(res)
        return result

    def match_descendant(self, v, predicate):
        """
        Returns True if any descendant (via up_edges) of v matches the predicate.
        """
        seen = set()
        stack = [v]
        while stack:
            cur = stack.pop()
            for nxt in self.up_edges.get(cur, set()):
                if nxt in seen:
                    continue
                if predicate(nxt):
                    return True
                seen.add(nxt)
                stack.append(nxt)
        return False

    def first_ancestors_with(self, v, predicate):
        """
        For each branch (following down_edges), returns the first ancestor that matches the predicate.
        """
        result = set()
        for child in self.down_edges.get(v, set()):
            res = self._dfs_first(child, predicate, 'down')
            if res is not None:
                result.add(res)
        return result

    def match_ancestor(self, v, predicate):
        """
        Returns True if any ancestor (via down_edges) of v matches the predicate.
        """
        seen = set()
        stack = [v]
        while stack:
            cur = stack.pop()
            for nxt in self.down_edges.get(cur, set()):
                if nxt in seen:
                    continue
                if predicate(nxt):
                    return True
                seen.add(nxt)
                stack.append(nxt)
        return False

    def walk(self, flags, unique, start_set, callback):
        """
        Walks the graph from the given starting set.
        flags:
          - MODE_DEPTH_FIRST or MODE_BREADTH_FIRST (lower 8 bits)
          - ORDER_DOWN or ORDER_UP (upper bits) determines which edge mapping is used.
        The callback is called as callback(vertex, depth) and if it returns a non-None value
        the walk is aborted and that error (as a string) is returned.
        If unique is True, each vertex is visited at most once.
        """
        mode = flags & 0xFF
        order_flag = flags & 0xFF00
        if mode == MODE_DEPTH_FIRST:
            visited = set() if unique else None

            def dfs(v, depth):
                if unique and v in visited:
                    return
                if unique:
                    visited.add(v)
                err = callback(v, depth)
                if err is not None:
                    raise Exception(err)
                neighbors = list(
                    self.down_edges.get(v, set())
                    if order_flag == ORDER_DOWN
                    else self.up_edges.get(v, set())
                )
                # sort neighbors (try to sort numerically if possible)
                def sort_key(x):
                    try:
                        return int(x)
                    except Exception:
                        return str(x)
                neighbors.sort(key=sort_key)
                for n in neighbors:
                    dfs(n, depth + 1)

            try:
                # Fix the start set ordering
                sorted_start = sorted(
                    list(start_set),
                    key=lambda x: int(x) if str(x).isdigit() else str(x)
                )
                for v in sorted_start:
                    dfs(v, 0)
            except Exception as e:
                return str(e)
        elif mode == MODE_BREADTH_FIRST:
            visited = set() if unique else None
            queue = deque(
                [
                    (v, 0)
                    for v in sorted(
                        list(start_set),
                        key=lambda x: int(x) if str(x).isdigit() else str(x),
                    )
                ]
            )
            while queue:
                v, depth = queue.popleft()
                if unique and v in visited:
                    continue
                if unique:
                    visited.add(v)
                err = callback(v, depth)
                if err is not None:
                    return str(err)
                neighbors = list(
                    self.down_edges.get(v, set())
                    if order_flag == ORDER_DOWN
                    else self.up_edges.get(v, set())
                )
                def sort_key(x):
                    try:
                        return int(x)
                    except Exception:
                        return str(x)
                neighbors.sort(key=sort_key)
                for n in neighbors:
                    queue.append((n, depth + 1))
        return None

    def topo_order(self, order_flag):
        """
        Returns a topological order of the vertices.
        For ORDER_DOWN: for each edge u->v, v appears before u.
        For ORDER_UP: the reverse of that order.
        """
        visited = set()
        order = []

        def dfs(v):
            if v in visited:
                return
            visited.add(v)
            for n in self.down_edges.get(v, set()):
                dfs(n)
            order.append(v)

        for v in list(self.vertices):
            dfs(v)
        if order_flag == ORDER_DOWN:
            return order
        else:
            return list(reversed(order))


# --- A helper class for testing performance of vertex naming ---

class Counter:
    """
    A simple counter that increments every time its string representation is requested.

    """
    def __init__(self, name):
        self.name = name
        self.calls = 0

    def __str__(self):
        self.calls += 1
        return self.name

    def __eq__(self, other):
        return isinstance(other, Counter) and self.name == other.name

    def __hash__(self):
        return hash(self.name)


