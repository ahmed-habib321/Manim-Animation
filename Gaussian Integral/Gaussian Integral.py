from manim import *

class GaussianIntegral(Scene):
    def construct(self):
        # Title
        title = Text("Gaussian Integral", font_size=48).to_corner(corner=UP)
        self.play(Write(title))

        # Display initial integral
        integral = MathTex(r"I = \int_{-\infty}^{\infty} e^{-x^2} dx")
        self.play(Write(integral))
        self.wait()
        
        # Square both sides
        sq_integral_a = MathTex(r"I^2 = \left(\int_{-\infty}^{\infty} e^{-x^2} dx\right)^2")
        self.play(Transform(integral, sq_integral_a))
        self.wait()
        
        
        # Separate the integrals
        sq_integral_b = MathTex(r"I^2 = \left(\int_{-\infty}^{\infty} e^{-x^2} dx\right)\left(\int_{-\infty}^{\infty} e^{-x^2} dx\right)")
        self.play(Transform(integral, sq_integral_b))
        self.wait()

        # Use different variables for the second integral
        sq_integral_c = MathTex(r"I^2 = \left(\int_{-\infty}^{\infty} e^{-x^2} dx\right)\left(\int_{-\infty}^{\infty} e^{-y^2} dy\right)")
        self.play(Transform(integral, sq_integral_c))
        self.wait()

        # Merge the integrals using double integral notation
        merged_integral = MathTex(r"I^2 = \int_{-\infty}^{\infty}\int_{-\infty}^{\infty} e^{-(x^2+y^2)} dxdy")
        self.play(Transform(integral, merged_integral))
        self.wait()

        # Display the Jacobian matrix
        jacobian = MathTex(r"J = \begin{bmatrix} \frac{\partial u_1}{\partial q_1} & \frac{\partial u_1}{\partial q_2} \\\frac{\partial u_2}{\partial q_1} & \frac{\partial u_2}{\partial q_2} \end{bmatrix}")
        jacobian.next_to(integral, DOWN)
        self.play(Create(jacobian))
        self.wait()

        # Replace the Jacobian matrix with the polar coordinate Jacobian
        polar_jacobian = MathTex(r"J = \begin{bmatrix} \cos\theta & -r\sin\theta \\ \sin\theta & r\cos\theta \end{bmatrix}")
        polar_jacobian.next_to(integral, DOWN)
        self.play(Transform(jacobian, polar_jacobian))
        self.wait()

        # Simplify the polar coordinate Jacobian
        polar_jacobian_result = MathTex(r"J = \begin{bmatrix} \cos\theta & -r\sin\theta \\ \sin\theta & r\cos\theta \end{bmatrix} = r")
        polar_jacobian_result.next_to(integral, DOWN)
        self.play(Transform(jacobian, polar_jacobian_result))
        self.wait()

        # Convert the integral to polar coordinates
        polar_integral = MathTex(r"I^2 = \int_{0}^{\infty}\int_{0}^{2\pi} e^{-(r^2)} rdrd\theta")
        self.play(Transform(integral, polar_integral))
        self.play(FadeOut(jacobian))
        self.wait()

        # Separate the polar integral
        polar_integral_1 = MathTex(r"I^2 = \int_{0}^{\infty}re^{-r^2}dr \int_{0}^{2\pi}d\theta")
        self.play(Transform(integral, polar_integral_1))
        self.wait()

        # Evaluate the first integral
        eva_polar_integral = MathTex(r"I^2 = -\frac{1}{2}\int_{0}^{\infty}-2re^{-r^2}dr \left[\theta\right]_{0}^{2\pi}")
        self.play(Transform(integral, eva_polar_integral))
        self.wait()

        # Evaluate the second integral
        eva_polar_integral_1 = MathTex(r"I^2 = -\frac{1}{2}\left[ e^{-r^2} \right]_{0}^{\infty} 2\pi")
        self.play(Transform(integral, eva_polar_integral_1))
        self.wait()

        # Simplify the expression
        eva_polar_integral_2 = MathTex(r"I^2 = -2\frac{1}{2}\left[ 0-1 \right] \pi")
        self.play(Transform(integral, eva_polar_integral_2))
        self.wait()

        # Simplify further to get the final result
        eva_polar_integral_3 = MathTex(r"I^2 = \pi")
        self.play(Transform(integral, eva_polar_integral_3))
        self.wait()

        # Take the square root to obtain the final result
        result = MathTex(r"I = \sqrt{\pi}")
        self.play(Transform(integral, result))
        self.wait()


# Render the scene
GaussianIntegral().render()