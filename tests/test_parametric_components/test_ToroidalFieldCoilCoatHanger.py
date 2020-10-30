
import paramak
import pytest
import unittest


class test_ToroidalFieldCoilCoatHanger(unittest.TestCase):
    def test_ToroidalFieldCoilCoatHanger_creation(self):
        """Creates a tf coil using the ToroidalFieldCoilCoatHanger parametric
        component and checks that a cadquery solid is created."""

        test_shape = paramak.ToroidalFieldCoilCoatHanger(
            horizontal_start_point=(200, 500),
            horizontal_length=400,
            vertical_start_point=(700, 50),
            vertical_length=500,
            thickness=50,
            distance=50,
            number_of_coils=5,
        )

        assert test_shape.solid is not None
        assert test_shape.volume > 1000

    def test_ToroidalFieldCoilCoatHanger_rotation_angle(self):
        """Creates a tf coil with a rotation_angle < 360 degrees and checks
        that the correct cut is performed and the volume is correct."""

        test_shape = paramak.ToroidalFieldCoilCoatHanger(
            horizontal_start_point=(200, 500),
            horizontal_length=400,
            vertical_start_point=(700, 0),
            vertical_length=500,
            thickness=50,
            distance=50,
            number_of_coils=8,
        )

        test_shape.rotation_angle = 360
        test_shape.workplane = "XZ"
        test_volume = test_shape.volume
        test_shape.rotation_angle = 180
        assert test_shape.volume == pytest.approx(test_volume * 0.5, rel=0.01)

        test_shape.rotation_angle = 360
        test_shape.workplane = "YZ"
        test_volume = test_shape.volume
        test_shape.rotation_angle = 180
        assert test_shape.volume == pytest.approx(test_volume * 0.5, rel=0.01)

        # this test will remain commented until workplane issue #308 is resolved
        # currently causes terminal to crash due to large number of unions
        # test_shape.rotation_angle = 360
        # test_shape.workplane = "XY"
        # test_volume = test_shape.volume
        # test_shape.rotation_angle = 180
        # assert test_shape.volume == pytest.approx(test_volume * 0.5)
