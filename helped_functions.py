import NemAll_Python_Geometry as geometry
from lab3_beam import Lab2_Beam as lb


def tp_1(build_ele):
    d = lb.get(build_ele)
    polil = geometry.Polygon3D()
    polil += geometry.Point3D(d[0], d[1] - d[2] -
                              (d[1] - d[2] * 2 - d[3]) / 2, d[4] + d[5])
    polil += geometry.Point3D(d[0], d[6] -
                              (d[6] - d[1]) / 2, d[4] + d[5] + d[7])
    polil += geometry.Point3D(d[0], -(d[6] - d[1]) / 2, d[4] + d[5] + d[7])
    polil += geometry.Point3D(d[0], d[2] +
                              (d[1] - d[2] * 2 - d[3]) / 2, d[4] + d[5])
    polil += geometry.Point3D(d[0], d[1] - d[2] -
                              (d[1] - d[2] * 2 - d[3]) / 2, d[4] + d[5])
    direction = geometry.Polyline3D()
    direction += geometry.Point3D(d[0], d[1] - d[2] -
                                  (d[1] - d[2] * 2 - d[3]) / 2, d[4] + d[5])
    direction += geometry.Point3D(d[8] - d[0], d[1] -
                                  d[2] - (d[1] - d[2] * 2 - d[3]) / 2, d[4] + d[5])

    error, figure = geometry.CreatePolyhedron(polil, direction)

    return figure


def tp_2(build_ele):
    d = lb.get(build_ele)
    polil = geometry.Polygon3D()
    polil += geometry.Point3D(d[8] - d[0], d[1] - d[2], d[4] + d[5])
    polil += geometry.Point3D(d[8] - d[0] - d[9], d[1] -
                              d[2] - (d[1] - d[2] * 2 - d[3]) / 2, d[4] + d[5])
    polil += geometry.Point3D(d[8] - d[0] - d[9] - (d[1] - d[2] * 2 - d[3]) / 2, d[1] - (
        d[1] - d[2] * 2 - d[3]) / 2 + (d[6] - d[1]) / 2, d[4] + d[5] + d[7])
    polil += geometry.Point3D(d[8] - d[0] - (d[1] - d[2] * 2 - d[3]) / 2,
                              d[1] + (d[6] - d[1]) / 2, d[4] + d[5] + d[7])
    polil += geometry.Point3D(d[8] - d[0], d[1] - d[2], d[4] + d[5])

    direction = geometry.Polyline3D()
    direction += geometry.Point3D(d[8] - d[0], d[1] - d[2], d[4] + d[5])
    direction += geometry.Point3D(d[8] - d[0] +
                                  10, d[1] - d[2] - 10, d[4] + d[5] + 10)

    error, figure = geometry.CreatePolyhedron(polil, direction)
    return figure


def tp_3(build_ele, sign=0):
    d = lb.get(build_ele)
    polil = geometry.Polygon3D()
    polil += geometry.Point3D(sign, d[2], d[4] + d[5])
    polil += geometry.Point3D(sign, d[1] - d[2], d[4] + d[5])
    polil += geometry.Point3D(sign, d[1] +
                              (d[6] - d[1]) / 2, d[4] + d[5] + d[7])
    polil += geometry.Point3D(sign, -(d[6] - d[1]) / 2, d[4] + d[5] + d[7])
    polil += geometry.Point3D(sign, d[2], d[4] + d[5])

    direction = geometry.Polyline3D()
    direction += geometry.Point3D(sign, d[2], d[4] + d[5])
    direction += geometry.Point3D(sign + d[0], d[2], d[4] + d[5])

    error, figure = geometry.CreatePolyhedron(polil, direction)
    return figure


def tp_4(build_ele, minus_1=0, minus_2=0, digit=-10):
    d = lb.get(build_ele)
    polil = geometry.Polygon3D()
    polil += geometry.Point3D(d[8] - d[0], d[1] - d[2] - minus_1, d[4] + d[5])
    polil += geometry.Point3D(d[8] - d[0], d[6] -
                              (d[6] - d[1]) / 2 - minus_2, d[4] + d[5] + d[7])
    polil += geometry.Point3D(d[8] - d[0] - (d[1] - d[2] * 2 - d[3]) / 2,
                              d[1] + (d[6] - d[1]) / 2 - minus_2, d[4] + d[5] + d[7])
    polil += geometry.Point3D(d[8] - d[0], d[1] - d[2] - minus_1, d[4] + d[5])

    direction = geometry.Polyline3D()
    direction += geometry.Point3D(d[8] - d[0],
                                  d[1] - d[2] - minus_1, d[4] + d[5])
    direction += geometry.Point3D(d[8] - d[0],
                                  d[1] - d[2] + digit - minus_1, d[4] + d[5])
    error, figure = geometry.CreatePolyhedron(polil, direction)
    return figure


