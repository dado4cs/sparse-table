from manim import *

class Escena4_Complejidad(Scene):
    def construct(self):
        # animacion (titulo de complejidad)
        title = Text("Análisis de Complejidad", font_size=40, color=YELLOW)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(1)

        # animacion (textos de preprocesamiento)
        prep_title = Text("1. Preprocesamiento: O(N log N)", font_size=32, color=GREEN)
        prep_desc = Text("Se construye una matriz de dimensiones N × log₂(N).", font_size=24)
        prep_op = Text("Cada celda toma O(1) calculando min(A, B).", font_size=24)
        
        prep_group = VGroup(prep_title, prep_desc, prep_op).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        prep_group.next_to(title, DOWN, buff=1.0).to_edge(LEFT, buff=1.0)
        
        self.play(FadeIn(prep_title, shift=RIGHT*0.5))
        self.play(FadeIn(prep_desc))
        self.play(FadeIn(prep_op))
        self.wait(2)

        # animacion (textos de consultas)
        query_title = Text("2. Consultas: O(1)", font_size=32, color=TEAL)
        query_desc = Text("Para cualquier rango, se calculan exactamente dos bloques superpuestos.", font_size=24)
        query_op = Text("Se obtiene el mínimo entre esos dos bloques en un solo paso.", font_size=24)
        
        query_group = VGroup(query_title, query_desc, query_op).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        query_group.next_to(prep_group, DOWN, buff=1.0).to_edge(LEFT, buff=1.0)

        self.play(FadeIn(query_title, shift=RIGHT*0.5))
        self.play(FadeIn(query_desc))
        self.play(FadeIn(query_op))
        self.wait(3)

        # animacion (despedida)
        thanks = Text("¡Gracias por ver!", font_size=40, color=YELLOW)
        self.play(FadeOut(title), FadeOut(prep_group), FadeOut(query_group))
        self.play(Write(thanks))
        self.wait(2)
