import numpy as np

from screen import Screen
from camera import PerspectiveCamera,OrthoCamera
from mesh import Mesh
from renderer import Renderer
from light import PointLight



if __name__ == '__main__':
    screen = Screen(500,500)

    camera = PerspectiveCamera(-1.0, 1.0, -1.0, 1.0, -1.0, -10)
    camera.transform.set_position(0, 0, 2.5)


    mesh_sphere = Mesh.from_stl("unit_sphere.stl", np.array([1.0, 0.0, 1.0]), \
                                np.array([1.0, 1.0, 1.0]), 0.05, 1.0, 0.5, 1000)
    mesh_sphere.transform.set_rotation(15, 0, 20)


    light = PointLight(50.0, np.array([1, 1, 1]))
    light.transform.set_position(0, 5, 3)

    renderer = Renderer(screen, camera, [mesh_sphere], light)
    renderer.render("phong",[80,80,80], [0.2, 0.2, 0.2])

    screen.show()