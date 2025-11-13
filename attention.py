"""
Visualização de mecanismos de atenção para modelos de linguagem
"""
from manim_imports_ext import *


class AttentionPatterns(InteractiveScene):
    """Visualização de padrões de atenção em transformers"""

    def construct(self):
        # Título
        title = Tex("Mecanismo de Atenção", font_size=60)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait()

        # Criar tokens de entrada
        tokens = ["O", "gato", "está", "no", "telhado"]
        token_objects = VGroup(*[
            Tex(token, font_size=40)
            for token in tokens
        ])
        token_objects.arrange(RIGHT, buff=0.8)
        token_objects.move_to(ORIGIN)

        # Adicionar boxes ao redor dos tokens
        boxes = VGroup(*[
            SurroundingRectangle(token, color=BLUE, buff=0.1)
            for token in token_objects
        ])

        self.play(
            LaggedStart(*[
                FadeIn(token, shift=UP*0.3)
                for token in token_objects
            ], lag_ratio=0.2)
        )
        self.play(ShowCreation(boxes, lag_ratio=0.1))
        self.wait()

        # Criar matriz de atenção
        self.show_attention_matrix(token_objects, tokens)

    def show_attention_matrix(self, token_objects, tokens):
        """Mostra a matriz de atenção"""
        # Título da matriz
        matrix_title = Tex("Matriz de Atenção", font_size=40)
        matrix_title.to_edge(UP)

        # Criar grid de valores de atenção (exemplo simplificado)
        n = len(tokens)
        attention_values = [
            [0.1, 0.2, 0.3, 0.2, 0.2],  # Atenção de "O"
            [0.2, 0.4, 0.2, 0.1, 0.1],  # Atenção de "gato"
            [0.15, 0.15, 0.3, 0.2, 0.2],  # Atenção de "está"
            [0.1, 0.1, 0.2, 0.4, 0.2],  # Atenção de "no"
            [0.1, 0.3, 0.1, 0.2, 0.3],  # Atenção de "telhado"
        ]

        # Criar células da matriz
        cell_size = 0.6
        matrix = VGroup()
        for i in range(n):
            row = VGroup()
            for j in range(n):
                value = attention_values[i][j]
                # Cor baseada no valor de atenção
                color = interpolate_color(BLUE, RED, value)

                cell = Square(side_length=cell_size)
                cell.set_fill(color, opacity=0.7)
                cell.set_stroke(WHITE, width=1)

                # Adicionar valor numérico
                text = Tex(f"{value:.1f}", font_size=20, color=WHITE)
                text.move_to(cell)

                cell_group = VGroup(cell, text)
                row.add(cell_group)

            row.arrange(RIGHT, buff=0)
            matrix.add(row)

        matrix.arrange(DOWN, buff=0)
        matrix.scale(0.8)

        # Adicionar labels
        row_labels = VGroup(*[
            Tex(token, font_size=25)
            for token in tokens
        ])
        row_labels.arrange(DOWN, buff=cell_size * 0.8)
        row_labels.next_to(matrix, LEFT, buff=0.3)

        col_labels = VGroup(*[
            Tex(token, font_size=25)
            for token in tokens
        ])
        col_labels.arrange(RIGHT, buff=cell_size * 0.8)
        col_labels.next_to(matrix, UP, buff=0.3)

        # Animar
        self.play(
            FadeOut(token_objects),
            FadeOut(VGroup(*self.mobjects)),
            Write(matrix_title)
        )
        self.wait()

        self.play(
            FadeIn(row_labels, shift=RIGHT*0.5),
            FadeIn(col_labels, shift=DOWN*0.5)
        )
        self.wait()

        # Mostrar matriz célula por célula
        for row in matrix:
            self.play(
                LaggedStart(*[
                    FadeIn(cell, scale=0.8)
                    for cell in row
                ], lag_ratio=0.1),
                run_time=0.5
            )

        self.wait(2)


