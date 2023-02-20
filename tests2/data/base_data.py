import random

from geomstats.test.data import TestData


class _ProjectionMixinsTestData:
    def projection_vec_test_data(self):
        return self.generate_vec_data()

    def projection_belongs_test_data(self):
        return self.generate_random_data()


class _LieGroupMixinsTestData:
    def compose_vec_test_data(self):
        return self.generate_vec_data()

    def inverse_vec_test_data(self):
        return self.generate_vec_data()

    def compose_with_inverse_is_identity_test_data(self):
        return self.generate_random_data()

    def compose_with_identity_is_point_test_data(self):
        return self.generate_random_data()

    def exp_vec_test_data(self):
        return self.generate_vec_data()

    def log_vec_test_data(self):
        return self.generate_vec_data()

    def exp_after_log_test_data(self):
        return self.generate_random_data()

    def log_after_exp_test_data(self):
        return self.generate_random_data()

    def to_tangent_at_identity_belongs_to_lie_algebra_test_data(self):
        return self.generate_random_data()

    def tangent_translation_map_vec_test_data(self):
        data = []
        for inverse in [True, False]:
            for left in [True, False]:
                data.extend(
                    [
                        dict(n_reps=n_reps, left=left, inverse=inverse)
                        for n_reps in self.N_VEC_REPS
                    ]
                )
        return self.generate_tests(data)

    def lie_bracket_vec_test_data(self):
        return self.generate_vec_data()


class _ManifoldMixinsTestData:
    def belongs_vec_test_data(self):
        return self.generate_vec_data()

    def not_belongs_test_data(self):
        return self.generate_random_data()

    def random_point_belongs_test_data(self):
        return self.generate_random_data()

    def random_point_shape_test_data(self):
        return self.generate_shape_data()

    def is_tangent_vec_test_data(self):
        return self.generate_vec_data()

    def to_tangent_vec_test_data(self):
        return self.generate_vec_data()

    def to_tangent_is_tangent_test_data(self):
        return self.generate_random_data()

    def regularize_vec_test_data(self):
        return self.generate_vec_data()


class ManifoldTestData(_ManifoldMixinsTestData, TestData):
    pass


class ComplexManifoldTestData(_ManifoldMixinsTestData, TestData):
    def random_point_is_complex_test_data(self):
        return self.generate_random_data()

    def random_point_imaginary_nonzero_test_data(self):
        return self.generate_tests([dict(n_points=5)])


class _VectorSpaceMixinsTestData(_ProjectionMixinsTestData):
    def basis_cardinality_test_data(self):
        return None

    def basis_belongs_test_data(self):
        return self.generate_tests([dict()])

    def random_point_is_tangent_test_data(self):
        return self.generate_random_data()

    def to_tangent_is_projection_test_data(self):
        return self.generate_random_data()


class VectorSpaceTestData(_VectorSpaceMixinsTestData, ManifoldTestData):
    pass


class ComplexVectorSpaceTestData(_VectorSpaceMixinsTestData, ComplexManifoldTestData):
    pass


class MatrixVectorSpaceMixinsTestData(TestData):
    def to_vector_vec_test_data(self):
        return self.generate_vec_data()

    def to_vector_and_basis_test_data(self):
        return self.generate_random_data()

    def from_vector_vec_test_data(self):
        return self.generate_vec_data()

    def from_vector_belongs_test_data(self):
        return self.generate_random_data()

    def from_vector_after_to_vector_test_data(self):
        return self.generate_random_data()

    def to_vector_after_from_vector_test_data(self):
        return self.generate_random_data()


ComplexMatrixVectorSpaceMixinsTestData = MatrixVectorSpaceMixinsTestData