def tp_2_2(build_ele):
    d = lb.get(build_ele)
    polil = geometry.Polygon3D()
    polil += geometry.Point3D(d[8] - d[0], d[2], d[4] + d[5])
    polil += geometry.Point3D(d[8] - d[0] - d[9],
                              d[2] + (d[1] - d[2] * 2 - d[3]) / 2, d[4] + d[5])
    polil += geometry.Point3D(d[8] - d[0] - d[9] - (d[1] - d[2] * 2 - d[3]) / 2,
                              (d[1] - d[2] * 2 - d[3]) / 2 - (d[6] - d[1]) / 2, d[4] + d[5] + d[7])
    polil += geometry.Point3D(d[8] - d[0] - (d[1] - d[2] *
                              2 - d[3]) / 2, -(d[6] - d[1]) / 2, d[4] + d[5] + d[7])
    polil += geometry.Point3D(d[8] - d[0],  d[2], d[4] + d[5])

    direction = geometry.Polyline3D()
    direction += geometry.Point3D(d[8] - d[0], d[2], d[4] + d[5])
    direction += geometry.Point3D(d[8] - d[0] +
                                  10, d[2] + 10, d[4] + d[5] + 10)

    error, figure = geometry.CreatePolyhedron(polil, direction)
    return figure


def tp_2_3(build_ele):
    d = lb.get(build_ele)
    polil = geometry.Polygon3D()
    polil += geometry.Point3D(d[0], d[1] - d[2], d[4] + d[5])
    polil += geometry.Point3D(d[0] + d[9], d[1] -
                              d[2] - (d[1] - d[2] * 2 - d[3]) / 2, d[4] + d[5])
    polil += geometry.Point3D(d[0] + d[9] + (d[1] - d[2] * 2 - d[3]) / 2, d[1] - (
        d[1] - d[2] * 2 - d[3]) / 2 + (d[6] - d[1]) / 2, d[4] + d[5] + d[7])
    polil += geometry.Point3D(d[0] + (d[1] - d[2] * 2 - d[3]) / 2,
                              d[1] + (d[6] - d[1]) / 2, d[4] + d[5] + d[7])
    polil += geometry.Point3D(d[0], d[1] - d[2], d[4] + d[5])

    direction = geometry.Polyline3D()
    direction += geometry.Point3D(d[0], d[1] - d[2], d[4] + d[5])
    direction += geometry.Point3D(d[0] - 10,
                                  d[1] - d[2] - 10, d[4] + d[5] - 10)
    error, figure = geometry.CreatePolyhedron(polil, direction)

    return figure


def tp_4_2(build_ele, minus_1=0, minus_2=0, digit=-10):
    d = lb.get(build_ele)
    polil = geometry.Polygon3D()
    polil += geometry.Point3D(d[0], d[1] - d[2] - minus_1, d[4] + d[5])
    polil += geometry.Point3D(d[0], d[1] + (d[6] - d[1]) /
                              2 - minus_2, d[4] + d[5] + d[7])
    polil += geometry.Point3D(d[0] + (d[1] - d[2] * 2 - d[3]) / 2,
                              d[1] + (d[6] - d[1]) / 2 - minus_2, d[4] + d[5] + d[7])
    polil += geometry.Point3D(d[0], d[1] - d[2] - minus_1, d[4] + d[5])

    direction = geometry.Polyline3D()
    direction += geometry.Point3D(d[0], d[1] - d[2] - minus_1, d[4] + d[5])
    direction += geometry.Point3D(d[0], d[1] -
                                  d[2] - minus_1 + digit, d[4] + d[5])

    error, figure = geometry.CreatePolyhedron(polil, direction)

    return figure


