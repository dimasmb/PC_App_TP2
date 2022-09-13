# PyQt5 modules
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QTimer,QDateTime

# Project modules
from src.ui.mainwindow import Ui_Stations

# Utilities
from matplotlib.backends.backend_qt5agg import (FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
import matplotlib.animation as anim
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

        self.start_elev = 30
        self.start_xy = -45

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

        for i in range(len(self.axes)):
            self.axes[i].quiver([0, 0], [-4, -4], [0, 0], [-1, 0], [0, 0], [0, 1], length=2, color='red',
                                    normalize=True)
            self.axes[i].plot_surface(X, Y, zs)
            self.axes[i].set_xlim(-4, 4)
            self.axes[i].set_ylim(-4, 4)
            self.axes[i].set_zlim(-4, 4)
            self.axes[i].set_axis_off()
            self.axes[i].set_axis_off()
            self.axes[i].view_init(self.start_elev, self.start_xy - 10)
            self.canvases[i].show()

        # inicializo timer
        # self.timer = QTimer()
        # self.timer.timeout.connect(self.refreshGrafik)
        # self.timer.start(1000)
        val=np.zeros((4, 3))
        anim.FuncAnimation(self.figure_station0, self.refresh, interval=1000/60, fargs=(1, val))
    #https://www.youtube.com/watch?v=xEhgxJcH5hk
    def refresh(self, frames, values):
        for i in range(len(self.rolidos)):
            self.rolidos[i].setText(str(values[i, 0] + frames) + 'º')
            self.cabeceos[i].setText(str(values[i, 1]) + 'º')
            self.orientaciones[i].setText(str(values[i, 2]) + 'º')

        rolido_val = [int(i.text()[:-1]) for i in self.rolidos]
        cabeceo_val = [int(i.text()[:-1]) for i in self.cabeceos]
        orient_val = [int(i.text()[:-1]) for i in self.orientaciones]

        x=np.linspace(-4*np.cos(cabeceo_val), 4*np.cos(cabeceo_val), 10)
        y=np.linspace(-4*np.cos(rolido_val), 4*np.cos(rolido_val), 10)

        # z = x*np.sin(cabeceo_val) + y*np.sin(cabeceo_val)
        zx = (x*np.sin(cabeceo_val))
        zy = (y*np.sin(cabeceo_val))

        for i in range(len(self.axes)):
            # self.axes[i].cla()
            # self.axes[i] = self.figures[i].add_subplot(projection='3d')
            self.axes[i].plot_surface(x[:, i], y[:, i], np.array([zx[:, i], zy[:, i]]))
            self.canvases[i].show()

        self.ax_station0.view_init(30, -50)




