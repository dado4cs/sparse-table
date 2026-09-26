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
            "Integrantes:\n- Maxwell Lupo Gregorio Collazos Solis\n- Renzo Vladimir Cuba Zari\n- José Luis Villalobos Jiménez",
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
