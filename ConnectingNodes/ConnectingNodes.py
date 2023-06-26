from manim import *

class ConnectingNodes(Scene):
    def construct(self):
        """
        This scene demonstrates connecting two nodes with an edge and labeling them.
        """

        # Create nodes
        node_A = Circle(radius=0.5, color=GREEN).move_to(LEFT * 3 + UP * 0)
        node_B = Circle(radius=0.5, color=BLUE).move_to(RIGHT * 3)

        # Create edge
        edge_AB = Line(start=node_A.get_right(), end=node_B.get_left())

        # Add labels
        label_A = Text("A").next_to(node_A, aligned_edge=(-3,0,0))
        label_B = Text("B").next_to(node_B, aligned_edge=(-3,0,0))
        label_AB = Text("AB").next_to(edge_AB, DOWN)

        # Add nodes and edge to the scene
        self.play(Create(node_A), Create(node_B), Create(edge_AB))
        self.play(Create(label_A), Create(label_B), Create(label_AB))

        # Wait for the animation to finish
        self.wait()

ConnectingNodes().render()