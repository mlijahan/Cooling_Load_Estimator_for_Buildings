
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QTableWidgetItem

import sqlite3
import numpy as np
import pandas as pd

import add_zone as adz
import envelopes as envp
import infiltration as inf
import ventilation as vn
import add_envelopes as adenvp
import add_envelopes_properties as adevpr
import fenestrations as fnst
import add_fenestration_area as fnstar
import add_fenestration_u_factor as fnsu
import air_thermal_resistance as air
import hi as hi
import ho as ho
import layers as ly
import add_insulation as adinsl
import add_Insulation0 as adinsl0
import add_Insulation1 as adinsl1
import add_Insulation2 as adinsl2
import add_Insulation3 as adinsl3
import add_Insulation4 as adinsl4
import add_Insulation5 as adinsl5
import add_Insulation6 as adinsl6
import add_Insulation7 as adinsl7
import wndow_door as wd
import door as d
import door01 as d1
import door02 as d2
import door03 as d3
import door04 as d4
import cf_ceiling as ceiling
import cf_wall as wall
import cf_floor as floor
import cf_slab as slab
import shgc
import appliance
import heatgain
import lights
import add_lights as adlight
import add_appliance as addappl


#Create a database or connect  to one
conn = sqlite3.connect('cooling_load.db')
#Create a cursor
c = conn.cursor()

# Drop the fenestration_properties table if already exists.
c.execute("DROP TABLE IF EXISTS fenestration_properties")
#Create a new table
c.execute(""" CREATE TABLE if not exists fenestration_properties(
    fenestration_id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    fenestration_name text,
    fenestration_area_m2 real,
    fenestration_u real
    )
    """)

# Drop the materialsinsulations_properties table if already exists.
c.execute("DROP TABLE IF EXISTS materialsinsulations_properties")
#Create a table
c.execute(""" CREATE TABLE if not exists materialsinsulations_properties(
    layer_id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    layer_number integer,
    layer_name text,
    layer_thickness_m real,
    material_type text,
    r_factor real,
    k_factor real
    )
    """)

# Drop the envelopes_properties table if already exists.
c.execute("DROP TABLE IF EXISTS envelopes_properties")
#Create a table
c.execute(""" CREATE TABLE if not exists envelopes_properties(
    envelope_id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    envelope_name text,
    envelope_type text,
    dt real,
    envelope_area_m2 real,
    fenestration_area_m2 real,
    transparent_surface_cooling_load real,
    opaque_surface_cooling_load real
    )
    """)

# Drop the zone_properties table if already exists.
c.execute("DROP TABLE IF EXISTS zone_properties")
#Create a table
c.execute(""" CREATE TABLE if not exists zone_properties(
    zone_id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    zone_name text,
    infiltration_flow real,
    ventilation_flow real,
    infiltration_load real,
    ventilation_load real,
    heat_gain_envelope real,
    lights_heat real,
    appliances_heat real,
    internal_heat real,
    total_heating_load real
    )
    """)

c.execute("DROP TABLE IF EXISTS light_properties")
#Create a table
c.execute(""" CREATE TABLE if not exists light_properties(
    light_id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    light_type text,
    light_power integer,
    light_number integer,
    light_total real
    )
    """)

c.execute("DROP TABLE IF EXISTS appliance_properties")
#Create a table
c.execute(""" CREATE TABLE if not exists appliance_properties(
    appliance_id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    appliance_type text,
    appliance_power integer,
    appliance_number integer,
    watt_total real
    )
    """)

conn.commit()

conn.close()


