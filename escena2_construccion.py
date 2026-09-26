from manim import *
from estructura import MinSparseTable, INPUT_ARRAY, SMALL_FONT, FONT, _sup
from visual_utils import create_base_layout

class Escena2_Construccion(Scene):
    def construct(self):
        # preparacion de datos
        in_array = INPUT_ARRAY
        n = len(in_array)
        st = MinSparseTable(in_array)
        y = len(st.mat)

        # animacion (titulo principal)
        title = Text("Sparse Table — Preprocesamiento", font_size=36, color=YELLOW)
        title.to_edge(UP, buff=0.35)
        self.play(Write(title), run_time=1.0)
        self.wait(0.5)

        # creacion de la disposicion visual
        arr_group, arr_cells, mat_group, mob_mat, idx_labels, i_header, j_labels, j_header, full, everything = create_base_layout(in_array, st)

        # animacion (aparicion del arreglo)
        self.play(FadeIn(arr_group, shift=DOWN * 0.3), run_time=1.0)
        self.play(FadeIn(idx_labels), FadeIn(i_header), run_time=0.8)
        self.wait(0.5)

        # animacion (aparicion de la cuadricula vacia)
        self.play(FadeIn(mat_group, shift=DOWN * 0.3), run_time=1.0)
        self.play(FadeIn(j_labels), FadeIn(j_header), run_time=0.8)
        self.wait(0.6)

        # animacion (texto fase j=0)
        phase_text = Text("j = 0  →  copiar el arreglo original", font_size=SMALL_FONT, color=GREEN)
        phase_text.to_edge(DOWN, buff=0.30)
        self.play(FadeIn(phase_text), run_time=0.6)

        brace_target = VGroup(arr_cells[0][0])
        brace = Brace(brace_target, direction=DOWN, buff=0.1, color=GREEN)
        brace_label = Text(f"2{_sup(0)} = 1", font_size=SMALL_FONT, color=GREEN)
        brace_label.next_to(brace, DOWN, buff=0.06)
        brace_grp = VGroup(brace, brace_label)
        self.play(FadeIn(brace_grp), run_time=0.4)

        # iteracion para llenar la fila 0
        for i in range(n):
            val = st.mat[0][i]
            new_txt = Text(str(val), font_size=FONT, color=GREEN_B)
            new_txt.move_to(mob_mat[0][i][0].get_center())

            # animacion (resaltar origen)
            self.play(arr_cells[i][0].animate.set_fill(GREEN, opacity=0.25), run_time=0.25)
            
            # animacion (escribir valor)
            self.play(FadeOut(mob_mat[0][i][1]), FadeIn(new_txt), run_time=0.3)
            mob_mat[0][i] = VGroup(mob_mat[0][i][0], new_txt)

            if i < n - 1:
                new_target = VGroup(arr_cells[i + 1][0])
                new_brace = Brace(new_target, direction=DOWN, buff=0.1, color=GREEN)
                new_label = Text(f"2{_sup(0)} = 1", font_size=SMALL_FONT, color=GREEN)
                new_label.next_to(new_brace, DOWN, buff=0.06)
                
                # animacion (mover llave)
                self.play(
                    Transform(brace, new_brace), Transform(brace_label, new_label), run_time=0.25
                )
            self.play(arr_cells[i][0].animate.set_fill(GREEN, opacity=0), run_time=0.15)

        self.play(FadeOut(brace_grp), FadeOut(phase_text), run_time=0.4)
        self.wait(0.4)

        # iteracion para llenar las siguientes filas
        for j in range(1, y):
            rango = n - 2**j + 1
            block_size = 2**j
            half = 2 ** (j - 1)

            # animacion (texto de formula)
            phase_text = Text(f"j = {j}  →  min(mat[{j-1}][i], mat[{j-1}][i+{half}])", font_size=SMALL_FONT, color=ORANGE)
            phase_text.to_edge(DOWN, buff=0.30)
            self.play(FadeIn(phase_text), run_time=0.5)

            for i in range(rango):
                off = i + half

                # construccion de llaves separadas para mostrar las mitades que componen j
                cov1 = VGroup(*[arr_cells[k][0] for k in range(i, i + half)])
                brace1 = Brace(cov1, direction=DOWN, buff=0.1, color=BLUE_C)
                lbl1 = Text(f"2{_sup(j-1)}", font_size=SMALL_FONT, color=BLUE_C).next_to(brace1, DOWN, buff=0.06)

                cov2 = VGroup(*[arr_cells[k][0] for k in range(off, off + half)])
                brace2 = Brace(cov2, direction=DOWN, buff=0.1, color=RED_C)
                lbl2 = Text(f"2{_sup(j-1)}", font_size=SMALL_FONT, color=RED_C).next_to(brace2, DOWN, buff=0.06)

                brace_grp = VGroup(brace1, lbl1, brace2, lbl2)

                src1_sq = mob_mat[j - 1][i][0]
                src2_sq = mob_mat[j - 1][off][0]

                # animacion (resaltar celdas previas y llaves divididas)
                high_arr1 = [arr_cells[k][0].animate.set_fill(BLUE, opacity=0.3) for k in range(i, i + half)]
                high_arr2 = [arr_cells[k][0].animate.set_fill(RED, opacity=0.3) for k in range(off, off + half)]
                
                self.play(
                    FadeIn(brace_grp),
                    src1_sq.animate.set_fill(BLUE, opacity=0.35),
                    src2_sq.animate.set_fill(RED, opacity=0.35),
                    *high_arr1,
                    *high_arr2,
                    run_time=0.4,
                )

                val = st.mat[j][i]
                new_txt = Text(str(val), font_size=FONT, color=ORANGE)
                new_txt.move_to(mob_mat[j][i][0].get_center())

                # animacion (escribir nuevo valor)
                self.play(FadeOut(mob_mat[j][i][1]), FadeIn(new_txt), run_time=0.4)
                mob_mat[j][i] = VGroup(mob_mat[j][i][0], new_txt)

                # animacion (quitar resaltado)
                unhigh_arr1 = [arr_cells[k][0].animate.set_fill(BLUE, opacity=0) for k in range(i, i + half)]
                unhigh_arr2 = [arr_cells[k][0].animate.set_fill(RED, opacity=0) for k in range(off, off + half)]
                
                self.play(
                    src1_sq.animate.set_fill(BLUE, opacity=0),
                    src2_sq.animate.set_fill(RED, opacity=0),
                    *unhigh_arr1,
                    *unhigh_arr2,
                    FadeOut(brace_grp),
                    run_time=0.3,
                )

            self.play(FadeOut(phase_text), run_time=0.4)
            self.wait(0.3)

        self.wait(0.8)
        
        # animacion (mensaje final de construccion)
        complete_text = Text("¡Sparse Table construida!", font_size=30, color=GREEN)
        complete_text.to_edge(DOWN, buff=0.35)
        self.play(FadeIn(complete_text, scale=1.2), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(complete_text), FadeOut(title), run_time=0.5)
