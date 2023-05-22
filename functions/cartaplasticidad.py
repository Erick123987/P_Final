import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.pyplot as plt
import numpy as np
from clasificacion import clasificar_suelo  # Reemplaza "codigo1" con el nombre real del archivo del código 1

# Llamar a la función `clasificar_suelo()` del código 1
resultados1 = clasificar_suelo()

# Obtener los valores de LL e IP del diccionario de resultados
LL = resultados1["LL"]
IP = resultados1["IP"]

# Verificar si hay datos de LL e IP disponibles
if LL is None or IP is None:
    print('No hay datos disponibles de LL e IP.')
    print('El suelo es clasificado como una categoría de grueso.')
else:
    def Funcion_carta(Limite_liquido, Indice_plasticidad):
        # Con los datos del limite liquido y el Indice de plasticidad se grafica la ubicación del suelo en la carta de plasticidad.
        plt.plot(Limite_liquido,Indice_plasticidad,'ro')
        plt.vlines(Limite_liquido,0,60,'k','--')
        plt.annotate(' LL ',(Limite_liquido,55))
        plt.annotate(' IP ', (20,Indice_plasticidad + 2))
        plt.hlines(Indice_plasticidad,0,100,'k','--')

        # Se establecen los limites de los ejes x,y.
        plt.xlim(0,100)
        plt.ylim(0,60)

        # Para graficar las lineas de la carta de plasticidad utilizamos las ecuaciones conocidas para la Linea A y la Linea U:
        x=np.array([0,100])
        LineaA =0.73*(x-20)
        LineaU = 0.9*(x-8)
        plt.annotate('Linea A', (90,50),rotation=38) # Etiqueta de la linea A
        plt.annotate('Linea U', (60,45),rotation=45) # Etiqueta de la linea U

        # Estas lineas gráfican las lineas A y U de forma estética
        plt.plot(x, LineaA, 'darkblue', label = "Linea A" )
        plt.plot(x, LineaU, 'k:', label = "Linea U")

        # Graficamos lineas frontera de la carta de plasticidad donde se encuentran los suelos CL-ML
        plt.hlines(7,15.7,29.5,'m')
        plt.hlines(4,12.4,25.5,'m')
        #Aqui ocurre la magia
        region_MH = np.array([[50,0], [50,22], [100,58], [100,0]])
        region_ML = np.array([[25.5,4], [12.4,4], [8,0], [20,0], [50,0], [50,22]])
        region_CH = np.array([[50,22], [100,58], [100,60], [75,60], [50,38]])
        region_CL_ML = np.array([[29.5,7], [15.7,7], [12.4,4], [25.5,4]])
        region_CL = np.array([[15.7,7], [29.5,7], [50,22], [50,38]])

        path_MH = mpath.Path(region_MH)
        path_CH = mpath.Path(region_CH)
        path_CL = mpath.Path(region_CL)
        path_CL_ML = mpath.Path(region_CL_ML)
        path_ML = mpath.Path(region_ML)

        point = np.array([Limite_liquido,Indice_plasticidad])
        if path_MH.contains_point(point):
            print('El punto se encuentra en la zona MH')
        elif path_CH.contains_point(point):
            print('El punto se encuentra en la zona CH')
        elif path_CL.contains_point(point):
            print('El punto se encuentra en la zona CL')
        elif path_CL_ML.contains_point(point):
            print('El punto se encuentra en la zona CL-ML')
        elif path_ML.contains_point(point):
            print('El punto se encuentra en la zona ML')
        else:
            print('El punto no se encuentra en la carta de plasticidad')

        plt.annotate('CL-ML', (15,5))
        plt.annotate('MH', (80,20))
        plt.annotate('CL', (30,15))
        plt.annotate('CH', (62,40))
        plt.annotate('ML', (35,5))
        plt.annotate('NO EXISTE', (15,35))

        # Divide la gráfica cuando el limite liquido es igual a 50 para diferenciar si el suelo es de plasticidad alta o baja
        plt.vlines(50,0,60,'g')

        # Estas lineas mejoran la estetica de la gráfica, hacen que se sombreen las diferentes zonas de la carta de plasticidad
        # Dentro de las variables de la d a la m se guardan las coordenadas que delimitan cada zona.
        d=[50,50,100,100]
        e=[0,22,58,0]
        plt.fill(d,e,'pink')
        f=[25.5,12.4,8,20,50,50]
        g=[4,4,0,0,0,22]
        plt.fill(f,g,'lightgray')
        h=[50,100,100,75,50]
        i=[22,58,60,60,38]
        plt.fill(h,i,'lightgreen')
        j=[29.5,15.7,12.4,25.5]
        k=[7,7,4,4]
        plt.fill(j,k,'m')
        l=[15.7,29.5,50,50]
        m=[7,7,22,38]
        plt.fill(l,m,'bisque')

        # Se grafica la grilla, el titulo y las etiquetas de los ejes.
        plt.grid()
        plt.title("Carta de plasticidad",fontsize=10)
        plt.xlabel("Limite liquido",fontsize=10)
        plt.ylabel("Indice de plasticidad",fontsize=10)
        plt.legend()
        plt.show()

    Funcion_carta(LL, IP)
