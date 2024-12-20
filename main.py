from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import SlideTransition

KV = '''
<MDFloatLayout>:
    md_bg_color: 0.73,0.75,0.72,1
<MDBoxLayout>:
    orientation: 'vertical'
    md_bg_color: 0.73,0.75,0.72,1
<Contenido@MDBoxLayout>:
    spacing: dp(10)
    size_hint_y: None
    height: self.minimum_height
<Texto@MDLabel>:
    size_hint_y: None
    padding: dp(10),0,dp(10),0
    height: self.texture_size[1]
<Imgcontent@Image>:
    size_hint_y: None
    height: dp(200)
<IndicacionR@Texto>:
    text: ''
    color: 'red'
    font_size: sp(23)
    halign: 'right'
<Separador@Widget>:
    size_hint_y: None
    height: dp(25)
<Titulo@Texto>:
    font_size: sp(30)
    color: 'purple'
<Subtitulo@Texto>:
    font_size: sp(25)
    padding: dp(10),dp(23),dp(10),0
ScreenManager:
    id: screen_manager
    Screen:
        name: 'opciones_calculadora'
        MDBoxLayout:
            ScrollView:
                MDList:
                    OneLineAvatarListItem:
                        text: 'Area'
                        on_release: app.cambio('areas')
                        IconLeftWidget:
                            icon: 'alpha-a-box'
                    OneLineAvatarListItem:
                        text: 'Volumen'
                        on_release: app.cambio('volumenes')
                        IconLeftWidget:
                            icon: "alpha-v-box"
                    OneLineAvatarListItem:
                        text: 'Matrices'
                        on_release: app.cambio('matrices')
                        IconLeftWidget:
                            icon: 'alpha-m-box'
                    OneLineAvatarListItem:
                        text: 'Vectores'
                        on_release: app.cambio('vectores')
                        IconLeftWidget:
                            icon: 'alpha-v-box'
    Screen:
        name: 'areas'
        MDFloatLayout:
            MDIconButton:
                icon: 'arrow-left-bold-circle-outline'
                pos_hint: {'left':1,'top': 1}
                on_press: app.regresar('opciones_calculadora')
            Image:
                source: "areas.jpg"
                size_hint: 1,1
                pos_hint: {'center_x': 0.5,'center_y': 0.5}
    Screen:
        name: 'volumenes'
        MDFloatLayout:
            MDIconButton:
                icon: 'arrow-left-bold-circle-outline'
                pos_hint: {'left':1,'top': 1}
                on_press: app.regresar('opciones_calculadora')
            FitImage:
                size_hint: None, None
                size: dp(380),dp(380)
                source: "volumenes.jpg"
                pos_hint: {'center_x': 0.5,'center_y': 0.5}
    Screen:
        name: 'matrices'
        MDBoxLayout:
            MDIconButton:
                icon: 'arrow-left-bold-circle-outline'
                on_press: app.regresar('opciones_calculadora')
            ScrollView:
                MDList:
                    OneLineListItem:
                        text: 'Suma y resta'
                        on_release: app.cambio('srmatriz')
                    OneLineListItem:
                        text: 'Multiplicación'
                        on_release: app.cambio('xmatriz')
                    OneLineListItem:
                        text: 'Sistemas de Ecuaciones'
                        on_release: app.cambio('ec_sys')
                    OneLineListItem:
                        text: 'Determinantes'
                        on_release: app.cambio('determinantes')
                    OneLineListItem:
                        text: 'Inversa por Adjunta'
                        on_release: app.cambio('inversa')
    Screen:
        name: 'srmatriz'
        MDBoxLayout:
            Contenido:
                MDIconButton:
                    icon: 'arrow-left-bold-circle-outline'
                    on_press: app.regresar('matrices')
            ScrollView:
                Contenido:
                    Titulo:
                        text: 'Suma y Resta'
                    Texto:
                        text: "Para la suma y la resta se debe cumplir que tengan el mismo tamaño. Es decir, la misma cantidad de filas y columnas. Y se suma o resta directamente con el elemento que esté en la misma posición, así:"
                        halign: 'left'
                    Imgcontent:
                        source: 'sumamatriz.png'
                    Texto:
                        text: 'Nota: Si es sumando, revisar los signos'
                        font_size: sp(15)
                        color: 'red'
    Screen:
        name: 'xmatriz'
        MDBoxLayout:
            Contenido:
                MDIconButton:
                    icon: 'arrow-left-bold-circle-outline'
                    on_press: app.regresar('matrices')
            ScrollView:
                Contenido:
                    Titulo:
                        text: 'Multiplicación'
                    Texto:
                        text: "El tamaño de cualquier matriz se representa como (filas x columnas). Para multiplicar 2 matrices, se necesita que el numero de columnas de la matriz 1 sea igual al numero de filas de la matriz 2. Como en el siguiente ejemplo, donde se multiplica una matriz 3x2 con una 2x1."
                    Imgcontent:
                        source: 'multmatriz.png'
    Screen:
        name: 'ec_sys'
        MDBoxLayout:
            Contenido:
                MDIconButton:
                    icon: 'arrow-left-bold-circle-outline'
                    on_press: app.regresar('matrices')
            MDScrollView:
                Contenido:
                    Titulo:
                        text: 'Sistemas de ecuaciones'
                    Texto:
                        text: "Para resolver sistemas de ecuaciones, siempre se repite el mismo procedimiento:"
                    Subtitulo:
                        text: '1. Organizar'
                    Texto:
                        text: 'Se organizan todas las ecuaciones como una matriz. Cada Ecuación es una fila en la matriz, ordenada con cada columna con la misma variable (columna 1 con las "x", col 2 con las "y", etc). Se usan solo los coeficientes (El numero que acompaña la letra) con su signo:'
                    Imgcontent:
                        source: 'ec_sys_1.png'
                    Subtitulo:
                        text: '2. Dividir'
                    Texto:
                        text: 'Se divide toda la primera fila (primera ecuación) por el primer numero que hay en ella, en este caso, por -3. Esto nos dejará con un 1 como primer numero, lo que facilitará el siguiente paso.'
                    Imgcontent:
                        source: 'ec_sys_2.png'
                    Subtitulo:
                        text: '3. Buscar el 0'
                    Texto:
                        text: 'Buscamos convertir los primeros numeros de las otras filas (las que no dividimos), en un 0. Esto se hace buscando un numero que sumado o restado al que vamos a volver 0, da 0.'
                    Imgcontent:
                        source: 'ec_sys_3.png'
                    Texto:
                        text: 'Una vez encontrado el numero, aplicamos la siguiente formula en las filas que no dividimos:'
                    Imgcontent:
                        source:'ec_sys_4.png'
                    Subtitulo:
                        text: '4. Repetir'
                    Texto:
                        text: 'Se repite el proceso cambiando de fila. Ahora, se dividirá toda la fila 2 por el segundo numero (en este caso -5/3). Pero esta vez, se busca el numero que haga 0 solo la fila 3, ya no la fila 1. Al final se aplica la misma formula y se despeja.'
                    Texto:
                        text: 'El procedimiento de lo anteriormente dicho, sería:'
                    Imgcontent:
                        source: 'ec_sys_5.png'
                    Imgcontent:
                        source: 'ec_sys_6.png'
                    Imgcontent:
                        source: 'ec_sys_7.png'
                    Texto:
                        text: 'Tal como se halla el valor de "Z", ahora se halla el de "Y", utilizando la segunda fila de la matriz. Por último se hallaría "X", utilizando los valores de "Y" y "Z" en la primera fila de la matriz.'
                    Texto:
                        text: 'Para un sistema de ecuación 2x2, se habría despejado en vez de dividir la fila 2 (primera imagen del punto 4). Si es más grande el sistema, se continua hasta llegar al despeje.'
                    Separador:
    Screen:
        name: 'determinantes'
        MDBoxLayout:
            Contenido:
                orientation: 'horizontal'
                MDIconButton:
                    icon: 'arrow-left-bold-circle-outline'
                    on_press: app.regresar('matrices')
            ScrollView:
                Contenido:
                    Titulo:
                        text: 'Determinantes'
                    Texto:
                        text: 'El resultado de un determinante es un numero. Para hallar un determinante se necesita que la matriz tenga el mismo numero de filas y columnas (Ejemplo: 2x2, 3x3, 4x4).'
                    Subtitulo:
                        text: 'Determinante 2x2'
                    Texto:
                        text: 'Es el más sencillo. Se multiplica en diagonal, primero desde la parte superior izquierda y se resta con la multiplicación diagonal contraria, como se muestra en la imágen:'
                    Imgcontent:
                        source: 'det_1.png'
                    Texto:
                        text: 'Siempre se resuelve así, se multiplica la flecha roja y se resta la multiplicación de la azul.'
                    Subtitulo:
                        text: 'Determinantes > 2x2'
                    Texto:
                        text: 'Para las matrices de 3x3 en adelante, existen varios metodos para hallar su determinante. Sin embargo, el metodo recomendado por su utilidad en otros temas es el siguiente:'
                    Subtitulo:
                        text: '1. Organizar'
                        font_size: sp(23)
                    Texto:
                        text: 'Utilizaremos los numeros de la primera fila como se muestra en la imagen (los numeros -3, 5, -7). Empezaremos con el primer numero (-3) multiplicandolo por una matriz 2x2 conformada por los numeros que no compartan fila ni columna con él, como se ve en la imagen 2.'
                    Imgcontent:
                        source: 'det_2.png'
                    Imgcontent:
                        source: 'det_3.png'
                    Texto:
                        text: 'Lo que está encerrado en ROJO, no se usa pues comparte fila o columna con el primer numero de la fila 1 (-3). Mientras que lo encerrado en verde es lo que sobra, lo que no comparte, con ello se arma una matriz 2x2 y se multiplica por el numero que estamos evitando (-3)'
                        padding: dp(10),dp(30),dp(10),0
                    Texto:
                        text: 'Ahora se hace el mismo procedimiento pero con el segundo numero (en este caso, 5) y finalmente con el tercero (-7). Si la matriz es más grande, se continua hasta terminar con los numeros de la primer fila. Por cada matriz 2x2 se intercala entre positivo y negativo. La primera matriz (imagen anterior) quedó como -3 pues (+)(-) = (-) . Al ser la primera matriz, se mulriplica por +, la segunda será por - y se repite hasta terminar, como en la imagen:'
                    Imgcontent:
                        source:'det_4.png'
                    Texto:
                        text: '2. Resolver'
                        font_size: sp(23)
                    Texto:
                        text: 'Se resuelven los determinantes (como 2x2), se multiplican por el numero que tienen adelante y se suman o restan correspondientemente:'
                    Imgcontent:
                        source: 'det_5.png'
                    Separador:
    Screen:
        name: 'inversa'
        MDBoxLayout:
            Contenido:
                MDIconButton:
                    icon: 'arrow-left-bold-circle-outline'
                    on_press: app.regresar('matrices')
            ScrollView:
                Contenido:
                    Titulo:
                        text: 'Matriz Inversa (Adj)'
                    Texto:
                        text: 'Existen principalmente 2 metodos para calcular la matriz inversa, pero el metodo de la adjunta es más sencillo aunque más largo. La matriz inversa solo se puede calcular de una matriz que tenga el mismo numero de filas que de columnas (matrices 2x2, 3x3, etc).'
                    Subtitulo:
                        text: '1. Determinante'
                    Texto:
                        text: 'Lo primero es hallar el determinante de la matriz, se utilizará para el último punto'
                    Subtitulo:
                        text: '2. Cofactores'
                    Texto:
                        text: 'Los cofactores se hallan de una manera parecida a un determinante de matrices 3x3 y mayores. Se toman matrices 2x2, sin multiplicarse por el numero que ignoramos (vease determinantes), pero no nos limitamos a la fila 1, sino por cada una de las filas y los numeros en ellas. Por lo tanto, la cantidad de cofactores será igual a la cantidad de elementos en la matriz:'
                    Imgcontent:
                        source: 'cof_1.png'
                    Texto:
                        text: 'Cada cofactor se saca como las matrices 2x2 en determinantes, tomando los numeros que no comparten fila ni columna con el numero que estamos ignorando (en el Cofactor 1 es el 0, en el Cofactor 2 el -1 y en el 3 el 3). Se intercalan signos entre positivo y negativo.'
                    Texto:
                        text: 'Una forma fácil de verlo, es que los cofactores pares se multiplicarán por (-), como sucede en el Cofactor 2 en la imagen anterior, y pasará en los cofactores 4, 6 y 8.'
                    Imgcontent:
                        source: 'cof_2.png'
                    Imgcontent:
                        source: 'cof_3.png'
                    Subtitulo:
                        text: '3. Organizar'
                    Texto:
                        text: 'Ahora, se organiza una matriz conformada por los cofactores, en el mismo orden y posición en que fueron hallados.'
                    Imgcontent:
                        source: 'cof_4.png'
                    Texto:
                        text: 'Ya teniendo la matriz, ahora convertimos las columnas en filas y filas en columnas, de la siguiente manera:'
                    Imgcontent:
                        source: 'cof_5.png'
                    Subtitulo:
                        text: '4. Añadir determinante'
                    Texto:
                        text: 'Multiplicamos la matriz resultante por 1/determinante, finalizando con la matriz inversa:'
                    Imgcontent:
                        source: 'cof_6.png'
                    Separador:
    Screen:
        name: 'vectores'
        MDBoxLayout:
            Contenido:
                orientation: 'horizontal'
                MDIconButton:
                    icon: 'arrow-left-bold-circle-outline'
                    on_press: app.regresar('opciones_calculadora')
                Texto:
                    text: 'Aquí arriba se indicará por c/u si aplica para R2 y/o R3'
                    color: 'red'
            ScrollView:
                MDList:
                    OneLineListItem:
                        text: 'Introducción'
                        on_release: app.cambio('intvectores')
                    OneLineListItem:
                        text: 'Magnitud, dirección sentido'
                        on_release: app.cambio('m-d-s-vector')
                    OneLineListItem:
                        text: 'Suma y resta de vectores'
                        on_release: app.cambio('srvectores')
                    OneLineListItem:
                        text: 'Grafica de suma y resta'
                        on_release: app.cambio('grafica_vector')
                    OneLineListItem:
                        text: 'Vector Unitario'
                        on_release: app.cambio('vUnitario')
                    OneLineListItem:
                        text: 'Producto Punto/Escalar'
                        on_release: app.cambio('producto.')
                    OneLineListItem:
                        text: 'Ángulo entre vectores'
                        on_release: app.cambio('angulo_2_v')
                    OneLineListItem:
                        text: 'Proyección'
                        on_release: app.cambio('proyeccion_v')
                    OneLineListItem:
                        text: 'R³'
                        on_release: app.cambio('r3')
    Screen:
        name: 'r3'
        MDBoxLayout:
            Contenido:
                orientation: 'horizontal'
                MDIconButton:
                    icon: 'arrow-left-bold-circle-outline'
                    on_press: app.regresar('vectores')
                IndicacionR:
                    text: 'Solo aplican para R3'
            ScrollView:
                MDList:
                    OneLineListItem:
                        text: 'Cosenos Directores'
                        on_release: app.cambio('cosenosdirectores')
                    OneLineListItem:
                        text: 'Producto cruz'
                        on_release: app.cambio('Producto Cruz')
                    OneLineListItem:
                        text: 'Areas y Volumen'
                        on_release: app.cambio('areas_vectores')
                    OneLineListItem:
                        text: 'Ecuaciones'
                        on_release: app.cambio('ecuaciones_v')
                    OneLineListItem:
                        text: 'Ecuación del plano'
                        on_release: app.cambio('ec_plano')
    Screen:
        name: 'intvectores'
        MDBoxLayout:
            Contenido:
                orientation: 'horizontal'
                MDIconButton:
                    icon: 'arrow-left-bold-circle-outline'
                    on_press: app.regresar('vectores')
                IndicacionR:
                    text: 'R2 y R3'
            ScrollView:
                Contenido:
                    Titulo:
                        text: 'Introducción'
                    Texto:
                        text: 'Un vector en R2 (dos dimensiones) tiene 2 coordenadas, "x" y "y", expresadas como "i" y "j". En R3 contiene una más llamada "k". Estas componentes indican hacia donde va el vector, generalmente no se dice desde dónde empieza, por lo que se toma desde el origen.'
                    Texto:
                        text: 'En otras palabras, un vector v = 2i + 7j, es un vector que va desde el origen del plano (Punto (0,0)) hasta el punto (2,7). Sin embargo, también se pueden formar vectores que van de un punto en especifico a otro. Formemos el vector que va desde P(1,6) hasta Q(3,-2):'
                    Imgcontent:
                        source: 'v1.png'
                    Texto:
                        text: 'La formula es "Coordenada final menos Coordenada inicial", por cada componente ("X","Y",etc), al ser un vector en R2, solo tiene componente o coordenada en "X" y "Y". Al formar el vector PQ, indica que el inicio es el punto P y el final el punto Q. También es posible formar un vector QP, que sería distinto al vector PQ, ya es opcional cuál formar, no tiene consecuencia.'
                        padding: dp(10),dp(10),dp(10),0
                    Texto:
                        text: 'Un vector debe tener al menos una componente, por ejemplo el vector a = -3j. El vector valdría 0 en i y -3 en j. De igual manera puede pasar en R3, como a = 7k. Es un vector en R3, pues contiene k (Coordenada en "Z") y valdría 0 en i, 0 en j y 7 en k'
                    Separador:
    Screen:
        name: 'm-d-s-vector'
        MDBoxLayout:
            Contenido:
                orientation: 'horizontal'
                MDIconButton:
                    icon: 'arrow-left-bold-circle-outline'
                    on_release: app.regresar('vectores')
                IndicacionR:
                    text: 'R2'
            ScrollView:
                Contenido:
                    Titulo:
                        text: 'Magnitud (R2 y R3)'
                    Texto:
                        text: 'La magnitud de un vector es su longitud o su medida. Esta se representa con el nombre del vector en valor abs. La magnitud nos puede servir para hallar la distancia entre 2 puntos. Siempre se calcula con la siguiente formula:'
                    Imgcontent:
                        source: 'v2.png'
                    Texto:
                        text: 'Veamos lo en un ejemplo:'
                    Imgcontent:
                        source: 'v3.png'
                    Texto:
                        text: 'En este caso no hay "k", por lo que vale 0.'
                    Titulo:
                        text: 'Dirección y Sentido'
                        padding: dp(10),dp(30),dp(10),0
                    Texto:
                        text: 'En palabras simples, la dirección es el ángulo (siempre positivo) del vector con respecto al eje "X", y el sentido indica el cuadrante donde está, se indica sumando o restando al ángulo de la dirección. La dirección se calcula:'
                    Imgcontent:
                        source: 'v4.png'
                    Texto:
                        text: 'Ambos refieren a lo mismo, lo que hay en la coordenada "Y" o en j en el vector, sobre la coordenada "X" o i en el vector. Esto nos dará la dirección.'
                    Texto:
                        text: 'Para añadir el sentido hay que ubicar el Cuadrante donde se ubica el vector. Para hallar lo podemos comprobar lo siguiente:'
                    Imgcontent:
                        source: 'v5.png'
                    Texto:
                        text: '"X" y "Y" se pueden referir también a los componentes i y j del vector. Por ejemplo, el vector b = 4i - 2j, está en cuadrante IV, pues i es un número positivo y j es negativo.'
                    Texto:
                        text: 'Para los cuadrantes I y IV, no se hace añade nada al ángulo de la dirección, ese mismo ya es la dirección y el sentido.'
                    Texto:
                        text: 'Para el cuadrante II, se suma 180°, dejando el ángulo positivo entre 180° y -180°. Para el cuadrante III, se resta 180°, dejando un ángulo entre 180° y -180°'
                    Separador:
    Screen:
        name: 'srvectores'
        MDBoxLayout:
            Contenido:
                orientation: 'horizontal'
                MDIconButton:
                    icon: 'arrow-left-bold-circle-outline'
                    on_release: app.regresar('vectores')
                IndicacionR:
                    text: 'R2 y R3'
            ScrollView:
                Contenido:
                    Titulo:
                        text: 'Suma y Resta'
                    Texto:
                        text: 'La suma entre dos vectores se hace como si fueran variable, se suman las componentes de i entre sí y las compenentes de j entre sí.'
                    Imgcontent:
                        source: 'v6.png'
                    Texto:
                        text: 'La resta tiene 3 formas, siempre se cambiarán los signos según lo indicado y se resuelve como una suma:'
                    Imgcontent:
                        source: 'v7.png'
                    Imgcontent:
                        source: 'v8.png'
                    Texto:
                        text: 'La ultima forma sería con ambos vectores en negativo, eso es todo.'
                    Separador:
    Screen:
        name: 'grafica_vector'
        MDBoxLayout:
            Contenido:
                orientation: 'horizontal'
                MDIconButton:
                    icon: 'arrow-left-bold-circle-outline'
                    on_release: app.regresar('vectores')
                IndicacionR:
                    text: 'R2 y R3'
            ScrollView:
                Contenido:
                    Titulo:
                        text: 'Grafica'
                    Texto:
                        text: 'Lo mejor es resolver la suma y/o resta de vectores algebraicamente antes de graficarlo, para comprobar el resultado y cambiar los signos que sean necesarios. Los pasos para graficar son:'
                    Subtitulo:
                        text: '1. Primer vector'
                    Texto:
                        text: 'Se grafica el primer vector (ejemplo, si es v + a, se grafica el vector "v") desde el origen (0,0) hasta las coordenadas de sus componentes, por ejemplo:'
                    Imgcontent:
                        source: 'grafica_v1.png'
                    Subtitulo:
                        text: '2. Segundo vector'
                    Texto:
                        text: 'Se grafica el segundo vector desde el punto donde terminó el anterior'
                    Imgcontent:
                        source: 'grafica_v2.png'
                    Subtitulo:
                        text: 'Resultado'
                    Texto:
                        text: 'En caso de haber más vectores en la suma/resta, se continua hasta terminar de graficar los vectores. Una vez terminado, el resultado será un vector desde el origen (0,0) hasta el último punto donde llegó la grafica del último vector'
                    Imgcontent:
                        source: 'grafica_v3.png'
                    Separador:
    Screen:
        name: 'vUnitario'
        MDBoxLayout:
            Contenido:
                orientation: 'horizontal'
                MDIconButton:
                    icon: 'arrow-left-bold-circle-outline'
                    on_release: app.regresar('vectores')
                IndicacionR:
                    text: 'R2 y R3'
            ScrollView:
                Contenido:
                    Titulo:
                        text: 'Vector Unitario'
                    Texto:
                        text: 'Todos lo vectores tienen su vector unitario (si no lo tiene, no es un vector). Otra ley es que el vector unitario siempre debe tener una magnitud = 1. Existen 2 maneras de hallar el vector unitario:'
                    Subtitulo:
                        text: '1. Formula normal'
                    Texto:
                        text: 'Esta formula es la usual para calcular el vector unitario:'
                    Imgcontent:
                        source: 'vu1.png'
                    Texto:
                        text: 'Por ejemplo:'
                        padding: dp(10),dp(20),dp(10),0
                    Imgcontent:
                        source: 'vu2.png'
                    Subtitulo:
                        text: '2. Por ángulo (R3 por cosenos)'
                    Texto:
                        text: 'Se requiere calcular el ángulo (por Dirección y Sentido) del vector para hallar el vector unitario de la siguiente manera:'
                    Imgcontent:
                        source: 'vu3.png'
                    Texto:
                        text: 'Se calcula el coseno y seno del ángulo (es el mismo ángulo para ambas operaciones) y se usa como ese decimal (sea positivo o negativo)'
                    Separador:
    Screen:
        name: 'producto.'
        MDBoxLayout:
            Contenido:
                orientation: 'horizontal'
                MDIconButton:
                    icon: 'arrow-left-bold-circle-outline'
                    on_release: app.regresar('vectores')
                IndicacionR:
                    text: 'R2 y R3'
            ScrollView:
                Contenido:
                    Titulo:
                        text: 'Producto Punto'
                    Texto:
                        text: 'Es la "multiplicación" entre 2 vectores. También es llamado producto escalar, pues el resultado de esta operación siempre será un solo número. Se realiza de la siguiente manera:'
                    Imgcontent:
                        source: 'productop.png'
    Screen:
        name: 'angulo_2_v'
        MDBoxLayout:
            Contenido:
                orientation: 'horizontal'
                MDIconButton:
                    icon: 'arrow-left-bold-circle-outline'
                    on_release: app.regresar('vectores')
                IndicacionR:
                    text: 'R2 y R3'
            ScrollView:
                Contenido:
                    Titulo:
                        text: 'Ángulo entre V'
                    Texto:
                        text: 'Solo se puede calcular entre 2 vectores, no más. Siempre se utiliza la misma formula:'
                    Imgcontent:
                        source: 'angulo_2_v1.png'
                    Texto:
                        text: 'La formula indica que hay que calcular el producto punto entre los vectores y dividirlo entre la multiplicación de las dos magnitudes (el de cada vector)'
                    Texto:
                        text: 'Eso da el resultado del coseno del ángulo, pero necesitamos es el ángulo. Por lo que se puede despejar así:'
                    Imgcontent:
                        source: 'angulo_2_v2.png'
                    Texto:
                        text: 'Siempre debe calcularse el arccoseno.'
                    Separador:
    Screen:
        name: 'proyeccion_v'
        MDBoxLayout:
            Contenido:
                orientation: 'horizontal'
                MDIconButton:
                    icon: 'arrow-left-bold-circle-outline'
                    on_release: app.regresar('vectores')
                IndicacionR:
                    text: 'R2 y R3'
            ScrollView:
                Contenido:
                    Titulo:
                        text: 'Proyecciones'
                    Texto:
                        text: 'La proyección de un vector sobre otro, se calcula así:'
                    Imgcontent:
                        source: 'proy1.png'
                    Texto:
                        text: 'Tener en cuenta, la proyección de v sobre u no es igual a la proyección de u sobre v'
                        color: 'red'
                    Texto:
                        text: 'No sé de qué sirva, pero dejo este dato:'
                    Imgcontent:
                        source: 'proy2.png'
                    Texto:
                        text: 'Un ejemplo de proyección:'
                    Imgcontent:
                        source: 'proy3.png'
                    Subtitulo:
                        text: 'Vector W'
                    Texto:
                        text: 'El vector "W" es un vector perpendicular a la proyección y llega al otro vector de la proyección. Este sirve para calcular la distancia más corta entre ambos vectores (hallando |W|). "W" se calcula:'
                    Imgcontent:
                        source: 'proy4.png'
                    Texto:
                        text: 'O, también se puede decir que es U - la proyección.'
                    Separador:
    Screen:
        name: 'cosenosdirectores'
        MDBoxLayout:
            Contenido:
                MDIconButton:
                    icon: 'arrow-left-bold-circle-outline'
                    on_release: app.regresar('r3')
            ScrollView:
                Contenido:
                    Titulo:
                        text: 'Cosenos Directores'
                    Texto:
                        text: 'Siendo un vector en R3, tiene 3 ángulo, uno por cada eje. Estos ángulos son llamados Cosenos Directores, y se calculan de la siguiente forma:'
                    Imgcontent:
                        source: 'cosd1.png'
                    Texto:
                        text: 'Con los cosenos directores también es posible armar el vector unitario, como se especificó en R2'
    Screen:
        name: 'Producto Cruz'
        MDBoxLayout:
            Contenido:
                MDIconButton:
                    icon: 'arrow-left-bold-circle-outline'
                    on_release: app.regresar('r3')
            ScrollView:
                Contenido:
                    Titulo:
                        text: 'Producto Cruz'
                    Texto:
                        text: 'El producto Cruz se calcula como un determinante 3x3, de la misma manera, sigue los mismos pasos. Veamos un ejemplo resuelto:'
                    Imgcontent:
                        source: 'pcruz1.png'
                    Texto:
                        text: 'El producto cruz da como resultado un vector, que suele ser llamado "w", en este caso, resolviendo, sería:'
                    Imgcontent:
                        source: 'pcruz2.png'
                    Texto:
                        text: 'El producto cruz da como resultad un vector que es ortogonal (perpendicular) a los otros 2 vectores.'
                    Separador:
    Screen:
        name: 'areas_vectores'
        MDBoxLayout:
            Contenido:
                MDIconButton:
                    icon: 'arrow-left-bold-circle-outline'
                    on_release: app.regresar('r3')
            ScrollView:
                Contenido:
                    Titulo:
                        text: 'Aréa Paralelogramo'
                    Imgcontent:
                        source: 'a_paralelogramo.png'
                    Titulo:
                        text: 'Altura Paralelepípedo'
                    Imgcontent:
                        source: 'h_prllppd.png'
                    Titulo:
                        text: 'Volumen Paralelepípedo'
                    Imgcontent:
                        source: 'vol_prllppd.png'
                    Separador:
    Screen:
        name: 'ecuaciones_v'
        MDBoxLayout:
            Contenido:
                MDIconButton:
                    icon: 'arrow-left-bold-circle-outline'
                    on_release: app.regresar('r3')
            ScrollView:
                Contenido:
                    Titulo:
                        text: 'Ecuacion Vectorial'
                    Imgcontent:
                        source: 'ec_v.png'
                    Texto:
                        text: 'ni 0R ni t se reemplazan, solo 0P y el vector V. 0P será un vector desde el origen (0,0) hasta el punto P. Mientras que el vector V será un vector conformado por el vector P y otro Punto (para saber cómo se hace, vease la introducción)'
                    Titulo:
                        text: 'Ecuaciones Paramétricas'
                        padding: dp(10),dp(20),dp(10),0
                    Texto:
                        text: 'Las ecuaciones paramétricas se pueden representar, por así decirlo, de dos maneras:'
                    Imgcontent:
                        source: 'ec_p1.png'
                    Texto:
                        text: 'La primera forma es la de arriba, una sola ecuación que representa las 3 paramétricas (x,y,z). Y en la parte de abajo, están separadas por cada letra.'
                    Texto:
                        text: 'Las letras (x,y,z) no se reemplazan. P1,2 y 3 refieren a las coordenadas (x,y,z) de un punto dado. Mientras que (i,j,k), refieren a las compenentes del vector "V" (El vector V se calcula como en la Ecuación Vectorial).'
                    Texto:
                        text: 'Veamos un ejemplo de ecuaciones paramétricas.'
                    Imgcontent:
                        source: 'ec_p2.png'
                    Texto:
                        text: 'En caso de ser 0 una de las componentes del vector, no se pondría el parametro "t" en la forma separada. Esto es importante para la siguiente Ecuación.'
                    Titulo:
                        text: 'Ecuación Simétrica'
                        padding: dp(10),dp(20),dp(10),0
                    Texto:
                        text: 'Esta ecuación puede hallarse despejando el parámetro "t" de las ecuaciones paramétricas, y luego igualando las 3 ecuaciones. O la forma normal de hallarla es:'
                    Imgcontent:
                        source: 'ec_sim1.png'
                    Texto:
                        text: 'P1, 2 y 3 son las coordenadas de un punto dado, (i,j,k) son las componentes del vector V. Igualmente, las letras (x,y,z) no se reemplazan'
                    Texto:
                        text: 'En caso que una de las componentes del vector V sea 0 (en el siguiente ejemplo será k), se pone de la siguiente manera:'
                    Imgcontent:
                        source: 'ec_sim2.png'
                    Texto:
                        text: 'Sea (i,j o k) = 0, se separará esa componente con un ";" y se igualará a la coordenada del Punto que le corresponde.'
                    Separador:
    Screen:
        name: 'ec_plano'
        MDBoxLayout:
            Contenido:
                MDIconButton:
                    icon: 'arrow-left-bold-circle-outline'
                    on_release: app.regresar('r3')
            ScrollView:
                Contenido:
                    Titulo:
                        text: 'Ecuación del Plano'
                    Imgcontent:
                        source: 'ec_plano1.png'
                    Texto:
                        text: 'Siendo (a,b,c) = (i,j,k) del vector normal respectivamente. El vector normal (n) se calcula como el producto cruz entre 2 vectores que conformen el plano.'
                    Texto:
                        text: 'El vector (n) nos sirve también para calcular "d":'
                    Imgcontent:
                        source: 'ec_plano2.png'
'''

class main(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'DeepPurple'
        return Builder.load_string(KV)
    
    def regresar(self,pantalla):
        self.root.transition = SlideTransition(direction='right')
        self.root.current = pantalla
        self.root.transition = SlideTransition(direction='left')
    
    def cambio(self,nombre_pantalla):
        self.root.current = nombre_pantalla

main().run()
