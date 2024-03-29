from manim import *

class DefPolinomio(Scene):
    def construct(self):
        #rejilla  = NumberPlane()
        #self.add(rejilla)
        Emerald = "#00A99D"
        OrangeRed = "#ED135A"
        YellowOrange = "#FAA21A"
        texto1 = Text("Series de potencias y polinomios ").set_color_by_gradient(Emerald,WHITE)
        texto2 = Text("Series de potencias y polinomios").set_color_by_gradient(Emerald,WHITE).move_to(UP*2.95)
        texto2_b = Text("en varias variables").set_color_by_gradient(Emerald,WHITE).move_to(UP*2.25)
        self.play(Write(texto1))
        self.wait()
        self.play(Transform(texto1,texto2))
        self.play(Write(texto2_b))
        self.wait()
        texto3 = MathTex(r"\textit{Definición}").set_color(Emerald)
        texto4 = MathTex(r"\textit{Def:}").set_color(Emerald).move_to(UP *1.5+LEFT*5.5).scale(0.8)
        texto4_b = MathTex(r"R[[X]]=R\left[\left[\left(x_{i}\right)_{i \in I}\right]\right]").move_to(UP *1.5+LEFT*3).scale(0.6)
        texto5 = MathTex(r"X=\left\{x_{i} \mid i \in I\right\}")
        texto5_b = MathTex(r"X=\left\{x_{i} \mid i \in I\right\}").move_to(UP *1.5+RIGHT*4).scale(0.5)
        self.play(Write(texto3))
        self.wait()   
        self.play((Transform(texto3,texto4)))
        self.play(Write(texto4_b))
        self.wait()
        self.play(Write(texto5))
        self.wait(2)
        self.play((Transform(texto5,texto5_b)))
        eqn0 = MathTex(r"a_0", r"+\sum_{i \in I} a_{i} x_{i}", r"+\sum_{i, j \in I} a_{i j} {x}_{i} x_{j}",r"+\sum_{i, j, k \in I} a_{i j k} x_{i} x_{j} x_{k}",r"+ \ldots").scale(0.7)
        eqn0_peque = MathTex(r"a_0", r"+\sum_{i \in I} a_{i} x_{i}", r"+\sum_{i, j \in I} a_{i j} {x}_{i} x_{j}",r"+\sum_{i, j, k \in I} a_{i j k} x_{i} x_{j} x_{k}",r"+ \ldots").scale(0.5).move_to(UP*0.5)
        self.play(Write(eqn0[0]))
        self.wait(2)
        self.play(Write(eqn0[1]))
        self.wait(2)
        self.play(Write(eqn0[2]))
        self.wait(2)
        self.play(Write(eqn0[3]))
        self.wait(2)
        self.play(Write(eqn0[4]))
        self.wait(2)
        texto6 = MathTex("a_i,a_{i j}, a_{i j k}.\ldots \in R").move_to(DOWN * 2).scale(0.5)
        texto7 = MathTex(r"\textit{Cada suma que ocurre en la expresión tiene finitos coeficientes no nulos}").move_to(DOWN * 3).scale(0.6)
        self.play(Write(texto7))
        self.wait(2)
        self.play(Write(texto6))
        self.wait(5)
        self.play((Transform(eqn0,eqn0_peque)))
        secuencias = MathTex(r"\left(a_{0},\left(a_{i}\right)_{i \in I},\left(a_{i j}\right)_{i, j \in I},\left(a_{i j k}\right)_{i, j, k \in I}, \ldots\right)").move_to(DOWN*1).scale(0.8)
        self.play(Write(secuencias))
        self.wait(4)
        arrays = MathTex(r"\textit{Cada arreglo }\left(a_{i_{1} i_{2} \ldots i_{n}}\right)_{i_{1}, i_{2}, \ldots, i_{n} \in I} \textit{ tiene finitos miembros no nulos.}").move_to(DOWN * 3).scale(0.6)
        self.play(Transform(texto7,arrays))
        self.wait(8)