def tp_3_3(build_ele):
    d = lb.get(build_ele)
    polil = geometry.Polygon3D()
    polil += geometry.Point3D(d[0], d[2], d[4] + d[5])
    polil += geometry.Point3D(d[0] + d[9], d[2] +
                              (d[1] - d[2] * 2 - d[3]) / 2, d[4] + d[5])
    polil += geometry.Point3D(d[0] + d[9] + (d[1] - d[2] * 2 - d[3]) / 2,
                              (d[1] - d[2] * 2 - d[3]) / 2 - (d[6] - d[1]) / 2, d[4] + d[5] + d[7])
    polil += geometry.Point3D(d[0] + (d[1] - d[2] * 2 - d[3]) /
                              2, -(d[6] - d[1]) / 2, d[4] + d[5] + d[7])
    polil += geometry.Point3D(d[0], d[2], d[4] + d[5])

    direction = geometry.Polyline3D()
    direction += geometry.Point3D(d[0], d[2], d[4] + d[5])
    direction += geometry.Point3D(d[0] - 10, d[2] + 10, d[4] + d[5] - 10)

    error, figure = geometry.CreatePolyhedron(polil, direction)

    return figure


def tp_last(build_ele):
    d = lb.get(build_ele)
    polil = geometry.Polygon3D()
    polil += geometry.Point3D(0, -(d[6] - d[1]) / 2, d[4] + d[5] + d[7])
    polil += geometry.Point3D(0, d[6] - (d[6] - d[1]) / 2, d[4] + d[5] + d[7])
    polil += geometry.Point3D(0, d[6] - (d[6] - d[1]) / 2, d[4] + d[5] + d[7])
    polil += geometry.Point3D(0, d[6] - (d[6] - d[1]) /
                              2 - d[10], d[4] + d[5] + d[7])
    polil += geometry.Point3D(0, d[6] - (d[6] - d[1]) /
                              2 - d[10], d[4] + d[5] + d[7] + build_ele.hp.value)
    polil += geometry.Point3D(0, - (d[6] - d[1]) / 2 +
                              d[10], d[4] + d[5] + d[7] + build_ele.hp.value)
    polil += geometry.Point3D(0, - (d[6] - d[1]) /
                              2 + d[10], [4] + d[5] + d[7])
    polil += geometry.Point3D(0, - (d[6] - d[1]) / 2, d[4] + d[5] + d[7])
    polil += geometry.Point3D(0, -(d[6] - d[1]) / 2,  d[4] + d[5] + d[7])

    direction = geometry.Polyline3D()
    direction += geometry.Point3D(0, -(d[6] - d[1]) / 2, d[4] + d[5] + d[7])
    direction += geometry.Point3D(d[8], -(d[6] - d[1]) / 2, d[4] + d[5] + d[7])
    error, figure = geometry.CreatePolyhedron(polil, direction)

    return figure


def bp_1(build_ele):
    d = lb.get(build_ele)
    polil = geometry.Polygon3D()
    polil += geometry.Point3D(d[0], d[1], d[4] - d[10])
    polil += geometry.Point3D(d[0], d[1] - d[2] -
                              (d[1] - d[2] * 2 - d[3]) / 2, d[4])
    polil += geometry.Point3D(d[0], d[1] - d[2] -
                              (d[1] - d[2] * 2 - d[3]) / 2 - d[3], d[4])
    polil += geometry.Point3D(d[0], 0, d[4] - d[10])
    polil += geometry.Point3D(d[0], d[1], d[4] - d[10])

    direction = geometry.Polyline3D()
    direction += geometry.Point3D(d[0], d[1], d[4] - d[10])
    direction += geometry.Point3D(d[8] - d[0], d[1], d[4] - d[10])
    error, figure = geometry.CreatePolyhedron(polil, direction)

    return figure


def bp_2(build_ele):
    d = lb.get(build_ele)
    polil = geometry.Polygon3D()
    polil += geometry.Point3D(d[0], d[1] - d[2], d[4])
    polil += geometry.Point3D(d[0] + d[9], d[1] -
                              d[2] - (d[1] - d[2] * 2 - d[3]) / 2, d[4])
    polil += geometry.Point3D(d[0] + d[9] + (d[1] - d[2] * 2 - d[3]) / 2,
                              d[1] - (d[1] - d[2] * 2 - d[3]) / 2, d[4] - d[10])
    polil += geometry.Point3D(d[0] + (d[1] - d[2]
                              * 2 - d[3]) / 2, d[1], d[4] - d[10])
    polil += geometry.Point3D(d[0], d[1] - d[2], d[4])

    direction = geometry.Polyline3D()
    direction += geometry.Point3D(d[0], d[1] - d[2], d[4])
    direction += geometry.Point3D(d[0] - 10, d[1] - d[2] - 10, d[4] - 10)

    error, figure = geometry.CreatePolyhedron(polil, direction)
    return figure


