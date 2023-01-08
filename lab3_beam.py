import NemAll_Python_Geometry as geometry
import NemAll_Python_BaseElements as base_elements
import NemAll_Python_BasisElements as basis_elements


def check_allplan_version(build_ele, version):
    del build_ele
    del version
    return True


def create_element(build_ele, doc):
    el = Lab2_Beam(doc)
    return el.create(build_ele)


class Lab2_Beam:
    def __init__(self, doc):
        self.model_ele_list = []
        self.handle_list = []
        self.document = doc

    def create(self, build_ele):
        self.un(build_ele)
        self.bottom_part(build_ele)
        return (self.model_ele_list, self.handle_list)

    def un(self, build_ele):
        style = base_elements.CommonProperties()
        style.GetGlobalProperties()
        style.Pen = 1
        style.Color = 3
        style.Stroke = 1
        down = self.bottom_part(build_ele)
        center = self.center_part(build_ele)
        up = self.top_part(build_ele)
        error, figure = geometry.MakeUnion(down, center)
        error, figure = geometry.MakeUnion(figure, up)
        self.model_ele_list.append(
            basis_elements.ModelElement3D(style, figure))

    def bottom_part(self, build_ele):
        figure = self.bp_1(build_ele)
        error, figure = geometry.MakeUnion(figure, self.bp_2(build_ele))
        error, figure = geometry.MakeUnion(figure, self.bp_3(build_ele))
        error, figure = geometry.MakeUnion(figure, self.bp_4(build_ele))
        error, figure = geometry.MakeUnion(figure, self.bp_2_2(build_ele))
        error, figure = geometry.MakeUnion(figure, self.bp_3_2(build_ele))
        error, figure = geometry.MakeUnion(figure, self.bp_4_2(build_ele))
        error, figure = geometry.MakeUnion(figure, self.bp_2_3(build_ele))
        error, figure = geometry.MakeUnion(figure, self.bp_3_3(build_ele))
        error, figure = geometry.MakeUnion(figure, self.bp_2_4(build_ele))
        error, figure = geometry.MakeUnion(figure, self.bp_3_4(build_ele))
        error, figure = geometry.MakeUnion(figure, self.bp_last(build_ele))
        return figure

    def top_part(self, build_ele):
        sign = (build_ele.len.value - build_ele.cenw.value)
        figure = self.tp_1(build_ele)
        error, figure = geometry.MakeUnion(figure, self.tp_3(build_ele))
        error, figure = geometry.MakeUnion(figure, self.tp_2(build_ele))
        error, figure = geometry.MakeUnion(
            figure, self.tp_3(build_ele, sign=sign))
        error, figure = geometry.MakeUnion(figure, self.tp_4(build_ele))
        error, figure = geometry.MakeUnion(figure, self.tp_2_2(build_ele))
        error, figure = geometry.MakeUnion(figure, self.tp_4(
            build_ele, build_ele.widb.value - build_ele.sectionbb.value * 2, build_ele.wit.value, 10))
        error, figure = geometry.MakeUnion(figure, self.tp_2_3(build_ele))
        error, figure = geometry.MakeUnion(figure, self.tp_4_2(build_ele))
        error, figure = geometry.MakeUnion(figure, self.tp_4_2(
            build_ele, build_ele.widb.value - build_ele.sectionbb.value * 2, build_ele.wit.value, 10))
        error, figure = geometry.MakeUnion(figure, self.tp_3_3(build_ele))
        error, figure = geometry.MakeUnion(figure, self.tp_last(build_ele))
        return figure

    def center_part(self, build_ele):
        d = self.get(build_ele)
        polil = geometry.Polygon3D()
        polil += geometry.Point3D(0, d[0], d[1])
        polil += geometry.Point3D(0, d[2] - d[0], d[1])
        polil += geometry.Point3D(d[3], d[2] - d[0], d[1])
        polil += geometry.Point3D(d[3] + d[4], d[2] -
                                  d[0] - (d[2] - d[0] * 2 - d[5]) / 2, d[1])
        polil += geometry.Point3D(d[6] - (d[3] + d[4]),
                                  d[2] - d[0] - (d[2] - d[0] * 2 - d[5]) / 2, d[1])
        polil += geometry.Point3D(d[6] - d[3], d[2] - d[0], d[1])
        polil += geometry.Point3D(d[6], d[2] - d[0], d[1])
        polil += geometry.Point3D(d[6], d[0], d[1])
        polil += geometry.Point3D(d[6] - d[3], d[0], d[1])
        polil += geometry.Point3D(d[6] - d[3] - d[4],
                                  d[0] + (d[2] - d[0] * 2 - d[5]) / 2, d[1])
        polil += geometry.Point3D(d[3] + d[4],
                                  d[0] + (d[2] - d[0] * 2 - d[5]) / 2, d[1])
        polil += geometry.Point3D(d[3], d[0], d[1])
        polil += geometry.Point3D(0, d[0], d[1])

        direction = geometry.Polyline3D()
        direction += geometry.Point3D(0, d[0], d[1])
        direction += geometry.Point3D(0, d[0], d[1] + build_ele.cenhe.value)

        error, figure = geometry.CreatePolyhedron(polil, direction)
        return figure

    def get(self, build_ele):
        cenw = build_ele.cenw.value
        widb = build_ele.widb.value
        sectionbb = build_ele.sectionbb.value
        cenwi = build_ele.cenwi.value
        heb = build_ele.heb.value
        cenhe = build_ele.cenhe.value
        wit = build_ele.wit.value
        ths = build_ele.ths.value
        len = build_ele.len.value
        tent = build_ele.tent.value
        inte = build_ele.inte.value
        return [cenw, widb, sectionbb, cenwi, heb, cenhe, wit, ths, len, tent, inte]