class QueryKeyValue(InteractiveScene):
    """Visualização de Query, Key e Value"""

    def construct(self):
        title = Tex("Query, Key, Value", font_size=60)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait()

        # Criar exemplo de palavra
        word = Tex("gato", font_size=50, color=YELLOW)
        word_box = SurroundingRectangle(word, color=WHITE)
        word_group = VGroup(word, word_box)
        word_group.move_to(LEFT * 4)

        self.play(FadeIn(word_group, shift=UP))
        self.wait()

        # Criar vetores Q, K, V
        vectors = VGroup()
        labels = ["Query (Q)", "Key (K)", "Value (V)"]
        colors = [BLUE, GREEN, RED]

        for i, (label, color) in enumerate(zip(labels, colors)):
            # Label
            vec_label = Tex(label, font_size=35, color=color)

            # Vetor (representado como matriz)
            vector = Matrix(
                [[0.2], [0.5], [0.8], [0.3]],
                element_to_mobject_config={"font_size": 25}
            )
            vector.set_color(color)

            vec_group = VGroup(vec_label, vector)
            vec_group.arrange(DOWN, buff=0.3)

            vectors.add(vec_group)

        vectors.arrange(RIGHT, buff=1)
        vectors.next_to(word_group, RIGHT, buff=1.5)

        # Animar criação dos vetores
        self.play(
            LaggedStart(*[
                FadeIn(vec, shift=UP*0.5)
                for vec in vectors
            ], lag_ratio=0.3)
        )
        self.wait()

        # Mostrar transformações
        arrow1 = Arrow(word_group.get_right(), vectors[0].get_left(), color=BLUE)
        arrow2 = Arrow(word_group.get_right(), vectors[1].get_left(), color=GREEN)
        arrow3 = Arrow(word_group.get_right(), vectors[2].get_left(), color=RED)

        # Labels das transformações
        w_q = Tex(R"W_Q", font_size=30, color=BLUE).next_to(arrow1, UP, buff=0.1)
        w_k = Tex(R"W_K", font_size=30, color=GREEN).next_to(arrow2, UP, buff=0.1)
        w_v = Tex(R"W_V", font_size=30, color=RED).next_to(arrow3, DOWN, buff=0.1)

        self.play(
            ShowCreation(arrow1),
            ShowCreation(arrow2),
            ShowCreation(arrow3),
        )
        self.play(
            Write(w_q),
            Write(w_k),
            Write(w_v),
        )
        self.wait(2)


class SelfAttentionMechanism(InteractiveScene):
    """Visualização completa do mecanismo de self-attention"""

    def construct(self):
        title = Tex("Mecanismo de Self-Attention", font_size=60)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait()

        # Fórmula da atenção
        formula = Tex(
            R"\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V",
            font_size=40
        )
        formula.next_to(title, DOWN, buff=0.5)

        self.play(Write(formula))
        self.wait(2)

        # Explicação passo a passo
        steps = [
            R"1. Calcular $QK^T$ (similaridade)",
            R"2. Dividir por $\sqrt{d_k}$ (escalar)",
            R"3. Aplicar softmax (normalizar)",
            R"4. Multiplicar por $V$ (combinar valores)",
        ]

        step_objects = VGroup(*[
            Tex(step, font_size=35)
            for step in steps
        ])
        step_objects.arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        step_objects.next_to(formula, DOWN, buff=0.8)

        # Animar passos
        for step in step_objects:
            self.play(FadeIn(step, shift=RIGHT*0.3))
            self.wait(0.5)

        self.wait(2)


class AttentionVisualization(InteractiveScene):
    """Visualização animada do fluxo de atenção"""

    def construct(self):
        title = Tex("Fluxo de Atenção", font_size=60)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait()

        # Tokens
        tokens = ["O", "gato", "subiu"]
        token_mobs = VGroup(*[
            Tex(token, font_size=40)
            for token in tokens
        ])
        token_mobs.arrange(RIGHT, buff=1.5)
        token_mobs.shift(UP * 2)

        # Círculos ao redor dos tokens
        circles = VGroup(*[
            Circle(radius=0.5, color=BLUE).move_to(token)
            for token in token_mobs
        ])

        self.play(
            LaggedStart(*[Write(token) for token in token_mobs], lag_ratio=0.2),
            LaggedStart(*[ShowCreation(circle) for circle in circles], lag_ratio=0.2)
        )
        self.wait()

        # Animar conexões de atenção
        # "gato" atende para todos os outros tokens
        target_idx = 1  # "gato"
        target = token_mobs[target_idx]

        for i, token in enumerate(token_mobs):
            if i != target_idx:
                # Desenhar linha de atenção
                line = Line(
                    target.get_center(),
                    token.get_center(),
                    color=YELLOW,
                    stroke_width=3
                )
                line.set_opacity(0.7)

                # Peso da atenção
                weight = 0.8 if i == 2 else 0.3  # Mais atenção para "subiu"
                label = Tex(f"{weight:.1f}", font_size=25, color=YELLOW)
                label.next_to(line.get_center(), UP, buff=0.1)

                self.play(
                    ShowCreation(line),
                    FadeIn(label),
                    circles[i].animate.set_color(YELLOW),
                    run_time=0.8
                )
                self.wait(0.5)

        self.wait(2)


# Cena para testar rapidamente
class TestScene(InteractiveScene):
    def construct(self):
        text = Tex("Olá, ManimGL!", font_size=72, color=BLUE)
        circle = Circle(radius=3, color=YELLOW)
        self.play(Write(text))
        self.play(ShowCreation(circle))
        self.wait()
