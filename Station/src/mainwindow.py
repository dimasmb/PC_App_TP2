# PyQt5 modules
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QTimer

# Project modules
from src.ui.mainwindow import Ui_Stations

# Utilities
from matplotlib.backends.backend_qt5agg import (FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

import numpy as np

class Stations(QMainWindow, Ui_Stations):

    def __init__(self):
        super(Stations, self).__init__()
        self.setupUi(self)

        #inicializo los valores
        self.rolidos = [self.rolido0_val, self.rolido1_val, self.rolido2_val, self.rolido3_val, self.rolido4_val]
        self.cabeceos = [self.cabeceo0_val, self.cabeceo1_val, self.cabeceo2_val, self.cabeceo3_val, self.cabeceo4_val]
        self.orientaciones = [self.orient0_val, self.orient1_val, self.orient2_val, self.orient3_val, self.orient4_val]

        for i in range(len(self.rolidos)):
            self.rolidos[i].setText('0º')
            self.cabeceos[i].setText('0º')
            self.orientaciones[i].setText('0º')

        #inicializo los graficos

        self.x_init = np.array([-2, -2, 2, 2])
        self.y_init = np.array([-4, 4, 4, -4])
        self.z_init = np.array([0, 0, 0, 0])

        self.vert0_init = np.arctan(2)*(180/np.pi)
        self.vert1_init = 180 - self.vert0_init
        self.vert2_init = -self.vert1_init
        self.vert3_init = -self.vert0_init
        self.vert_init = [self.vert0_init, self.vert1_init, self.vert2_init, self.vert3_init, ]
        # self.x_init = np.linspace(-2.0, 2.0, 10)
        # self.y_init = np.linspace(-4.0, 4.0, 10)
        # X, Y = np.meshgrid(self.x_init, self.y_init)
        # zs = np.zeros(X.shape)

        self.figure_station0 = Figure(figsize=(3, 3))
        self.canvas_station0 = FigureCanvas(self.figure_station0)
        self.Imagen_estacion0.addWidget(self.canvas_station0)
        self.ax_station0 = self.figure_station0.add_subplot(projection='3d')

        self.figure_station1 = Figure(figsize=(3, 3))
        self.canvas_station1 = FigureCanvas(self.figure_station1)
        self.Imagen_estacion1.addWidget(self.canvas_station1)
        self.ax_station1 = self.figure_station1.add_subplot(projection='3d')

        self.figure_station2 = Figure(figsize=(3, 3))
        self.canvas_station2 = FigureCanvas(self.figure_station2)
        self.Imagen_estacion2.addWidget(self.canvas_station2)
        self.ax_station2 = self.figure_station2.add_subplot(projection='3d')

        self.figure_station3 = Figure(figsize=(3, 3))
        self.canvas_station3 = FigureCanvas(self.figure_station3)
        self.Imagen_estacion3.addWidget(self.canvas_station3)
        self.ax_station3 = self.figure_station3.add_subplot(projection='3d')

        self.figure_station4 = Figure(figsize=(3, 3))
        self.canvas_station4 = FigureCanvas(self.figure_station4)
        self.Imagen_estacion4.addWidget(self.canvas_station4)
        self.ax_station4 = self.figure_station4.add_subplot(projection='3d')

        self.figures = [self.figure_station0, self.figure_station1, self.figure_station2, self.figure_station3, self.figure_station4]
        self.axes = [self.ax_station0, self.ax_station1, self.ax_station2, self.ax_station3, self.ax_station4]
        self.canvases = [self.canvas_station0, self.canvas_station1, self.canvas_station2, self.canvas_station3, self.canvas_station4]

        vertices = [list(zip(self.x_init, self.y_init, self.z_init))]
        for i in range(len(self.axes)):
            self.axes[i].quiver([0, 0], [-4, -4], [0, 0], [-1, 0], [0, 0], [0, 1], length=2, color='red', normalize=True)
            self.axes[i].add_collection3d(Poly3DCollection(vertices))
            self.axes[i].set_xlim(-4, 4)
            self.axes[i].set_ylim(-4, 4)
            self.axes[i].set_zlim(-4, 4)
            self.figures[i].tight_layout()
            self.axes[i].disable_mouse_rotation()
            self.axes[i].view_init(30, 45)
            self.axes[i].axis('off')
            self.canvases[i].show()

        self.timer = QTimer()
        self.timer.timeout.connect(self.refreshGrafik)
        self.timer.start(50)

        self.cont=0

    def refreshGrafik(self):
        self.cont+=1

        self.rolidos[0].setText(str(self.cont)+'º')
        self.orientaciones[1].setText(str(self.cont)+'º')
        self.cabeceos[2].setText(str(self.cont)+'º')

        rolido_val = [int(i.text()[:-1]) for i in self.rolidos]
        cabeceo_val = [int(i.text()[:-1]) for i in self.cabeceos]
        orient_val = [int(i.text()[:-1]) for i in self.orientaciones]

        sin = np.sin(orient_val * ((np.pi / 180)*np.ones(5)))
        cos = np.cos(orient_val * ((np.pi / 180)*np.ones(5)))
        for i in range(len(self.axes)):
            xx = self.x_init * np.cos(rolido_val[i]*(np.pi/180))
            yy = self.y_init * np.cos(cabeceo_val[i]*(np.pi/180))
            zz = self.x_init * np.sin(rolido_val[i]*(np.pi/180)) + self.y_init * np.sin(cabeceo_val[i]*(np.pi/180))

            vertices = [list(zip(xx, yy, zz))]
            self.axes[i].cla()
            # self.axes[i].quiver([(xx[2]+xx[3])/2], [(yy[2]+yy[3])/2], [(zz[2]+zz[3])/2], [0], [0], [1], length=2, color='red', normalize=True)
            norte = self.axes[i].quiver([0], [0], [5], [-sin[i]], [cos[i]], [0],
                                length=2, color='red', normalize=True) #Norte
            self.axes[i].quiver([0], [0], [5], [sin[i]], [-cos[i]], [0],
                                length=2, color='blue', normalize=True)  # Sur
            self.axes[i].quiver([0], [0], [5], [-cos[i]], [-sin[i]], [0],
                                length=2, color='green', normalize=True)  # Norte
            self.axes[i].quiver([0], [0], [5], [cos[i]], [sin[i]], [0],
                                length=2, color='orange', normalize=True)  # Norte
            self.axes[i].text(-sin[i]*2.5, cos[i]*2.5, 5, 'N')
            self.axes[i].text(sin[i]*2.5, -cos[i]*2.5, 5, 'S')
            self.axes[i].text(-cos[i]*2.5, -sin[i]*2.5, 5, 'E')
            self.axes[i].text(cos[i]*3.5, sin[i]*3.5, 5, 'O')
            self.axes[i].add_collection3d(Poly3DCollection(vertices))
            self.axes[i].set_xlim(-4, 4)
            self.axes[i].set_ylim(-4, 4)
            self.axes[i].set_zlim(-4, 4)

            self.axes[i].axis('off')

            self.figures[i].tight_layout()
            self.axes[i].view_init(30, 45+orient_val[i])
            self.canvases[i].draw()