class operaciones(Scene):
    def construct(self):
        #rejilla  = NumberPlane()
        #self.add(rejilla)
        Emerald = "#00A99D"

        texto1 = MathTex(r"\textit{Operaciones en } R[[X]]").set_color_by_gradient(Emerald,WHITE)
        texto2 = MathTex(r"\textit{Operaciones en } R[[X]]").set_color_by_gradient(Emerald,WHITE).move_to(UP*3)
        self.play(Write(texto1))
        self.wait()
        self.play(Transform(texto1,texto2))
        self.wait()
        texto3 = MathTex(r"\textit{Adición}").set_color(Emerald)
        texto4 = MathTex(r"\textit{Def: + en }R[[X]]").set_color(Emerald).move_to(UP *2.1+LEFT*5).scale(0.8)
        eqn0 = MathTex(r"\begin{gathered} \left(a_{0},\left(a_{i}\right)_{i},\left(a_{i j}\right)_{i, j},\left(a_{i j k}\right)_{i, j, k}, \ldots\right)+\left(b_{0},\left(b_{i}\right)_{i},\left(b_{i j}\right)_{i, j},\left(b_{i j k}\right)_{i, j, k}, \ldots\right)= \\ \left(a_{0}+b_{0},\left(a_{i}+b_{i}\right)_{i},\left(a_{i j}+b_{i j}\right)_{i, j},\left(a_{i j k}+b_{i j k}\right)_{i, j, k}, \ldots\right)\end{gathered}").move_to(DOWN*0.5).scale(0.7)
        self.play(Write(texto3))
        self.wait(2)
        self.play(Transform(texto3,texto4))
        self.wait(4)
        self.play(Write(eqn0))
        self.wait(6)

        texto5 = MathTex(r"\textit{Multiplicación}").set_color(Emerald)
        texto6 = MathTex(r"\textit{Def: x en }R[[X]]").set_color(Emerald).move_to(UP *2.1+LEFT*5).scale(0.8)
        self.play(FadeOut(texto3))
        self.play(FadeOut(eqn0))

        eqn1 = MathTex(r"\begin{gathered} \left(a_{0},\left(a_{i}\right)_{i},\left(a_{i j}\right)_{i, j},\left(a_{i j k}\right)_{i, j, k}, \ldots\right) \cdot\left(b_{0},\left(b_{i}\right)_{i},\left(b_{i j}\right)_{i, j},\left(b_{i j k}\right)_{i, j, k}, \ldots\right)= \\ \left(a_{0} b_{0}, \sum_{i}\left(a_{0} b_{i}+a_{i} b_{0}\right), \sum_{i, j}\left(a_{0} b_{i j}+a_{i} b_{j}+a_{i j} b_{0}\right), \sum_{i, j, k}\left(a_{0} b_{i j k}+a_{i} b_{j k}+a_{i j} b_{k}+a_{i j k} b_{0}\right), \ldots\right)\end{gathered}").scale(0.7)
        
        self.play(Write(texto5))
        self.wait(2)
        self.play(Transform(texto5,texto6))
        self.wait(4)
        self.play(Write(eqn1))
        self.wait(6)
        arrays = MathTex(r"\begin{gathered} \textit{The set of all polynomials over } R \textit{ in the variables }\left(x_{i}\right)_{i \in I} \textit{ is denoted by } R\left[\left(x_{i}\right)_{i \in I}\right] \\ \textit{ and forms a subring of }R\left[\left[\left(x_{i}\right)_{i \in I}\right]\right] \end{gathered}").move_to(DOWN*3).scale(0.7)
        self.play(Write(arrays))
        self.wait(6)

