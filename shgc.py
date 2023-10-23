
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 650)
        Dialog.setMinimumSize(QtCore.QSize(800, 650))
        Dialog.setMaximumSize(QtCore.QSize(800, 650))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("srcs/oven_6301569.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        self.pushButton_9 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_9.setGeometry(QtCore.QRect(170, 550, 121, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 53, 16))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 144, 122))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 98, 69))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 26, 8))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 35, 11))
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
        brush = QtGui.QBrush(QtGui.QColor(240, 53, 16))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 154, 135))
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
        brush = QtGui.QBrush(QtGui.QColor(240, 53, 16))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 144, 122))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 98, 69))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 26, 8))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 35, 11))
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
        brush = QtGui.QBrush(QtGui.QColor(240, 53, 16))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 154, 135))
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
        brush = QtGui.QBrush(QtGui.QColor(120, 26, 8))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 53, 16))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 144, 122))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 98, 69))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 26, 8))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 35, 11))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 26, 8))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 26, 8))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 53, 16))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 53, 16))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 53, 16))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 26, 8, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        self.pushButton_9.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_10.setGeometry(QtCore.QRect(520, 550, 121, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(116, 199, 116))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 255, 192))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 227, 154))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 99, 58))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(77, 133, 77))
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
        brush = QtGui.QBrush(QtGui.QColor(116, 199, 116))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 227, 185))
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
        brush = QtGui.QBrush(QtGui.QColor(116, 199, 116))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 255, 192))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 227, 154))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 99, 58))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(77, 133, 77))
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
        brush = QtGui.QBrush(QtGui.QColor(116, 199, 116))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 227, 185))
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
        brush = QtGui.QBrush(QtGui.QColor(58, 99, 58))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(116, 199, 116))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 255, 192))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 227, 154))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 99, 58))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(77, 133, 77))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 99, 58))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 99, 58))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(116, 199, 116))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(116, 199, 116))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(116, 199, 116))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 99, 58, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        self.pushButton_10.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_10.setObjectName("pushButton_10")
        self.comboBox = QtWidgets.QComboBox(parent=Dialog)
        self.comboBox.setGeometry(QtCore.QRect(120, 52, 661, 24))
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(parent=Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(140, 91, 311, 24))
        self.comboBox_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(20, 50, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 93, 101, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox_4 = QtWidgets.QComboBox(parent=Dialog)
        self.comboBox_4.setGeometry(QtCore.QRect(150, 386, 291, 24))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_5 = QtWidgets.QComboBox(parent=Dialog)
        self.comboBox_5.setGeometry(QtCore.QRect(140, 427, 91, 24))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.label_4 = QtWidgets.QLabel(parent=Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 384, 112, 24))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(parent=Dialog)
        self.label_7.setGeometry(QtCore.QRect(20, 427, 106, 24))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_10 = QtWidgets.QLabel(parent=Dialog)
        self.label_10.setGeometry(QtCore.QRect(20, 470, 137, 24))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(180, 470, 113, 24))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.comboBox_7 = QtWidgets.QComboBox(parent=Dialog)
        self.comboBox_7.setGeometry(QtCore.QRect(110, 338, 151, 24))
        self.comboBox_7.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.label_11 = QtWidgets.QLabel(parent=Dialog)
        self.label_11.setGeometry(QtCore.QRect(20, 337, 106, 24))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.comboBox_6 = QtWidgets.QComboBox(parent=Dialog)
        self.comboBox_6.setGeometry(QtCore.QRect(230, 130, 261, 24))
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.label_9 = QtWidgets.QLabel(parent=Dialog)
        self.label_9.setGeometry(QtCore.QRect(20, 130, 187, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(370, 210, 113, 24))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(190, 250, 113, 24))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(170, 170, 113, 24))
        self.lineEdit.setObjectName("lineEdit")
        self.label_5 = QtWidgets.QLabel(parent=Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 170, 136, 24))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_8 = QtWidgets.QLabel(parent=Dialog)
        self.label_8.setGeometry(QtCore.QRect(20, 250, 155, 24))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_6 = QtWidgets.QLabel(parent=Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 210, 335, 24))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.comboBox_3 = QtWidgets.QComboBox(parent=Dialog)
        self.comboBox_3.setGeometry(QtCore.QRect(240, 295, 281, 24))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 293, 206, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def shgc_factors(self):
        self.glazing_type = self.comboBox.currentIndex()
        self.installation_type = self.comboBox_2.currentIndex()
        if self.glazing_type == 0:
            if self.installation_type == 1:
                self.shg_fc = 0.78
            elif self.installation_type == 2:
                self.shg_fc = 0.79
            elif self.installation_type == 3:
                self.shg_fc = 0.70
            else:
                self.shg_fc = 0.76
        elif self.glazing_type == 1:
            if self.installation_type == 1:
                self.shg_fc = 0.74
            elif self.installation_type == 2:
                self.shg_fc = 0.74
            elif self.installation_type == 3:
                self.shg_fc = 0.66
            else:
                self.shg_fc = 0.72
        elif self.glazing_type == 2:
            if self.installation_type == 1:
                self.shg_fc = 0.67
            elif self.installation_type == 2:
                self.shg_fc = 0.67
            elif self.installation_type == 3:
                self.shg_fc = 0.59
            else:
                self.shg_fc = 0.65
        elif self.glazing_type == 3:
            if self.installation_type == 1:
                self.shg_fc = 0.57
            elif self.installation_type == 2:
                self.shg_fc = 0.57
            elif self.installation_type == 3:
                self.shg_fc = 0.50
            else:
                self.shg_fc = 0.55
        elif self.glazing_type == 4:
            if self.installation_type == 1:
                self.shg_fc = 0.64
            elif self.installation_type == 2:
                self.shg_fc = 0.64
            elif self.installation_type == 3:
                self.shg_fc = 0.57
            else:
                self.shg_fc = 0.62
        elif self.glazing_type == 5:
            if self.installation_type == 1:
                self.shg_fc = 0.55
            elif self.installation_type == 2:
                self.shg_fc = 0.55
            elif self.installation_type == 3:
                self.shg_fc = 0.49
            else:
                self.shg_fc = 0.53
        elif self.glazing_type == 6:
            if self.installation_type == 1:
                self.shg_fc = 0.64
            elif self.installation_type == 2:
                self.shg_fc = 0.64
            elif self.installation_type == 3:
                self.shg_fc = 0.57
            else:
                self.shg_fc = 0.62
        elif self.glazing_type == 7:
            if self.installation_type == 1:
                self.shg_fc = 0.54
            elif self.installation_type == 2:
                self.shg_fc = 0.54
            elif self.installation_type == 3:
                self.shg_fc = 0.48
            else:
                self.shg_fc = 0.52
        elif self.glazing_type == 8:
            if self.installation_type == 1:
                self.shg_fc = 0.57
            elif self.installation_type == 2:
                self.shg_fc = 0.57
            elif self.installation_type == 3:
                self.shg_fc = 0.50
            else:
                self.shg_fc = 0.55
        elif self.glazing_type == 9:
            if self.installation_type == 1:
                self.shg_fc = 0.18
            elif self.installation_type == 2:
                self.shg_fc = 0.18
            elif self.installation_type == 3:
                self.shg_fc = 0.16
            else:
                self.shg_fc = 0.17
        elif self.glazing_type == 10:
            if self.installation_type == 1:
                self.shg_fc = 0.24
            elif self.installation_type == 2:
                self.shg_fc = 0.24
            elif self.installation_type == 3:
                self.shg_fc = 0.21
            else:
                self.shg_fc = 0.22
        elif self.glazing_type == 11:
            if self.installation_type == 1:
                self.shg_fc = 0.29
            elif self.installation_type == 2:
                self.shg_fc = 0.29
            elif self.installation_type == 3:
                self.shg_fc = 0.26
            else:
                self.shg_fc = 0.28
        elif self.glazing_type == 12:
            if self.installation_type == 1:
                self.shg_fc = 0.24
            elif self.installation_type == 2:
                self.shg_fc = 0.24
            elif self.installation_type == 3:
                self.shg_fc = 0.21
            else:
                self.shg_fc = 0.22
        elif self.glazing_type == 13:
            if self.installation_type == 1:
                self.shg_fc = 0.27
            elif self.installation_type == 2:
                self.shg_fc = 0.27
            elif self.installation_type == 3:
                self.shg_fc = 0.24
            else:
                self.shg_fc = 0.26
        elif self.glazing_type == 14:
            if self.installation_type == 1:
                self.shg_fc = 0.36
            elif self.installation_type == 2:
                self.shg_fc = 0.36
            elif self.installation_type == 3:
                self.shg_fc = 0.32
            else:
                self.shg_fc = 0.35
        elif self.glazing_type == 15:
            if self.installation_type == 1:
                self.shg_fc = 0.69
            elif self.installation_type == 2:
                self.shg_fc = 0.70
            elif self.installation_type == 3:
                self.shg_fc = 0.62
            else:
                self.shg_fc = 0.67
        elif self.glazing_type == 16:
            if self.installation_type == 1:
                self.shg_fc = 0.64
            elif self.installation_type == 2:
                self.shg_fc = 0.64
            elif self.installation_type == 3:
                self.shg_fc = 0.57
            else:
                self.shg_fc = 0.62
        elif self.glazing_type == 17:
            if self.installation_type == 1:
                self.shg_fc = 0.57
            elif self.installation_type == 2:
                self.shg_fc = 0.57
            elif self.installation_type == 3:
                self.shg_fc = 0.50
            else:
                self.shg_fc = 0.55
        elif self.glazing_type == 18:
            if self.installation_type == 1:
                self.shg_fc = 0.45
            elif self.installation_type == 2:
                self.shg_fc = 0.45
            elif self.installation_type == 3:
                self.shg_fc = 0.40
            else:
                self.shg_fc = 0.43
        elif self.glazing_type == 19:
            if self.installation_type == 1:
                self.shg_fc = 0.55
            elif self.installation_type == 2:
                self.shg_fc = 0.55
            elif self.installation_type == 3:
                self.shg_fc = 0.49
            else:
                self.shg_fc = 0.53
        elif self.glazing_type == 20:
            if self.installation_type == 1:
                self.shg_fc = 0.45
            elif self.installation_type == 2:
                self.shg_fc = 0.45
            elif self.installation_type == 3:
                self.shg_fc = 0.40
            else:
                self.shg_fc = 0.43
        elif self.glazing_type == 21:
            if self.installation_type == 1:
                self.shg_fc = 0.55
            elif self.installation_type == 2:
                self.shg_fc = 0.55
            elif self.installation_type == 3:
                self.shg_fc = 0.49
            else:
                self.shg_fc = 0.53
        elif self.glazing_type == 22:
            if self.installation_type == 1:
                self.shg_fc = 0.43
            elif self.installation_type == 2:
                self.shg_fc = 0.43
            elif self.installation_type == 3:
                self.shg_fc = 0.38
            else:
                self.shg_fc = 0.42
        elif self.glazing_type == 23:
            if self.installation_type == 1:
                self.shg_fc = 0.46
            elif self.installation_type == 2:
                self.shg_fc = 0.46
            elif self.installation_type == 3:
                self.shg_fc = 0.41
            else:
                self.shg_fc = 0.44
        elif self.glazing_type == 24:
            if self.installation_type == 1:
                self.shg_fc = 0.36
            elif self.installation_type == 2:
                self.shg_fc = 0.36
            elif self.installation_type == 3:
                self.shg_fc = 0.32
            else:
                self.shg_fc = 0.35
        elif self.glazing_type == 25:
            if self.installation_type == 1:
                self.shg_fc = 0.13
            elif self.installation_type == 2:
                self.shg_fc = 0.13
            elif self.installation_type == 3:
                self.shg_fc = 0.11
            else:
                self.shg_fc = 0.12
        elif self.glazing_type == 26:
            if self.installation_type == 1:
                self.shg_fc = 0.17
            elif self.installation_type == 2:
                self.shg_fc = 0.16
            elif self.installation_type == 3:
                self.shg_fc = 0.14
            else:
                self.shg_fc = 0.15
        elif self.glazing_type == 27:
            if self.installation_type == 1:
                self.shg_fc = 0.21
            elif self.installation_type == 2:
                self.shg_fc = 0.21
            elif self.installation_type == 3:
                self.shg_fc = 0.18
            else:
                self.shg_fc = 0.20
        elif self.glazing_type == 28:
            if self.installation_type == 1:
                self.shg_fc = 0.16
            elif self.installation_type == 2:
                self.shg_fc = 0.16
            elif self.installation_type == 3:
                self.shg_fc = 0.14
            else:
                self.shg_fc = 0.14
        elif self.glazing_type == 29:
            if self.installation_type == 1:
                self.shg_fc = 0.20
            elif self.installation_type == 2:
                self.shg_fc = 0.20
            elif self.installation_type == 3:
                self.shg_fc = 0.18
            else:
                self.shg_fc = 0.19
        elif self.glazing_type == 30:
            if self.installation_type == 1:
                self.shg_fc = 0.27
            elif self.installation_type == 2:
                self.shg_fc = 0.27
            elif self.installation_type == 3:
                self.shg_fc = 0.24
            else:
                self.shg_fc = 0.26
        elif self.glazing_type == 31:
            if self.installation_type == 1:
                self.shg_fc = 0.59
            elif self.installation_type == 2:
                self.shg_fc = 0.60
            elif self.installation_type == 3:
                self.shg_fc = 0.53
            else:
                self.shg_fc = 0.58
        elif self.glazing_type == 32:
            if self.installation_type == 1:
                self.shg_fc = 0.55
            elif self.installation_type == 2:
                self.shg_fc = 0.55
            elif self.installation_type == 3:
                self.shg_fc = 0.49
            else:
                self.shg_fc = 0.53
        elif self.glazing_type == 33:
            if self.installation_type == 1:
                self.shg_fc = 0.64
            elif self.installation_type == 2:
                self.shg_fc = 0.64
            elif self.installation_type == 3:
                self.shg_fc = 0.57
            else:
                self.shg_fc = 0.62
        elif self.glazing_type == 34:
            if self.installation_type == 1:
                self.shg_fc = 0.59
            elif self.installation_type == 2:
                self.shg_fc = 0.60
            elif self.installation_type == 3:
                self.shg_fc = 0.53
            else:
                self.shg_fc = 0.58
        elif self.glazing_type == 35:
            if self.installation_type == 1:
                self.shg_fc = 0.52
            elif self.installation_type == 2:
                self.shg_fc = 0.52
            elif self.installation_type == 3:
                self.shg_fc = 0.46
            else:
                self.shg_fc = 0.51
        elif self.glazing_type == 36:
            if self.installation_type == 1:
                self.shg_fc = 0.42
            elif self.installation_type == 2:
                self.shg_fc = 0.42
            elif self.installation_type == 3:
                self.shg_fc = 0.37
            else:
                self.shg_fc = 0.40
        elif self.glazing_type == 37:
            if self.installation_type == 1:
                self.shg_fc = 0.50
            elif self.installation_type == 2:
                self.shg_fc = 0.50
            elif self.installation_type == 3:
                self.shg_fc = 0.45
            else:
                self.shg_fc = 0.49
        elif self.glazing_type == 38:
            if self.installation_type == 1:
                self.shg_fc = 0.38
            elif self.installation_type == 2:
                self.shg_fc = 0.38
            elif self.installation_type == 3:
                self.shg_fc = 0.34
            else:
                self.shg_fc = 0.36
        elif self.glazing_type == 39:
            if self.installation_type == 1:
                self.shg_fc = 0.50
            elif self.installation_type == 2:
                self.shg_fc = 0.50
            elif self.installation_type == 3:
                self.shg_fc = 0.44
            else:
                self.shg_fc = 0.48
        elif self.glazing_type == 40:
            if self.installation_type == 1:
                self.shg_fc = 0.36
            elif self.installation_type == 2:
                self.shg_fc = 0.36
            elif self.installation_type == 3:
                self.shg_fc = 0.32
            else:
                self.shg_fc = 0.35
        elif self.glazing_type == 41:
            if self.installation_type == 1:
                self.shg_fc = 0.42
            elif self.installation_type == 2:
                self.shg_fc = 0.42
            elif self.installation_type == 3:
                self.shg_fc = 0.37
            else:
                self.shg_fc = 0.40
        elif self.glazing_type == 42:
            if self.installation_type == 1:
                self.shg_fc = 0.32
            elif self.installation_type == 2:
                self.shg_fc = 0.32
            elif self.installation_type == 3:
                self.shg_fc = 0.28
            else:
                self.shg_fc = 0.30
        elif self.glazing_type == 43:
            if self.installation_type == 1:
                self.shg_fc = 0.59
            elif self.installation_type == 2:
                self.shg_fc = 0.60
            elif self.installation_type == 3:
                self.shg_fc = 0.53
            else:
                self.shg_fc = 0.58
        elif self.glazing_type == 44:
            if self.installation_type == 1:
                self.shg_fc = 0.55
            elif self.installation_type == 2:
                self.shg_fc = 0.55
            elif self.installation_type == 3:
                self.shg_fc = 0.49
            else:
                self.shg_fc = 0.53
        elif self.glazing_type == 45:
            if self.installation_type == 1:
                self.shg_fc = 0.55
            elif self.installation_type == 2:
                self.shg_fc = 0.55
            elif self.installation_type == 3:
                self.shg_fc = 0.49
            else:
                self.shg_fc = 0.53
        elif self.glazing_type == 46:
            if self.installation_type == 1:
                self.shg_fc = 0.51
            elif self.installation_type == 2:
                self.shg_fc = 0.52
            elif self.installation_type == 3:
                self.shg_fc = 0.46
            else:
                self.shg_fc = 0.50
        elif self.glazing_type == 47:
            if self.installation_type == 1:
                self.shg_fc = 0.44
            elif self.installation_type == 2:
                self.shg_fc = 0.44
            elif self.installation_type == 3:
                self.shg_fc = 0.39
            else:
                self.shg_fc = 0.43
        elif self.glazing_type == 48:
            if self.installation_type == 1:
                self.shg_fc = 0.36
            elif self.installation_type == 2:
                self.shg_fc = 0.36
            elif self.installation_type == 3:
                self.shg_fc = 0.32
            else:
                self.shg_fc = 0.35
        elif self.glazing_type == 49:
            if self.installation_type == 1:
                self.shg_fc = 0.42
            elif self.installation_type == 2:
                self.shg_fc = 0.43
            elif self.installation_type == 3:
                self.shg_fc = 0.38
            else:
                self.shg_fc = 0.31
        elif self.glazing_type == 50:
            if self.installation_type == 1:
                self.shg_fc = 0.34
            elif self.installation_type == 2:
                self.shg_fc = 0.34
            elif self.installation_type == 3:
                self.shg_fc = 0.20
            else:
                self.shg_fc = 0.32
        elif self.glazing_type == 51:
            if self.installation_type == 1:
                self.shg_fc = 0.42
            elif self.installation_type == 2:
                self.shg_fc = 0.43
            elif self.installation_type == 3:
                self.shg_fc = 0.38
            else:
                self.shg_fc = 0.41
        elif self.glazing_type == 52:
            if self.installation_type == 1:
                self.shg_fc = 0.32
            elif self.installation_type == 2:
                self.shg_fc = 0.32
            elif self.installation_type == 3:
                self.shg_fc = 0.28
            else:
                self.shg_fc = 0.30
        elif self.glazing_type == 53:
            if self.installation_type == 1:
                self.shg_fc = 0.36
            elif self.installation_type == 2:
                self.shg_fc = 0.36
            elif self.installation_type == 3:
                self.shg_fc = 0.32
            else:
                self.shg_fc = 0.35
        elif self.glazing_type == 54:
            if self.installation_type == 1:
                self.shg_fc = 0.29
            elif self.installation_type == 2:
                self.shg_fc = 0.29
            elif self.installation_type == 3:
                self.shg_fc = 0.26
            else:
                self.shg_fc = 0.28
        elif self.glazing_type == 55:
            if self.installation_type == 1:
                self.shg_fc = 0.38
            elif self.installation_type == 2:
                self.shg_fc = 0.38
            elif self.installation_type == 3:
                self.shg_fc = 0.34
            else:
                self.shg_fc = 0.36
        elif self.glazing_type == 56:
            if self.installation_type == 1:
                self.shg_fc = 0.34
            elif self.installation_type == 2:
                self.shg_fc = 0.34
            elif self.installation_type == 3:
                self.shg_fc = 0.30
            else:
                self.shg_fc = 0.33
        elif self.glazing_type == 57:
            if self.installation_type == 1:
                self.shg_fc = 0.25
            elif self.installation_type == 2:
                self.shg_fc = 0.25
            elif self.installation_type == 3:
                self.shg_fc = 0.22
            else:
                self.shg_fc = 0.23
        elif self.glazing_type == 58:
            if self.installation_type == 1:
                self.shg_fc = 0.29
            elif self.installation_type == 2:
                self.shg_fc = 0.29
            elif self.installation_type == 3:
                self.shg_fc = 0.26
            else:
                self.shg_fc = 0.28
        elif self.glazing_type == 59:
            if self.installation_type == 1:
                self.shg_fc = 0.23
            elif self.installation_type == 2:
                self.shg_fc = 0.23
            elif self.installation_type == 3:
                self.shg_fc = 0.20
            else:
                self.shg_fc = 0.21
        elif self.glazing_type == 60:
            if self.installation_type == 1:
                self.shg_fc = 0.26
            elif self.installation_type == 2:
                self.shg_fc = 0.25
            elif self.installation_type == 3:
                self.shg_fc = 0.22
            else:
                self.shg_fc = 0.24
        elif self.glazing_type == 61:
            if self.installation_type == 1:
                self.shg_fc = 0.26
            elif self.installation_type == 2:
                self.shg_fc = 0.25
            elif self.installation_type == 3:
                self.shg_fc = 0.22
            else:
                self.shg_fc = 0.24
        elif self.glazing_type == 62:
            if self.installation_type == 1:
                self.shg_fc = 0.62
            elif self.installation_type == 2:
                self.shg_fc = 0.62
            elif self.installation_type == 3:
                self.shg_fc = 0.55
            else:
                self.shg_fc = 0.60
        elif self.glazing_type == 63:
            if self.installation_type == 1:
                self.shg_fc = 0.56
            elif self.installation_type == 2:
                self.shg_fc = 0.56
            elif self.installation_type == 3:
                self.shg_fc = 0.50
            else:
                self.shg_fc = 0.54
        elif self.glazing_type == 64:
            if self.installation_type == 1:
                self.shg_fc = 0.30
            elif self.installation_type == 2:
                self.shg_fc = 0.30
            elif self.installation_type == 3:
                self.shg_fc = 0.26
            else:
                self.shg_fc = 0.29
        elif self.glazing_type == 65:
            if self.installation_type == 1:
                self.shg_fc = 0.55
            elif self.installation_type == 2:
                self.shg_fc = 0.55
            elif self.installation_type == 3:
                self.shg_fc = 0.49
            else:
                self.shg_fc = 0.53
        elif self.glazing_type == 66:
            if self.installation_type == 1:
                self.shg_fc = 0.49
            elif self.installation_type == 2:
                self.shg_fc = 0.49
            elif self.installation_type == 3:
                self.shg_fc = 0.43
            else:
                self.shg_fc = 0.47
        elif self.glazing_type == 67:
            if self.installation_type == 1:
                self.shg_fc = 0.57
            elif self.installation_type == 2:
                self.shg_fc = 0.57
            elif self.installation_type == 3:
                self.shg_fc = 0.50
            else:
                self.shg_fc = 0.55
        elif self.glazing_type == 68:
            if self.installation_type == 1:
                self.shg_fc = 0.51
            elif self.installation_type == 2:
                self.shg_fc = 0.52
            elif self.installation_type == 3:
                self.shg_fc = 0.46
            else:
                self.shg_fc = 0.50
        elif self.glazing_type == 69:
            if self.installation_type == 1:
                self.shg_fc = 0.38
            elif self.installation_type == 2:
                self.shg_fc = 0.38
            elif self.installation_type == 3:
                self.shg_fc = 0.34
            else:
                self.shg_fc = 0.36
        elif self.glazing_type == 70:
            if self.installation_type == 1:
                self.shg_fc = 0.34
            elif self.installation_type == 2:
                self.shg_fc = 0.34
            elif self.installation_type == 3:
                self.shg_fc = 0.30
            else:
                self.shg_fc = 0.32
        elif self.glazing_type == 71:
            if self.installation_type == 1:
                self.shg_fc = 0.26
            elif self.installation_type == 2:
                self.shg_fc = 0.25
            elif self.installation_type == 3:
                self.shg_fc = 0.22
            else:
                self.shg_fc = 0.25
        else:
            if self.installation_type == 1:
                self.shg_fc = 0.25
            elif self.installation_type == 2:
                self.shg_fc = 0.25
            elif self.installation_type == 3:
                self.shg_fc = 0.21
            else:
                self.shg_fc = 0.24

        return self.shg_fc

    def tx_factor(self):
        self.attachment_type = self.comboBox_3.currentIndex()
        if self.attachment_type == 0:
            self.tx = 1
        elif self.attachment_type == 1:
            self.tx = 0.64
        else:
            self.tx = 0.4

        return self.tx

    def et_factor(self):
        self.direction_type = self.comboBox_4.currentIndex()
        self.latitude_type = self.comboBox_5.currentIndex()

        if self.direction_type == 0:
            if self.latitude_type == 0:
                self.et = 203
            elif self.latitude_type == 1:
                self.et = 183
            elif self.latitude_type == 2:
                self.et = 172
            elif self.latitude_type == 3:
                self.et = 169
            elif self.latitude_type == 4:
                self.et = 174
            elif self.latitude_type == 5:
                self.et = 187
            elif self.latitude_type == 6:
                self.et = 208
            elif self.latitude_type == 7:
                self.et = 237
            else:
                self.et = 203
        elif self.direction_type == 1:
            if self.latitude_type == 0:
                self.et = 590
            elif self.latitude_type == 1:
                self.et = 582
            elif self.latitude_type == 2:
                self.et = 575
            elif self.latitude_type == 3:
                self.et = 571
            elif self.latitude_type == 4:
                self.et = 568
            elif self.latitude_type == 5:
                self.et = 568
            elif self.latitude_type == 6:
                self.et = 570
            elif self.latitude_type == 7:
                self.et = 574
            else:
                self.et = 590
        elif self.direction_type == 2:
            if self.latitude_type == 0:
                self.et = 702
            elif self.latitude_type == 1:
                self.et = 719
            elif self.latitude_type == 2:
                self.et = 734
            elif self.latitude_type == 3:
                self.et = 748
            elif self.latitude_type == 4:
                self.et = 761
            elif self.latitude_type == 5:
                self.et = 773
            elif self.latitude_type == 6:
                self.et = 783
            elif self.latitude_type == 7:
                self.et = 792
            else:
                self.et = 702
        elif self.direction_type == 3:
            if self.latitude_type == 0:
                self.et = 492
            elif self.latitude_type == 1:
                self.et = 542
            elif self.latitude_type == 2:
                self.et = 589
            elif self.latitude_type == 3:
                self.et = 632
            elif self.latitude_type == 4:
                self.et = 673
            elif self.latitude_type == 5:
                self.et = 710
            elif self.latitude_type == 6:
                self.et = 744
            elif self.latitude_type == 7:
                self.et = 775
            else:
                self.et = 492
        elif self.direction_type == 4:
            if self.latitude_type == 0:
                self.et = 218
            elif self.latitude_type == 1:
                self.et = 306
            elif self.latitude_type == 2:
                self.et = 391
            elif self.latitude_type == 3:
                self.et = 471
            elif self.latitude_type == 4:
                self.et = 547
            elif self.latitude_type == 5:
                self.et = 619
            elif self.latitude_type == 6:
                self.et = 986
            elif self.latitude_type == 7:
                self.et = 749
            else:
                self.et = 218
        elif self.direction_type == 5:
            if self.latitude_type == 0:
                self.et = 492
            elif self.latitude_type == 1:
                self.et = 542
            elif self.latitude_type == 2:
                self.et = 589
            elif self.latitude_type == 3:
                self.et = 632
            elif self.latitude_type == 4:
                self.et = 673
            elif self.latitude_type == 5:
                self.et = 710
            elif self.latitude_type == 6:
                self.et = 744
            elif self.latitude_type == 7:
                self.et = 775
            else:
                self.et = 492
        elif self.direction_type == 6:
            if self.latitude_type == 0:
                self.et = 702
            elif self.latitude_type == 1:
                self.et = 719
            elif self.latitude_type == 2:
                self.et = 734
            elif self.latitude_type == 3:
                self.et = 748
            elif self.latitude_type == 4:
                self.et = 761
            elif self.latitude_type == 5:
                self.et = 773
            elif self.latitude_type == 6:
                self.et = 783
            elif self.latitude_type == 7:
                self.et = 792
            else:
                self.et = 702
        elif self.direction_type == 7:
            if self.latitude_type == 0:
                self.et = 0.2
            elif self.latitude_type == 1:
                self.et = 0.2
            elif self.latitude_type == 2:
                self.et = 0.2
            elif self.latitude_type == 3:
                self.et = 0.2
            elif self.latitude_type == 4:
                self.et = 0.2
            elif self.latitude_type == 5:
                self.et = 0.2
            elif self.latitude_type == 6:
                self.et = 0.2
            elif self.latitude_type == 7:
                self.et = 0.2
            else:
                self.et = 0.2
        else:
            if self.latitude_type == 0:
                self.et = 590
            elif self.latitude_type == 1:
                self.et = 582
            elif self.latitude_type == 2:
                self.et = 575
            elif self.latitude_type == 3:
                self.et = 571
            elif self.latitude_type == 4:
                self.et = 568
            elif self.latitude_type == 5:
                self.et = 568
            elif self.latitude_type == 6:
                self.et = 570
            elif self.latitude_type == 7:
                self.et = 574
            else:
                self.et = 590
        return self.et

    def ed_factor(self):
        self.direction_type = self.comboBox_4.currentIndex()
        self.latitude_type = self.comboBox_5.currentIndex()
        if self.direction_type == 0:
            if self.latitude_type == 0:
                self.ed = 106
            elif self.latitude_type == 1:
                self.ed = 98
            elif self.latitude_type == 2:
                self.ed = 98
            elif self.latitude_type == 3:
                self.ed = 104
            elif self.latitude_type == 4:
                self.ed = 117
            elif self.latitude_type == 5:
                self.ed = 138
            elif self.latitude_type == 6:
                self.ed = 167
            elif self.latitude_type == 7:
                self.ed = 203
            else:
                self.ed = 106
        elif self.direction_type == 1:
            if self.latitude_type == 0:
                self.ed = 442
            elif self.latitude_type == 1:
                self.ed = 442
            elif self.latitude_type == 2:
                self.ed = 444
            elif self.latitude_type == 3:
                self.ed = 447
            elif self.latitude_type == 4:
                self.ed = 451
            elif self.latitude_type == 5:
                self.ed = 457
            elif self.latitude_type == 6:
                self.ed = 465
            elif self.latitude_type == 7:
                self.ed = 474
            else:
                self.et = 442
        elif self.direction_type == 2:
            if self.latitude_type == 0:
                self.ed = 542
            elif self.latitude_type == 1:
                self.ed = 548
            elif self.latitude_type == 2:
                self.ed = 570
            elif self.latitude_type == 3:
                self.ed = 590
            elif self.latitude_type == 4:
                self.ed = 608
            elif self.latitude_type == 5:
                self.ed = 624
            elif self.latitude_type == 6:
                self.ed = 638
            elif self.latitude_type == 7:
                self.ed = 651
            else:
                self.ed = 524
        elif self.direction_type == 3:
            if self.latitude_type == 0:
                self.ed = 299
            elif self.latitude_type == 1:
                self.ed = 355
            elif self.latitude_type == 2:
                self.ed = 407
            elif self.latitude_type == 3:
                self.ed = 455
            elif self.latitude_type == 4:
                self.ed = 499
            elif self.latitude_type == 5:
                self.ed = 540
            elif self.latitude_type == 6:
                self.ed = 577
            elif self.latitude_type == 7:
                self.ed = 610
            else:
                self.ed = 299
        elif self.direction_type == 4:
            if self.latitude_type == 0:
                self.ed = 21
            elif self.latitude_type == 1:
                self.ed = 114
            elif self.latitude_type == 2:
                self.ed = 203
            elif self.latitude_type == 3:
                self.ed = 286
            elif self.latitude_type == 4:
                self.ed = 365
            elif self.latitude_type == 5:
                self.ed = 439
            elif self.latitude_type == 6:
                self.ed = 509
            elif self.latitude_type == 7:
                self.ed = 574
            else:
                self.ed = 21
        elif self.direction_type == 5:
            if self.latitude_type == 0:
                self.ed = 299
            elif self.latitude_type == 1:
                self.ed = 355
            elif self.latitude_type == 2:
                self.ed = 407
            elif self.latitude_type == 3:
                self.ed = 455
            elif self.latitude_type == 4:
                self.ed = 499
            elif self.latitude_type == 5:
                self.ed = 540
            elif self.latitude_type == 6:
                self.ed = 577
            elif self.latitude_type == 7:
                self.ed = 610
            else:
                self.ed = 299
        elif self.direction_type == 6:
            if self.latitude_type == 0:
                self.ed = 524
            elif self.latitude_type == 1:
                self.ed = 548
            elif self.latitude_type == 2:
                self.ed = 570
            elif self.latitude_type == 3:
                self.ed = 590
            elif self.latitude_type == 4:
                self.ed = 608
            elif self.latitude_type == 5:
                self.ed = 624
            elif self.latitude_type == 6:
                self.ed = 638
            elif self.latitude_type == 7:
                self.ed = 651
            else:
                self.ed = 524
        elif self.direction_type == 7:
            if self.latitude_type == 0:
                self.ed = 442
            elif self.latitude_type == 1:
                self.ed = 442
            elif self.latitude_type == 2:
                self.ed = 444
            elif self.latitude_type == 3:
                self.ed = 447
            elif self.latitude_type == 4:
                self.ed = 451
            elif self.latitude_type == 5:
                self.ed = 457
            elif self.latitude_type == 6:
                self.ed = 465
            elif self.latitude_type == 7:
                self.ed = 474
            else:
                self.ed = 442
        else:
            if self.latitude_type == 0:
                self.ed = 787
            elif self.latitude_type == 1:
                self.ed = 790
            elif self.latitude_type == 2:
                self.ed = 782
            elif self.latitude_type == 3:
                self.ed = 765
            elif self.latitude_type == 4:
                self.ed = 739
            elif self.latitude_type == 5:
                self.ed = 705
            elif self.latitude_type == 6:
                self.ed = 661
            elif self.latitude_type == 7:
                self.ed = 608
            else:
                self.ed = 788
        return self.ed

    def ed_diffuse_factor(self):
        self.direction_type = self.comboBox_4.currentIndex()
        self.latitude_type = self.comboBox_5.currentIndex()
        if self.direction_type == 0:
            if self.latitude_type == 0:
                self.edd = 95
            elif self.latitude_type == 1:
                self.edd = 87
            elif self.latitude_type == 2:
                self.edd = 74
            elif self.latitude_type == 3:
                self.edd = 65
            elif self.latitude_type == 4:
                self.edd = 56
            elif self.latitude_type == 5:
                self.edd = 48
            elif self.latitude_type == 6:
                self.edd = 41
            elif self.latitude_type == 7:
                self.edd = 34
            else:
                self.edd = 97
        elif self.direction_type == 1:
            if self.latitude_type == 0:
                self.edd = 149
            elif self.latitude_type == 1:
                self.edd = 139
            elif self.latitude_type == 2:
                self.edd = 131
            elif self.latitude_type == 3:
                self.edd = 124
            elif self.latitude_type == 4:
                self.edd = 117
            elif self.latitude_type == 5:
                self.edd = 11
            elif self.latitude_type == 6:
                self.edd = 106
            elif self.latitude_type == 7:
                self.edd = 100
            else:
                self.edd = 149
        elif self.direction_type == 2:
            if self.latitude_type == 0:
                self.edd = 178
            elif self.latitude_type == 1:
                self.edd = 171
            elif self.latitude_type == 2:
                self.edd = 164
            elif self.latitude_type == 3:
                self.edd = 159
            elif self.latitude_type == 4:
                self.edd = 154
            elif self.latitude_type == 5:
                self.edd = 149
            elif self.latitude_type == 6:
                self.edd = 145
            elif self.latitude_type == 7:
                self.edd = 141
            else:
                self.edd = 178
        elif self.direction_type == 3:
            if self.latitude_type == 0:
                self.edd = 193
            elif self.latitude_type == 1:
                self.edd = 187
            elif self.latitude_type == 2:
                self.edd = 182
            elif self.latitude_type == 3:
                self.edd = 178
            elif self.latitude_type == 4:
                self.edd = 174
            elif self.latitude_type == 5:
                self.edd = 170
            elif self.latitude_type == 6:
                self.edd = 167
            elif self.latitude_type == 7:
                self.edd = 164
            else:
                self.edd = 193
        elif self.direction_type == 4:
            if self.latitude_type == 0:
                self.edd= 197
            elif self.latitude_type == 1:
                self.edd = 192
            elif self.latitude_type == 2:
                self.edd = 188
            elif self.latitude_type == 3:
                self.edd = 185
            elif self.latitude_type == 4:
                self.edd = 182
            elif self.latitude_type == 5:
                self.edd = 180
            elif self.latitude_type == 6:
                self.edd = 177
            elif self.latitude_type == 7:
                self.edd = 175
            else:
                self.edd = 197
        elif self.direction_type == 5:
            if self.latitude_type == 0:
                self.edd = 193
            elif self.latitude_type == 1:
                self.edd = 187
            elif self.latitude_type == 2:
                self.edd = 182
            elif self.latitude_type == 3:
                self.edd = 178
            elif self.latitude_type == 4:
                self.edd = 174
            elif self.latitude_type == 5:
                self.edd = 170
            elif self.latitude_type == 6:
                self.edd = 167
            elif self.latitude_type == 7:
                self.edd = 164
            else:
                self.edd = 193
        elif self.direction_type == 6:
            if self.latitude_type == 0:
                self.edd = 178
            elif self.latitude_type == 1:
                self.edd = 171
            elif self.latitude_type == 2:
                self.edd = 164
            elif self.latitude_type == 3:
                self.edd = 159
            elif self.latitude_type == 4:
                self.edd = 154
            elif self.latitude_type == 5:
                self.edd = 149
            elif self.latitude_type == 6:
                self.edd = 145
            elif self.latitude_type == 7:
                self.edd = 141
            else:
                self.edd = 178
        elif self.direction_type == 7:
            if self.latitude_type == 0:
                self.edd = 149
            elif self.latitude_type == 1:
                self.edd = 139
            elif self.latitude_type == 2:
                self.edd = 131
            elif self.latitude_type == 3:
                self.edd = 124
            elif self.latitude_type == 4:
                self.edd = 117
            elif self.latitude_type == 5:
                self.edd = 111
            elif self.latitude_type == 6:
                self.edd = 106
            elif self.latitude_type == 7:
                self.edd = 100
            else:
                self.edd = 149
        else:
                self.edd = 170
        return self.edd

    def slf_factor(self):
        self.direction_type = self.comboBox_4.currentIndex()
        self.latitude_type = self.comboBox_5.currentIndex()
        if self.direction_type == 0:
            if self.latitude_type == 0:
                self.slf = 2.8
            elif self.latitude_type == 1:
                self.slf = 2.1
            elif self.latitude_type == 2:
                self.slf = 1.4
            elif self.latitude_type == 3:
                self.slf = 1.5
            elif self.latitude_type == 4:
                self.slf = 1.7
            elif self.latitude_type == 5:
                self.slf = 1
            elif self.latitude_type == 6:
                self.slf = 0.8
            elif self.latitude_type == 7:
                self.slf = 0.9
            else:
                self.slf = 0.8
        elif self.direction_type == 1:
            if self.latitude_type == 0:
                self.slf = 1.4
            elif self.latitude_type == 1:
                self.slf = 1.5
            elif self.latitude_type == 2:
                self.slf = 1.6
            elif self.latitude_type == 3:
                self.slf = 1.2
            elif self.latitude_type == 4:
                self.slf = 1.3
            elif self.latitude_type == 5:
                self.slf = 1.3
            elif self.latitude_type == 6:
                self.slf = 0.9
            elif self.latitude_type == 7:
                self.slf = 0.9
            else:
                self.slf = 0.8
        elif self.direction_type == 2:
            if self.latitude_type == 0:
                self.slf = 1.2
            elif self.latitude_type == 1:
                self.slf = 1.2
            elif self.latitude_type == 2:
                self.slf = 1.1
            elif self.latitude_type == 3:
                self.slf = 1.1
            elif self.latitude_type == 4:
                self.slf = 1.1
            elif self.latitude_type == 5:
                self.slf = 1
            elif self.latitude_type == 6:
                self.slf = 1
            elif self.latitude_type == 7:
                self.slf = 0.9
            else:
                self.slf = 0.8
        elif self.direction_type == 3:
            if self.latitude_type == 0:
                self.slf = 2.1
            elif self.latitude_type == 1:
                self.slf = 1.8
            elif self.latitude_type == 2:
                self.slf = 2
            elif self.latitude_type == 3:
                self.slf = 1.7
            elif self.latitude_type == 4:
                self.slf = 1.5
            elif self.latitude_type == 5:
                self.slf = 1.6
            elif self.latitude_type == 6:
                self.slf = 1.4
            elif self.latitude_type == 7:
                self.slf = 1.2
            else:
                self.slf = 1.1
        elif self.direction_type == 4:
            if self.latitude_type == 0:
                self.slf = 2.8
            elif self.latitude_type == 1:
                self.slf = 2.1
            elif self.latitude_type == 2:
                self.slf = 1.4
            elif self.latitude_type == 3:
                self.slf = 1.5
            elif self.latitude_type == 4:
                self.slf = 1.7
            elif self.latitude_type == 5:
                self.slf = 1
            elif self.latitude_type == 6:
                self.slf = 0.8
            elif self.latitude_type == 7:
                self.slf = 0.9
            else:
                self.slf = 0.8
        elif self.direction_type == 5:
            if self.latitude_type == 0:
                self.slf = 2.1
            elif self.latitude_type == 1:
                self.slf = 1.8
            elif self.latitude_type == 2:
                self.slf = 2
            elif self.latitude_type == 3:
                self.slf = 1.7
            elif self.latitude_type == 4:
                self.slf = 1.5
            elif self.latitude_type == 5:
                self.slf = 1.6
            elif self.latitude_type == 6:
                self.slf = 1.4
            elif self.latitude_type == 7:
                self.slf = 1.2
            else:
                self.slf = 1.1
        elif self.direction_type == 6:
            if self.latitude_type == 0:
                self.slf = 1.2
            elif self.latitude_type == 1:
                self.slf = 1.2
            elif self.latitude_type == 2:
                self.slf = 1.1
            elif self.latitude_type == 3:
                self.slf = 1.1
            elif self.latitude_type == 4:
                self.slf = 1.1
            elif self.latitude_type == 5:
                self.slf = 1
            elif self.latitude_type == 6:
                self.slf = 1
            elif self.latitude_type == 7:
                self.slf = 0.9
            else:
                self.slf = 0.8
        elif self.direction_type == 7:
            if self.latitude_type == 0:
                self.slf = 1.4
            elif self.latitude_type == 1:
                self.slf = 1.5
            elif self.latitude_type == 2:
                self.slf = 1.6
            elif self.latitude_type == 3:
                self.slf = 1.2
            elif self.latitude_type == 4:
                self.slf = 1.3
            elif self.latitude_type == 5:
                self.slf = 1.3
            elif self.latitude_type == 6:
                self.slf = 0.9
            elif self.latitude_type == 7:
                self.slf = 0.9
            else:
                self.slf = 0.8
        else:
            if self.latitude_type == 0:
                self.slf = 1.2
            elif self.latitude_type == 1:
                self.slf = 1.2
            elif self.latitude_type == 2:
                self.slf = 1.1
            elif self.latitude_type == 3:
                self.slf = 1.1
            elif self.latitude_type == 4:
                self.slf = 1.1
            elif self.latitude_type == 5:
                self.slf = 1
            elif self.latitude_type == 6:
                self.slf = 1
            elif self.latitude_type == 7:
                self.slf = 0.9
            else:
                self.slf = 0.8
        return self.slf


    def fsh_factor(self):
        self.depth = self.lineEdit.text()
        self.vertical_distance = self.lineEdit_2.text()
        self.height = self.lineEdit_3.text()
        self.maxffs = ((self.slf_factor() * float(self.direction_type)) - float(self.vertical_distance))\
                      /float(self.height)
        return (min (1, max(0, self.maxffs)))

    def pxi_factor(self):
        self.shading = self.comboBox_7.currentIndex()
        if self.shading == 0:
            self.pxi = self.tx_factor() * self.et_factor()
        else:
            self.pxi = self.tx_factor() * (self.ed_diffuse_factor() + ((1-self.fsh_factor()) * self.ed_factor()))
        return self.pxi

    def ffs_factor(self):
        self.direction_type = self.comboBox_4.currentIndex()
        self.attach = self.comboBox_6.currentIndex()
        if self.attach == 0:
            if self.direction_type == 0:
                self.ffs = 0.44
            elif self.direction_type == 1:
                self.ffs = 0.21
            elif self.direction_type == 2:
                self.ffs = 0.31
            elif self.direction_type == 3:
                self.ffs = 0.37
            elif self.direction_type == 4:
                self.ffs = 0.47
            elif self.direction_type == 5:
                self.ffs = 0.58
            elif self.direction_type == 6:
                self.ffs = 0.56
            elif self.direction_type == 7:
                self.ffs = 0.46
            else:
                self.ffs = 0.58
        else:
            if self.direction_type == 0:
                self.ffs = 0.27
            elif self.direction_type == 1:
                self.ffs = 0.43
            elif self.direction_type == 2:
                self.ffs = 0.56
            elif self.direction_type == 3:
                self.ffs = 0.54
            elif self.direction_type == 4:
                self.ffs = 0.53
            elif self.direction_type == 5:
                self.ffs = 0.61
            elif self.direction_type == 6:
                self.ffs = 0.65
            elif self.direction_type == 7:
                self.ffs = 0.57
            else:
                self.ffs = 0.73
        return self.ffs

    def range_colling_temp(self):
        self.coolingrange = self.lineEdit_4.text()
        return float(self.coolingrange)

    def reset_shgc_factors(self):
        self.comboBox.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(0)
        self.comboBox_6.setCurrentIndex(0)
        self.comboBox_3.setCurrentIndex(0)
        self.comboBox_7.setCurrentIndex(0)
        self.comboBox_4.setCurrentIndex(0)
        self.comboBox_5.setCurrentIndex(0)
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()

    def reset_shgc_installation_factor(self):
        self.comboBox_2.setCurrentIndex(0)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Solar heat gain coefficient"))
        self.pushButton_9.setText(_translate("Dialog", "Clear"))
        self.pushButton_10.setText(_translate("Dialog", "Save"))
        self.comboBox.setItemText(0, _translate("Dialog", "Uncoated Single Glazing-3 mm-clear"))
        self.comboBox.setItemText(1, _translate("Dialog", "Uncoated Single Glazing-6 mm-clear"))
        self.comboBox.setItemText(2, _translate("Dialog", "Uncoated Single Glazing-3 mm-Bronze"))
        self.comboBox.setItemText(3, _translate("Dialog", "Uncoated Single Glazing-6 mm-Bronze"))
        self.comboBox.setItemText(4, _translate("Dialog", "Uncoated Single Glazing-3 mm-Green"))
        self.comboBox.setItemText(5, _translate("Dialog", "Uncoated Single Glazing-6 mm-Green"))
        self.comboBox.setItemText(6, _translate("Dialog", "Uncoated Single Glazing-3 mm-Gray"))
        self.comboBox.setItemText(7, _translate("Dialog", "Uncoated Single Glazing-6 mm-Gray"))
        self.comboBox.setItemText(8, _translate("Dialog", "Uncoated Single Glazing-6 mm-BlueGreen"))
        self.comboBox.setItemText(9, _translate("Dialog", "Reflective Single Glazing-6mm-stainless steel reflective coating on Clear 8%"))
        self.comboBox.setItemText(10, _translate("Dialog", "Reflective Single Glazing-6mm-stainless steel reflective coating on Clear 14%"))
        self.comboBox.setItemText(11, _translate("Dialog", "Reflective Single Glazing-6mm-stainless steel reflective coating on Clear 20%"))
        self.comboBox.setItemText(12, _translate("Dialog", "Reflective Single Glazing-6mm-stainless steel reflective coating on Green 14%"))
        self.comboBox.setItemText(13, _translate("Dialog", "Reflective Single Glazing-6mm-titanium reflective coating on Clear 20%"))
        self.comboBox.setItemText(14, _translate("Dialog", "Reflective Single Glazing-6mm-titanium reflective coating on Clear 30%"))
        self.comboBox.setItemText(15, _translate("Dialog", "Uncoated Double Glazing-3 mm-13 mm airspace-Clear Clear"))
        self.comboBox.setItemText(16, _translate("Dialog", "Uncoated Double Glazing-6 mm-13 mm airspace-Clear Clear"))
        self.comboBox.setItemText(17, _translate("Dialog", "Uncoated Double Glazing-3 mm-13 mm airspace-Bronze Clear"))
        self.comboBox.setItemText(18, _translate("Dialog", "Uncoated Double Glazing-6 mm-13 mm airspace-Bronze Clear"))
        self.comboBox.setItemText(19, _translate("Dialog", "Uncoated Double Glazing-3 mm-13 mm airspace-Green Clear"))
        self.comboBox.setItemText(20, _translate("Dialog", "Uncoated Double Glazing-6 mm-13 mm airspace-Green Clear"))
        self.comboBox.setItemText(21, _translate("Dialog", "Uncoated Double Glazing-3 mm-13 mm airspace-Gray Clear"))
        self.comboBox.setItemText(22, _translate("Dialog", "Uncoated Double Glazing-6 mm-13 mm airspace-Gray Clear"))
        self.comboBox.setItemText(23, _translate("Dialog", "Uncoated Double Glazing-3 mm-13 mm airspace-BlueGreen Clear"))
        self.comboBox.setItemText(24, _translate("Dialog", "Uncoated Double Glazing-6 mm-13 mm airspace-high-performance green tinted Clear Clear"))
        self.comboBox.setItemText(25, _translate("Dialog", "Reflective Double Glazing-6 mm-13 mm airspace-stainless steel reflective coating on Clear 8% Clear"))
        self.comboBox.setItemText(26, _translate("Dialog", "Reflective Double Glazing-6 mm-13 mm airspace-stainless steel reflective coating on Clear 14% Clear"))
        self.comboBox.setItemText(27, _translate("Dialog", "Reflective Double Glazing-6 mm-13 mm airspace-stainless steel reflective coating on Clear 20% Clear"))
        self.comboBox.setItemText(28, _translate("Dialog", "Reflective Double Glazing-6 mm-13 mm airspace-stainless steel reflective coating on Green 14% Clear"))
        self.comboBox.setItemText(29, _translate("Dialog", "Reflective Double Glazing-6 mm-13 mm airspace-titanium reflective coating on Clear 20% Clear"))
        self.comboBox.setItemText(30, _translate("Dialog", "Reflective Double Glazing-6 mm-13 mm airspace-titanium reflective coating on Clear 30% Clear"))
        self.comboBox.setItemText(31, _translate("Dialog", "Low-e Double Glazing, e = 0.2 on surface 2-3mm-13 mm airspace-low-emissivity coating Clear"))
        self.comboBox.setItemText(32, _translate("Dialog", "Low-e Double Glazing, e = 0.2 on surface 2-6mm-13 mm airspace-low-emissivity coating Clear"))
        self.comboBox.setItemText(33, _translate("Dialog", "Low-e Double Glazing, e = 0.2 on surface 3-3mm-13 mm airspace-Clear low-emissivity coating "))
        self.comboBox.setItemText(34, _translate("Dialog", "Low-e Double Glazing, e = 0.2 on surface 3-6mm-13 mm airspace-Clear low-emissivity coating "))
        self.comboBox.setItemText(35, _translate("Dialog", "Low-e Double Glazing, e = 0.2 on surface 3-3mm-13 mm airspace-Bronze low-emissivity coating "))
        self.comboBox.setItemText(36, _translate("Dialog", "Low-e Double Glazing, e = 0.2 on surface 3-6mm-13 mm airspace-Bronze low-emissivity coating "))
        self.comboBox.setItemText(37, _translate("Dialog", "Low-e Double Glazing, e = 0.2 on surface 3-3mm-13 mm airspace-Green low-emissivity coating "))
        self.comboBox.setItemText(38, _translate("Dialog", "Low-e Double Glazing, e = 0.2 on surface 3-6mm-13 mm airspace-Green low-emissivity coating "))
        self.comboBox.setItemText(39, _translate("Dialog", "Low-e Double Glazing, e = 0.2 on surface 3-3mm-13 mm airspace-Gray low-emissivity coating "))
        self.comboBox.setItemText(40, _translate("Dialog", "Low-e Double Glazing, e = 0.2 on surface 3-6mm-13 mm airspace-Gray low-emissivity coating "))
        self.comboBox.setItemText(41, _translate("Dialog", "Low-e Double Glazing, e = 0.2 on surface 3-6mm-13 mm airspace-BlueGreen low-emissivity coating "))
        self.comboBox.setItemText(42, _translate("Dialog", "Low-e Double Glazing, e = 0.2 on surface 3-6mm-13 mm airspace-high-performance green low-emissivity coating Clear"))
        self.comboBox.setItemText(43, _translate("Dialog", "Low-e Double Glazing, e = 0.1 on surface 2-3mm-13 mm airspace low-emissivity coating Clear"))
        self.comboBox.setItemText(44, _translate("Dialog", "Low-e Double Glazing, e = 0.1 on surface 2-6mm-13 mm airspace low-emissivity coating Clear"))
        self.comboBox.setItemText(45, _translate("Dialog", "Low-e Double Glazing, e = 0.1 on surface 3-3mm-13 mm airspace Clear low-emissivity coating"))
        self.comboBox.setItemText(46, _translate("Dialog", "Low-e Double Glazing, e = 0.1 on surface 3-6mm-13 mm airspace Clear low-emissivity coating"))
        self.comboBox.setItemText(47, _translate("Dialog", "Low-e Double Glazing, e = 0.1 on surface 3-3mm-13 mm airspace Bronze low-emissivity coating"))
        self.comboBox.setItemText(48, _translate("Dialog", "Low-e Double Glazing, e = 0.1 on surface 3-6mm-13 mm airspace Bronze low-emissivity coating"))
        self.comboBox.setItemText(49, _translate("Dialog", "Low-e Double Glazing, e = 0.1 on surface 3-3mm-13 mm airspace Green low-emissivity coating"))
        self.comboBox.setItemText(50, _translate("Dialog", "Low-e Double Glazing, e = 0.1 on surface 3-6mm-13 mm airspace Green low-emissivity coating"))
        self.comboBox.setItemText(51, _translate("Dialog", "Low-e Double Glazing, e = 0.1 on surface 3-3mm-13 mm airspace Gray low-emissivity coating"))
        self.comboBox.setItemText(52, _translate("Dialog", "Low-e Double Glazing, e = 0.1 on surface 3-6mm-13 mm airspace Gray low-emissivity coating"))
        self.comboBox.setItemText(53, _translate("Dialog", "Low-e Double Glazing, e = 0.1 on surface 3-6mm-13 mm airspace BlueGreenGreen low-emissivity coating"))
        self.comboBox.setItemText(54, _translate("Dialog", "Low-e Double Glazing, e = 0.1 on surface 3-6mm-13 mm airspace high-performance green tinted low-emissivity coating Clear"))
        self.comboBox.setItemText(55, _translate("Dialog", "Low-e Double Glazing, e = 0.05 on surface 2-3mm-13 mm airspace- low-emissivity coating Clear "))
        self.comboBox.setItemText(56, _translate("Dialog", "Low-e Double Glazing, e = 0.05 on surface 2-6mm-13 mm airspace- low-emissivity coating Clear "))
        self.comboBox.setItemText(57, _translate("Dialog", "Low-e Double Glazing, e = 0.05 on surface 2-6mm-13 mm airspace-Bronze low-emissivity coating Clear "))
        self.comboBox.setItemText(58, _translate("Dialog", "Low-e Double Glazing, e = 0.05 on surface 2-6mm-13 mm airspace-Green low-emissivity coating Clear "))
        self.comboBox.setItemText(59, _translate("Dialog", "Low-e Double Glazing, e = 0.05 on surface 2-6mm-13 mm airspace-Gray low-emissivity coating Clear "))
        self.comboBox.setItemText(60, _translate("Dialog", "Low-e Double Glazing, e = 0.05 on surface 2-6mm-13 mm airspace-Blue low-emissivity coating Clear "))
        self.comboBox.setItemText(61, _translate("Dialog", "Low-e Double Glazing, e = 0.05 on surface 2-6mm-13 mm airspace-high-performance green tinted low-emissivity coating Clear "))
        self.comboBox.setItemText(62, _translate("Dialog", "Triple Glazing-3mm-13 mm airspace-Clear Clear Clear"))
        self.comboBox.setItemText(63, _translate("Dialog", "Triple Glazing-6mm-13 mm airspace-Clear Clear Clear"))
        self.comboBox.setItemText(64, _translate("Dialog", "Triple Glazing-6mm-13 mm airspace-high-performance green Clear Clear"))
        self.comboBox.setItemText(65, _translate("Dialog", "Triple Glazing, e = 0.2 on surface 2-3mm-13 mm airspace- low-emissivity coating Clear Clear"))
        self.comboBox.setItemText(66, _translate("Dialog", "Triple Glazing, e = 0.2 on surface 2-6mm-13 mm airspace- low-emissivity coating Clear Clear"))
        self.comboBox.setItemText(67, _translate("Dialog", "Triple Glazing, e = 0.2 on surface 5-3mm-13 mm airspace-Clear Clear low-emissivity coating "))
        self.comboBox.setItemText(68, _translate("Dialog", "Triple Glazing, e = 0.2 on surface 5-6mm-13 mm airspace-Clear Clear low-emissivity coating "))
        self.comboBox.setItemText(69, _translate("Dialog", "Triple Glazing, e = 0.2 on surface 2&5-3mm-13 mm airspace-low-emissivity coating Clear low-emissivity coating"))
        self.comboBox.setItemText(70, _translate("Dialog", "Triple Glazing, e = 0.2 on surface 2&5-6mm-13 mm airspace-low-emissivity coating Clear low-emissivity coating"))
        self.comboBox.setItemText(71, _translate("Dialog", "Triple Glazing, e = 0.2 on surface 2&4-3mm-13 mm airspace-low-emissivity coating low-emissivity coating Clear"))
        self.comboBox.setItemText(72, _translate("Dialog", "Triple Glazing, e = 0.2 on surface 2&4-6mm-13 mm airspace-low-emissivity coating low-emissivity coating Clear"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "Operable-Aluminum"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "Fixed-Aluminum"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "Operable-Other Frame"))
        self.comboBox_2.setItemText(3, _translate("Dialog", "Fixed-Other Frame"))
        self.label.setText(_translate("Dialog", "Glazing Type :"))
        self.label_2.setText(_translate("Dialog", "Installation Type :"))
        self.comboBox_4.setItemText(0, _translate("Dialog", "North"))
        self.comboBox_4.setItemText(1, _translate("Dialog", "Northeast"))
        self.comboBox_4.setItemText(2, _translate("Dialog", "East"))
        self.comboBox_4.setItemText(3, _translate("Dialog", "Southeast"))
        self.comboBox_4.setItemText(4, _translate("Dialog", "South"))
        self.comboBox_4.setItemText(5, _translate("Dialog", "SouthWest"))
        self.comboBox_4.setItemText(6, _translate("Dialog", "West"))
        self.comboBox_4.setItemText(7, _translate("Dialog", "NorthWest"))
        self.comboBox_4.setItemText(8, _translate("Dialog", "Horizontal"))
        self.comboBox_5.setItemText(0, _translate("Dialog", "20"))
        self.comboBox_5.setItemText(1, _translate("Dialog", "25"))
        self.comboBox_5.setItemText(2, _translate("Dialog", "30"))
        self.comboBox_5.setItemText(3, _translate("Dialog", "35"))
        self.comboBox_5.setItemText(4, _translate("Dialog", "40"))
        self.comboBox_5.setItemText(5, _translate("Dialog", "45"))
        self.comboBox_5.setItemText(6, _translate("Dialog", "50"))
        self.comboBox_5.setItemText(7, _translate("Dialog", "55"))
        self.comboBox_5.setItemText(8, _translate("Dialog", "60"))
        self.label_4.setText(_translate("Dialog", "Exposure direction :"))
        self.label_7.setText(_translate("Dialog", "Exposure latitude :"))
        self.label_10.setText(_translate("Dialog", "Cooling daily range (K) :"))
        self.comboBox_7.setItemText(0, _translate("Dialog", "No Shaded"))
        self.comboBox_7.setItemText(1, _translate("Dialog", "Shaded"))
        self.label_11.setText(_translate("Dialog", "Shade Type :"))
        self.comboBox_6.setItemText(0, _translate("Dialog", "Single Family Detached"))
        self.comboBox_6.setItemText(1, _translate("Dialog", "Multifamily"))
        self.label_9.setText(_translate("Dialog", "attachment type of fenestration :"))
        self.label_5.setText(_translate("Dialog", "Depth of overhang (m) :"))
        self.label_8.setText(_translate("Dialog", "Height of fenestration (m) :"))
        self.label_6.setText(_translate("Dialog", "Vertical distance from top of fenestration to overhang (m) :"))
        self.comboBox_3.setItemText(0, _translate("Dialog", "None"))
        self.comboBox_3.setItemText(1, _translate("Dialog", "Exterior insect screen"))
        self.comboBox_3.setItemText(2, _translate("Dialog", "Shade screen"))
        self.label_3.setText(_translate("Dialog", "Exterior attachment of fenestration :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
