"""Unit tests for the graphspace quotient space."""

import geomstats.backend as gs
from geomstats.geometry.graphspace import GraphSpace, GraphSpaceMetric
from tests.conftest import Parametrizer, TestCase
from tests.data.graphspace_data import GraphSpaceMetricTestData, GraphSpaceTestData


class TestGraphSpace(TestCase, metaclass=Parametrizer):
    space = GraphSpace

    testing_data = GraphSpaceTestData()

    def test_random_point_belongs(self, n, n_points):
        space = self.space(n)
        point = space.random_point(n_points)
        self.assertTrue(gs.all(space.belongs(point)))

    def test_belongs(self, n, mat, expected):
        space = self.space(n)
        self.assertAllClose(space.belongs(gs.array(mat)), gs.array(expected))

    def test_permute(self, n, graph, permutation, expected):
        space = self.space(n)
        result = space.permute(gs.array(graph), permutation)
        self.assertAllClose(result, expected)


class TestGraphSpaceMetric(TestCase, metaclass=Parametrizer):
    metric = GraphSpaceMetric

    testing_data = GraphSpaceMetricTestData()

    def test_matchers(self, n, set1, set2):
        metric = self.metric(n)
        d1 = metric.dist(set1, set2, matcher="FAQ")
        d2 = metric.dist(set1, set2, matcher="ID")
        result1 = d1[0] < d2[0]
        result2 = d1[1] == d2[1]
        self.assertAllClose(result1, True)
        self.assertAllClose(result2, True)