# Grado, subgrado, monomios, polinomios homogéneos.
class grado(Scene):
    def construct(self):
        #rejilla  = NumberPlane()
        #self.add(rejilla)
        Emerald = "#00A99D"

        texto1 = MathTex(r"\textit{Monomios, grado  y polinomios homogéneos}").set_color_by_gradient(Emerald,WHITE)
        texto2 = MathTex(r"\textit{Monomios, grado  y polinomios homogéneos}").set_color_by_gradient(Emerald,WHITE).move_to(UP*3.5)
        self.play(Write(texto1))
        self.wait(4)
        self.play(Transform(texto1,texto2))
        self.wait()
        notacion = MathTex(r"\begin{gathered} \textit{Notación: Para }  i_{1}, \ldots, i_{n} \in \mathbb{N} \textit{ definimos un multi índice: } I = \left(i_{1}, \ldots, i_{n}\right)\\ \textit{ cuya longitud es: } |I| = i_1 \ldots i_n \textit{ y escribimos } x^I = x_1^{i_1} \ldots x_n^{i_n}\end{gathered}").move_to(UP*2.3).scale(0.7)
        self.play(Write(notacion))
        eqn0 = MathTex(r"\textit{Usando esta notación }f(x)=\sum_{I \in \mathbb{N}^{m}} a_{I} x^{I}\in R\left[x_{1}, \ldots, x_{n}\right]\textit{ sobre el anillo } R").move_to(UP*0.8).scale(0.7)
        self.play(Write(eqn0))
        self.wait(4)

        texto3 = MathTex(r"\textit{Monomio}").set_color(Emerald)
        texto4 = MathTex(r"\textit{Def: Monomio en }R[X]").set_color(Emerald).move_to(LEFT*5.2).scale(0.7)
        monomio = MathTex(r"\textit{Es un polinomio de la forma } x^{l}").move_to(DOWN*0.5).scale(0.7)
        self.play(Write(texto3))
        self.wait(2)
        self.play(Transform(texto3,texto4))
        self.wait(2)
        self.play(Write(monomio))
        self.wait(4)
        texto5 = MathTex(r"\textit{grado}").set_color(Emerald).move_to(DOWN*1)
        texto6 = MathTex(r"\textit{Def: Deg(f) en }R[X]").set_color(Emerald).move_to(DOWN*1+LEFT*5.4).scale(0.7)
        deg = MathTex(r"\textit{Sea }f\in R[X]\textit{, no nulo, el Deg}(f)\textit{ es el más grande multi índice I que ocurre en } f").move_to(DOWN*1.5).scale(0.7)
        self.play(Write(texto5))
        self.wait(2)
        self.play(Transform(texto5,texto6))
        self.wait(2)
        self.play(Write(deg))
        self.wait(2)
        texto7 = MathTex(r"\textit{subgrado}").set_color(Emerald).move_to(DOWN*2)
        texto8 = MathTex(r"\textit{Def: subdeg(f) en }R[X]").set_color(Emerald).move_to(DOWN*2+LEFT*5.2).scale(0.7)
        subdeg = MathTex(r"\textit{Sea }f\in R[X]\textit{, no nulo, el subeg}(f)\textit{ es el más pequeño multi índice I que ocurre en } f").move_to(DOWN*2.5).scale(0.7)
        self.play(Write(texto7))
        self.wait(2)
        self.play(Transform(texto7,texto8))
        self.wait(2)
        self.play(Write(subdeg))
        self.wait(2)
        texto9 = MathTex(r"\textit{Polinomios Homogeneos}").set_color(Emerald).move_to(DOWN*3)
        texto10 = MathTex(r"\textit{Def: f Homogeneo }R[X]").set_color(Emerald).move_to(DOWN*3+LEFT*5.2).scale(0.7)
        homogeneos = MathTex(r"f\in R[X]\textit{ es homogeneo si deg} (f) = \textit{subdeg}(f)").move_to(DOWN*3.5).scale(0.7)
        self.play(Write(texto9))
        self.wait(2)
        self.play(Transform(texto9,texto10))
        self.wait(2)
        self.play(Write(homogeneos))
        self.wait(6)