class MatrixLieAlgebraTestData(VectorSpaceTestData):
    def baker_campbell_hausdorff_vec_test_data(self):
        order = [2] + random.sample(range(3, 10), 1)
        data = []
        for order_ in order:
            data.extend(
                [dict(n_reps=n_reps, order=order_) for n_reps in self.N_VEC_REPS]
            )

        return self.generate_tests(data)

    def basis_representation_vec_test_data(self):
        return self.generate_vec_data()

    def basis_representation_and_basis_test_data(self):
        return self.generate_random_data()

    def matrix_representation_vec_test_data(self):
        return self.generate_vec_data()

    def matrix_representation_belongs_test_data(self):
        return self.generate_random_data()

    def matrix_representation_after_basis_representation_test_data(self):
        return self.generate_random_data()

    def basis_representation_after_matrix_representation_test_data(self):
        return self.generate_random_data()


class MatrixLieGroupTestData(_LieGroupMixinsTestData, ManifoldTestData):
    pass


class LieGroupTestData(_LieGroupMixinsTestData, ManifoldTestData):
    def jacobian_translation_vec_test_data(self):
        data = []
        for left in [True, False]:
            data.extend([dict(n_reps=n_reps, left=left) for n_reps in self.N_VEC_REPS])
        return self.generate_tests(data)

    def exp_from_identity_vec_test_data(self):
        return self.generate_vec_data()

    def log_from_identity_vec_test_data(self):
        return self.generate_vec_data()

    def exp_from_identity_after_log_from_identity_test_data(self):
        return self.generate_random_data()

    def log_from_identity_after_exp_from_identity_test_data(self):
        return self.generate_random_data()


class LevelSetTestData(_ProjectionMixinsTestData, ManifoldTestData):
    def submersion_vec_test_data(self):
        return self.generate_vec_data()

    def tangent_submersion_vec_test_data(self):
        return self.generate_vec_data()


class _OpenSetMixinsTestData(_ProjectionMixinsTestData):
    def to_tangent_is_tangent_in_embedding_space_test_data(self):
        return self.generate_random_data()


class OpenSetTestData(_OpenSetMixinsTestData, ManifoldTestData):
    pass


class ComplexOpenSetTestData(_OpenSetMixinsTestData, ComplexManifoldTestData):
    pass


class FiberBundleTestData(ManifoldTestData):
    def riemannian_submersion_vec_test_data(self):
        return self.generate_vec_data()

    def riemannian_submersion_belongs_to_base_test_data(self):
        return self.generate_random_data()

    def lift_vec_test_data(self):
        return self.generate_vec_data()

    def lift_belongs_to_total_space_test_data(self):
        return self.generate_random_data()

    def riemannian_submersion_after_lift_test_data(self):
        return self.generate_random_data()

    def tangent_riemannian_submersion_vec_test_data(self):
        return self.generate_vec_data()

    def tangent_riemannian_submersion_is_tangent_test_data(self):
        return self.generate_random_data()

    def align_vec_test_data(self):
        return self.generate_vec_data()

    def log_after_align_is_horizontal_test_data(self):
        return self.generate_random_data()

    def horizontal_projection_vec_test_data(self):
        return self.generate_vec_data()

    def horizontal_projection_is_horizontal_test_data(self):
        return self.generate_random_data()

    def vertical_projection_vec_test_data(self):
        return self.generate_vec_data()

    def vertical_projection_is_vertical_test_data(self):
        return self.generate_random_data()

    def tangent_riemannian_submersion_after_vertical_projection_test_data(self):
        return self.generate_random_data()

    def is_horizontal_vec_test_data(self):
        return self.generate_vec_data()

    def is_vertical_vec_test_data(self):
        return self.generate_vec_data()

    def horizontal_lift_vec_test_data(self):
        return self.generate_vec_data()

    def horizontal_lift_is_horizontal_test_data(self):
        return self.generate_random_data()

    def tangent_riemannian_submersion_after_horizontal_lift_test_data(self):
        return self.generate_random_data()

    def integrability_tensor_vec_test_data(self):
        return self.generate_vec_data()

    def integrability_tensor_derivative_vec_test_data(self):
        return self.generate_vec_data()
