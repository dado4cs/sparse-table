from manim import *


class Escena1_Intro(Scene):
    def construct(self):
        title = Text("Estructura de Datos: Sparse Table", font_size=48, color=YELLOW)
        subtitle = Text(
            "Ideal para consultas de rango en arreglos estáticos",
            font_size=28,
            color=LIGHT_GREY,
        )

        members = Text(
            "Integrantes:\nMaxwell Lupo Gregorio Collazos Solis\n- Renzo Vladimir Cuba Zari\n- José Luis Villalobos Jiménez",
            font_size=24,
            color=WHITE,
        )

        title.shift(UP * 1.5)
        subtitle.next_to(title, DOWN, buff=0.3)
        members.next_to(subtitle, DOWN, buff=1.0)

        self.play(Write(title), run_time=1.5)
        self.play(FadeIn(subtitle, shift=UP * 0.3), run_time=1)
        self.play(FadeIn(members), run_time=1)
        self.wait(2)

        self.play(FadeOut(title), FadeOut(subtitle), FadeOut(members), run_time=1)

        concept_title = Text("¿Qué es una Sparse Table?", font_size=40, color=BLUE)
        concept_title.to_edge(UP)

        p1 = Text(
            "1. Precalcula respuestas para rangos en potencias de 2.", font_size=28
        )
        p2 = Text(
            "2. Permite responder consultas superponiendo dos bloques.", font_size=28
        )
        p3 = Text(
            "3. Perfecta para operaciones idempotentes: Mínimo, Máximo, GCD.",
            font_size=28,
        )

        bullets = VGroup(p1, p2, p3).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        bullets.next_to(concept_title, DOWN, buff=1.0)

        self.play(Write(concept_title), run_time=1)
        for bullet in bullets:
            self.play(FadeIn(bullet, shift=RIGHT * 0.5), run_time=1)
            self.wait(0.5)

        self.wait(2)
        self.play(FadeOut(concept_title), FadeOut(bullets), run_time=1)

        # animacion (titulo de pseudocodigo)
        pseudo_title = Text("Pseudocódigo — Sparse Table", font_size=40, color=YELLOW)
        pseudo_title.to_edge(UP, buff=0.4)
        self.play(Write(pseudo_title))
        self.wait(0.5)

        # preparacion de codigo
        code_str = """function build(A):
    n = length(A)
    for i = 0 to n - 1:
        mat[0][i] = A[i]
        
    for j = 1 to floor(log2(n)):
        for i = 0 to n - 2^j:
            mat[j][i] = min(mat[j-1][i], mat[j-1][i + 2^(j-1)])

function query(L, R):
    k = floor(log2(R - L + 1))
    return min(mat[k][L], mat[k][R - 2^k + 1])"""

        # creacion de bloque de codigo
        code = Code(
            code_string=code_str,
            tab_width=4,
            background="window",
            language="python",
            add_line_numbers=False,
            formatter_style="monokai",
        )
        code.next_to(pseudo_title, DOWN, buff=0.5)

        # animacion (mostrar codigo completo)
        self.play(FadeIn(code), run_time=1.5)
        self.wait(5)

        # animacion (salida final)
        self.play(FadeOut(pseudo_title), FadeOut(code), run_time=1)