#Raíz, pol irreducible
class irreducibles(Scene):
    def construct(self):
        #rejilla  = NumberPlane()
        #self.add(rejilla)
        Emerald = "#00A99D"
        texto1 = MathTex(r"\textit{Raíces y polinomios irreducíbles}").set_color_by_gradient(Emerald,WHITE)
        texto2 = MathTex(r"\textit{Raíces y polinomios irreducíbles}").set_color_by_gradient(Emerald,WHITE).move_to(UP*3.5)
        self.play(Write(texto1))
        self.wait()
        self.play(Transform(texto1,texto2))
        self.wait()
        texto3 = MathTex(r"\textit{Raíz de un polinomio en varias variables}").set_color(Emerald)
        texto4 = MathTex(r"\textit{Def: Raíces en }R[X]").set_color(Emerald).move_to(UP *2.1+LEFT*5).scale(0.8)
        eqn0 = MathTex(r"\begin{gathered} \textit{Sea } R \textit{ un anillo conmutativo y }f \in R\left[x_{1}, \ldots, x_{n}\right], \textit{Si } f\left(r_{1}, \ldots, r_{n}\right)=0 \textit{ con } r_{1}, \ldots, r_{n} \in R, \\ \textit{ entonces } \left(r_{1}, \ldots, r_{n}\right) \textit{ se conoce como una raíz o cero de }f\end{gathered}").scale(0.7)
        eqn0_b = MathTex(r"\begin{gathered} \textit{Sea } R \textit{ un anillo conmutativo y }f \in R\left[x_{1}, \ldots, x_{n}\right], \textit{Si } f\left(r_{1}, \ldots, r_{n}\right)=0 \textit{ con } r_{1}, \ldots, r_{n} \in R, \\ \textit{ entonces } \left(r_{1}, \ldots, r_{n}\right) \textit{ se conoce como una raíz o cero de }f\end{gathered}").move_to(UP*1.2).scale(0.5)
        self.play(Write(texto3))
        self.wait(4)
        self.play(Transform(texto3,texto4))
        self.wait()
        self.play(Write(eqn0))
        self.wait(6)
        self.play(Transform(eqn0,eqn0_b))
        texto5 = MathTex(r"\textit{Def: Polinomio irreducible en }R[X], X ={x_1,\ldots,x_n}").set_color_by_gradient(Emerald,WHITE)
        texto6 = MathTex(r"\textit{Def: Polinomio irreducible en }R[X]").set_color_by_gradient(Emerald,WHITE).move_to(UP*0.5+LEFT*4).scale(0.8)
        self.play(Write(texto5))
        self.wait(4)
        self.play(Transform(texto5,texto6))
        self.wait()
        eqn1 = MathTex(r"\begin{gathered} f \in R[X] \textit{ es irreducible sobre }R \textit{ si no es constante} \\ \textit{ y no es producto de dos polinomios no constantes en }R[X] \end{gathered}").move_to(DOWN*0.5).scale(0.7)
        eqn1_b = MathTex(r"\begin{gathered} f \in R[X] \textit{ es irreducible sobre }R \textit{ si no es constante} \\ \textit{ y no es producto de dos polinomios no constantes en }R[X] \end{gathered}").move_to(DOWN*0.5).scale(0.5)
        self.play(Write(eqn1))
        self.wait(4)
        self.play(Transform(eqn1,eqn1_b))
        self.wait(4)

# Teorema del factor en 1 variable (recordemos)
        """
        Acá me falta recordar el teorema en 1 variable
        """
class teoremafactor(Scene):
    def construct(self):
        Emerald = "#00A99D"
        texto1 = MathTex(r"\begin{gathered}\textit{¿Se puede establecer un Teorema del factor } \\ \textit{en el caso de varias variables?}\end{gathered}").set_color_by_gradient(Emerald,WHITE)
        texto2 = MathTex(r"\textit{Teorema del factor}").set_color_by_gradient(Emerald,WHITE).move_to(UP*3.5)
        self.play(Write(texto1))
        self.wait()
        self.play(Transform(texto1,texto2))
        self.wait()
        texto3 = MathTex(r"\textit{Recordemos el teorema del factor en }R[x]").set_color(Emerald)
        texto4 = MathTex(r"\textit{Teorema del factor en }R[x]").set_color(Emerald).move_to(UP *2.1+LEFT*4).scale(0.8)
        eqn0 = MathTex(r"\begin{gathered} \textit{Sea } R \textit{ un anillo conmutativo y }f \in R[x], \textit{Si } f(r)=0 \textit{ con } r \in R, \\ \textit{ Entonces existe un polinomio }q \in R[x] \textit{ tal que } f = q(x-r) \end{gathered}").scale(0.7)
        eqn0_b = MathTex(r"\begin{gathered} \textit{Sea } R \textit{ un anillo conmutativo y }f \in R[x], \textit{Si } f(r)=0 \textit{ con } r \in R, \\ \textit{ Entonces existe un polinomio }q \in R[x] \textit{ tal que } f = q(x-r) \end{gathered}").move_to(UP*1.2).scale(0.5)
        self.play(Write(texto3))
        self.wait(2)
        self.play(Transform(texto3,texto4))
        self.wait(4)
        self.play(Write(eqn0))
        self.wait(6)
        self.play(Transform(eqn0,eqn0_b))
        texto5 = MathTex(r"\textit{Veamos si la demostración se puede llevar de }R[x] \textit{ a }R[X], X ={x_1,\ldots,x_n}").set_color_by_gradient(Emerald,WHITE)
        texto6 = MathTex(r"\textit{Pasos en la demostración: ").set_color_by_gradient(Emerald,WHITE).move_to(UP*0.5+LEFT*4).scale(0.8)
        self.play(Write(texto5))
        self.wait()
        self.play(Transform(texto5,texto6))
        self.wait()
        eqn1 = MathTex(r"\begin{gathered} \end{gathered}").move_to(DOWN*0.5).scale(0.7)
        eqn1_b = MathTex(r"\begin{gathered} \end{gathered}").move_to(DOWN*0.5).scale(0.5)
        self.play(Write(eqn1))
        self.wait(6)
        self.play(Transform(eqn1,eqn1_b))
        self.wait()