def bp_3(build_ele):
    d = lb.get(build_ele)
    polil = geometry.Polygon3D()
    polil += geometry.Point3D(0, d[1], d[4] - d[10])
    polil += geometry.Point3D(0, d[1] - d[2], d[4])
    polil += geometry.Point3D(0, d[2], d[4])
    polil += geometry.Point3D(0, 0, d[4] - d[10])
    polil += geometry.Point3D(0, d[1], d[4] - d[10])

    direction = geometry.Polyline3D()
    direction += geometry.Point3D(0, d[1], d[4] - d[10])
    direction += geometry.Point3D(d[0], d[1], d[4] - d[10])

    error, figure = geometry.CreatePolyhedron(polil, direction)

    return figure


def bp_4(build_ele):
    d = lb.get(build_ele)
    polil = geometry.Polygon3D()
    polil += geometry.Point3D(d[0], d[1] - d[2], d[4])
    polil += geometry.Point3D(d[0], d[1], d[4] - d[10])
    polil += geometry.Point3D(d[0] + (d[1] - d[2]
                              * 2 - d[3]) / 2, d[1], d[4] - d[10])
    polil += geometry.Point3D(d[0], d[1] - d[2], d[4])

    direction = geometry.Polyline3D()
    direction += geometry.Point3D(d[0], d[1] - d[2], d[4])
    direction += geometry.Point3D(d[0], d[1] - d[2] - 10, d[4])

    error, figure = geometry.CreatePolyhedron(polil, direction)
    return figure


def bp_2_2(build_ele):
    d = lb.get(build_ele)
    polil = geometry.Polygon3D()
    polil += geometry.Point3D(d[0], d[2], d[4])
    polil += geometry.Point3D(d[0] + d[9], d[2] +
                              (d[1] - d[2] * 2 - d[3]) / 2, d[4])
    polil += geometry.Point3D(d[0] + d[9] + (d[1] - d[2] * 2 - d[3]) / 2,
                              (d[1] - d[2] * 2 - d[3]) / 2, d[4] - d[10])
    polil += geometry.Point3D(d[0] + (d[1] - d[2]
                              * 2 - d[3]) / 2, 0, d[4] - d[10])
    polil += geometry.Point3D(d[0], d[2], d[4])

    direction = geometry.Polyline3D()
    direction += geometry.Point3D(d[0], d[2], d[4])
    direction += geometry.Point3D(d[0] - 10, d[2] + 10, d[4] - 10)

    error, figure = geometry.CreatePolyhedron(polil, direction)

    return figure


def bp_3_2(build_ele):
    d = lb.get(build_ele)
    polil = geometry.Polygon3D()
    polil += geometry.Point3D(d[8] - d[0], d[1], d[4] - d[10])
    polil += geometry.Point3D(d[8] - d[0], d[1] - d[2], d[4])
    polil += geometry.Point3D(d[8] - d[0], d[2], d[4])
    polil += geometry.Point3D(d[8] - d[0], 0, d[4] - d[10])
    polil += geometry.Point3D(d[8] - d[0], d[1], d[4] - d[10])

    direction = geometry.Polyline3D()
    direction += geometry.Point3D(d[8] - d[0], d[1], d[4] - d[10])
    direction += geometry.Point3D(d[8], d[1], d[4] - d[10])

    error, figure = geometry.CreatePolyhedron(polil, direction)
    return figure


def bp_4_2(build_ele):
    d = lb.get(build_ele)
    polil = geometry.Polygon3D()
    polil += geometry.Point3D(d[0], d[2], d[4])
    polil += geometry.Point3D(d[0], 0, d[4] - d[10])
    polil += geometry.Point3D(d[0] + (d[1] - d[2]
                              * 2 - d[3]) / 2, 0, d[4] - d[10])
    polil += geometry.Point3D(d[0], d[2], d[4])

    direction = geometry.Polyline3D()
    direction += geometry.Point3D(d[0], d[2], d[4])
    direction += geometry.Point3D(d[0], d[2] + 10, d[4])

    error, figure = geometry.CreatePolyhedron(polil, direction)
    return figure


