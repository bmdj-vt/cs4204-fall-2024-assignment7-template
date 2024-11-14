import numpy as np

from mesh import Mesh
from transform import Transform
from camera import PerspectiveCamera

def test_inverse_point():
    camera = PerspectiveCamera(-1.5, 1.5, -1.5, 1.5, -1, -50)
    camera.transform.set_position(0,0,3)

    #Test just camera translation
    assert np.allclose(camera.inverse_project_point(np.array([0.5,0.5,-0.5])),np.array([2.83018868,2.83018868,-0.77358491]))


if __name__ == '__main__':
    test_inverse_point()