#Def: Acción del grupo simétrico, polinomios simétricos y sim elementales.
class polisimetricos(Scene):
    def construct(self):
        Emerald = "#00A99D"
        texto1 = MathTex(r"\textit{Polinomios simétricos y polinomios simétricos elementales}").set_color_by_gradient(Emerald,WHITE)
        texto2 = MathTex(r"\textit{Polinomios simétricos en } R[X] ").set_color_by_gradient(Emerald,WHITE).move_to(UP*3.5)
        self.play(Write(texto1))
        self.wait()
        self.play(Transform(texto1,texto2))
        self.wait()
        texto3 = MathTex(r"\textit{Acción del grupo }\operatorname{Sym}_n \textit{ sobre }R(X) \textit{ y sobre }R\left[X]").set_color(Emerald)
        texto4 = MathTex(r"\operatorname{Sym}_n \textit{ actua en }R[X] \textit{ vía }").set_color(Emerald).move_to(UP *2.5+LEFT*4).scale(0.8)
        eqn0 = MathTex(r"\begin{gathered} (\sigma \star f)\left(x_{1}, \ldots, x_{n}\right)=f\left(x_{\sigma^{-1}(1)}, \ldots, x_{\sigma^{-1}(n)}\right)\end{gathered}").scale(0.8)
        eqn0_b = MathTex(r"\begin{gathered} (\sigma \star f)\left(x_{1}, \ldots, x_{n}\right)=f\left(x_{\sigma^{-1}(1)}, \ldots, x_{\sigma^{-1}(n)}\right)\\ \textit{Luego un elemento }f \in R[X] \textit{ se dice simétrico si es invariante bajo esta acción.}\end{gathered}").move_to(UP*1.5).scale(0.7)        
        self.play(Write(texto3))
        self.wait(2)
        self.play(Transform(texto3,texto4))
        self.wait(4)
        self.play(Write(eqn0))
        self.wait(6)
        self.play(Transform(eqn0,eqn0_b))
        self.wait(6)
        texto5 = MathTex(r"\textit{Polinomios simétricos}").set_color(Emerald)
        texto6 = MathTex(r"\textit{Def: Un polinomio } f \in R[X] \textit{ se llama simétrico si } ").set_color(Emerald).move_to(UP *0.5+LEFT*1.8).scale(0.8)
        eqn1 = MathTex(r"\begin{gathered} f\left(x_{\sigma(1)}, \ldots, x_{\sigma(n)}\right)=f\left(x_{1}, \ldots, x_{n}\right) \text { para todas las permutaciones } \sigma \in \operatorname{Sym}_{n} \end{gathered}").move_to(DOWN*0.5).scale(0.7)
        eqn1_b = MathTex(r"\begin{gathered} f\left(x_{\sigma(1)}, \ldots, x_{\sigma(n)}\right)=f\left(x_{1}, \ldots, x_{n}\right) \text { para todas las permutaciones } \sigma \in \operatorname{Sym}_{n} \end{gathered}").move_to(DOWN*0.5).scale(0.7)
        self.play(Write(texto5))
        self.wait(2)
        self.play(Transform(texto5,texto6))
        self.wait(4)
        self.play(Write(eqn1))
        self.wait(6)
        self.play(Transform(eqn1,eqn1_b))
        self.wait(6)
        texto7 = MathTex(r"\begin{gathered} \textit{Def: polinomios elementales } s_{1}, \ldots, s_{n} \textit{ en n variables} \end{gathered}").set_color(Emerald).move_to(DOWN*1.5).scale(0.8)
        texto8 = MathTex(r"\textit{Def: polinomios elementales } s_{1}, \ldots, s_{n} \textit{ en n variables}  ").set_color(Emerald).move_to(DOWN*1.5).scale(0.8)
        subdeg = MathTex(r"\begin{gathered} s_{k}\left(x_{1}, \ldots, x_{n}\right)=\sum_{1 \leq i_{1}<\cdots<i_{k} \leq n} x_{i_{1}} \cdots x_{i_{k}} \end{gathered}").move_to(DOWN*2.6).scale(0.7)
        self.play(Write(texto7))
        self.wait(2)
        self.play(Transform(texto7,texto8))
        self.wait(2)
        self.play(Write(subdeg))
        self.wait(6)