class Ui_rfr(object):
    def setupUi(self, rfr):
        rfr.setObjectName("rfr")
        rfr.resize(941, 545)
        rfr.setMinimumSize(QtCore.QSize(941, 545))
        rfr.setMaximumSize(QtCore.QSize(941, 545))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 127, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 170, 170))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 127, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 170, 170))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 127, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 127, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 170, 170))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 127, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 127, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 127, 127, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        rfr.setPalette(palette)
        rfr.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("srcs/house_3637591.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        rfr.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=rfr)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 50, 921, 20))
        self.line.setLineWidth(2)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(660, 440, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton.setIconSize(QtCore.QSize(16, 16))
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(130, 80, 681, 337))
        self.tableWidget.setMinimumSize(QtCore.QSize(681, 337))
        self.tableWidget.setMaximumSize(QtCore.QSize(681, 337))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(87, 0, 130))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(87, 0, 130))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        self.tableWidget.setPalette(palette)
        self.tableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(11)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setStrikeOut(False)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 170, 255))
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 170, 255))
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        item.setBackground(QtGui.QColor(0, 0, 255))
        self.tableWidget.setHorizontalHeaderItem(10, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(165)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setMinimumSectionSize(20)
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(490, 440, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_8.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_8.setAutoDefault(False)
        self.pushButton_8.setDefault(False)
        self.pushButton_8.setFlat(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 16, 121, 31))
        font = QtGui.QFont()
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(790, 15, 101, 31))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_4.setObjectName("pushButton_4")
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(660, 16, 111, 31))
        self.comboBox.setObjectName("comboBox")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(570, 22, 101, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.line_3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(530, 0, 3, 61))
        self.line_3.setLineWidth(2)
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 101, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 20, 221, 24))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(310, 451, 113, 24))
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 450, 171, 24))
        self.pushButton_3.setObjectName("pushButton_3")
        self.line.raise_()
        self.pushButton.raise_()
        self.tableWidget.raise_()
        self.pushButton_8.raise_()
        self.pushButton_2.raise_()
        self.pushButton_4.raise_()
        self.comboBox.raise_()
        self.label_2.raise_()
        self.line_3.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.pushButton_3.raise_()
        self.label.raise_()
        rfr.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=rfr)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 941, 21))
        self.menubar.setObjectName("menubar")
        rfr.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=rfr)
        self.statusbar.setObjectName("statusbar")
        rfr.setStatusBar(self.statusbar)

        self.retranslateUi(rfr)
        QtCore.QMetaObject.connectSlotsByName(rfr)

    # Grab all the items from the database
    def grab_zone(self):
        # Create a database or connect  to one
        conn = sqlite3.connect('cooling_load.db')
        # Create a cursor
        c = conn.cursor()
        self.current_id = self.comboBox.currentIndex() + 1

        c.execute(" SELECT * FROM zone_properties WHERE zone_id = ? ", (self.current_id,))
        records = c.fetchall()

        # Loop through records and add to screen
        record1 = [item[1] for item in records]
        record2 = [item[2] for item in records]
        record3 = [item[3] for item in records]
        record4 = [item[4] for item in records]
        record5 = [item[5] for item in records]
        record6 = [item[6] for item in records]
        record7 = [item[7] for item in records]
        record8 = [item[8] for item in records]
        record9 = [item[9] for item in records]
        record10 = [item[10] for item in records]

        self.zone_name = record1[0]
        self.infiltration_flow = record2[0]
        self.infiltration_load = record3[0]
        self.ventilation_flow = record4[0]
        self.ventilation_load = record5[0]
        self.heatgain_envelopes = record6[0]
        self.lighting_load = record7[0]
        self.appliances_heating_load = record8[0]
        self.internal_load = record9[0]
        self.total_heatgain_load = record10[0]

        self.ROW = self.tableWidget.rowCount()
        self.tableWidget.insertRow(self.ROW)
        self.tableWidget.setItem(self.ROW, 0, QTableWidgetItem(str(self.zone_name)))
        self.tableWidget.setItem(self.ROW, 2, QTableWidgetItem(str(self.infiltration_flow)))
        self.tableWidget.setItem(self.ROW, 3, QTableWidgetItem(str(self.ventilation_flow)))
        self.tableWidget.setItem(self.ROW, 4, QTableWidgetItem(str(self.infiltration_load)))
        self.tableWidget.setItem(self.ROW, 5, QTableWidgetItem(str(self.ventilation_load)))
        self.tableWidget.setItem(self.ROW, 6, QTableWidgetItem(str(self.heatgain_envelopes)))
        self.tableWidget.setItem(self.ROW, 7, QTableWidgetItem(str(self.lighting_load)))
        self.tableWidget.setItem(self.ROW, 8, QTableWidgetItem(str(self.appliances_heating_load)))
        self.tableWidget.setItem(self.ROW, 9, QTableWidgetItem(str(self.internal_load)))
        self.tableWidget.setItem(self.ROW, 10, QTableWidgetItem(str(self.total_heatgain_load)))

        conn.commit()

        conn.close()

    def save_database_zones(self):
        # Create a database or connect  to one
        conn = sqlite3.connect('cooling_load.db')
        # Create a cursor
        c = conn.cursor()

        # Create Blank Dictionary To Hold Fenestration's Properties Items
        items = new_zone.zone_properties_list()

        # Add stuf to the table
        c.execute("INSERT INTO zone_properties (zone_name, infiltration_flow,"
                      "ventilation_flow, infiltration_load, ventilation_load, heat_gain_envelope,"
                      "lights_heat, appliances_heat, internal_heat, total_heating_load) VALUES (?,?,?,?,?,?,?,?,?,?)",

                      (items[0], items[1], items[2], items[3], items[4], items[5], items[6], items[7], items[8], items[9])
                      )

        conn.commit()

        conn.close()

    def grab_envelope(self):
        # Create a database or connect  to one
        conn = sqlite3.connect('cooling_load.db')
        # Create a cursor
        c = conn.cursor()
        self.current_id = envelope.comboBox_2.currentIndex() + 1

        c.execute(" SELECT * FROM envelopes_properties WHERE envelope_id = ? ", (self.current_id,))
        records = c.fetchall()

        # Loop through records and add to screen
        record1 = [item[1] for item in records]
        record2 = [item[2] for item in records]
        record3 = [item[3] for item in records]
        record4 = [item[4] for item in records]
        record5 = [item[5] for item in records]
        record6 = [item[6] for item in records]
        record7 = [item[7] for item in records]


        self.name = record1[0]
        self.envelope_type = record2[0]
        self.dt = record3[0]
        self.gross_envelope_area = record4[0]
        self.fenestration_area = record5[0]
        self.transparent_surface_load = record6[0]
        self.opaque_load = record7[0]


        self.ROW = envelope.tableWidget.rowCount()
        envelope.tableWidget.insertRow(self.ROW)
        envelope.tableWidget.setItem(self.ROW, 0, QTableWidgetItem(str(self.name)))
        envelope.tableWidget.setItem(self.ROW, 1, QTableWidgetItem(str(self.envelope_type)))
        envelope.tableWidget.setItem(self.ROW, 2, QTableWidgetItem(str(self.dt)))
        envelope.tableWidget.setItem(self.ROW, 3, QTableWidgetItem(str(self.gross_envelope_area)))
        envelope.tableWidget.setItem(self.ROW, 4, QTableWidgetItem(str(self.fenestration_area)))
        envelope.tableWidget.setItem(self.ROW, 5, QTableWidgetItem(str(self.transparent_surface_load)))
        envelope.tableWidget.setItem(self.ROW, 6, QTableWidgetItem(str(self.opaque_load)))


        conn.commit()

        conn.close()

    def save_database_envelopes(self):
        # Create a database or connect  to one
        conn = sqlite3.connect('cooling_load.db')
        # Create a cursor
        c = conn.cursor()

        # Create Blank Dictionary To Hold Envelope's Properties Items
        items = add_envelopes.envelopes_properties_list()

        # Add stuff to the table
        c.execute("INSERT INTO envelopes_properties (envelope_name,"
                      "envelope_type, dt, envelope_area_m2, fenestration_area_m2, transparent_surface_cooling_load"
                  ", opaque_surface_cooling_load)"
                  " VALUES (?,?,?,?,?,?,?)",

                      (items[0], items[1], items[2], items[3], items[4], items[5], items[6])
                      )

        conn.commit()

        conn.close()

    def grab_insullation(self):
        # Create a database or connect  to one
        conn = sqlite3.connect('cooling_load.db')
        # Create a cursor
        c = conn.cursor()
        self.current_id = add_layers.comboBox.currentIndex() + 1

        c.execute(" SELECT * FROM materialsinsulations_properties WHERE layer_id = ? ", (self.current_id,))
        records = c.fetchall()

        # Loop through records and add to screen
        record1 = [item[1] for item in records]
        record2 = [item[2] for item in records]
        record3 = [item[3] for item in records]
        record4 = [item[4] for item in records]
        record5 = [item[5] for item in records]
        record6 = [item[6] for item in records]

        self.layer_number = record1[0]
        self.layer_name = record2[0]
        self.thickness = record3[0]
        self.material_type = record4[0]
        self.r_factor = record5[0]
        self.k_factor = record6[0]

        self.ROW = add_layers.tableWidget.rowCount()
        add_layers.tableWidget.insertRow(self.ROW)
        add_layers.tableWidget.setItem(self.ROW, 0, QTableWidgetItem(str(self.layer_number)))
        add_layers.tableWidget.setItem(self.ROW, 1, QTableWidgetItem(str(self.layer_name)))
        add_layers.tableWidget.setItem(self.ROW, 2, QTableWidgetItem(str(self.thickness)))
        add_layers.tableWidget.setItem(self.ROW, 3, QTableWidgetItem(str(self.material_type)))
        add_layers.tableWidget.setItem(self.ROW, 4, QTableWidgetItem(str(self.k_factor)))
        add_layers.tableWidget.setItem(self.ROW, 5, QTableWidgetItem(str(self.r_factor)))

        conn.commit()

        conn.close()

    def save_database_insulation(self):
        # Create a database or connect  to one
        conn = sqlite3.connect('cooling_load.db')
        # Create a cursor
        c = conn.cursor()

        # Create Blank Dictionary To Hold Fenestration's Properties Items
        items = add_insulation.insulation_properties_list()

        # Add stuf to the table
        c.execute("INSERT INTO materialsinsulations_properties (layer_number, layer_name,"
                      "layer_thickness_m, material_type, r_factor, k_factor) VALUES (?,?,?,?,?,?)",

                      (items[0], items[1], items[2], items[3], items[4], items[5])
                      )

        conn.commit()

        conn.close()

    def grab_fenestration(self):
        # Create a database or connect  to one
        conn = sqlite3.connect('heating_load.db')
        # Create a cursor
        c = conn.cursor()
        self.current_id = fenestrations.comboBox.currentIndex() + 1

        c.execute(" SELECT * FROM fenestration_properties WHERE fenestration_id = ? ", (self.current_id,))
        records = c.fetchall()

        # Loop through records and add to screen
        record1 = [item[1] for item in records]
        record2 = [item[2] for item in records]
        record3 = [item[3] for item in records]

        self.fenestration_name = record1[0]
        self.fenestration_area = record2[0]
        self.fenestration_u_factor = record3[0]

        self.ROW = fenestrations.tableWidget.rowCount()
        fenestrations.tableWidget.insertRow(self.ROW)
        fenestrations.tableWidget.setItem(self.ROW, 0, QTableWidgetItem(str(self.fenestration_name)))
        fenestrations.tableWidget.setItem(self.ROW, 1, QTableWidgetItem(str(self.fenestration_area)))
        fenestrations.tableWidget.setItem(self.ROW, 2, QTableWidgetItem(str(self.fenestration_u_factor)))

        conn.commit()

        conn.close()

    def save_database_fenestration(self):
        # Create a database or connect  to one
        conn = sqlite3.connect('heating_load.db')
        # Create a cursor
        c = conn.cursor()

        # Create Blank Dictionary To Hold Fenestration's Properties Items
        items = fenestration_area.fenestration_properties_list()

        # Add stuf to the table
        c.execute("INSERT INTO fenestration_properties (fenestration_name,fenestration_area_m2,"
                      "fenestration_u) VALUES (?,?,?)",

                      (items[0], items[1], items[2])
                      )

        conn.commit()

        conn.close()

    def grab_lights(self):
        # Create a database or connect  to one
        conn = sqlite3.connect('cooling_load.db')
        # Create a cursor
        c = conn.cursor()
        self.current_id = light_factor.comboBox.currentIndex() + 1

        c.execute(" SELECT * FROM light_properties WHERE light_id = ? ", (self.current_id,))
        records = c.fetchall()

        # Loop through records and add to screen
        record1 = [item[1] for item in records]
        record2 = [item[2] for item in records]
        record3 = [item[3] for item in records]
        record4 = [item[4] for item in records]


        self.light_name = record1[0]
        self.light_power = record2[0]
        self.number = record3[0]
        self.total_loghts = record4[0]


        self.ROW = light_factor.tableWidget.rowCount()
        light_factor.tableWidget.insertRow(self.ROW)
        light_factor.tableWidget.setItem(self.ROW, 0, QTableWidgetItem(str(self.light_name)))
        light_factor.tableWidget.setItem(self.ROW, 1, QTableWidgetItem(str(self.light_power)))
        light_factor.tableWidget.setItem(self.ROW, 2, QTableWidgetItem(str(self.number)))
        light_factor.tableWidget.setItem(self.ROW, 3, QTableWidgetItem(str(self.total_loghts)))


        conn.commit()

        conn.close()

    def save_database_lights(self):
        # Create a database or connect  to one
        conn = sqlite3.connect('cooling_load.db')
        # Create a cursor
        c = conn.cursor()

        # Delete everything in the database table
        # c.execute('DELETE FROM fenestration_properties')

        # Create Blank Dictionary To Hold Fenestration's Properties Items
        items = add_lights.light_properties_list()

        # Add stuf to the table
        c.execute("INSERT INTO light_properties (light_type, light_power,"
                      "light_number, light_total) VALUES (?,?,?,?)",

                      (items[0], items[1], items[2], items[3])
                      )

        conn.commit()

        conn.close()

        # Grab all the items from the database

    def grab_appliances(self):
        # Create a database or connect  to one
        conn = sqlite3.connect('cooling_load.db')
        # Create a cursor
        c = conn.cursor()
        self.current_id = appliance_factor.comboBox.currentIndex() + 1

        c.execute(" SELECT * FROM appliance_properties WHERE appliance_id = ? ", (self.current_id,))
        records = c.fetchall()

        # Loop through records and add to screen
        record1 = [item[1] for item in records]
        record2 = [item[2] for item in records]
        record3 = [item[3] for item in records]
        record4 = [item[4] for item in records]

        self.appliance_name = record1[0]
        self.apliance_power = record2[0]
        self.numberappliance = record3[0]
        self.total_wat= record4[0]

        self.ROW = appliance_factor.tableWidget.rowCount()
        appliance_factor.tableWidget.insertRow(self.ROW)
        appliance_factor.tableWidget.setItem(self.ROW, 0, QTableWidgetItem(str(self.appliance_name)))
        appliance_factor.tableWidget.setItem(self.ROW, 1, QTableWidgetItem(str(self.apliance_power)))
        appliance_factor.tableWidget.setItem(self.ROW, 2, QTableWidgetItem(str(self.numberappliance)))
        appliance_factor.tableWidget.setItem(self.ROW, 3, QTableWidgetItem(str(self.total_wat)))

        conn.commit()

        conn.close()

    def save_database_appliances(self):
        #appliance_type text,appliance_power integer,appliance_number integer,watt_total
        # Create a database or connect  to one
        conn = sqlite3.connect('cooling_load.db')
        # Create a cursor
        c = conn.cursor()

        # Delete everything in the database table
        # c.execute('DELETE FROM fenestration_properties')

        # Create Blank Dictionary To Hold Fenestration's Properties Items
        items = add_appliances.appliance_properties_list()

        # Add stuf to the table
        c.execute("INSERT INTO appliance_properties (appliance_type, appliance_power,"
                  "appliance_number, watt_total) VALUES (?,?,?,?)",

                  (items[0], items[1], items[2], items[3])
                  )

        conn.commit()

        conn.close()



    def total_bilding_heatingload(self):
        self.building_heatingload = []
        self.ROW = self.tableWidget.rowCount()
        for row in range(self.ROW):
            self.building_heatingload.append(float(self.tableWidget.item(row, 9).text()))
        self.total_building_load = sum(self.building_heatingload)
        return np.round( self.total_building_load)

    def show_building_heating_load(self):
        self.buildingload = self.lineEdit_2.setText(str(self.total_bilding_heatingload()))
        return self.buildingload

    def delete_total_heating_load_building(self):
        self.total_heating_loads_of_building = self.lineEdit_2.clear()
        return self.total_heating_loads_of_building

    def retranslateUi(self, rfr):
        _translate = QtCore.QCoreApplication.translate
        rfr.setWindowTitle(_translate("rfr", "Cooling Load"))
        self.pushButton.setText(_translate("rfr", "Clear Table"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("rfr", "Zone Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("rfr", "Zone Envelopes Properties"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("rfr", "Infiltration Flow Rate (L/s)"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("rfr", "Ventilation Flow Rate (L/s)"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("rfr", "Infiltration Load (W)"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("rfr", "Ventilation Load (W)"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("rfr", "Lights Heat (W)"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("rfr", "Heat Gain Envelopes(W)"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("rfr", "Appliances Heat (W)"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("rfr", "Internal Heat Gain (W)"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("rfr", "Total Cooling Load (W)"))
        self.pushButton_8.setText(_translate("rfr", "Print Table"))
        self.pushButton_2.setText(_translate("rfr", "Add New Zone"))
        self.pushButton_4.setText(_translate("rfr", "Add to List"))
        self.label_2.setText(_translate("rfr", "Select Zone :"))
        self.label.setText(_translate("rfr", "Project Name :"))
        self.pushButton_3.setText(_translate("rfr", "Building Cooling Load :"))
        ### =============================================================== Add from comboBox to the list
        self.pushButton_4.clicked.connect(lambda: self.grab_zone())
        ### ===============================================================  Delete all items from table
        self.pushButton.clicked.connect(lambda: self.tableWidget.clearContents())
        self.pushButton.clicked.connect(lambda: self.delete_row_layers())
        self.pushButton.clicked.connect(lambda: self.delete_total_heating_load_building())
        ### =============================================================== Add tatal building heating load
        self.pushButton_3.clicked.connect(lambda: self.show_building_heating_load())
        # self.pushButton_8.clicked.connect(lambda: self.loadData())
        self.pushButton_8.clicked.connect(lambda: self.exportToExcel())

    def delete_row_layers(self):
        self.ROW = self.tableWidget.rowCount()
        for row in range(self.ROW):
            self.tableWidget.removeRow(row)

    def infiltration_flow(self):
        self.inflow = new_zone.lineEdit_8.setText(str(infiltration.infiltration_flow()))
        return self.inflow

    def ventilation_flow(self):
        self.ventflow = new_zone.lineEdit_9.setText(str(ventilation.ventilation_flow()))
        return self.ventflow

    def sensible_load(self):
        self.sens_load = 0.24 * 1.2 * infiltration.infiltration_flow() * new_zone.delta_temperature()
        return np.round(self.sens_load)

    def latent_load(self):
        self.latentload = 597 * 1.2 * infiltration.infiltration_flow() * new_zone.delta_humidity()
        return np.round(self.latentload)

    def sensible_load_ventilation(self):
        self.sens_load = 0.24 * 1.2 * ventilation.ventilation_flow() * new_zone.delta_temperature()
        return np.round(self.sens_load)

    def latent_load_ventilation(self):
        self.latentload = 597 * 1.2 * ventilation.ventilation_flow() * new_zone.delta_humidity()
        return np.round(self.latentload)

    def total_infiltration(self):
        self.infiltration = self.sensible_load() + self.latent_load()
        return self.infiltration

    def total_ventilation(self):
        self.ventilation = self.sensible_load_ventilation() + self.latent_load_ventilation()
        return self.ventilation

    def infiltrationload(self):
        self.infload = new_zone.lineEdit_11.setText(str(self.total_infiltration()))
        return self.infload

    def ventilationload(self):
        self.ventload = new_zone.lineEdit_12.setText(str(self.total_ventilation()))
        return self.ventload

    def dt_add_envelopes(self):
        self.dt_value = add_envelopes.lineEdit_2.setText(str(new_zone.delta_design_temperature()))

    def show_total_heating_load(self):
        self.total_heat = new_zone.lineEdit_16.setText(str(new_zone.total_coolingload()))
        return self.total_heat

    def show_zone_total_heatgain(self):
        self.zone_heatgain_load = new_zone.lineEdit_10.setText(str(envelope.Transparent_surface_cooling_load()))
        return self.zone_heatgain_load

    def zone_name(self):
        self.zonname = envelope.lineEdit.setText(str(new_zone.zone_names()))
        return self.zonname

    def total_heatgain_through_envelope(self):
        self.heatgain_envelope_show = envelope.lineEdit_2.setText(str(envelope.totalheat()))
        return self.heatgain_envelope_show

    def envelope_envelopes_name(self):
        self.envelopesname = add_layers.lineEdit.setText(str(add_envelopes.envelopes_name()))
        return self.envelopesname

    def fenestration_envelopes_name(self):
        self.envelopesname = fenestrations.lineEdit.setText(str(add_envelopes.envelopes_name()))
        return self.envelopesname


    def insulation_R_factor(self):
        self.insulation_type = add_insulation.comboBox.currentIndex()
        if self.insulation_type == 0:
            self.insulation_R = add_insulation.lineEdit_4.setText(str(0))
        elif self.insulation_type == 1:
            self.insulation_R = add_insulation.lineEdit_4.setText(str(add_insulation1.R_factor()))
        elif self.insulation_type == 2:
            self.insulation_R = add_insulation.lineEdit_4.setText(str(add_insulation2.R_factor()))
        elif self.insulation_type == 3:
            self.insulation_R = add_insulation.lineEdit_4.setText(str(add_insulation3.R_factor()))
        elif self.insulation_type == 4:
            self.insulation_R = add_insulation.lineEdit_4.setText(str(add_insulation4.R_factor()))
        elif self.insulation_type == 5:
            self.insulation_R = add_insulation.lineEdit_4.setText(str(add_insulation5.R_factor()))
        elif self.insulation_type == 6:
            self.insulation_R = add_insulation.lineEdit_4.setText(str(add_insulation6.R_factor()))
        elif self.insulation_type == 7:
            self.insulation_R = add_insulation.lineEdit_4.setText(str(0))

        return self.insulation_R

    def insulation_K_factor(self):
        self.insulation_type = add_insulation.comboBox.currentIndex()
        if self.insulation_type == 0:
            self.insulation_K = add_insulation.lineEdit_5.setText(str(add_insulation0.K_factor()))
        elif self.insulation_type == 1:
            self.insulation_K = add_insulation.lineEdit_5.setText(str(add_insulation1.K_factor()))
        elif self.insulation_type == 2:
            self.insulation_K = add_insulation.lineEdit_5.setText(str(0))
        elif self.insulation_type == 3:
            self.insulation_K = add_insulation.lineEdit_5.setText(str(add_insulation3.K_factor()))
        elif self.insulation_type == 4:
            self.insulation_K = add_insulation.lineEdit_5.setText(str(add_insulation4.K_factor()))
        elif self.insulation_type == 5:
            self.insulation_K = add_insulation.lineEdit_5.setText(str(add_insulation5.K_factor()))
        elif self.insulation_type == 6:
            self.insulation_K = add_insulation.lineEdit_5.setText(str(add_insulation6.K_factor()))
        elif self.insulation_type == 7:
            self.insulation_K = add_insulation.lineEdit_5.setText(str(add_insulation7.K_factor()))

        return self.insulation_K

    def total_r_factor_per_layer_show(self):
        self.total_r_layer = add_layers.lineEdit_2.setText(str(add_layers.total_r_factor_per_layer()))
        return self.total_r_layer

    def total_r_add_envelopes_properties(self):
        self.total_r_enevelope = add_envelopes_properties.lineEdit_6.setText(str(add_layers.total_r_factor_per_layer()))
        return self.total_r_enevelope

    def air_resistance(self):
        self.air_res = add_envelopes_properties.lineEdit_5.setText(str(add_air.air_resistance()))
        return self.air_res

    def indoor(self):
        self.indoor_heat = add_envelopes_properties.lineEdit_3.setText(str(add_hi.surface_heat()))
        return self.indoor_heat

    def outdoor(self):
        self.outdoor_heat = add_envelopes_properties.lineEdit_4.setText(str(add_ho.ho()))
        return self.outdoor_heat

    def net_envelope_area(self):
        self.net_envelope = add_envelopes_properties.lineEdit.setText(str(add_envelopes.enevelope_area()))
        return self.net_envelope

    def fenestration_installation_u_factors(self):
        self.installation_u_fact = fenestration_area.lineEdit_5.setText(str(fenestration_ufactor.u_factor_installation_func()))
        return self.installation_u_fact

    def fenestration_area_u(self):
        self.u_fenestration = fenestrations.lineEdit_2.setText(str(fenestrations.total_u_factor_per_area()))
        return self.u_fenestration

    def save_fenestration_u_factor(self):
        self.u_fenestration = add_envelopes.lineEdit_5.setText(str(fenestrations.total_u_factor_per_area()))
        return self.u_fenestration

    def select_fenestration_according_to_area(self):
        self.fenestration_area = add_envelopes.lineEdit_3.text()
        if self.fenestration_area == '0':
            add_envelopes.lineEdit_5.setText(str(0))
        else:
            dialog_fenestrations.exec()


    def chek(self, class1_1):
        t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18 = class1_1.check_line()
        if (t1 != -1 and t2 != -1 and t3 != -1 and t4 != -1 and t5 != -1 and t6 != -1 and t7 != -1 and t8 != -1
                and t9 != -1 and t10 != -1 and t11 != -1 and t12 != -1 and t13 != -1 and t14 != -1
        and t15 != -1 and t16 != -1 and t17 != -1 and t18 != -1):
            self.comboBox.addItem(str(t1))
        else:
            pass

    def chek_envelopes(self, class1_1):
        t1, t2, t3, t4, t5, t6, t7, t8 = class1_1.check_line()
        if (t1 != -1 and t2 != -1 and t3 != -1 and t4 != -1 and t5 != -1 and t6 != -1 and t7 != -1 and t8 != -1):
            envelope.comboBox_2.addItem(str(t1))
        else:
            pass

    def chek_envelopes_properties(self, class1_1):
        t1, t2, t3, t4, t5 = class1_1.check_line()
        if (t1 != -1 and t2 != -1 and t3 != -1 and t4 != -1 and t5 != -1):
            add_envelopes.lineEdit_4.setText(str(add_envelopes_properties.total_u_factor_per_area()))
        else:
            pass

    def chek_insulation(self, class1_1):
        t1, t2, t3, t4, t5 = class1_1.check_line()
        if (t1 != -1 and t2 != -1 and t3 != -1 and t4 != -1 and t5 != -1):
            add_layers.comboBox.addItem(str(t2))
        else:
            pass

    def chek_fenestration(self, class1_1):
        t1, t2, t3 = class1_1.check_line()
        if (t1 != -1 and t2 != -1 and t3 != -1):
            fenestrations.comboBox.addItem(str(t1))
        else:
            pass

    def chek_lights(self, class1_1):
        t1, t2, t3 = class1_1.check_line()
        if (t1 != -1 and t2 != -1 and t3 != -1):
            light_factor.comboBox.addItem(str(t1))
        else:
            pass

    def chek_appliance(self, class1_1):
        t1, t2 = class1_1.check_line()
        if (t1 != -1 and t2 != -1 ):
            appliance_factor.comboBox.addItem(str(t1))
        else:
            pass

    def select_insulation(self):
        self.insulation = add_insulation.comboBox.currentIndex()
        if self.insulation == 0:
            dialog_addinsulation0.exec()
        elif self.insulation == 1:
            dialog_addinsulation1.exec()
        elif self.insulation == 2:
            dialog_addinsulation2.exec()
        elif self.insulation == 3:
            dialog_addinsulation3.exec()
        elif self.insulation == 4:
            dialog_addinsulation4.exec()
        elif self.insulation == 5:
            dialog_addinsulation5.exec()
        elif self.insulation == 6:
            dialog_addinsulation6.exec()
        else:
            dialog_addinsulation7.exec()

    def select_door_type(self):
        self.door_types_s= door.comboBox.currentIndex()
        if self.door_types_s == 0:
            dialog_door01.exec()
        elif self.door_types_s == 1:
            dialog_door02.exec()
        elif self.door_types_s == 2:
            dialog_door03.exec()
        elif self.door_types_s == 3:
            dialog_door04.exec()
        else:
            dialog_afenestration_ufactor.exec()

    def door_1_u_factor(self):
        self.doors_1_u_fact = fenestration_area.lineEdit_5.setText(str(door01.door1_u_factors()))
        return self.doors_1_u_fact

    def door_1_insu_u_factor(self):
        self.doors_1_instal_u_fact = fenestration_area.lineEdit_5.setText(str(0))
        return self.doors_1_instal_u_fact

    def door_2_u_factor(self):
        self.doors_2_u_fact = fenestration_area.lineEdit_5.setText(str(door02.door2_u_factors()))
        return self.doors_2_u_fact

    def door_2_ins_u_factor(self):
        self.doors_2_instal_u_fact = fenestration_area.lineEdit_5.setText(str(0))
        return self.doors_2_instal_u_fact

    def door_3_u_factor(self):
        self.doors_3_u_fact = fenestration_area.lineEdit_5.setText(str(door03.door3_u_factors()))
        return self.doors_3_u_fact

    def door_3_ins_u_factor(self):
        self.doors_3_instal_u_fact = fenestration_area.lineEdit_5.setText(str(0))
        return self.doors_3_instal_u_fact

    def door_4_u_factor(self):
        self.doors_4_u_fact = fenestration_area.lineEdit_5.setText(str(door04.door4_u_factors()))
        return self.doors_4_u_fact

    def door_4_ins_u_factor(self):
        self.doors_4_instal_u_fact = fenestration_area.lineEdit_5.setText(str(0))
        return self.doors_4_instal_u_fact

    def select_opaque_surface(self):
        self.opaque_surface = add_envelopes.comboBox.currentIndex()
        if self.opaque_surface == 0:
            dialog_wallcf.exec()
        elif self.opaque_surface == 1:
            dialog_floorcf.exec()
        elif self.opaque_surface == 2:
            dialog_ceilingcf.exec()
        else:
            dialog_slabcf.exec()

    def total_cf_factor_walls(self):
        self.total_value_cf = wall_cf.ofr_reducing_temp_effect() + wall_cf.oft_buffering_effect()\
                              + wall_cf.ofb_incident_solargain()

        self.total_ua_wall = float(add_envelopes.lineEdit_5.text()) + float (add_envelopes.lineEdit_4.text())
        self.total_cf_ua = self.total_value_cf * self.total_ua_wall
        return np.round(self.total_cf_ua,2)

    def show_total_cffactors_walls(self):
        self.show_cffactor = add_envelopes.lineEdit_6.setText(str(self.total_cf_factor_walls()))
        return self.show_cffactor

    def total_cf_factor_floors(self):
        self.total_value_cf_floor = floor_cf.ofr_reducing_temp_effect_floor() + floor_cf.oft_buffering_effect_floor()
        self.total_ua_floor = float(add_envelopes.lineEdit_5.text()) + float(add_envelopes.lineEdit_4.text())
        self.total_cf_ua_floor = self.total_value_cf_floor * self.total_ua_floor
        return np.round(self.total_cf_ua_floor, 2)

    def show_total_cffactors_floors(self):
        self.show_cffactor_floor = add_envelopes.lineEdit_6.setText(str(self.total_cf_factor_floors()))
        return self.show_cffactor_floor

    def total_cf_factor_ceilings(self):
        self.total_value_cf_ceiling = ceiling_cf.ofr_reducing_temp_effect_ceiling() + \
                                      ceiling_cf.oft_buffering_effect_ceiling()+\
                                      ceiling_cf.ofb_incident_solargain_ceiling()
        self.total_ua_ceiling = float(add_envelopes.lineEdit_5.text()) + float(add_envelopes.lineEdit_4.text())
        self.total_cf_ua_ceiling = self.total_value_cf_ceiling * self.total_ua_ceiling
        return np.round(self.total_cf_ua_ceiling, 2)

    def show_total_cffactors_ceilings(self):
        self.show_cffactor_ceiling = add_envelopes.lineEdit_6.setText(str(self.total_cf_factor_ceilings()))
        return self.show_cffactor_ceiling

    def total_cf_factor_slabs(self):
        self.total_value_cf_slab = slab_cf.opaque_load_slab()
        self.total_ua_slab = float(add_envelopes.lineEdit_7.text())
        self.total_cf_ua_slab = self.total_value_cf_slab * self.total_ua_slab
        return self.total_cf_ua_slab

    def show_total_cffactors_slabs(self):
        self.show_cffactor_slab = add_envelopes.lineEdit_6.setText(str(self.total_cf_factor_slabs()))
        return self.show_cffactor_slab

    def total_cooling_surface_loads(self):
        self.fenestration_u_surface = float(add_envelopes.lineEdit_5.text()) / float(add_envelopes.lineEdit_3.text())
        self.part2_equ = shgcfactor.shgc_factors() * shgcfactor.pxi_factor() * shgcfactor.ffs_factor() *\
                         shgcfactor.sc_factores()
        self.part1_equ = self.fenestration_u_surface * (float(add_envelopes.lineEdit_2.text())
                                                        - (0.46 * shgcfactor.range_colling_temp()))
        return np.round ((float(add_envelopes.lineEdit_3.text()) * (self.part1_equ + self.part2_equ)), 2)

    def show_total_cooling_surface_loads(self):
        self.show_surf_cool_load = add_envelopes.lineEdit_8.setText(str(self.total_cooling_surface_loads()))
        return self.show_surf_cool_load

    def show_total_heat_gain(self):
        self.show_heatgain = new_zone.lineEdit_15.setText(str(heatgain_factor.heatgain_total_load()))
        return self.show_heatgain

    def show_light_watts(self):
        self.show_total_lightwatt = light_factor.lineEdit_2.setText(str(light_factor.total_light()))
        return self.show_total_lightwatt

    def show_total_heat_light(self):
        self.showlight = new_zone.lineEdit_17.setText(str(light_factor.total_light()))
        return self.showlight

    def show_appliance_watts(self):
        self.show_total_appwatt = appliance_factor.lineEdit_2.setText(str(appliance_factor.total_apps()))
        return self.show_total_appwatt

    def show_total_heat_app(self):
        self.showapp = new_zone.lineEdit_14.setText(str(appliance_factor.total_apps()))
        return self.showapp

    def exportToExcel(self):
        zone_names = []
        zone_envelopes_properties_list = []
        infiltration_flows = []
        ventilation_flows = []
        conductive_loads = []
        infiltration_loads = []
        ventilation_loads = []
        lightheat_loads = []
        heatenvelope_losses = []
        heatappliance_loads = []
        heatinternal_loads = []
        totalcool_loads = []
        for row in range(self.tableWidget.rowCount()):
            zone_name = self.tableWidget.item(row, 0).text()
            zone_envelopes_properties = self.tableWidget.item(row, 1).text()
            infiltration_flow = float(self.tableWidget.item(row, 2).text())
            ventilation_flow = float(self.tableWidget.item(row, 3).text())
            conductive_load = float(self.tableWidget.item(row, 4).text())
            infiltration_load = float(self.tableWidget.item(row, 5).text())
            ventilation_load = float(self.tableWidget.item(row, 6).text())
            light_heat_load = float(self.tableWidget.item(row, 7).text())
            heat_through_envelopes = float(self.tableWidget.item(row, 8).text())
            appliance_heat = float(self.tableWidget.item(row, 9).text())
            internal_heat = float(self.tableWidget.item(row, 10).text())
            total_cooling_load = float(self.tableWidget.item(row, 11).text())
            zone_names.append(zone_name)
            zone_envelopes_properties_list.append(zone_envelopes_properties)
            infiltration_flows.append(infiltration_flow)
            ventilation_flows.append(ventilation_flow)
            conductive_loads.append(conductive_load)
            infiltration_loads.append(infiltration_load)
            ventilation_loads.append(ventilation_load)
            lightheat_loads.append(light_heat_load)
            heatenvelope_losses.append(heat_through_envelopes)
            heatappliance_loads.append(appliance_heat)
            heatinternal_loads.append(internal_heat)
            totalcool_loads.append(total_cooling_load)


        data = {'Zone Name': zone_names,
                'Zone Envelopes Properties': zone_envelopes_properties_list,
                'Infiltration Flow Rate (L/s)': infiltration_flows,
                'Ventilation Flow Rate (L/s)': ventilation_flows,
                'Conductive Load (W)': conductive_loads,
                'Infiltration Load (W)': infiltration_loads,
                'Ventilation Load (W)': ventilation_loads,
                'light gain Load (W)': lightheat_loads,
                'Heat through envelopes Losses (W)': heatenvelope_losses,
                'Appliance gain Load (W)': heatappliance_loads,
                'Internal Load (W)': heatinternal_loads,
                'Total Cooling Load (W)': totalcool_loads}
        df = pd.DataFrame(data)
        df.to_excel('Building_Cooling_Loads.xlsx', index=False)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    rfr = QtWidgets.QMainWindow()
    ui = Ui_rfr()
    ui.setupUi(rfr)
    rfr.show()
    ##============================================================================================= Add New Zone
    new_zone = adz.Ui_Dialog()
    dialog_addzone = QtWidgets.QDialog()
    new_zone.setupUi(dialog_addzone)
    ui.pushButton_2.clicked.connect(lambda: dialog_addzone.exec())
    new_zone.pushButton_10.clicked.connect(lambda: ui.chek(new_zone))
    new_zone.pushButton_10.clicked.connect(lambda: ui.save_database_zones())
    new_zone.pushButton_9.clicked.connect(lambda: new_zone.clear_lineedits())
    ##================================================================= Add Envelopes Form
    envelope = envp.Ui_Dialog()
    dialog_envelope = QtWidgets.QDialog()
    envelope.setupUi(dialog_envelope)
    new_zone.pushButton_3.clicked.connect(lambda: ui.zone_name())
    new_zone.pushButton_3.clicked.connect(lambda: dialog_envelope.exec())
    new_zone.pushButton_8.clicked.connect(lambda: dialog_appliancefactor.exec())
    new_zone.pushButton_7.clicked.connect(lambda: dialog_heatgainfactor.exec())
    envelope.pushButton_3.clicked.connect(lambda: ui.dt_add_envelopes())
    ##================================================================= Add Infiltration
    infiltration = inf.Ui_Dialog()
    dialog_infiltration = QtWidgets.QDialog()
    infiltration.setupUi(dialog_infiltration)
    new_zone.pushButton.clicked.connect(lambda: dialog_infiltration.exec())
    new_zone.pushButton_4.clicked.connect(lambda: ui.infiltrationload())
    new_zone.pushButton_6.clicked.connect(lambda: dialog_lightfactor.exec())
    infiltration.pushButton.clicked.connect(lambda: infiltration.delete_line())
    infiltration.pushButton.clicked.connect(lambda: infiltration.reset_design_temp())
    infiltration.pushButton.clicked.connect(lambda: infiltration.reset_area_height())
    infiltration.pushButton.clicked.connect(lambda: infiltration.reset_construction_type())
    infiltration.pushButton_2.clicked.connect(lambda: ui.infiltration_flow())
    infiltration.pushButton_2.clicked.connect(lambda: dialog_infiltration.close())
    ##================================================================= Add Ventilation
    ventilation = vn.Ui_Dialog()
    dialog_ventilation = QtWidgets.QDialog()
    ventilation.setupUi(dialog_ventilation)
    new_zone.pushButton_2.clicked.connect(lambda: dialog_ventilation.exec())
    new_zone.pushButton_5.clicked.connect(lambda: ui.ventilationload())
    ventilation.pushButton.clicked.connect(lambda: ventilation.delete_line())
    ventilation.pushButton_2.clicked.connect(lambda: ui.ventilation_flow())
    ventilation.pushButton_2.clicked.connect(lambda: dialog_ventilation.close())
    new_zone.pushButton_11.clicked.connect(lambda: ui.show_total_heating_load())
    ###================================================================= Add New Envelope
    add_envelopes = adenvp.Ui_Dialog()
    dialog_addenvelopes = QtWidgets.QDialog()
    add_envelopes.setupUi(dialog_addenvelopes)
    envelope.pushButton_3.clicked.connect(lambda: dialog_addenvelopes.exec())
    envelope.pushButton_6.clicked.connect(lambda: ui.grab_envelope())
    envelope.pushButton_5.clicked.connect(lambda: ui.total_heatgain_through_envelope())
    envelope.pushButton.clicked.connect(lambda: envelope.tableWidget.clearContents())
    envelope.pushButton.clicked.connect(lambda: envelope.delete_row_layers())
    envelope.pushButton.clicked.connect(lambda: envelope.delete_zone_name_from())
    envelope.pushButton.clicked.connect(lambda: envelope.delete_total_heatgain_through_envelopes())
    envelope.pushButton.clicked.connect(lambda: add_envelopes.clear_data_dt())
    envelope.pushButton_2.clicked.connect(lambda: ui.show_zone_total_heatgain())
    ##================================================================= Add Envelopes Properties Form
    add_envelopes_properties = adevpr.Ui_Dialog()
    dialog_add_envelopes_properties = QtWidgets.QDialog()
    add_envelopes_properties.setupUi(dialog_add_envelopes_properties)
    add_envelopes.pushButton_5.clicked.connect(lambda: ui.net_envelope_area())
    add_envelopes.pushButton_5.clicked.connect(lambda: dialog_add_envelopes_properties.exec())
    add_envelopes_properties.pushButton_10.clicked.connect(lambda: ui.chek_envelopes_properties(add_envelopes_properties))
    add_envelopes.pushButton_10.clicked.connect(lambda: ui.chek_envelopes(add_envelopes))
    add_envelopes.pushButton_10.clicked.connect(lambda: ui.save_database_envelopes())
    add_envelopes.pushButton_9.clicked.connect(lambda: add_envelopes.clear_data())
    add_envelopes.pushButton_9.clicked.connect(lambda: add_envelopes.reset_envelope_type())
    add_envelopes_properties.pushButton_9.clicked.connect(lambda: add_envelopes_properties.clear_data())
    add_envelopes.pushButton_6.clicked.connect(lambda: add_envelopes.clear_data_dt())
    ##================================================================= Fenestration Form
    fenestrations = fnst.Ui_Dialog()
    dialog_fenestrations = QtWidgets.QDialog()
    fenestrations.setupUi(dialog_fenestrations)
    add_envelopes.pushButton_7.clicked.connect(lambda: ui.fenestration_envelopes_name())
    add_envelopes.pushButton_7.clicked.connect(lambda: ui.select_fenestration_according_to_area())
    fenestrations.pushButton_2.clicked.connect(lambda: fenestrations.total_u_factor_per_area())
    fenestrations.pushButton_2.clicked.connect(lambda: ui.fenestration_area_u())
    fenestrations.pushButton_6.clicked.connect(lambda: fenestrations.tableWidget.clearContents())
    fenestrations.pushButton_6.clicked.connect(lambda: fenestrations.delete_row_fenestration())
    fenestrations.pushButton_6.clicked.connect(lambda: fenestrations.delete_envelope_name())
    fenestrations.pushButton_6.clicked.connect(lambda: fenestrations.delete_total_u())
    add_envelopes.pushButton_3.clicked.connect(lambda: ui.select_opaque_surface())
    fenestrations.pushButton.clicked.connect(lambda: ui.save_fenestration_u_factor())
    ##================================================================= Add Fenestration Area Form
    fenestration_area = fnstar.Ui_Dialog()
    dialog_fenestration_area = QtWidgets.QDialog()
    fenestration_area.setupUi(dialog_fenestration_area)
    fenestrations.pushButton_3.clicked.connect(lambda: dialog_fenestration_area.exec())
    fenestration_area.pushButton_10.clicked.connect(lambda: ui.chek_fenestration(fenestration_area))
    fenestration_area.pushButton_10.clicked.connect(lambda: ui.save_database_fenestration())
    fenestration_area.pushButton_9.clicked.connect(lambda: fenestration_area.clear_data())
    fenestrations.pushButton_4.clicked.connect(lambda: ui.grab_fenestration())
    ###=======================================================================Add Fenestration U factor
    fenestration_ufactor = fnsu.Ui_Dialog()
    dialog_afenestration_ufactor = QtWidgets.QDialog()
    fenestration_ufactor.setupUi(dialog_afenestration_ufactor)
    fenestration_area.pushButton_5.clicked.connect(lambda: dialog_windowdoors.exec())
    fenestration_ufactor.pushButton_10.clicked.connect(lambda: ui.fenestration_installation_u_factors())
    fenestration_ufactor.pushButton_9.clicked.connect(lambda: fenestration_ufactor.reset_fenestration_u_factor_installation())
    ###====================================================== Add Indoor surface heat transfer (kcal/m2hC)
    add_hi = hi.Ui_Dialog()
    dialog_hi = QtWidgets.QDialog()
    add_hi.setupUi(dialog_hi)
    add_envelopes_properties.pushButton_4.clicked.connect(lambda: dialog_hi.exec())
    add_hi.pushButton_2.clicked.connect(lambda: ui.indoor())
    add_hi.pushButton_2.clicked.connect(lambda: dialog_hi.close())
    add_hi.pushButton.clicked.connect(lambda: add_hi.reset_position_surface())
    add_hi.pushButton.clicked.connect(lambda: add_hi.reset_surface_emittance())
    ##========================================================== Add Outdoor surface heat transfer (kcal/m2hC)
    add_ho = ho.Ui_Dialog()
    dialog_ho = QtWidgets.QDialog()
    add_ho.setupUi(dialog_ho)
    add_envelopes_properties.pushButton_5.clicked.connect(lambda: dialog_ho.exec())
    add_ho.pushButton_2.clicked.connect(lambda: ui.outdoor())
    add_ho.pushButton_2.clicked.connect(lambda: dialog_ho.close())
    add_ho.pushButton.clicked.connect(lambda: add_ho.reset_season())
    ###========================================================== Thermal Resistance Plane of Air Space (m2k/W)
    add_air = air.Ui_Dialog()
    dialog_air = QtWidgets.QDialog()
    add_air.setupUi(dialog_air)
    add_envelopes_properties.pushButton_7.clicked.connect(lambda: dialog_air.exec())
    add_air.pushButton_2.clicked.connect(lambda: ui.air_resistance())
    add_air.pushButton_2.clicked.connect(lambda: dialog_air.close())
    add_air.pushButton.clicked.connect(lambda: add_air.reset_air_space_temp())
    add_air.pushButton.clicked.connect(lambda: add_air.reset_air_apace_thickness())
    add_air.pushButton.clicked.connect(lambda: add_air.reset_effective_emittance())
    add_air.pushButton.clicked.connect(lambda: add_air.reset_air_position())
    ##====================================================================== Add New Layer of Envelopes
    add_layers = ly.Ui_Dialog()
    dialog_addlayers = QtWidgets.QDialog()
    add_layers.setupUi(dialog_addlayers)
    add_envelopes_properties.pushButton_3.clicked.connect(lambda: ui.envelope_envelopes_name())
    add_envelopes_properties.pushButton_3.clicked.connect(lambda: dialog_addlayers.exec())
    ##====================================================================== Add New insulation
    add_insulation = adinsl.Ui_Dialog()
    dialog_addinsulation = QtWidgets.QDialog()
    add_insulation.setupUi(dialog_addinsulation)
    add_layers.pushButton_3.clicked.connect(lambda: dialog_addinsulation.exec())
    add_insulation.pushButton.clicked.connect(lambda: ui.select_insulation())
    add_insulation.pushButton_10.clicked.connect(lambda: ui.chek_insulation(add_insulation))
    add_insulation.pushButton_10.clicked.connect(lambda: ui.save_database_insulation())
    add_insulation.pushButton_9.clicked.connect(lambda: add_insulation.clear_data())
    add_insulation.pushButton_9.clicked.connect(lambda: add_insulation.reset_insullation_type())
    add_layers.pushButton_4.clicked.connect(lambda: ui.grab_insullation())
    add_layers.pushButton_5.clicked.connect(lambda: ui.total_r_factor_per_layer_show())
    add_layers.pushButton_2.clicked.connect(lambda: add_layers.tableWidget.clearContents())
    add_layers.pushButton_2.clicked.connect(lambda: add_layers.delete_row_layers())
    add_layers.pushButton_2.clicked.connect(lambda: add_layers.delete_envelope_name())
    add_layers.pushButton_2.clicked.connect(lambda: add_layers.delete_total_r())
    add_layers.pushButton.clicked.connect(lambda: ui.total_r_add_envelopes_properties())
    ##====================================================================== Find insulation's R or K Factor
    # for insulation Material
    add_insulation0 = adinsl0.Ui_Dialog()
    dialog_addinsulation0 = QtWidgets.QDialog()
    add_insulation0.setupUi(dialog_addinsulation0)
    add_insulation0.pushButton_10.clicked.connect(lambda: ui.insulation_R_factor())
    add_insulation0.pushButton_10.clicked.connect(lambda: ui.insulation_K_factor())
    add_insulation0.pushButton_9.clicked.connect(lambda: add_insulation0.reset_insullation_material())
    ##====================================================================== Find insulation's R or K Factor
    # for Board and Siding Material
    add_insulation1 = adinsl1.Ui_Dialog()
    dialog_addinsulation1 = QtWidgets.QDialog()
    add_insulation1.setupUi(dialog_addinsulation1)
    add_insulation1.pushButton_10.clicked.connect(lambda: ui.insulation_R_factor())
    add_insulation1.pushButton_10.clicked.connect(lambda: ui.insulation_K_factor())
    add_insulation1.pushButton_9.clicked.connect(lambda: add_insulation1.reset_board_material())
    ##====================================================================== Find insulation's R or K Factor
    # for Membrane Materials
    add_insulation2 = adinsl2.Ui_Dialog()
    dialog_addinsulation2 = QtWidgets.QDialog()
    add_insulation2.setupUi(dialog_addinsulation2)
    add_insulation2.pushButton_10.clicked.connect(lambda: ui.insulation_R_factor())
    add_insulation2.pushButton_10.clicked.connect(lambda: ui.insulation_K_factor())
    add_insulation2.pushButton_9.clicked.connect(lambda: add_insulation2.reset_membrane_material())
    ##====================================================================== Find insulation's R or K Factor
    # for Finish Flooring Materials
    add_insulation3 = adinsl3.Ui_Dialog()
    dialog_addinsulation3 = QtWidgets.QDialog()
    add_insulation3.setupUi(dialog_addinsulation3)
    add_insulation3.pushButton_10.clicked.connect(lambda: ui.insulation_R_factor())
    add_insulation3.pushButton_10.clicked.connect(lambda: ui.insulation_K_factor())
    add_insulation3.pushButton_9.clicked.connect(lambda: add_insulation3.reset_finish_flooring())
    ##====================================================================== Find insulation's R or K Factor
    # for Roofing Materials
    add_insulation4 = adinsl4.Ui_Dialog()
    dialog_addinsulation4 = QtWidgets.QDialog()
    add_insulation4.setupUi(dialog_addinsulation4)
    add_insulation4.pushButton_10.clicked.connect(lambda: ui.insulation_R_factor())
    add_insulation4.pushButton_10.clicked.connect(lambda: ui.insulation_K_factor())
    add_insulation4.pushButton_9.clicked.connect(lambda: add_insulation4.reset_roofing_material())
    ##====================================================================== Find insulation's R or K Factor
    # for Plastering Materials
    add_insulation5 = adinsl5.Ui_Dialog()
    dialog_addinsulation5 = QtWidgets.QDialog()
    add_insulation5.setupUi(dialog_addinsulation5)
    add_insulation5.pushButton_10.clicked.connect(lambda: ui.insulation_R_factor())
    add_insulation5.pushButton_10.clicked.connect(lambda: ui.insulation_K_factor())
    add_insulation5.pushButton_9.clicked.connect(lambda: add_insulation5.reset_plastering_material())
    ##====================================================================== Find insulation's R or K Factor
    # for Masonry Materials
    add_insulation6 = adinsl6.Ui_Dialog()
    dialog_addinsulation6 = QtWidgets.QDialog()
    add_insulation6.setupUi(dialog_addinsulation6)
    add_insulation6.pushButton_10.clicked.connect(lambda: ui.insulation_R_factor())
    add_insulation6.pushButton_10.clicked.connect(lambda: ui.insulation_K_factor())
    add_insulation6.pushButton_9.clicked.connect(lambda: add_insulation6.reset_masonry_material())
    ##====================================================================== Find insulation's R or K Factor
    # for Woods
    add_insulation7 = adinsl7.Ui_Dialog()
    dialog_addinsulation7 = QtWidgets.QDialog()
    add_insulation7.setupUi(dialog_addinsulation7)
    add_insulation7.pushButton_10.clicked.connect(lambda: ui.insulation_R_factor())
    add_insulation7.pushButton_10.clicked.connect(lambda: ui.insulation_K_factor())
    add_insulation7.pushButton_9.clicked.connect(lambda: add_insulation7.reset_wood_type())
    ##====================================================================== Select fenestration type
    window_door = wd.Ui_Dialog()
    dialog_windowdoors = QtWidgets.QDialog()
    window_door.setupUi(dialog_windowdoors)
    window_door.pushButton.clicked.connect(lambda: dialog_door.exec())
    window_door.pushButton_2.clicked.connect(lambda: dialog_afenestration_ufactor.exec())
    ##====================================================================== Select door type
    door = d.Ui_Dialog()
    dialog_door = QtWidgets.QDialog()
    door.setupUi(dialog_door)
    door.pushButton_10.clicked.connect(lambda: ui.select_door_type())
    door.pushButton_9.clicked.connect(lambda: door.reset_door_type())
    ##====================================================================== door1 u factor Calculation and Show
    door01 = d1.Ui_Dialog()
    dialog_door01 = QtWidgets.QDialog()
    door01.setupUi(dialog_door01)
    door01.pushButton_10.clicked.connect(lambda: ui.door_1_u_factor())
    door01.pushButton_10.clicked.connect(lambda: ui.door_1_insu_u_factor())
    door01.pushButton_10.clicked.connect(lambda: dialog_door01.close())
    door01.pushButton_10.clicked.connect(lambda: dialog_door.close())
    door01.pushButton_10.clicked.connect(lambda: dialog_windowdoors.close())
    door01.pushButton_9.clicked.connect(lambda: door01.reset_door1_u())
    ##====================================================================== door2 u factor Calculation and Show
    door02 = d2.Ui_Dialog()
    dialog_door02 = QtWidgets.QDialog()
    door02.setupUi(dialog_door02)
    door02.pushButton_10.clicked.connect(lambda: ui.door_2_u_factor())
    door02.pushButton_10.clicked.connect(lambda: ui.door_2_ins_u_factor())
    door02.pushButton_10.clicked.connect(lambda: dialog_door02.close())
    door02.pushButton_10.clicked.connect(lambda: dialog_door.close())
    door02.pushButton_10.clicked.connect(lambda: dialog_windowdoors.close())
    door02.pushButton_9.clicked.connect(lambda: door02.reset_door2_u())
    ##======================================================================door3 u factor Calculation and Show
    door03 = d3.Ui_Dialog()
    dialog_door03 = QtWidgets.QDialog()
    door03.setupUi(dialog_door03)
    door03.pushButton_10.clicked.connect(lambda: ui.door_3_u_factor())
    door03.pushButton_10.clicked.connect(lambda: ui.door_3_ins_u_factor())
    door03.pushButton_10.clicked.connect(lambda: dialog_door03.close())
    door03.pushButton_10.clicked.connect(lambda: dialog_door.close())
    door03.pushButton_10.clicked.connect(lambda: dialog_windowdoors.close())
    door03.pushButton_9.clicked.connect(lambda: door03.reset_door3_u())
    ##======================================================================door4 u factor Calculation and Show
    door04 = d4.Ui_Dialog()
    dialog_door04 = QtWidgets.QDialog()
    door04.setupUi(dialog_door04)
    door04.pushButton_10.clicked.connect(lambda: ui.door_4_u_factor())
    door04.pushButton_10.clicked.connect(lambda: ui.door_4_ins_u_factor())
    door04.pushButton_10.clicked.connect(lambda: dialog_door04.close())
    door04.pushButton_10.clicked.connect(lambda: dialog_door.close())
    door04.pushButton_10.clicked.connect(lambda: dialog_windowdoors.close())
    door04.pushButton_9.clicked.connect(lambda: door04.reset_door4_u())
    ##======================================================================Wall opaque factor calculation
    wall_cf = wall.Ui_Dialog()
    dialog_wallcf = QtWidgets.QDialog()
    wall_cf.setupUi(dialog_wallcf)
    wall_cf.pushButton_2.clicked.connect(lambda: ui.show_total_cffactors_walls())
    wall_cf.pushButton.clicked.connect(lambda: wall_cf.reset_cf_wall())
    wall_cf.pushButton.clicked.connect(lambda: wall_cf.reset_cf_wall_dt())
    ##======================================================================Floor opaque factor calculation
    floor_cf = floor.Ui_Dialog()
    dialog_floorcf = QtWidgets.QDialog()
    floor_cf.setupUi(dialog_floorcf)
    floor_cf.pushButton_2.clicked.connect(lambda: ui.show_total_cffactors_floors())
    floor_cf.pushButton.clicked.connect(lambda: floor_cf.reset_cf_floor())
    floor_cf.pushButton.clicked.connect(lambda: floor_cf.reset_cf_floor_dt())
    ##======================================================================Ceiling opaque factor calculation
    ceiling_cf = ceiling.Ui_Dialog()
    dialog_ceilingcf = QtWidgets.QDialog()
    ceiling_cf.setupUi(dialog_ceilingcf)
    ceiling_cf.pushButton_2.clicked.connect(lambda: ui.show_total_cffactors_ceilings())
    ceiling_cf.pushButton.clicked.connect(lambda: ceiling_cf.reset_cf_ceiling())
    ceiling_cf.pushButton.clicked.connect(lambda: ceiling_cf.reset_cf_ceiling_dt())
    ##======================================================================Slab opaque factor calculation
    slab_cf = slab.Ui_Dialog()
    dialog_slabcf = QtWidgets.QDialog()
    slab_cf.setupUi(dialog_slabcf)
    slab_cf.pushButton_2.clicked.connect(lambda: ui.show_total_cffactors_slabs())
    slab_cf.pushButton.clicked.connect(lambda: slab_cf.reset_cf_slab())
    ##======================================================================SHGC factor calculation
    shgcfactor = shgc.Ui_Dialog()
    dialog_shgcfactor = QtWidgets.QDialog()
    shgcfactor.setupUi(dialog_shgcfactor)
    add_envelopes.pushButton_4.clicked.connect(lambda: dialog_shgcfactor.exec())
    shgcfactor.pushButton_10.clicked.connect(lambda: ui.show_total_cooling_surface_loads())
    shgcfactor.pushButton_9.clicked.connect(lambda: shgcfactor.reset_shgc_factors())
    ##======================================================================Appliance factor calculation
    appliance_factor = appliance.Ui_Dialog()
    dialog_appliancefactor = QtWidgets.QDialog()
    appliance_factor.setupUi(dialog_appliancefactor)
    appliance_factor.pushButton_3.clicked.connect(lambda: dialog_addappliances.exec())
    appliance_factor.pushButton_4.clicked.connect(lambda: ui.grab_appliances())
    appliance_factor.pushButton_2.clicked.connect(lambda: ui.show_appliance_watts())
    appliance_factor.pushButton_6.clicked.connect(lambda: appliance_factor.delete_row_app())
    appliance_factor.pushButton_6.clicked.connect(lambda: appliance_factor.delete_total_totalapp())
    appliance_factor.pushButton.clicked.connect(lambda: ui.show_total_heat_app())
    ##======================================================================Add Appliances
    add_appliances = addappl.Ui_Dialog()
    dialog_addappliances = QtWidgets.QDialog()
    add_appliances.setupUi(dialog_addappliances)
    add_appliances.pushButton_2.clicked.connect(lambda: ui.save_database_appliances())
    add_appliances.pushButton_2.clicked.connect(lambda: ui.chek_appliance(add_appliances))
    add_appliances.pushButton.clicked.connect(lambda: add_appliances.reset_appliance_factors())
    ##======================================================================Lights factor calculation
    light_factor = lights.Ui_Dialog()
    dialog_lightfactor = QtWidgets.QDialog()
    light_factor.setupUi(dialog_lightfactor)
    light_factor.pushButton_3.clicked.connect(lambda: dialog_addlights.exec())
    light_factor.pushButton_4.clicked.connect(lambda: ui.grab_lights())
    light_factor.pushButton_2.clicked.connect(lambda: ui.show_light_watts())
    light_factor.pushButton_6.clicked.connect(lambda: light_factor.delete_row_light())
    light_factor.pushButton_6.clicked.connect(lambda: light_factor.delete_total_totallight())
    light_factor.pushButton.clicked.connect(lambda: ui.show_total_heat_light())
    ##======================================================================Add Lights
    add_lights = adlight.Ui_Dialog()
    dialog_addlights = QtWidgets.QDialog()
    add_lights.setupUi(dialog_addlights)
    add_lights.pushButton_2.clicked.connect(lambda: ui.save_database_lights())
    add_lights.pushButton_2.clicked.connect(lambda: ui.chek_lights(add_lights))
    add_lights.pushButton.clicked.connect(lambda: add_lights.reset_light_factors())
    ##======================================================================heatgain factor calculation
    heatgain_factor = heatgain.Ui_Dialog()
    dialog_heatgainfactor = QtWidgets.QDialog()
    heatgain_factor.setupUi(dialog_heatgainfactor)
    heatgain_factor.pushButton_2.clicked.connect(lambda: ui.show_total_heat_gain())
    heatgain_factor.pushButton.clicked.connect(lambda: heatgain_factor.reset_heat_gain())
    ###===================================================================================================

    sys.exit(app.exec())
