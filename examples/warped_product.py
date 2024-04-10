"""Demonstrate use of WarpedProductRiemannianMetric."""

import geomstats.backend as gs
from geomstats.geometry.euclidean import Euclidean
from geomstats.geometry.hypersphere import Hypersphere
from geomstats.geometry.product_manifold import (
    ProductManifold,
    WarpedProductRiemannianMetric,
)

base = Euclidean(1)
fiber = Hypersphere(1)
product_manifold = ProductManifold([base, fiber])


def warping_function(args):
    """Calculate cos^2, the warping function on the sphere."""
    return gs.power(gs.cos(args), 2)


warped_product_metric = WarpedProductRiemannianMetric(
    product_manifold, warping_function
)
product_manifold.equip_with_metric(warped_product_metric)

point = product_manifold.random_point()
vec1 = product_manifold.random_tangent_vec(point)
vec2 = product_manifold.random_tangent_vec(point)

K = product_manifold.metric.sectional_curvature(vec1, vec2, point)
print(K)
