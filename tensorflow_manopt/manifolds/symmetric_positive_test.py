import tensorflow as tf

from absl.testing import parameterized
from tensorflow.python.keras import combinations

from tensorflow_manopt.manifolds.test_invariants import TestInvariants
from tensorflow_manopt.manifolds.symmetric_positive import SPDAffineInvariant
from tensorflow_manopt.manifolds.symmetric_positive import SPDLogEuclidean
from tensorflow_manopt.manifolds.symmetric_positive import SPDLogCholesky


@combinations.generate(
    combinations.combine(
        mode=["graph", "eager"],
        manifold=[SPDAffineInvariant(), SPDLogCholesky()],
        shape=[(2, 3, 3), (3, 3)],
        dtype=[tf.float64],
    )
)
class SymmetricPositiveTest(tf.test.TestCase, parameterized.TestCase):
    test_random = TestInvariants.check_random

    test_dist = TestInvariants.check_dist

    test_inner = TestInvariants.check_inner

    test_proj = TestInvariants.check_proj

    test_exp_log_inverse = TestInvariants.check_exp_log_inverse

    test_transp_retr = TestInvariants.check_transp_retr

    test_ptransp_inverse = TestInvariants.check_ptransp_inverse

    test_ptransp_inner = TestInvariants.check_ptransp_inner

    test_geodesic = TestInvariants.check_geodesic

    test_pairmean = TestInvariants.check_pairmean


@combinations.generate(
    combinations.combine(
        mode=["graph", "eager"],
        manifold=[SPDLogEuclidean()],
        shape=[(2, 3, 3), (3, 3)],
        dtype=[tf.float32, tf.float64],
    )
)
class SymmetricPositiveLETest(tf.test.TestCase, parameterized.TestCase):
    test_random = TestInvariants.check_random

    test_dist = TestInvariants.check_dist

    test_inner = TestInvariants.check_inner

    test_proj = TestInvariants.check_proj

    test_exp_log_inverse = TestInvariants.check_exp_log_inverse

    test_geodesic = TestInvariants.check_geodesic

    test_pairmean = TestInvariants.check_pairmean
