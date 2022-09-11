# PyQt5 modules
from PyQt5.QtWidgets import QMainWindow

# Project modules
from src.ui.mainwindow import Ui_Stations

# Utilities
from matplotlib.backends.backend_qt5agg import (FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
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
        x = np.arange(-2.0, 2.0, 0.5)
        y = np.arange(-4.0, 4.0, 0.5)
        X, Y = np.meshgrid(x, y)
        zs = np.zeros(X.shape)
        self.figure_station0 = Figure()
        self.canvas_station0 = FigureCanvas(self.figure_station0)
        self.Imagen_estacion0.addWidget(self.canvas_station0)
        self.ax_station0 = self.figure_station0.add_subplot(projection='3d')
        self.ax_station0.quiver([0, 0], [-4, -4], [0, 0], [-1, 0], [0, 0], [0, 1], length=2, color ='red', normalize=True)
        self.ax_station0.plot_surface(X, Y, zs)
        self.ax_station0.set_xlim(-4, 4)
        self.ax_station0.set_ylim(-4, 4)
        self.ax_station0.set_zlim(-4, 4)
        # self.ax_station0.set_axis_off()
        self.ax_station0.grid(True)
        self.ax_station0.set_xticklabels([])
        self.ax_station0.set_yticklabels([])
        self.ax_station0.set_zticklabels([])
        self.ax_station0.view_init(30, -45)
        self.canvas_station0.show()

        self.figure_station1 = Figure(figsize=(3, 3))
        self.canvas_station1 = FigureCanvas(self.figure_station1)
        self.Imagen_estacion1.addWidget(self.canvas_station1)
        self.ax_station1 = self.figure_station1.add_subplot(projection='3d')
        self.ax_station1.quiver([-3, -3, -3], [-3, -3, -3], [3, 3, 3], [1, 0, 0], [0, -1, 0], [0, 0, 1], length=2, color ='red', normalize=True)
        self.ax_station1.plot_surface(X, Y, zs)
        self.ax_station1.set_xlim(-4, 4)
        self.ax_station1.set_ylim(-4, 4)
        self.ax_station1.set_zlim(-4, 4)
        self.ax_station1.set_axis_off()
        self.canvas_station1.show()

        self.figure_station2 = Figure(figsize=(3, 3))
        self.canvas_station2 = FigureCanvas(self.figure_station2)
        self.Imagen_estacion2.addWidget(self.canvas_station2)
        self.ax_station2 = self.figure_station2.add_subplot(projection='3d')
        self.ax_station2.quiver([-3, -3, -3], [-3, -3, -3], [3, 3, 3], [1, 0, 0], [0, -1, 0], [0, 0, 1], length=2, color ='red', normalize=True)
        self.ax_station2.plot_surface(X, Y, zs)
        self.ax_station2.set_xlim(-4, 4)
        self.ax_station2.set_ylim(-4, 4)
        self.ax_station2.set_zlim(-4, 4)
        self.ax_station2.set_axis_off()
        self.figure_station2.tight_layout()
        self.canvas_station2.show()

        self.figure_station3 = Figure(figsize=(3, 3))
        self.canvas_station3 = FigureCanvas(self.figure_station3)
        self.Imagen_estacion3.addWidget(self.canvas_station3)
        self.ax_station3 = self.figure_station3.add_subplot(projection='3d')
        self.ax_station3.quiver([-3, -3, -3], [-3, -3, -3], [3, 3, 3], [1, 0, 0], [0, -1, 0], [0, 0, 1], length=2, color ='red', normalize=True)
        self.ax_station3.plot_surface(X, Y, zs)
        self.ax_station3.set_xlim(-4, 4)
        self.ax_station3.set_ylim(-4, 4)
        self.ax_station3.set_zlim(-4, 4)
        self.ax_station3.set_axis_off()
        self.figure_station3.tight_layout()
        self.canvas_station3.show()

        self.figure_station4 = Figure(figsize=(3, 3))
        self.canvas_station4 = FigureCanvas(self.figure_station4)
        self.Imagen_estacion4.addWidget(self.canvas_station4)
        self.ax_station4 = self.figure_station4.add_subplot(projection='3d')
        self.ax_station4.quiver([-3, -3, -3], [-3, -3, -3], [3, 3, 3], [1, 0, 0], [0, -1, 0], [0, 0, 1], length=2, color ='red', normalize=True)
        self.ax_station4.plot_surface(X, Y, zs)
        self.ax_station4.set_xlim(-4, 4)
        self.ax_station4.set_ylim(-4, 4)
        self.ax_station4.set_zlim(-4, 4)
        self.ax_station4.set_axis_off()
        self.figure_station4.tight_layout()
        self.canvas_station4.show()

        self.axes = [self.ax_station0, self.ax_station1, self.ax_station2, self.ax_station3, self.ax_station4]
        self.canvases = [self.canvas_station0, self.canvas_station1, self.canvas_station2, self.canvas_station3, self.canvas_station4]


    def refreshGrafik(self):
        rolido_val = [int(i.text()[:-1]) for i in self.rolidos]
        cabeceo_val = [int(i.text()[:-1]) for i in self.cabeceos]
        orient_val = [int(i.text()[:-1]) for i in self.orientaciones]