class teoremasimetricos(Scene):
    def construct(self):
        Emerald = "#00A99D"
        texto1 = MathTex(r"\begin{gathered}\textit{Descomposición de polinomios simétricos} \\ \textit{en simétricos elementales de }R[X]\end{gathered}").set_color_by_gradient(Emerald,WHITE)
        texto2 = MathTex(r"\begin{gathered}\textit{Descomposición de polinomios simétricos} \\ \textit{en simétricos elementales de }R[X]\end{gathered}").set_color_by_gradient(Emerald,WHITE).move_to(UP*3.1)
        self.play(Write(texto1))
        self.wait(3)
        self.play(Transform(texto1,texto2))
        self.wait()
        self.play(FadeOut(texto2))
        self.play(FadeOut(texto1))
        texto3 = MathTex(r"\begin{gathered}\textit{Si }p \in R\left[x_{1}, \ldots, x_{n}\right] \textit{ es un polinomio simétrico, } \\ \textit{entonces existe un único polinomio } \varphi \in R\left[x_{1}, \ldots, x_{n}\right] \\ \textit{ tal que } p=\varphi\left(s_{1}, \ldots, s_{n}\right) \end{gathered}").set_color(Emerald)
        texto4 = MathTex(r"\begin{gathered}\textit{Teorema: Si }p \in R\left[x_{1}, \ldots, x_{n}\right] \textit{ es un polinomio simétrico, } \\ \textit{entonces existe un único polinomio } \varphi \in R\left[x_{1}, \ldots, x_{n}\right] \\ \textit{ tal que } p=\varphi\left(s_{1}, \ldots, s_{n}\right)\end{gathered} \\ \textit{Demostración:}").set_color(Emerald).move_to(UP *2.5).scale(0.8)
        eqn0 = MathTex(r"\begin{gathered}\textit{Existencia: Demostración por inducción en el orden lexicográfico de } p.\\ \textit{Sea }p \textit{ un polinomio simétrico con } \operatorname{lexdeg} p=\left(i_{1}, \ldots, i_{n}\right) \textit{, entonces }\\ i_{1} \geq i_{2} \geq \cdots \geq i_{n} \textit{ pues, luego podemos construir el polinomio simétrico: } \\ \begin{aligned} f &=s_{1}^{i_{1}-i_{2}} s_{2}^{i_{2}-i_{3}} \cdots s_{n-1}^{i_{n-1}-i_{n}} s_{n}^{i_{n}}\textit{, cuyo grado es: } \\ \operatorname{lexdeg} f & =\left(i_{1}-i_{2}\right) \operatorname{lexdeg} s_{1}+\left(i_{2}-i_{3}\right) \operatorname{lexdeg} s_{2}+\cdots+i_{n} \operatorname{lexdeg} s_{n} \\ & =\left(i_{1}-i_{2}, 0, \ldots, 0\right)+\left(i_{2}-i_{3}, i_{2}-i_{3}, \ldots, 0\right)+\cdots+\left(i_{n}, i_{n}, \ldots, i_{n}\right) \\ & =\left(i_{1}, i_{2}, \ldots, i_{n}\right)=\operatorname{lexdeg} p \end{aligned}\end{gathered}").move_to(DOWN*1).scale(0.7)        
        #acá falta el teorema que referencian.
        self.play(Write(texto3))
        self.wait(2)
        self.play(Transform(texto3,texto4))
        self.wait()
        self.play(Write(eqn0))
        self.wait(6)
        """
        texto5 = MathTex(r"\textit{Polinomios simétricos}").set_color(Emerald)
        texto6 = MathTex(r"\textit{Def: Un polinomio } f \in R[X] \textit{ se llama simétrico si } ").set_color(Emerald).move_to(UP *0.5+LEFT*1.8).scale(0.8)
        eqn1 = MathTex(r"\begin{gathered} f\left(x_{\sigma(1)}, \ldots, x_{\sigma(n)}\right)=f\left(x_{1}, \ldots, x_{n}\right) \text { para todas las permutaciones } \sigma \in \operatorname{Sym}_{n} \end{gathered}").move_to(DOWN*0.5).scale(0.7)
        eqn1_b = MathTex(r"\begin{gathered} f\left(x_{\sigma(1)}, \ldots, x_{\sigma(n)}\right)=f\left(x_{1}, \ldots, x_{n}\right) \text { para todas las permutaciones } \sigma \in \operatorname{Sym}_{n} \end{gathered}").move_to(DOWN*0.5).scale(0.7)
        
        self.play(Write(texto5))
        self.wait(2)
        self.play(Transform(texto5,texto6))
        self.wait(4)
        self.play(Write(eqn1))
        self.wait(6)
        self.play(Transform(eqn1,eqn1_b))
        self.wait(6)
        texto7 = MathTex(r"\begin{gathered} \textit{Def: polinomios elementales } s_{1}, \ldots, s_{n} \textit{ en n variables} \end{gathered}").set_color(Emerald).move_to(DOWN*1.5).scale(0.8)
        texto8 = MathTex(r"\textit{Def: polinomios elementales } s_{1}, \ldots, s_{n} \textit{ en n variables}  ").set_color(Emerald).move_to(DOWN*1.5).scale(0.8)
        subdeg = MathTex(r"\begin{gathered} s_{k}\left(x_{1}, \ldots, x_{n}\right)=\sum_{1 \leq i_{1}<\cdots<i_{k} \leq n} x_{i_{1}} \cdots x_{i_{k}} \end{gathered}").move_to(DOWN*2.6).scale(0.7)
        self.play(Write(texto7))
        self.wait(2)
        self.play(Transform(texto7,texto8))
        self.wait(2)
        self.play(Write(subdeg))
        self.wait(6)
        """