def bp_2_3(build_ele):
    d = lb.get(build_ele)
    polil = geometry.Polygon3D()
    polil += geometry.Point3D(d[8] - d[0], d[1] - d[2], d[4])
    polil += geometry.Point3D(d[8] - d[0] - d[9],
                              d[1] - d[2] - (d[1] - d[2] * 2 - d[3]) / 2, d[4])
    polil += geometry.Point3D(d[8] - d[0] - d[9] - (d[1] - d[2] * 2 - d[3]) / 2,
                              d[1] - (d[1] - d[2] * 2 - d[3]) / 2, d[4] - d[10])
    polil += geometry.Point3D(d[8] - d[0] -
                              (d[1] - d[2] * 2 - d[3]) / 2, d[1], d[4] - d[10])
    polil += geometry.Point3D(d[8] - d[0], d[1] - d[2], d[4])

    direction = geometry.Polyline3D()
    direction += geometry.Point3D(d[8] - d[0], d[1] - d[2], d[4])
    direction += geometry.Point3D(d[8] - d[0] +
                                  10, d[1] - d[2] - 10, d[4] + 10)

    error, figure = geometry.CreatePolyhedron(polil, direction)

    return figure


def bp_3_3(build_ele):
    d = lb.get(build_ele)
    polil = geometry.Polygon3D()
    polil += geometry.Point3D(d[8] - d[0], d[1] - d[2], d[4])
    polil += geometry.Point3D(d[8] - d[0], d[1], d[4] - d[10])
    polil += geometry.Point3D(d[8] - d[0] -
                              (d[1] - d[2] * 2 - d[3]) / 2, d[1], d[4] - d[10])
    polil += geometry.Point3D(d[8] - d[0], d[1] - d[2], d[4])

    direction = geometry.Polyline3D()
    direction += geometry.Point3D(d[8] - d[0], d[1] - d[2], d[4])
    direction += geometry.Point3D(d[8] - d[0], d[1] - d[2] - 10, d[4])

    error, figure = geometry.CreatePolyhedron(polil, direction)
    return figure


def bp_2_4(build_ele):
    d = lb.get(build_ele)
    polil = geometry.Polygon3D()
    polil += geometry.Point3D(d[8] - d[0], d[2], d[4])
    polil += geometry.Point3D(d[8] - d[0] - d[9],
                              d[2] + (d[1] - d[2] * 2 - d[3]) / 2, d[4])
    polil += geometry.Point3D(d[8] - d[0] - d[9] - (d[1] - d[2]
                              * 2 - d[3]) / 2, (d[1] - d[2] * 2 - d[3]) / 2, d[4] - d[10])
    polil += geometry.Point3D(d[8] - d[0] -
                              (d[1] - d[2] * 2 - d[3]) / 2, 0, d[4] - d[10])
    polil += geometry.Point3D(d[8] - d[0], d[2], d[4])

    direction = geometry.Polyline3D()
    direction += geometry.Point3D(d[8] - d[0], d[2], d[4])
    direction += geometry.Point3D(d[8] - d[0] - 10, d[2] + 10, d[4] - 10)

    error, figure = geometry.CreatePolyhedron(polil, direction)

    return figure


def bp_3_4(build_ele):
    d = lb.get(build_ele)
    polil = geometry.Polygon3D()
    polil += geometry.Point3D(d[8] - d[0], d[2], d[4])
    polil += geometry.Point3D(d[8] - d[0], 0, d[4] - d[10])
    polil += geometry.Point3D(d[8] - d[0] -
                              (d[1] - d[2] * 2 - d[3]) / 2, 0, d[4] - d[10])
    polil += geometry.Point3D(d[8] - d[0], d[2], d[4])

    direction = geometry.Polyline3D()
    direction += geometry.Point3D(d[8] - d[0], d[2], d[4])
    direction += geometry.Point3D(d[8] - build_ele.mew.value, d[2] + 10, d[4])

    error, figure = geometry.CreatePolyhedron(polil, direction)

    return figure


def bp_last(build_ele):
    d = lb.get(build_ele)
    polil = geometry.Polygon3D()
    polil += geometry.Point3D(0, 20, 0)
    polil += geometry.Point3D(0, d[1] - 20, 0)
    polil += geometry.Point3D(0, d[1], 20)
    polil += geometry.Point3D(0, d[1], d[4] - d[10])
    polil += geometry.Point3D(0, 0, d[4] - d[10])
    polil += geometry.Point3D(0, 0, 20)
    polil += geometry.Point3D(0, 20, 0)

    direction = geometry.Polyline3D()
    direction += geometry.Point3D(0, 20, 0)
    direction += geometry.Point3D(d[8], 20, 0)
    error, figure = geometry.CreatePolyhedron(polil, direction)
    return figure
