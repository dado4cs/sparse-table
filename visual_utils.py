from manim import *
from estructura import CELL_SIZE, FONT, SMALL_FONT

# crea la disposicion visual base
def create_base_layout(in_array, st):
    n = len(in_array)
    y = len(st.mat)

    # dibuja el arreglo original
    arr_group = VGroup()
    arr_cells = []
    for idx, val in enumerate(in_array):
        sq = Square(side_length=CELL_SIZE, color=BLUE, stroke_width=2)
        txt = Text(str(val), font_size=FONT, color=WHITE)
        cell = VGroup(sq, txt)
        arr_cells.append(cell)
        arr_group.add(cell)
    arr_group.arrange(RIGHT, buff=0.08)

    # dibuja las etiquetas de indice i
    idx_labels = VGroup()
    for idx, cell in enumerate(arr_cells):
        lbl = Text(str(idx), font_size=SMALL_FONT, color=GRAY)
        lbl.next_to(cell, UP, buff=0.12)
        idx_labels.add(lbl)

    i_header = Text("i (columnas)", font_size=SMALL_FONT, color=GRAY, slant=ITALIC)

    # dibuja la cuadricula de la matriz
    mat_group = VGroup()
    mob_mat = []

    for row in range(y):
        vis_row = VGroup()
        mob_row = []
        rango = n - 2**row + 1
        for col in range(n):
            sq = Square(side_length=CELL_SIZE, stroke_width=1.5)
            if col < rango:
                sq.set_color(WHITE)
            else:
                sq.set_color(DARK_GRAY)
                sq.set_fill(DARK_GRAY, opacity=0.15)
            txt = Text("", font_size=FONT)
            cell = VGroup(sq, txt)
            vis_row.add(cell)
            mob_row.append(cell)
        vis_row.arrange(RIGHT, buff=0.08)
        mat_group.add(vis_row)
        mob_mat.append(mob_row)
    mat_group.arrange(DOWN, buff=0.15)

    # dibuja las etiquetas de indice j
    j_labels = VGroup()
    for row in range(y):
        lbl = Text(f"j={row}", font_size=SMALL_FONT, color=YELLOW_C)
        j_labels.add(lbl)

    j_header = Text("j (filas)", font_size=SMALL_FONT, color=YELLOW_C, slant=ITALIC)

    # agrupa y posiciona todo
    full = VGroup(arr_group, mat_group)
    full.arrange(DOWN, buff=0.9)
    full.move_to(ORIGIN).shift(DOWN * 0.2)

    for idx, cell in enumerate(arr_cells):
        idx_labels[idx].next_to(cell, UP, buff=0.12)
    i_header.next_to(idx_labels[0], LEFT, buff=0.35)
    for row in range(y):
        j_labels[row].next_to(mat_group[row], LEFT, buff=0.30)
    j_header.next_to(j_labels[0], UP, buff=0.35).align_to(j_labels, RIGHT)

    everything = VGroup(full, idx_labels, i_header, j_labels, j_header)

    return arr_group, arr_cells, mat_group, mob_mat, idx_labels, i_header, j_labels, j_header, full, everything

# llena la matriz sin animacion
def fill_table_instantly(mob_mat, st):
    y = len(st.mat)
    n = len(st.mat[0])
    for row in range(y):
        rango = n - 2**row + 1
        for col in range(rango):
            val = st.mat[row][col]
            color = GREEN_B if row == 0 else ORANGE
            txt = Text(str(val), font_size=FONT, color=color)
            txt.move_to(mob_mat[row][col][0].get_center())
            mob_mat[row][col][1].become(txt)
