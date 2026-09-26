from manim import *
from math import log2
from estructura import MinSparseTable, INPUT_ARRAY, QUERIES, SMALL_FONT, FONT, _sup
from visual_utils import create_base_layout, fill_table_instantly

class Escena3_Consultas(Scene):
    def construct(self):
        # preparacion de datos
        in_array = INPUT_ARRAY
        st = MinSparseTable(in_array)

        title = Text("Consultas — O(1)", font_size=36, color=YELLOW)
        title.to_edge(UP, buff=0.35)
        self.add(title)

        # creacion de la disposicion ya llena
        arr_group, arr_cells, mat_group, mob_mat, idx_labels, i_header, j_labels, j_header, full, everything = create_base_layout(in_array, st)
        fill_table_instantly(mob_mat, st)
        
        self.add(everything)
        self.wait(0.5)
        
        # animacion (desplazar a la izquierda)
        self.play(everything.animate.to_edge(LEFT, buff=0.5), run_time=1.5)
        self.wait(0.5)

        # iteracion sobre las consultas
        for q_idx, (ql, qr) in enumerate(QUERIES):
            size = qr - ql + 1
            k = int(log2(size))
            left2 = qr - 2**k + 1

            if ql == qr:
                q_desc = Text(f"Caso Borde: query({ql}, {qr})", font_size=28, color=TEAL)
            else:
                q_desc = Text(f"query({ql}, {qr})", font_size=28, color=TEAL)
                
            q_detail = Text(f"rango [{ql}..{qr}], tamaño {size}", font_size=24, color=TEAL)
            k_desc = Text(f"k = floor(log2({size})) = {k}", font_size=24, color=TEAL)
            
            query_info = VGroup(q_desc, q_detail, k_desc)
            query_info.arrange(DOWN, aligned_edge=LEFT, buff=0.25)
            query_info.to_edge(RIGHT, buff=0.8).shift(UP * 1.5)

            # animacion (mostrar informacion de la query)
            self.play(FadeIn(query_info), run_time=0.7)

            # animacion (resaltar rango en el arreglo)
            highlight_anims = [
                arr_cells[idx][0].animate.set_fill(TEAL, opacity=0.3)
                for idx in range(ql, qr + 1)
            ]
            self.play(*highlight_anims, run_time=0.5)

            int1 = VGroup(*[arr_cells[idx][0] for idx in range(ql, ql + 2**k)])
            brace1 = Brace(int1, direction=DOWN, buff=0.1, color=BLUE_C)
            
            int2 = VGroup(*[arr_cells[idx][0] for idx in range(left2, left2 + 2**k)])
            brace2 = Brace(int2, direction=DOWN, buff=0.25, color=RED_C)

            ref1 = Text(f"mat[{k}][{ql}] = {st.mat[k][ql]}", font_size=24, color=BLUE_C)
            ref2 = Text(f"mat[{k}][{left2}] = {st.mat[k][left2]}", font_size=24, color=RED_C)
            refs = VGroup(ref1, ref2).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            refs.next_to(query_info, DOWN, buff=0.6, aligned_edge=LEFT)

            cell1_sq = mob_mat[k][ql][0]
            cell2_sq = mob_mat[k][left2][0]

            # animacion (mostrar llaves azules y rojas)
            self.play(
                FadeIn(brace1), FadeIn(ref1),
                cell1_sq.animate.set_fill(BLUE, opacity=0.35),
                run_time=0.6,
            )
            
            if ql != left2:
                # animacion (resaltar bloques de la matriz)
                self.play(
                    FadeIn(brace2), FadeIn(ref2),
                    cell2_sq.animate.set_fill(RED, opacity=0.35),
                    run_time=0.6,
                )
            else:
                self.wait(0.5)

            result = st.query(ql, qr)
            res_text = Text(f"Resultado = {result}", font_size=28, color=GREEN)
            res_text.next_to(refs, DOWN, buff=0.6, aligned_edge=LEFT)
            
            # animacion (mostrar el resultado final)
            self.play(FadeIn(res_text, scale=1.15), run_time=0.7)
            self.wait(2.5)

            unhighlight = [arr_cells[idx][0].animate.set_fill(TEAL, opacity=0) for idx in range(ql, qr + 1)]
            
            fade_outs = [FadeOut(brace1), FadeOut(query_info), FadeOut(refs), FadeOut(res_text)]
            if ql != left2: fade_outs.append(FadeOut(brace2))
            
            # animacion (limpieza de la pantalla)
            self.play(
                *unhighlight,
                cell1_sq.animate.set_fill(BLUE, opacity=0),
                cell2_sq.animate.set_fill(RED, opacity=0),
                *fade_outs,
                run_time=0.6,
            )
            self.wait(0.4)

        # animacion (salida final)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=1.0)
