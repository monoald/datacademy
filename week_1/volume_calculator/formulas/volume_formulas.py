from math import pi


def volume_circular_cylinder(radius, height):
    """Get the volume of a circular cylinder

    Args:
    radius (float): base radius of the cylinder
    height (float): height of the cylinder

    Returns:
    float: Volume of the cylinder
    """
    volume = pi * (radius**2) * height

    return volume


def volume_cone(radius, height):
    """Get the volume of a cone

    Args:
    radius (float): base radius of the cone
    height (float): height of the cone

    Returns:
    float: Volume of the cone
    """
    volume = (1/3) * pi * (radius**2) * height

    return volume


def volume_cube(prism):
    """Get the volume of a cube

    Args:
    prism (float): prism of the cube


    Returns:
    float: Volume of the cube
    """
    volume = prism**3

    return volume


def volume_sphere(radius):
    """Get the volume of a sphere

    Args:
    radius (float): radius of the sphere


    Returns:
    float: Volume of the sphere
    """
    volume = (4/3) * pi * (radius**3)

    return volume