from manim import *





def create_cylinder(height=2, radius=2, stroke_width=4, color=GREEN, base_height=1.5):
    """
    Creates a cylinder object with the given dimensions and styling.

    Parameters:
    - height (float): The height of the cylinder.
    - radius (float): The radius of the cylinder.
    - stroke_width (float): The width of the cylinder's stroke.
    - color (str or hex): The color of the cylinder.
    - base_height (float): The height of the cylinder's base ellipse.

    Returns:
    - VGroup: The cylinder group containing two ellipses and two lines.
    """
    base_ellipse = Ellipse(width=radius*2, height=base_height, fill_opacity=0.2, color=color, stroke_width=stroke_width)
    top_ellipse = base_ellipse.copy().move_to([0, height, 0])
    base_line = Line([-radius, 0, 0], [-radius, height, 0], stroke_width=stroke_width).set_color(color)
    top_line = Line([radius, 0, 0], [radius, height, 0], stroke_width=stroke_width).set_color(color)
    cylinder_group = VGroup(base_ellipse, top_ellipse, base_line, top_line)
    return cylinder_group


class CylinderAnimation(Scene):
    def construct(self):
        # Introduction texts
        text1 = Text("Here we have a cylinder of radius 'r' and height 'h'", font_size=35)
        text2 = MarkupText(
            f'We can change its <span fgcolor="{GREEN}">height</span>',
            font_size=30
        ).move_to([2.5, 3.5, 0])

        # Value trackers and labels
        height_label = Text("h = ", color=GREEN).move_to([-6.5, 3.5, 0])
        radius_label = Text("r = ", color=GREEN).move_to([-6.5, 2.5, 0])

        height_tracker = ValueTracker(2)
        radius_tracker = ValueTracker(2)

        height_number = Text("2.0", color=GREEN).move_to([-5, 3.5, 0])
        radius_number = Text("2.0", color=GREEN).move_to([-5, 2.5, 0])

        # Create initial cylinder
        cylinder = create_cylinder().move_to([0, -1, 0])

        # Display the initial texts and cylinder
        self.play(Write(text1))
        self.wait(1)
        self.play(Transform(text1, cylinder))
        self.play(FadeIn(height_label, radius_label, height_number, radius_number))
        self.wait(0.5)
        self.play(Write(text2))
        self.wait(1)

        # Update height and cylinder based on the height tracker
        height_number.add_updater(
            lambda num: num.become(
                Text(str(round(height_tracker.get_value(), 3)), color=GREEN).move_to([-5, 3.5, 0])
            )
        )

        # Update radius and cylinder based on the radius tracker
        radius_number.add_updater(
            lambda num: num.become(
                Text(str(round(radius_tracker.get_value(), 3)), color=GREEN).move_to([-5, 2.5, 0])
            )
        )

        text1.add_updater(
            lambda cil: cil.become(
                create_cylinder(height=height_tracker.get_value(), radius=radius_tracker.get_value())
                .move_to([0, -1 + (height_tracker.get_value() - 2) / 2, 0])
            )
        )

        # Animate height changes
        self.play(ApplyMethod(height_tracker.set_value, 4, run_time=2))
        self.play(ApplyMethod(height_tracker.set_value, 0.5, run_time=2))
        self.play(ApplyMethod(height_tracker.set_value, 2, run_time=2))
        self.wait(0.5)

        # Update text2 for radius changes
        self.play(Transform(text2, MarkupText(
            f'We can also change its <span fgcolor="{GREEN}">radius</span>',
            font_size=30).move_to([2.5, 3.5, 0]))
        )
        self.wait(0.5)

        # Animate radius changes
        self.play(ApplyMethod(radius_tracker.set_value, 4, run_time=2))
        self.play(ApplyMethod(radius_tracker.set_value, 0.5, run_time=2))
        self.play(ApplyMethod(radius_tracker.set_value, 2, run_time=2))
        self.wait(0.5)

        # Clear updaters and fade out texts and labels
        height_number.clear_updaters()
        radius_number.clear_updaters()
        self.play(FadeOut(text2, height_label, radius_label, height_number, radius_number))

CylinderAnimation().render()