class ejemplo(Scene):
    def construct(self):
        texto1 = MathTex(r"\textit{Veamos un ejemplo}").set_color_by_gradient(Emerald,WHITE)


class discriminante(Scene):
    def construct(self):
        Emerald = "#00A99D"
        texto1 = MathTex(r"\textit{Discriminante en } R[X] ").set_color_by_gradient(Emerald,WHITE)
        texto2 = MathTex(r"\textit{Discriminante en } R[X] ").set_color_by_gradient(Emerald,WHITE).move_to(UP*3.5)
        self.play(Write(texto1))
        self.wait()
        self.play(Transform(texto1,texto2))
        self.wait()
        texto3 = MathTex(r"\textit{Discriminante de un polinomio en n variables}").set_color(Emerald)
        texto4 = MathTex(r"\textit{Def: }").set_color(Emerald).move_to(UP *2.5+LEFT*6).scale(0.8)
        eqn0 = MathTex(r"\begin{gathered} \textit{El polinomio }D\left(x_{1}, \ldots, x_{n}\right):=\prod_{1 \leq i<j \leq n}\left(x_{i}-x_{j}\right)^{2} \\ \textit{en }n \textit{ variables }x_1,\ldots,x_n \textit{ es el discriminante de }x_1,\ldots,x_n\end{gathered}").scale(0.7)
        eqn0_b = MathTex(r"\begin{gathered} D\left(x_{1}, \ldots, x_{n}\right):=\prod_{1 \leq i<j \leq n}\left(x_{i}-x_{j}\right)^{2} \\ \textit{en }n \textit{ variables }x_1,\ldots,x_n \textit{ es el discriminante de }x_1,\ldots,x_n\end{gathered}").move_to(UP*2).scale(0.5)
        self.play(Write(texto3))
        self.wait(2)
        self.play(Transform(texto3,texto4))
        self.wait(4)
        self.play(Write(eqn0))
        self.wait(6)
        self.play(Transform(eqn0,eqn0_b))
        self.wait(6)
        texto5 = MathTex(r"\textit{El discriminante es un polinomio simétrico}").set_color(Emerald)
        texto6 = MathTex(r"\textit{Discriminante como polinomio simétrico }").set_color(Emerald).move_to(UP *1+LEFT*3).scale(0.8)
        eqn1 = MathTex(r"\begin{gathered} \textit{El efecto de aplicar cualquier }\sigma \in \operatorname{Sym}_{n} \textit{ a } D   \textit{ es una premutación de los factores } \left(x_{i}-x_{j}\right)^{2} \\ \textit{ luego } D \textit{ es invariante bajo la acción de } \operatorname{Sym}_{n} \textit{ en X} \end{gathered}").move_to(DOWN*0.5).scale(0.7)
        eqn1_b = MathTex(r"\begin{gathered} \textit{El efecto de aplicar cualquier }\sigma \in \operatorname{Sym}_{n} \textit{ a } D   \textit{ es una premutación de los factores } \left(x_{i}-x_{j}\right)^{2} \\ \textit{ luego } D \textit{ es invariante bajo la acción de } \operatorname{Sym}_{n} \textit{ en X} \end{gathered}").scale(0.5)
        self.play(Write(texto5))
        self.wait(2)
        self.play(Transform(texto5,texto6))
        self.wait(4)
        self.play(Write(eqn1))
        self.wait(6)
        self.play(Transform(eqn1,eqn1_b))
        self.wait(6)
        texto7 = MathTex(r"\begin{gathered}\textit{Ejemplo: Discriminante de } x_1, x_2, x_3 \textit{ con } \sigma(x_1,x_2,x_3) = (x_2,x_3,x_1)\\ \textit{ permutación fija para ilustrar la acción del grupo }\operatorname{Sym}_3 \end{gathered}").set_color(Emerald).move_to(DOWN*1.5).scale(0.8)
        texto8 = MathTex(r"\textit{Ejemplo: Discriminante de } x_1, x_2, x_3 \textit{ con } \sigma(x_1,x_2,x_3) = (x_2,x_3,x_1)").set_color(Emerald).move_to(DOWN*1.5).scale(0.7)
        subdeg = MathTex(r"\begin{gathered} D(x_1, x_2, x_3) =\prod_{1 \leq i<j \leq 3}\left(x_{i}-x_{j}\right)^{2} = (x_1-x_2)^2(x_1-x_3)^2(x_2-x_3)^2\\ = (x_2-x_1)^2(x_3-x_1)^2(x_2-x_3)^2 = (x_2-x_3)^2(x_2-x_1)^2(x_3-x_1)^2 = D(x_2, x_3, x_1) =  D(\sigma(x_1, x_2, x_3)) \end{gathered}").move_to(DOWN*2.5).scale(0.6)
        self.play(Write(texto7))
        self.wait(2)
        self.play(Transform(texto7,texto8))
        self.wait(2)
        self.play(Write(subdeg))
        self.wait(6)



