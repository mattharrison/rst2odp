import preso


def test_add_cell():
    p = preso.Preso()
    p.add_slide()
    margin = 3
    top = 4
    preso.add_cell(p, 1, 1, 1, top_margin=top,left_margin=margin)
    width = 28
    height = 17
    assert preso.SLIDE_WIDTH == width
    w, h, x, y = p.slides[-1].grid_w_h_x_y
    assert w == "{:.1f}cm".format(width - margin * 2)

    assert x == "{:.1f}cm".format(margin)
    assert y == "{:.1f}cm".format(top)
    assert h == "{:.1f}cm".format(height)
    assert w == "{:.1f}cm".format(width - margin*2)