"""
Proposition. The discriminant is a symmetric polynomial.

Proof. The effect of applying any permutation 
$\sigma \in \operatorname{Sym}_{n}$ to $D$ 
is a mere per tation of the factors $\left(x_{i}-x_{j}\right)^{2}$;
 hence $\sigma \star D=D$ for all $\sigma \in \operatorname{Sym}_{n}$."""

class raizsincalcular(Scene):
    def construct(self):
        Emerald = "#00A99D"
        texto1 = MathTex(r"\textit{Discriminante para evaluar polinomios sin calcular raíces}").set_color_by_gradient(Emerald,WHITE)
        texto2 = MathTex(r"\textit{Discriminante para evaluar polinomios sin calcular raíces}").set_color_by_gradient(Emerald,WHITE).move_to(UP*3)
        self.play(Write(texto1))
        self.wait()
        self.play(Transform(texto1,texto2))
        self.wait(6)
        texto3 = MathTex(r"\begin{gathered} \textit{Evaluación de } f(x_1,x_2,x_3)= x_1^3(x_2+x_3)+x_2^3(x_1+x_3)+x_3^3(x_1+x_2) \\ \textit{en las raíces del polinomio } g(x) = x^3+5x^2-x+1 \end{gathered}").set_color(Emerald).scale(0.9)
        texto4 = MathTex(r"\begin{gathered} \textit{Ejemplo: } f(x_1,x_2,x_3)= x_1^3(x_2+x_3)+x_2^3(x_1+x_3)+x_3^3(x_1+x_2) \\ \textit{evaluado en las raíces de } g(x) = x^3+5x^2-x+1 \end{gathered}").set_color(Emerald).move_to(UP *2).scale(0.8)
        eqn0 = MathTex(r"\begin{gathered} eqn0 \end{gathered}").scale(0.7)
        eqn0_b = MathTex(r"\begin{gathered} eqn0_b \end{gathered}").scale(0.5)
        self.play(Write(texto3))
        self.wait(2)
        self.play(Transform(texto3,texto4))
        self.wait(4)
        self.play(Write(eqn0))
        self.wait(6)
        self.play(Transform(eqn0,eqn0_b))
        self.wait(6)