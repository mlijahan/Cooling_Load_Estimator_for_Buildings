
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 650)
        Dialog.setMinimumSize(QtCore.QSize(800, 650))
        Dialog.setMaximumSize(QtCore.QSize(800, 650))
        self.pushButton_9 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_9.setGeometry(QtCore.QRect(170, 570, 121, 41))
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
        self.pushButton_10.setGeometry(QtCore.QRect(520, 570, 121, 41))
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
        self.comboBox.setGeometry(QtCore.QRect(120, 49, 661, 24))
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
        self.comboBox_4.setGeometry(QtCore.QRect(150, 423, 291, 24))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_5 = QtWidgets.QComboBox(parent=Dialog)
        self.comboBox_5.setGeometry(QtCore.QRect(140, 466, 91, 24))
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
        self.label_4.setGeometry(QtCore.QRect(20, 423, 112, 24))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(parent=Dialog)
        self.label_7.setGeometry(QtCore.QRect(20, 465, 106, 24))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_10 = QtWidgets.QLabel(parent=Dialog)
        self.label_10.setGeometry(QtCore.QRect(20, 509, 137, 24))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(180, 509, 113, 24))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.comboBox_7 = QtWidgets.QComboBox(parent=Dialog)
        self.comboBox_7.setGeometry(QtCore.QRect(110, 338, 541, 24))
        self.comboBox_7.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
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
        self.label_12 = QtWidgets.QLabel(parent=Dialog)
        self.label_12.setGeometry(QtCore.QRect(20, 380, 141, 24))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(160, 380, 113, 24))
        self.lineEdit_5.setObjectName("lineEdit_5")

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

    def sc_factores(self):
        self.glazed_type = self.comboBox.currentIndex()
        self.shaded_types = self.comboBox_7.currentIndex()
        self.shadow_line = self.lineEdit_5.text()
        if self.glazed_type == 0:
            if self.shaded_types == 1:
                self.sc_0 = 0.98
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60)*(min((1.2 * float(self.shadow_line)), 60))/60)
            elif self.shaded_types == 2:
                self.sc_0 = 0.98
                self.sc_60 = 0.78
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 3:
                self.sc_0 = 0.73
                self.sc_60 = 0.78
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 4:
                self.sc_0 = 0.80
                self.sc_60 = 0.74
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 5:
                self.sc_0 = 0.70
                self.sc_60 = 0.70
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 6:
                self.sc_0 = 0.98
                self.sc_60 = 0.96
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 7:
                self.sc_0 = 0.98
                self.sc_60 = 0.70
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 8:
                self.sc_0 = 0.59
                self.sc_60 = 0.70
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 9:
                self.sc_0 = 0.69
                self.sc_60 = 0.58
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 10:
                self.sc_0 = 0.51
                self.sc_60 = 0.49
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 11:
                self.sc_0 = 0.97
                self.sc_60 = 0.96
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 12:
                self.sc_0 = 0.97
                self.sc_60 = 0.60
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 13:
                self.sc_0 = 0.45
                self.sc_60 = 0.60
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 14:
                self.sc_0 = 0.59
                self.sc_60 = 0.42
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 15:
                self.sc_0 = 0.33
                self.sc_60 = 0.29
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 31:
                self.sc_0 = 0.93
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 32:
                self.sc_0 = 0.93
                self.sc_60 = 0.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 33:
                self.sc_0 = 0.04
                self.sc_60 = 0.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 34:
                self.sc_0 = 0.2
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 35:
                self.sc_0 = 0.03
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 36:
                self.sc_0 = 0.94
                self.sc_60 = 0.95
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 37:
                self.sc_0 = 0.94
                self.sc_60 = 0.15
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 38:
                self.sc_0 = 0.08
                self.sc_60 = 0.15
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 39:
                self.sc_0 = 0.26
                self.sc_60 = 0.07
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 40:
                self.sc_0 = 0.05
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 41:
                self.sc_0 = 0.95
                self.sc_60 = 1.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 42:
                self.sc_0 = 0.95
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 43:
                self.sc_0 = 0.17
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 44:
                self.sc_0 = 0.34
                self.sc_60 = 0.12
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 45:
                self.sc_0 = 0.08
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 46:
                self.sc_fc = 0.7
            elif self.shaded_types == 47:
                self.sc_fc = 0.71
            elif self.shaded_types == 48:
                self.sc_fc = 0.59
            elif self.shaded_types == 49:
                self.sc_fc = 0.45
            elif self.shaded_types == 50:
                self.sc_fc = 0.75
            elif self.shaded_types == 51:
                self.sc_fc = 0.65
            elif self.shaded_types == 52:
                self.sc_fc = 0.56
            elif self.shaded_types == 53:
                self.sc_fc = 0.80
            elif self.shaded_types == 54:
                self.sc_fc = 0.71
            elif self.shaded_types == 55:
                self.sc_fc = 0.64
            elif self.shaded_types == 56:
                self.sc_fc = 0.73
            elif self.shaded_types == 57:
                self.sc_fc = 0.44
            elif self.shaded_types == 58:
                self.sc_fc = 0.34
            elif self.shaded_types == 59:
                self.sc_fc = 0.64
            elif self.shaded_types == 60:
                self.sc_fc = 0.61
            elif self.shaded_types == 61:
                self.sc_fc = 0.71
            elif self.shaded_types == 62:
                self.sc_fc = 0.3
            elif self.shaded_types == 63:
                self.sc_fc = 0.23
            elif self.shaded_types == 64:
                self.sc_fc = 0.64
            elif self.shaded_types == 65:
                self.sc_fc = 0.88
            else:
                self.sc_fc = 1
        elif self.glazed_type == 1:
            if self.shaded_types == 1:
                self.sc_0 = 0.98
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60)*(min((1.2 * float(self.shadow_line)), 60))/60)
            elif self.shaded_types == 2:
                self.sc_0 = 0.98
                self.sc_60 = 0.79
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 3:
                self.sc_0 = 0.74
                self.sc_60 = 0.79
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 4:
                self.sc_0 = 0.80
                self.sc_60 = 0.75
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 5:
                self.sc_0 = 0.70
                self.sc_60 = 0.70
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 6:
                self.sc_0 = 0.97
                self.sc_60 = 0.96
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 7:
                self.sc_0 = 0.97
                self.sc_60 = 0.70
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 8:
                self.sc_0 = 0.60
                self.sc_60 = 0.70
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 9:
                self.sc_0 = 0.70
                self.sc_60 = 0.59
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 10:
                self.sc_0 = 0.52
                self.sc_60 = 0.50
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 11:
                self.sc_0 = 0.97
                self.sc_60 = 0.96
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 12:
                self.sc_0 = 0.97
                self.sc_60 = 0.61
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 13:
                self.sc_0 = 0.47
                self.sc_60 = 0.61
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 14:
                self.sc_0 = 0.60
                self.sc_60 = 0.43
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 15:
                self.sc_0 = 0.35
                self.sc_60 = 0.31
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 31:
                self.sc_0 = 0.93
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 32:
                self.sc_0 = 0.93
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 33:
                self.sc_0 = 0.04
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 34:
                self.sc_0 = 0.2
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 35:
                self.sc_0 = 0.03
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 36:
                self.sc_0 = 0.94
                self.sc_60 = 0.95
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 37:
                self.sc_0 = 0.94
                self.sc_60 = 0.15
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 38:
                self.sc_0 = 0.08
                self.sc_60 = 0.15
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 39:
                self.sc_0 = 0.26
                self.sc_60 = 0.07
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 40:
                self.sc_0 = 0.05
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 41:
                self.sc_0 = 0.95
                self.sc_60 = 1.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 42:
                self.sc_0 = 0.95
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 43:
                self.sc_0 = 0.17
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 44:
                self.sc_0 = 0.34
                self.sc_60 = 0.12
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 45:
                self.sc_0 = 0.08
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 46:
                self.sc_fc = 0.71
            elif self.shaded_types == 47:
                self.sc_fc = 0.71
            elif self.shaded_types == 48:
                self.sc_fc = 0.60
            elif self.shaded_types == 49:
                self.sc_fc = 0.46
            elif self.shaded_types == 50:
                self.sc_fc = 0.75
            elif self.shaded_types == 51:
                self.sc_fc = 0.66
            elif self.shaded_types == 52:
                self.sc_fc = 0.57
            elif self.shaded_types == 53:
                self.sc_fc = 0.80
            elif self.shaded_types == 54:
                self.sc_fc = 0.72
            elif self.shaded_types == 55:
                self.sc_fc = 0.65
            elif self.shaded_types == 56:
                self.sc_fc = 0.73
            elif self.shaded_types == 57:
                self.sc_fc = 0.45
            elif self.shaded_types == 58:
                self.sc_fc = 0.35
            elif self.shaded_types == 59:
                self.sc_fc = 0.65
            elif self.shaded_types == 60:
                self.sc_fc = 0.62
            elif self.shaded_types == 61:
                self.sc_fc = 0.72
            elif self.shaded_types == 62:
                self.sc_fc = 0.32
            elif self.shaded_types == 63:
                self.sc_fc = 0.25
            elif self.shaded_types == 64:
                self.sc_fc = 0.64
            elif self.shaded_types == 65:
                self.sc_fc = 0.88
            else:
                self.sc_fc = 1
        if self.glazed_type == 2:
            if self.shaded_types == 1:
                self.sc_0 = 0.98
                self.sc_60 = 0.96
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60)*(min((1.2 * float(self.shadow_line)), 60))/60)
            elif self.shaded_types == 2:
                self.sc_0 = 0.98
                self.sc_60 = 0.80
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 3:
                self.sc_0 = 0.75
                self.sc_60 = 0.80
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 4:
                self.sc_0 = 0.81
                self.sc_60 = 0.76
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 5:
                self.sc_0 = 0.72
                self.sc_60 = 0.72
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 6:
                self.sc_0 = 0.97
                self.sc_60 = 0.96
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 7:
                self.sc_0 = 0.97
                self.sc_60 = 0.72
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 8:
                self.sc_0 = 0.63
                self.sc_60 = 0.72
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 9:
                self.sc_0 = 0.72
                self.sc_60 = 0.62
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 10:
                self.sc_0 = 0.55
                self.sc_60 = 0.53
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 11:
                self.sc_0 = 0.97
                self.sc_60 = 0.95
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 12:
                self.sc_0 = 0.97
                self.sc_60 = 0.64
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 13:
                self.sc_0 = 0.51
                self.sc_60 = 0.64
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 14:
                self.sc_0 = 0.63
                self.sc_60 = 0.48
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 15:
                self.sc_0 = 0.40
                self.sc_60 = 0.37
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 31:
                self.sc_0 = 0.93
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 32:
                self.sc_0 = 0.93
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 33:
                self.sc_0 = 0.04
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 34:
                self.sc_0 = 0.21
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 35:
                self.sc_0 = 0.04
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 36:
                self.sc_0 = 0.94
                self.sc_60 = 0.95
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 37:
                self.sc_0 = 0.94
                self.sc_60 = 0.15
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 38:
                self.sc_0 = 0.09
                self.sc_60 = 0.15
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 39:
                self.sc_0 = 0.26
                self.sc_60 = 0.07
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 40:
                self.sc_0 = 0.05
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 41:
                self.sc_0 = 0.95
                self.sc_60 = 1.01
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 42:
                self.sc_0 = 0.95
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 43:
                self.sc_0 = 0.17
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 44:
                self.sc_0 = 0.34
                self.sc_60 = 0.12
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 45:
                self.sc_0 = 0.09
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 46:
                self.sc_fc = 0.72
            elif self.shaded_types == 47:
                self.sc_fc = 0.72
            elif self.shaded_types == 48:
                self.sc_fc = 0.62
            elif self.shaded_types == 49:
                self.sc_fc = 0.50
            elif self.shaded_types == 50:
                self.sc_fc = 0.76
            elif self.shaded_types == 51:
                self.sc_fc = 0.68
            elif self.shaded_types == 52:
                self.sc_fc = 0.60
            elif self.shaded_types == 53:
                self.sc_fc = 0.81
            elif self.shaded_types == 54:
                self.sc_fc = 0.73
            elif self.shaded_types == 55:
                self.sc_fc = 0.68
            elif self.shaded_types == 56:
                self.sc_fc = 0.75
            elif self.shaded_types == 57:
                self.sc_fc = 0.49
            elif self.shaded_types == 58:
                self.sc_fc = 0.40
            elif self.shaded_types == 59:
                self.sc_fc = 0.67
            elif self.shaded_types == 60:
                self.sc_fc = 0.64
            elif self.shaded_types == 61:
                self.sc_fc = 0.73
            elif self.shaded_types == 62:
                self.sc_fc = 0.38
            elif self.shaded_types == 63:
                self.sc_fc = 0.31
            elif self.shaded_types == 64:
                self.sc_fc = 0.64
            elif self.shaded_types == 65:
                self.sc_fc = 0.89
            else:
                self.sc_fc = 1
        elif self.glazed_type == 3:
            if self.shaded_types == 1:
                self.sc_0 = 0.97
                self.sc_60 = 0.95
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60)*(min((1.2 * float(self.shadow_line)), 60))/60)
            elif self.shaded_types == 2:
                self.sc_0 = 0.97
                self.sc_60 = 0.82
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 3:
                self.sc_0 = 0.77
                self.sc_60 = 0.82
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 4:
                self.sc_0 = 0.82
                self.sc_60 = 0.78
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 5:
                self.sc_0 = 0.74
                self.sc_60 = 0.74
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 6:
                self.sc_0 = 0.97
                self.sc_60 = 0.95
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 7:
                self.sc_0 = 0.97
                self.sc_60 = 0.75
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 8:
                self.sc_0 = 0.67
                self.sc_60 = 0.75
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 9:
                self.sc_0 = 0.75
                self.sc_60 = 0.66
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 10:
                self.sc_0 = 0.60
                self.sc_60 = 0.58
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 11:
                self.sc_0 = 0.96
                self.sc_60 = 0.95
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 12:
                self.sc_0 = 0.96
                self.sc_60 = 0.68
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 13:
                self.sc_0 = 0.57
                self.sc_60 = 0.68
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 14:
                self.sc_0 = 0.67
                self.sc_60 = 0.54
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 15:
                self.sc_0 = 0.47
                self.sc_60 = 0.44
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 31:
                self.sc_0 = 0.93
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 32:
                self.sc_0 = 0.93
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 33:
                self.sc_0 = 0.05
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 34:
                self.sc_0 = 0.21
                self.sc_60 = 0.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 35:
                self.sc_0 = 0.04
                self.sc_60 = 0.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 36:
                self.sc_0 = 0.94
                self.sc_60 = 0.95
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 37:
                self.sc_0 = 0.94
                self.sc_60 = 0.15
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 38:
                self.sc_0 = 0.09
                self.sc_60 = 0.15
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 39:
                self.sc_0 = 0.26
                self.sc_60 = 0.07
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 40:
                self.sc_0 = 0.05
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 41:
                self.sc_0 = 0.95
                self.sc_60 = 1
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 42:
                self.sc_0 = 0.95
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 43:
                self.sc_0 = 0.17
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 44:
                self.sc_0 = 0.34
                self.sc_60 = 0.12
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 45:
                self.sc_0 = 0.09
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 46:
                self.sc_fc = 0.74
            elif self.shaded_types == 47:
                self.sc_fc = 0.74
            elif self.shaded_types == 48:
                self.sc_fc = 0.65
            elif self.shaded_types == 49:
                self.sc_fc = 0.55
            elif self.shaded_types == 50:
                self.sc_fc = 0.78
            elif self.shaded_types == 51:
                self.sc_fc = 0.70
            elif self.shaded_types == 52:
                self.sc_fc = 0.64
            elif self.shaded_types == 53:
                self.sc_fc = 0.82
            elif self.shaded_types == 54:
                self.sc_fc = 0.76
            elif self.shaded_types == 55:
                self.sc_fc = 0.71
            elif self.shaded_types == 56:
                self.sc_fc = 0.77
            elif self.shaded_types == 57:
                self.sc_fc = 0.55
            elif self.shaded_types == 58:
                self.sc_fc = 0.47
            elif self.shaded_types == 59:
                self.sc_fc = 0.69
            elif self.shaded_types == 60:
                self.sc_fc = 0.68
            elif self.shaded_types == 61:
                self.sc_fc = 0.76
            elif self.shaded_types == 62:
                self.sc_fc = 0.45
            elif self.shaded_types == 63:
                self.sc_fc = 0.39
            elif self.shaded_types == 64:
                self.sc_fc = 0.64
            elif self.shaded_types == 65:
                self.sc_fc = 0.9
            else:
                self.sc_fc = 1
        elif self.glazed_type == 4:
            if self.shaded_types == 1:
                self.sc_0 = 0.98
                self.sc_60 = 0.96
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60)*(min((1.2 * float(self.shadow_line)), 60))/60)
            elif self.shaded_types == 2:
                self.sc_0 = 0.98
                self.sc_60 = 0.80
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 3:
                self.sc_0 = 0.76
                self.sc_60 = 0.80
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 4:
                self.sc_0 = 0.81
                self.sc_60 = 0.77
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 5:
                self.sc_0 = 0.72
                self.sc_60 = 0.72
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 6:
                self.sc_0 = 0.97
                self.sc_60 = 0.96
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 7:
                self.sc_0 = 0.97
                self.sc_60 = 0.73
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 8:
                self.sc_0 = 0.64
                self.sc_60 = 0.73
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 9:
                self.sc_0 = 0.73
                self.sc_60 = 0.53
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 10:
                self.sc_0 = 0.56
                self.sc_60 = 0.54
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 11:
                self.sc_0 = 0.97
                self.sc_60 = 0.95
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 12:
                self.sc_0 = 0.97
                self.sc_60 = 0.65
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 13:
                self.sc_0 = 0.52
                self.sc_60 = 0.65
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 14:
                self.sc_0 = 0.64
                self.sc_60 = 0.49
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 15:
                self.sc_0 = 0.42
                self.sc_60 = 0.38
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 31:
                self.sc_0 = 0.93
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 32:
                self.sc_0 = 0.93
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 33:
                self.sc_0 = 0.04
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 34:
                self.sc_0 = 0.21
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 35:
                self.sc_0 = 0.04
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 36:
                self.sc_0 = 0.94
                self.sc_60 = 0.95
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 37:
                self.sc_0 = 0.94
                self.sc_60 = 0.15
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 38:
                self.sc_0 = 0.09
                self.sc_60 = 0.15
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 39:
                self.sc_0 = 0.26
                self.sc_60 = 0.07
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 40:
                self.sc_0 = 0.05
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 41:
                self.sc_0 = 0.95
                self.sc_60 = 1.01
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 42:
                self.sc_0 = 0.95
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 43:
                self.sc_0 = 0.17
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 44:
                self.sc_0 = 0.34
                self.sc_60 = 0.12
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 45:
                self.sc_0 = 0.09
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 46:
                self.sc_fc = 0.72
            elif self.shaded_types == 47:
                self.sc_fc = 0.72
            elif self.shaded_types == 48:
                self.sc_fc = 0.63
            elif self.shaded_types == 49:
                self.sc_fc = 0.51
            elif self.shaded_types == 50:
                self.sc_fc = 0.76
            elif self.shaded_types == 51:
                self.sc_fc = 0.68
            elif self.shaded_types == 52:
                self.sc_fc = 0.61
            elif self.shaded_types == 53:
                self.sc_fc = 0.82
            elif self.shaded_types == 54:
                self.sc_fc = 0.74
            elif self.shaded_types == 55:
                self.sc_fc = 0.68
            elif self.shaded_types == 56:
                self.sc_fc = 0.75
            elif self.shaded_types == 57:
                self.sc_fc = 0.51
            elif self.shaded_types == 58:
                self.sc_fc = 0.42
            elif self.shaded_types == 59:
                self.sc_fc = 0.67
            elif self.shaded_types == 60:
                self.sc_fc = 0.65
            elif self.shaded_types == 61:
                self.sc_fc = 0.74
            elif self.shaded_types == 62:
                self.sc_fc = 0.39
            elif self.shaded_types == 63:
                self.sc_fc = 0.33
            elif self.shaded_types == 64:
                self.sc_fc = 0.64
            elif self.shaded_types == 65:
                self.sc_fc = 0.89
            else:
                self.sc_fc = 1
        elif self.glazed_type == 5:
            if self.shaded_types == 1:
                self.sc_0 = 0.97
                self.sc_60 = 0.95
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60)*(min((1.2 * float(self.shadow_line)), 60))/60)
            elif self.shaded_types == 2:
                self.sc_0 = 0.98
                self.sc_60 = 0.82
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 3:
                self.sc_0 = 0.77
                self.sc_60 = 0.82
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 4:
                self.sc_0 = 0.83
                self.sc_60 = 0.79
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 5:
                self.sc_0 = 0.74
                self.sc_60 = 0.74
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 6:
                self.sc_0 = 0.97
                self.sc_60 = 0.95
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 7:
                self.sc_0 = 0.97
                self.sc_60 = 0.76
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 8:
                self.sc_0 = 0.67
                self.sc_60 = 0.76
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 9:
                self.sc_0 = 0.75
                self.sc_60 = 0.67
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 10:
                self.sc_0 = 0.60
                self.sc_60 = 0.59
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 11:
                self.sc_0 = 0.96
                self.sc_60 = 0.95
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 12:
                self.sc_0 = 0.96
                self.sc_60 = 0.69
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 13:
                self.sc_0 = 0.57
                self.sc_60 = 0.69
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 14:
                self.sc_0 = 0.68
                self.sc_60 = 0.55
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 15:
                self.sc_0 = 0.48
                self.sc_60 = 0.45
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 31:
                self.sc_0 = 0.93
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 32:
                self.sc_0 = 0.93
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 33:
                self.sc_0 = 0.05
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 34:
                self.sc_0 = 0.21
                self.sc_60 = 0.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 35:
                self.sc_0 = 0.05
                self.sc_60 = 0.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 36:
                self.sc_0 = 0.94
                self.sc_60 = 0.95
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 37:
                self.sc_0 = 0.94
                self.sc_60 = 0.15
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 38:
                self.sc_0 = 0.09
                self.sc_60 = 0.15
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 39:
                self.sc_0 = 0.26
                self.sc_60 = 0.07
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 40:
                self.sc_0 = 0.06
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 41:
                self.sc_0 = 0.95
                self.sc_60 = 1
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 42:
                self.sc_0 = 0.95
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 43:
                self.sc_0 = 0.17
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 44:
                self.sc_0 = 0.34
                self.sc_60 = 0.12
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 45:
                self.sc_0 = 0.09
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 46:
                self.sc_fc = 0.74
            elif self.shaded_types == 47:
                self.sc_fc = 0.74
            elif self.shaded_types == 48:
                self.sc_fc = 0.66
            elif self.shaded_types == 49:
                self.sc_fc = 0.56
            elif self.shaded_types == 50:
                self.sc_fc = 0.78
            elif self.shaded_types == 51:
                self.sc_fc = 0.71
            elif self.shaded_types == 52:
                self.sc_fc = 0.65
            elif self.shaded_types == 53:
                self.sc_fc = 0.83
            elif self.shaded_types == 54:
                self.sc_fc = 0.76
            elif self.shaded_types == 55:
                self.sc_fc = 0.71
            elif self.shaded_types == 56:
                self.sc_fc = 0.78
            elif self.shaded_types == 57:
                self.sc_fc = 0.56
            elif self.shaded_types == 58:
                self.sc_fc = 0.48
            elif self.shaded_types == 59:
                self.sc_fc = 0.7
            elif self.shaded_types == 60:
                self.sc_fc = 0.68
            elif self.shaded_types == 61:
                self.sc_fc = 0.76
            elif self.shaded_types == 62:
                self.sc_fc = 0.46
            elif self.shaded_types == 63:
                self.sc_fc = 0.4
            elif self.shaded_types == 64:
                self.sc_fc = 0.64
            elif self.shaded_types == 65:
                self.sc_fc = 0.9
            else:
                self.sc_fc = 1
        elif self.glazed_type == 6:
            if self.shaded_types == 1:
                self.sc_0 = 0.98
                self.sc_60 = 0.96
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60)*(min((1.2 * float(self.shadow_line)), 60))/60)
            elif self.shaded_types == 2:
                self.sc_0 = 0.98
                self.sc_60 = 0.8
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 3:
                self.sc_0 = 0.76
                self.sc_60 = 0.8
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 4:
                self.sc_0 = 0.81
                self.sc_60 = 0.77
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 5:
                self.sc_0 = 0.72
                self.sc_60 = 0.72
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 6:
                self.sc_0 = 0.97
                self.sc_60 = 0.96
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 7:
                self.sc_0 = 0.97
                self.sc_60 = 0.73
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 8:
                self.sc_0 = 0.64
                self.sc_60 = 0.73
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 9:
                self.sc_0 = 0.73
                self.sc_60 = 0.63
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 10:
                self.sc_0 = 0.56
                self.sc_60 = 0.54
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 11:
                self.sc_0 = 0.97
                self.sc_60 = 0.95
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 12:
                self.sc_0 = 0.97
                self.sc_60 = 0.65
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 13:
                self.sc_0 = 0.52
                self.sc_60 = 0.65
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 14:
                self.sc_0 = 0.64
                self.sc_60 = 0.49
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 15:
                self.sc_0 = 0.42
                self.sc_60 = 0.38
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 31:
                self.sc_0 = 0.93
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 32:
                self.sc_0 = 0.93
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 33:
                self.sc_0 = 0.04
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 34:
                self.sc_0 = 0.21
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 35:
                self.sc_0 = 0.04
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 36:
                self.sc_0 = 0.94
                self.sc_60 = 0.95
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 37:
                self.sc_0 = 0.94
                self.sc_60 = 0.15
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 38:
                self.sc_0 = 0.09
                self.sc_60 = 0.15
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 39:
                self.sc_0 = 0.26
                self.sc_60 = 0.07
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 40:
                self.sc_0 = 0.05
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 41:
                self.sc_0 = 0.95
                self.sc_60 = 1.01
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 42:
                self.sc_0 = 0.95
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 43:
                self.sc_0 = 0.17
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 44:
                self.sc_0 = 0.34
                self.sc_60 = 0.12
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 45:
                self.sc_0 = 0.09
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 46:
                self.sc_fc = 0.72
            elif self.shaded_types == 47:
                self.sc_fc = 0.72
            elif self.shaded_types == 48:
                self.sc_fc = 0.63
            elif self.shaded_types == 49:
                self.sc_fc = 0.51
            elif self.shaded_types == 50:
                self.sc_fc = 0.76
            elif self.shaded_types == 51:
                self.sc_fc = 0.68
            elif self.shaded_types == 52:
                self.sc_fc = 0.61
            elif self.shaded_types == 53:
                self.sc_fc = 0.82
            elif self.shaded_types == 54:
                self.sc_fc = 0.74
            elif self.shaded_types == 55:
                self.sc_fc = 0.68
            elif self.shaded_types == 56:
                self.sc_fc = 0.75
            elif self.shaded_types == 57:
                self.sc_fc = 0.51
            elif self.shaded_types == 58:
                self.sc_fc = 0.42
            elif self.shaded_types == 59:
                self.sc_fc = 0.67
            elif self.shaded_types == 60:
                self.sc_fc = 0.65
            elif self.shaded_types == 61:
                self.sc_fc = 0.74
            elif self.shaded_types == 62:
                self.sc_fc = 0.39
            elif self.shaded_types == 63:
                self.sc_fc = 0.33
            elif self.shaded_types == 64:
                self.sc_fc = 0.64
            elif self.shaded_types == 65:
                self.sc_fc = 0.89
            else:
                self.sc_fc = 1
        elif self.glazed_type == 7:
            if self.shaded_types == 1:
                self.sc_0 = 0.97
                self.sc_60 = 0.95
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60)*(min((1.2 * float(self.shadow_line)), 60))/60)
            elif self.shaded_types == 2:
                self.sc_0 = 0.97
                self.sc_60 = 0.82
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 3:
                self.sc_0 = 0.78
                self.sc_60 = 0.82
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 4:
                self.sc_0 = 0.83
                self.sc_60 = 0.79
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 5:
                self.sc_0 = 0.74
                self.sc_60 = 0.74
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 6:
                self.sc_0 = 0.97
                self.sc_60 = 0.95
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 7:
                self.sc_0 = 0.97
                self.sc_60 = 0.76
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 8:
                self.sc_0 = 0.67
                self.sc_60 = 0.76
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 9:
                self.sc_0 = 0.75
                self.sc_60 = 0.67
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 10:
                self.sc_0 = 0.61
                self.sc_60 = 0.59
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 11:
                self.sc_0 = 0.96
                self.sc_60 = 0.95
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 12:
                self.sc_0 = 0.96
                self.sc_60 = 0.69
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 13:
                self.sc_0 = 0.58
                self.sc_60 = 0.69
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 14:
                self.sc_0 = 0.68
                self.sc_60 = 0.56
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 15:
                self.sc_0 = 0.49
                self.sc_60 = 0.46
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 31:
                self.sc_0 = 0.93
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 32:
                self.sc_0 = 0.93
                self.sc_60 = 0.07
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 33:
                self.sc_0 = 0.05
                self.sc_60 = 0.07
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 34:
                self.sc_0 = 0.21
                self.sc_60 = 0.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 35:
                self.sc_0 = 0.05
                self.sc_60 = 0.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 36:
                self.sc_0 = 0.94
                self.sc_60 = 0.95
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 37:
                self.sc_0 = 0.94
                self.sc_60 = 0.15
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 38:
                self.sc_0 = 0.08
                self.sc_60 = 0.15
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 39:
                self.sc_0 = 0.26
                self.sc_60 = 0.07
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 40:
                self.sc_0 = 0.06
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 41:
                self.sc_0 = 0.95
                self.sc_60 = 1
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 42:
                self.sc_0 = 0.95
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 43:
                self.sc_0 = 0.17
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 44:
                self.sc_0 = 0.34
                self.sc_60 = 0.12
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 45:
                self.sc_0 = 0.09
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 46:
                self.sc_fc = 0.74
            elif self.shaded_types == 47:
                self.sc_fc = 0.74
            elif self.shaded_types == 48:
                self.sc_fc = 0.66
            elif self.shaded_types == 49:
                self.sc_fc = 0.56
            elif self.shaded_types == 50:
                self.sc_fc = 0.78
            elif self.shaded_types == 51:
                self.sc_fc = 0.71
            elif self.shaded_types == 52:
                self.sc_fc = 0.65
            elif self.shaded_types == 53:
                self.sc_fc = 0.83
            elif self.shaded_types == 54:
                self.sc_fc = 0.76
            elif self.shaded_types == 55:
                self.sc_fc = 0.72
            elif self.shaded_types == 56:
                self.sc_fc = 0.78
            elif self.shaded_types == 57:
                self.sc_fc = 0.57
            elif self.shaded_types == 58:
                self.sc_fc = 0.49
            elif self.shaded_types == 59:
                self.sc_fc = 0.7
            elif self.shaded_types == 60:
                self.sc_fc = 0.69
            elif self.shaded_types == 61:
                self.sc_fc = 0.76
            elif self.shaded_types == 62:
                self.sc_fc = 0.47
            elif self.shaded_types == 63:
                self.sc_fc = 0.41
            elif self.shaded_types == 64:
                self.sc_fc = 0.64
            elif self.shaded_types == 65:
                self.sc_fc = 0.9
            else:
                self.sc_fc = 1
        elif self.glazed_type == 8:
            if self.shaded_types == 1:
                self.sc_0 = 0.97
                self.sc_60 = 0.95
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60)*(min((1.2 * float(self.shadow_line)), 60))/60)
            elif self.shaded_types == 2:
                self.sc_0 = 0.97
                self.sc_60 = 0.82
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 3:
                self.sc_0 = 0.77
                self.sc_60 = 0.82
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 4:
                self.sc_0 = 0.82
                self.sc_60 = 0.77
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 5:
                self.sc_0 = 0.74
                self.sc_60 = 0.74
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 6:
                self.sc_0 = 0.97
                self.sc_60 = 0.95
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 7:
                self.sc_0 = 0.97
                self.sc_60 = 0.75
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 8:
                self.sc_0 = 0.67
                self.sc_60 = 0.75
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 9:
                self.sc_0 = 0.75
                self.sc_60 = 0.66
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 10:
                self.sc_0 = 0.60
                self.sc_60 = 0.58
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 11:
                self.sc_0 = 0.96
                self.sc_60 = 0.95
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 12:
                self.sc_0 = 0.96
                self.sc_60 = 0.68
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 13:
                self.sc_0 = 0.57
                self.sc_60 = 0.68
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 14:
                self.sc_0 = 0.68
                self.sc_60 = 0.54
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 15:
                self.sc_0 = 0.47
                self.sc_60 = 0.44
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 31:
                self.sc_0 = 0.93
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 32:
                self.sc_0 = 0.93
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 33:
                self.sc_0 = 0.05
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 34:
                self.sc_0 = 0.21
                self.sc_60 = 0.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 35:
                self.sc_0 = 0.04
                self.sc_60 = 0.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 36:
                self.sc_0 = 0.94
                self.sc_60 = 0.95
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 37:
                self.sc_0 = 0.94
                self.sc_60 = 0.15
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 38:
                self.sc_0 = 0.09
                self.sc_60 = 0.15
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 39:
                self.sc_0 = 0.26
                self.sc_60 = 0.07
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 40:
                self.sc_0 = 0.05
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 41:
                self.sc_0 = 0.95
                self.sc_60 = 1.01
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 42:
                self.sc_0 = 0.95
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 43:
                self.sc_0 = 0.17
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 44:
                self.sc_0 = 0.35
                self.sc_60 = 0.12
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 45:
                self.sc_0 = 0.09
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 46:
                self.sc_fc = 0.74
            elif self.shaded_types == 47:
                self.sc_fc = 0.74
            elif self.shaded_types == 48:
                self.sc_fc = 0.65
            elif self.shaded_types == 49:
                self.sc_fc = 0.55
            elif self.shaded_types == 50:
                self.sc_fc = 0.78
            elif self.shaded_types == 51:
                self.sc_fc = 0.70
            elif self.shaded_types == 52:
                self.sc_fc = 0.64
            elif self.shaded_types == 53:
                self.sc_fc = 0.82
            elif self.shaded_types == 54:
                self.sc_fc = 0.76
            elif self.shaded_types == 55:
                self.sc_fc = 0.71
            elif self.shaded_types == 56:
                self.sc_fc = 0.77
            elif self.shaded_types == 57:
                self.sc_fc = 0.55
            elif self.shaded_types == 58:
                self.sc_fc = 0.47
            elif self.shaded_types == 59:
                self.sc_fc = 0.69
            elif self.shaded_types == 60:
                self.sc_fc = 0.68
            elif self.shaded_types == 61:
                self.sc_fc = 0.76
            elif self.shaded_types == 62:
                self.sc_fc = 0.45
            elif self.shaded_types == 63:
                self.sc_fc = 0.39
            elif self.shaded_types == 64:
                self.sc_fc = 0.64
            elif self.shaded_types == 65:
                self.sc_fc = 0.9
            else:
                self.sc_fc = 1
        elif self.glazed_type == 15:
            if self.shaded_types == 1:
                self.sc_0 = 0.99
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60)*(min((1.2 * float(self.shadow_line)), 60))/60)
            elif self.shaded_types == 2:
                self.sc_0 = 0.99
                self.sc_60 = 0.88
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 3:
                self.sc_0 = 0.84
                self.sc_60 = 0.88
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 4:
                self.sc_0 = 0.88
                self.sc_60 = 0.85
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 5:
                self.sc_0 = 0.81
                self.sc_60 = 0.81
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 6:
                self.sc_0 = 0.98
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 7:
                self.sc_0 = 0.98
                self.sc_60 = 0.80
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 8:
                self.sc_0 = 0.70
                self.sc_60 = 0.80
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 9:
                self.sc_0 = 0.78
                self.sc_60 = 0.70
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 10:
                self.sc_0 = 0.63
                self.sc_60 = 0.63
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 11:
                self.sc_0 = 0.97
                self.sc_60 = 0.96
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 12:
                self.sc_0 = 0.97
                self.sc_60 = 0.71
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 13:
                self.sc_0 = 0.57
                self.sc_60 = 0.71
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 14:
                self.sc_0 = 0.68
                self.sc_60 = 0.56
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 15:
                self.sc_0 = 0.47
                self.sc_60 = 0.45
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 16:
                self.sc_0 = 0.97
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 17:
                self.sc_0 = 0.97
                self.sc_60 = 0.50
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 18:
                self.sc_0 = 0.43
                self.sc_60 = 0.50
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 19:
                self.sc_0 = 0.54
                self.sc_60 = 0.57
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 20:
                self.sc_0 = 0.42
                self.sc_60 = 0.45
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 21:
                self.sc_0 = 0.97
                self.sc_60 = 1.01
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 22:
                self.sc_0 = 0.97
                self.sc_60 = 0.49
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 23:
                self.sc_0 = 0.38
                self.sc_60 = 0.49
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 24:
                self.sc_0 = 0.51
                self.sc_60 = 0.38
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 25:
                self.sc_0 = 0.32
                self.sc_60 = 0.32
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 26:
                self.sc_0 = 0.97
                self.sc_60 = 1.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 27:
                self.sc_0 = 0.97
                self.sc_60 = 0.49
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 28:
                self.sc_0 = 0.35
                self.sc_60 = 0.49
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 29:
                self.sc_0 = 0.50
                self.sc_60 = 0.32
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 30:
                self.sc_0 = 0.24
                self.sc_60 = 0.20
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 31:
                self.sc_0 = 0.93
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 32:
                self.sc_0 = 0.93
                self.sc_60 = 0.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 33:
                self.sc_0 = 0.03
                self.sc_60 = 0.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 34:
                self.sc_0 = 0.19
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 35:
                self.sc_0 = 0.02
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 36:
                self.sc_0 = 0.94
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 37:
                self.sc_0 = 0.94
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 38:
                self.sc_0 = 0.07
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 39:
                self.sc_0 = 0.25
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 40:
                self.sc_0 = 0.04
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 41:
                self.sc_0 = 0.95
                self.sc_60 = 1.08
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 42:
                self.sc_0 = 0.95
                self.sc_60 = 0.29
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 43:
                self.sc_0 = 0.16
                self.sc_60 = 0.29
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 44:
                self.sc_0 = 0.34
                self.sc_60 = 0.12
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 45:
                self.sc_0 = 0.08
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 47:
                self.sc_fc = 0.81
            elif self.shaded_types == 48:
                self.sc_fc = 0.70
            elif self.shaded_types == 49:
                self.sc_fc = 0.57
            elif self.shaded_types == 50:
                self.sc_fc = 0.84
            elif self.shaded_types == 51:
                self.sc_fc = 0.75
            elif self.shaded_types == 52:
                self.sc_fc = 0.65
            elif self.shaded_types == 53:
                self.sc_fc = 0.88
            elif self.shaded_types == 54:
                self.sc_fc = 0.79
            elif self.shaded_types == 55:
                self.sc_fc = 0.72
            elif self.shaded_types == 56:
                self.sc_fc = 0.78
            elif self.shaded_types == 57:
                self.sc_fc = 0.55
            elif self.shaded_types == 58:
                self.sc_fc = 0.48
            elif self.shaded_types == 59:
                self.sc_fc = 0.76
            elif self.shaded_types == 60:
                self.sc_fc = 0.72
            elif self.shaded_types == 61:
                self.sc_fc = 0.81
            elif self.shaded_types == 62:
                self.sc_fc = 0.43
            elif self.shaded_types == 63:
                self.sc_fc = 0.37
            elif self.shaded_types == 64:
                self.sc_fc = 0.64
            elif self.shaded_types == 65:
                self.sc_fc = 0.92
            else:
                self.sc_fc = 1
        elif self.glazed_type == 16:
            if self.shaded_types == 1:
                self.sc_0 = 0.99
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60)*(min((1.2 * float(self.shadow_line)), 60))/60)
            elif self.shaded_types == 2:
                self.sc_0 = 0.99
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 3:
                self.sc_0 = 0.84
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 4:
                self.sc_0 = 0.88
                self.sc_60 = 0.85
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 5:
                self.sc_0 = 0.82
                self.sc_60 = 0.82
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 6:
                self.sc_0 = 0.98
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 7:
                self.sc_0 = 0.98
                self.sc_60 = 0.82
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 8:
                self.sc_0 = 0.72
                self.sc_60 = 0.82
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 9:
                self.sc_0 = 0.80
                self.sc_60 = 0.72
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 10:
                self.sc_0 = 0.66
                self.sc_60 = 0.65
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 11:
                self.sc_0 = 0.97
                self.sc_60 = 0.96
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 12:
                self.sc_0 = 0.97
                self.sc_60 = 0.73
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 13:
                self.sc_0 = 0.60
                self.sc_60 = 0.73
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 14:
                self.sc_0 = 0.71
                self.sc_60 = 0.60
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 15:
                self.sc_0 = 0.51
                self.sc_60 = 0.50
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 16:
                self.sc_0 = 0.97
                self.sc_60 = 0.99
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 17:
                self.sc_0 = 0.97
                self.sc_60 = 0.51
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 18:
                self.sc_0 = 0.45
                self.sc_60 = 0.51
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 19:
                self.sc_0 = 0.55
                self.sc_60 = 0.48
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 20:
                self.sc_0 = 0.44
                self.sc_60 = 0.47
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 21:
                self.sc_0 = 0.97
                self.sc_60 = 1.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 22:
                self.sc_0 = 0.97
                self.sc_60 = 0.5
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 23:
                self.sc_0 = 0.39
                self.sc_60 = 0.50
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 24:
                self.sc_0 = 0.52
                self.sc_60 = 0.40
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 25:
                self.sc_0 = 0.33
                self.sc_60 = 0.33
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 26:
                self.sc_0 = 0.97
                self.sc_60 = 1.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 27:
                self.sc_0 = 0.97
                self.sc_60 = 0.50
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 28:
                self.sc_0 = 0.36
                self.sc_60 = 0.50
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 29:
                self.sc_0 = 0.51
                self.sc_60 = 0.33
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 30:
                self.sc_0 = 0.25
                self.sc_60 = 0.22
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 31:
                self.sc_0 = 0.93
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 32:
                self.sc_0 = 0.93
                self.sc_60 = 0.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 33:
                self.sc_0 = 0.03
                self.sc_60 = 0.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 34:
                self.sc_0 = 0.19
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 35:
                self.sc_0 = 0.02
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 36:
                self.sc_0 = 0.94
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 37:
                self.sc_0 = 0.94
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 38:
                self.sc_0 = 0.07
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 39:
                self.sc_0 = 0.25
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 40:
                self.sc_0 = 0.04
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 41:
                self.sc_0 = 0.95
                self.sc_60 = 1.07
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 42:
                self.sc_0 = 0.95
                self.sc_60 = 0.29
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 43:
                self.sc_0 = 0.16
                self.sc_60 = 0.29
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 44:
                self.sc_0 = 0.34
                self.sc_60 = 0.12
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 45:
                self.sc_0 = 0.08
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 47:
                self.sc_fc = 0.82
            elif self.shaded_types == 48:
                self.sc_fc = 0.72
            elif self.shaded_types == 49:
                self.sc_fc = 0.60
            elif self.shaded_types == 50:
                self.sc_fc = 0.85
            elif self.shaded_types == 51:
                self.sc_fc = 0.76
            elif self.shaded_types == 52:
                self.sc_fc = 0.68
            elif self.shaded_types == 53:
                self.sc_fc = 0.88
            elif self.shaded_types == 54:
                self.sc_fc = 0.80
            elif self.shaded_types == 55:
                self.sc_fc = 0.74
            elif self.shaded_types == 56:
                self.sc_fc = 0.80
            elif self.shaded_types == 57:
                self.sc_fc = 0.58
            elif self.shaded_types == 58:
                self.sc_fc = 0.52
            elif self.shaded_types == 59:
                self.sc_fc = 0.77
            elif self.shaded_types == 60:
                self.sc_fc = 0.74
            elif self.shaded_types == 61:
                self.sc_fc = 0.82
            elif self.shaded_types == 62:
                self.sc_fc = 0.47
            elif self.shaded_types == 63:
                self.sc_fc = 0.42
            elif self.shaded_types == 64:
                self.sc_fc = 0.64
            elif self.shaded_types == 65:
                self.sc_fc = 0.93
            else:
                self.sc_fc = 1
        elif self.glazed_type == 17:
            if self.shaded_types == 1:
                self.sc_0 = 0.99
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60)*(min((1.2 * float(self.shadow_line)), 60))/60)
            elif self.shaded_types == 2:
                self.sc_0 = 0.99
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 3:
                self.sc_0 = 0.84
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 4:
                self.sc_0 = 0.88
                self.sc_60 = 0.85
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 5:
                self.sc_0 = 0.82
                self.sc_60 = 0.82
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 6:
                self.sc_0 = 0.98
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 7:
                self.sc_0 = 0.98
                self.sc_60 = 0.81
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 8:
                self.sc_0 = 0.72
                self.sc_60 = 0.81
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 9:
                self.sc_0 = 0.79
                self.sc_60 = 0.72
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 10:
                self.sc_0 = 0.65
                self.sc_60 = 0.65
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 11:
                self.sc_0 = 0.97
                self.sc_60 = 0.96
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 12:
                self.sc_0 = 0.97
                self.sc_60 = 0.73
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 13:
                self.sc_0 = 0.60
                self.sc_60 = 0.73
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 14:
                self.sc_0 = 0.70
                self.sc_60 = 0.59
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 15:
                self.sc_0 = 0.50
                self.sc_60 = 0.49
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 16:
                self.sc_0 = 0.96
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 17:
                self.sc_0 = 0.96
                self.sc_60 = 0.52
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 18:
                self.sc_0 = 0.46
                self.sc_60 = 0.52
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 19:
                self.sc_0 = 0.56
                self.sc_60 = 0.49
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 20:
                self.sc_0 = 0.44
                self.sc_60 = 0.47
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 21:
                self.sc_0 = 0.96
                self.sc_60 = 1
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 22:
                self.sc_0 = 0.96
                self.sc_60 = 0.51
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 23:
                self.sc_0 = 0.40
                self.sc_60 = 0.51
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 24:
                self.sc_0 = 0.53
                self.sc_60 = 0.41
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 25:
                self.sc_0 = 0.35
                self.sc_60 = 0.35
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 26:
                self.sc_0 = 0.96
                self.sc_60 = 1.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 27:
                self.sc_0 = 0.96
                self.sc_60 = 0.51
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 28:
                self.sc_0 = 0.37
                self.sc_60 = 0.51
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 29:
                self.sc_0 = 0.52
                self.sc_60 = 0.35
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 30:
                self.sc_0 = 0.27
                self.sc_60 = 0.25
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 31:
                self.sc_0 = 0.93
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 32:
                self.sc_0 = 0.93
                self.sc_60 = 0.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 33:
                self.sc_0 = 0.03
                self.sc_60 = 0.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 34:
                self.sc_0 = 0.2
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 35:
                self.sc_0 = 0.02
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 36:
                self.sc_0 = 0.94
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 37:
                self.sc_0 = 0.94
                self.sc_60 = 0.15
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 38:
                self.sc_0 = 0.08
                self.sc_60 = 0.15
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 39:
                self.sc_0 = 0.25
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 40:
                self.sc_0 = 0.04
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 41:
                self.sc_0 = 0.95
                self.sc_60 = 1.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 42:
                self.sc_0 = 0.95
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 43:
                self.sc_0 = 0.16
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 44:
                self.sc_0 = 0.33
                self.sc_60 = 0.12
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 45:
                self.sc_0 = 0.08
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 47:
                self.sc_fc = 0.82
            elif self.shaded_types == 48:
                self.sc_fc = 0.72
            elif self.shaded_types == 49:
                self.sc_fc = 0.59
            elif self.shaded_types == 50:
                self.sc_fc = 0.58
            elif self.shaded_types == 51:
                self.sc_fc = 0.76
            elif self.shaded_types == 52:
                self.sc_fc = 0.67
            elif self.shaded_types == 53:
                self.sc_fc = 0.88
            elif self.shaded_types == 54:
                self.sc_fc = 0.80
            elif self.shaded_types == 55:
                self.sc_fc = 0.73
            elif self.shaded_types == 56:
                self.sc_fc = 0.8
            elif self.shaded_types == 57:
                self.sc_fc = 0.58
            elif self.shaded_types == 58:
                self.sc_fc = 0.51
            elif self.shaded_types == 59:
                self.sc_fc = 0.77
            elif self.shaded_types == 60:
                self.sc_fc = 0.74
            elif self.shaded_types == 61:
                self.sc_fc = 0.82
            elif self.shaded_types == 62:
                self.sc_fc = 0.46
            elif self.shaded_types == 63:
                self.sc_fc = 0.41
            elif self.shaded_types == 64:
                self.sc_fc = 0.64
            elif self.shaded_types == 65:
                self.sc_fc = 0.93
            else:
                self.sc_fc = 1
        elif self.glazed_type == 18:
            if self.shaded_types == 1:
                self.sc_0 = 0.98
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60)*(min((1.2 * float(self.shadow_line)), 60))/60)
            elif self.shaded_types == 2:
                self.sc_0 = 0.98
                self.sc_60 = 0.90
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 3:
                self.sc_0 = 0.86
                self.sc_60 = 0.90
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 4:
                self.sc_0 = 0.89
                self.sc_60 = 0.87
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 5:
                self.sc_0 = 0.83
                self.sc_60 = 0.84
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 6:
                self.sc_0 = 0.98
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 7:
                self.sc_0 = 0.98
                self.sc_60 = 0.84
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 8:
                self.sc_0 = 0.75
                self.sc_60 = 0.84
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 9:
                self.sc_0 = 0.82
                self.sc_60 = 0.76
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 10:
                self.sc_0 = 0.7
                self.sc_60 = 0.7
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 11:
                self.sc_0 = 0.97
                self.sc_60 = 0.96
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 12:
                self.sc_0 = 0.97
                self.sc_60 = 0.77
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 13:
                self.sc_0 = 0.65
                self.sc_60 = 0.77
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 14:
                self.sc_0 = 0.74
                self.sc_60 = 0.65
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 15:
                self.sc_0 = 0.57
                self.sc_60 = 0.56
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 16:
                self.sc_0 = 0.95
                self.sc_60 = 0.96
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 17:
                self.sc_0 = 0.95
                self.sc_60 = 0.55
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 18:
                self.sc_0 = 0.49
                self.sc_60 = 0.55
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 19:
                self.sc_0 = 0.58
                self.sc_60 = 0.52
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 20:
                self.sc_0 = 0.47
                self.sc_60 = 0.50
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 21:
                self.sc_0 = 0.95
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 22:
                self.sc_0 = 0.95
                self.sc_60 = 0.54
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 23:
                self.sc_0 = 0.44
                self.sc_60 = 0.54
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 24:
                self.sc_0 = 0.56
                self.sc_60 = 0.45
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 25:
                self.sc_0 = 0.39
                self.sc_60 = 0.39
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 26:
                self.sc_0 = 0.95
                self.sc_60 = 1.01
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 27:
                self.sc_0 = 0.95
                self.sc_60 = 0.55
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 28:
                self.sc_0 = 0.42
                self.sc_60 = 0.55
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 29:
                self.sc_0 = 0.55
                self.sc_60 = 0.40
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 30:
                self.sc_0 = 0.32
                self.sc_60 = 0.30
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 31:
                self.sc_0 = 0.93
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 32:
                self.sc_0 = 0.93
                self.sc_60 = 0.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 33:
                self.sc_0 = 0.03
                self.sc_60 = 0.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 34:
                self.sc_0 = 0.2
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 35:
                self.sc_0 = 0.03
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 36:
                self.sc_0 = 0.94
                self.sc_60 = 0.96
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 37:
                self.sc_0 = 0.94
                self.sc_60 = 0.15
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 38:
                self.sc_0 = 0.08
                self.sc_60 = 0.15
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 39:
                self.sc_0 = 0.25
                self.sc_60 = 0.07
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 40:
                self.sc_0 = 0.04
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 41:
                self.sc_0 = 0.95
                self.sc_60 = 1.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 42:
                self.sc_0 = 0.95
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 43:
                self.sc_0 = 0.16
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 44:
                self.sc_0 = 0.33
                self.sc_60 = 0.12
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 45:
                self.sc_0 = 0.08
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 47:
                self.sc_fc = 0.83
            elif self.shaded_types == 48:
                self.sc_fc = 0.75
            elif self.shaded_types == 49:
                self.sc_fc = 0.64
            elif self.shaded_types == 50:
                self.sc_fc = 0.86
            elif self.shaded_types == 51:
                self.sc_fc = 0.79
            elif self.shaded_types == 52:
                self.sc_fc = 0.71
            elif self.shaded_types == 53:
                self.sc_fc = 0.89
            elif self.shaded_types == 54:
                self.sc_fc = 0.82
            elif self.shaded_types == 55:
                self.sc_fc = 0.77
            elif self.shaded_types == 56:
                self.sc_fc = 0.82
            elif self.shaded_types == 57:
                self.sc_fc = 0.63
            elif self.shaded_types == 58:
                self.sc_fc = 0.57
            elif self.shaded_types == 59:
                self.sc_fc = 0.8
            elif self.shaded_types == 60:
                self.sc_fc = 0.77
            elif self.shaded_types == 61:
                self.sc_fc = 0.84
            elif self.shaded_types == 62:
                self.sc_fc = 0.54
            elif self.shaded_types == 63:
                self.sc_fc = 0.49
            elif self.shaded_types == 64:
                self.sc_fc = 0.64
            elif self.shaded_types == 65:
                self.sc_fc = 0.93
            else:
                self.sc_fc = 1
        elif self.glazed_type == 19:
            if self.shaded_types == 1:
                self.sc_0 = 0.99
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60)*(min((1.2 * float(self.shadow_line)), 60))/60)
            elif self.shaded_types == 2:
                self.sc_0 = 0.99
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 3:
                self.sc_0 = 0.85
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 4:
                self.sc_0 = 0.88
                self.sc_60 = 0.86
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 5:
                self.sc_0 = 0.82
                self.sc_60 = 0.82
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 6:
                self.sc_0 = 0.98
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 7:
                self.sc_0 = 0.98
                self.sc_60 = 0.82
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 8:
                self.sc_0 = 0.73
                self.sc_60 = 0.82
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 9:
                self.sc_0 = 0.80
                self.sc_60 = 0.73
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 10:
                self.sc_0 = 0.66
                self.sc_60 = 0.66
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 11:
                self.sc_0 = 0.97
                self.sc_60 = 0.96
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 12:
                self.sc_0 = 0.97
                self.sc_60 = 0.73
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 13:
                self.sc_0 = 0.61
                self.sc_60 = 0.73
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 14:
                self.sc_0 = 0.71
                self.sc_60 = 0.60
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 15:
                self.sc_0 = 0.51
                self.sc_60 = 0.50
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 16:
                self.sc_0 = 0.95
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 17:
                self.sc_0 = 0.95
                self.sc_60 = 0.52
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 18:
                self.sc_0 = 0.46
                self.sc_60 = 0.52
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 19:
                self.sc_0 = 0.56
                self.sc_60 = 0.49
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 20:
                self.sc_0 = 0.45
                self.sc_60 = 0.48
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 21:
                self.sc_0 = 0.95
                self.sc_60 = 0.99
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 22:
                self.sc_0 = 0.95
                self.sc_60 = 0.52
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 23:
                self.sc_0 = 0.41
                self.sc_60 = 0.52
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 24:
                self.sc_0 = 0.53
                self.sc_60 = 0.42
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 25:
                self.sc_0 = 0.36
                self.sc_60 = 0.36
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 26:
                self.sc_0 = 0.96
                self.sc_60 = 1.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 27:
                self.sc_0 = 0.96
                self.sc_60 = 0.52
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 28:
                self.sc_0 = 0.38
                self.sc_60 = 0.52
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 29:
                self.sc_0 = 0.53
                self.sc_60 = 0.36
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 30:
                self.sc_0 = 0.28
                self.sc_60 = 0.26
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 31:
                self.sc_0 = 0.93
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 32:
                self.sc_0 = 0.93
                self.sc_60 = 0.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 33:
                self.sc_0 = 0.03
                self.sc_60 = 0.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 34:
                self.sc_0 = 0.2
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 35:
                self.sc_0 = 0.03
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 36:
                self.sc_0 = 0.94
                self.sc_60 = 0.95
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 37:
                self.sc_0 = 0.94
                self.sc_60 = 0.15
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 38:
                self.sc_0 = 0.08
                self.sc_60 = 0.15
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 39:
                self.sc_0 = 0.25
                self.sc_60 = 0.07
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 40:
                self.sc_0 = 0.05
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 41:
                self.sc_0 = 0.95
                self.sc_60 = 1.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 42:
                self.sc_0 = 0.95
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 43:
                self.sc_0 = 0.16
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 44:
                self.sc_0 = 0.33
                self.sc_60 = 0.12
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 45:
                self.sc_0 = 0.08
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 47:
                self.sc_fc = 0.82
            elif self.shaded_types == 48:
                self.sc_fc = 0.72
            elif self.shaded_types == 49:
                self.sc_fc = 0.60
            elif self.shaded_types == 50:
                self.sc_fc = 0.85
            elif self.shaded_types == 51:
                self.sc_fc = 0.76
            elif self.shaded_types == 52:
                self.sc_fc = 0.68
            elif self.shaded_types == 53:
                self.sc_fc = 0.88
            elif self.shaded_types == 54:
                self.sc_fc = 0.80
            elif self.shaded_types == 55:
                self.sc_fc = 0.74
            elif self.shaded_types == 56:
                self.sc_fc = 0.80
            elif self.shaded_types == 57:
                self.sc_fc = 0.58
            elif self.shaded_types == 58:
                self.sc_fc = 0.52
            elif self.shaded_types == 59:
                self.sc_fc = 0.78
            elif self.shaded_types == 60:
                self.sc_fc = 0.74
            elif self.shaded_types == 61:
                self.sc_fc = 0.82
            elif self.shaded_types == 62:
                self.sc_fc = 0.47
            elif self.shaded_types == 63:
                self.sc_fc = 0.42
            elif self.shaded_types == 64:
                self.sc_fc = 0.64
            elif self.shaded_types == 65:
                self.sc_fc = 0.93
            else:
                self.sc_fc = 1
        elif self.glazed_type == 20:
            if self.shaded_types == 1:
                self.sc_0 = 0.98
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60)*(min((1.2 * float(self.shadow_line)), 60))/60)
            elif self.shaded_types == 2:
                self.sc_0 = 0.98
                self.sc_60 = 0.90
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 3:
                self.sc_0 = 0.86
                self.sc_60 = 0.90
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 4:
                self.sc_0 = 0.89
                self.sc_60 = 0.87
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 5:
                self.sc_0 = 0.83
                self.sc_60 = 0.84
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 6:
                self.sc_0 = 0.98
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 7:
                self.sc_0 = 0.98
                self.sc_60 = 0.84
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 8:
                self.sc_0 = 0.76
                self.sc_60 = 0.84
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 9:
                self.sc_0 = 0.82
                self.sc_60 = 0.76
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 10:
                self.sc_0 = 0.70
                self.sc_60 = 0.70
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 11:
                self.sc_0 = 0.97
                self.sc_60 = 0.96
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 12:
                self.sc_0 = 0.97
                self.sc_60 = 0.77
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 13:
                self.sc_0 = 0.66
                self.sc_60 = 0.77
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 14:
                self.sc_0 = 0.75
                self.sc_60 = 0.76
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 15:
                self.sc_0 = 0.57
                self.sc_60 = 0.57
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 16:
                self.sc_0 = 0.95
                self.sc_60 = 0.95
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 17:
                self.sc_0 = 0.95
                self.sc_60 = 0.55
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 18:
                self.sc_0 = 0.49
                self.sc_60 = 0.55
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 19:
                self.sc_0 = 0.58
                self.sc_60 = 0.52
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 20:
                self.sc_0 = 0.48
                self.sc_60 = 0.51
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 21:
                self.sc_0 = 0.95
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 22:
                self.sc_0 = 0.95
                self.sc_60 = 0.55
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 23:
                self.sc_0 = 0.45
                self.sc_60 = 0.55
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 24:
                self.sc_0 = 0.56
                self.sc_60 = 0.46
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 25:
                self.sc_0 = 0.39
                self.sc_60 = 0.40
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 26:
                self.sc_0 = 0.95
                self.sc_60 = 1
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 27:
                self.sc_0 = 0.95
                self.sc_60 = 0.55
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 28:
                self.sc_0 = 0.42
                self.sc_60 = 0.55
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 29:
                self.sc_0 = 0.55
                self.sc_60 = 0.41
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 30:
                self.sc_0 = 0.33
                self.sc_60 = 0.31
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 31:
                self.sc_0 = 0.93
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 32:
                self.sc_0 = 0.93
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 33:
                self.sc_0 = 0.03
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 34:
                self.sc_0 = 0.2
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 35:
                self.sc_0 = 0.03
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 36:
                self.sc_0 = 0.94
                self.sc_60 = 0.95
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 37:
                self.sc_0 = 0.94
                self.sc_60 = 0.15
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 38:
                self.sc_0 = 0.08
                self.sc_60 = 0.15
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 39:
                self.sc_0 = 0.25
                self.sc_60 = 0.08
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 40:
                self.sc_0 = 0.04
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 41:
                self.sc_0 = 0.95
                self.sc_60 = 1.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 42:
                self.sc_0 = 0.95
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 43:
                self.sc_0 = 0.16
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 44:
                self.sc_0 = 0.33
                self.sc_60 = 0.12
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 45:
                self.sc_0 = 0.08
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 47:
                self.sc_fc = 0.83
            elif self.shaded_types == 48:
                self.sc_fc = 0.75
            elif self.shaded_types == 49:
                self.sc_fc = 0.65
            elif self.shaded_types == 50:
                self.sc_fc = 0.86
            elif self.shaded_types == 51:
                self.sc_fc = 0.79
            elif self.shaded_types == 52:
                self.sc_fc = 0.72
            elif self.shaded_types == 53:
                self.sc_fc = 0.89
            elif self.shaded_types == 54:
                self.sc_fc = 0.82
            elif self.shaded_types == 55:
                self.sc_fc = 0.77
            elif self.shaded_types == 56:
                self.sc_fc = 0.82
            elif self.shaded_types == 57:
                self.sc_fc = 0.64
            elif self.shaded_types == 58:
                self.sc_fc = 0.58
            elif self.shaded_types == 59:
                self.sc_fc = 0.8
            elif self.shaded_types == 60:
                self.sc_fc = 0.77
            elif self.shaded_types == 61:
                self.sc_fc = 0.84
            elif self.shaded_types == 62:
                self.sc_fc = 0.55
            elif self.shaded_types == 63:
                self.sc_fc = 0.50
            elif self.shaded_types == 64:
                self.sc_fc = 0.64
            elif self.shaded_types == 65:
                self.sc_fc = 0.93
            else:
                self.sc_fc = 1
        elif self.glazed_type == 21:
            if self.shaded_types == 1:
                self.sc_0 = 0.99
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60)*(min((1.2 * float(self.shadow_line)), 60))/60)
            elif self.shaded_types == 2:
                self.sc_0 = 0.99
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 3:
                self.sc_0 = 0.85
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 4:
                self.sc_0 = 0.88
                self.sc_60 = 0.86
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 5:
                self.sc_0 = 0.82
                self.sc_60 = 0.82
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 6:
                self.sc_0 = 0.98
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 7:
                self.sc_0 = 0.98
                self.sc_60 = 0.82
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 8:
                self.sc_0 = 0.73
                self.sc_60 = 0.82
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 9:
                self.sc_0 = 0.80
                self.sc_60 = 0.73
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 10:
                self.sc_0 = 0.66
                self.sc_60 = 0.66
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 11:
                self.sc_0 = 0.97
                self.sc_60 = 0.96
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 12:
                self.sc_0 = 0.97
                self.sc_60 = 0.73
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 13:
                self.sc_0 = 0.61
                self.sc_60 = 0.73
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 14:
                self.sc_0 = 0.71
                self.sc_60 = 0.60
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 15:
                self.sc_0 = 0.51
                self.sc_60 = 0.5
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 16:
                self.sc_0 = 0.95
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 17:
                self.sc_0 = 0.95
                self.sc_60 = 0.52
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 18:
                self.sc_0 = 0.46
                self.sc_60 = 0.52
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 19:
                self.sc_0 = 0.56
                self.sc_60 = 0.49
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 20:
                self.sc_0 = 0.45
                self.sc_60 = 0.48
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 21:
                self.sc_0 = 0.95
                self.sc_60 = 0.99
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 22:
                self.sc_0 = 0.95
                self.sc_60 = 0.52
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 23:
                self.sc_0 = 0.41
                self.sc_60 = 0.52
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 24:
                self.sc_0 = 0.53
                self.sc_60 = 0.42
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 25:
                self.sc_0 = 0.36
                self.sc_60 = 0.36
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 26:
                self.sc_0 = 0.96
                self.sc_60 = 1.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 27:
                self.sc_0 = 0.96
                self.sc_60 = 0.52
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 28:
                self.sc_0 = 0.38
                self.sc_60 = 0.52
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 29:
                self.sc_0 = 0.53
                self.sc_60 = 0.36
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 30:
                self.sc_0 = 0.28
                self.sc_60 = 0.26
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 31:
                self.sc_0 = 0.93
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 32:
                self.sc_0 = 0.93
                self.sc_60 = 0.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 33:
                self.sc_0 = 0.03
                self.sc_60 = 0.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 34:
                self.sc_0 = 0.2
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 35:
                self.sc_0 = 0.03
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 36:
                self.sc_0 = 0.94
                self.sc_60 = 0.96
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 37:
                self.sc_0 = 0.94
                self.sc_60 = 0.15
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 38:
                self.sc_0 = 0.08
                self.sc_60 = 0.15
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 39:
                self.sc_0 = 0.25
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 40:
                self.sc_0 = 0.04
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 41:
                self.sc_0 = 0.95
                self.sc_60 = 1.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 42:
                self.sc_0 = 0.95
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 43:
                self.sc_0 = 0.16
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 44:
                self.sc_0 = 0.33
                self.sc_60 = 0.12
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 45:
                self.sc_0 = 0.08
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 47:
                self.sc_fc = 0.82
            elif self.shaded_types == 48:
                self.sc_fc = 0.72
            elif self.shaded_types == 49:
                self.sc_fc = 0.60
            elif self.shaded_types == 50:
                self.sc_fc = 0.85
            elif self.shaded_types == 51:
                self.sc_fc = 0.76
            elif self.shaded_types == 52:
                self.sc_fc = 0.68
            elif self.shaded_types == 53:
                self.sc_fc = 0.88
            elif self.shaded_types == 54:
                self.sc_fc = 0.80
            elif self.shaded_types == 55:
                self.sc_fc = 0.74
            elif self.shaded_types == 56:
                self.sc_fc = 0.8
            elif self.shaded_types == 57:
                self.sc_fc = 0.58
            elif self.shaded_types == 58:
                self.sc_fc = 0.52
            elif self.shaded_types == 59:
                self.sc_fc = 0.78
            elif self.shaded_types == 60:
                self.sc_fc = 0.74
            elif self.shaded_types == 61:
                self.sc_fc = 0.82
            elif self.shaded_types == 62:
                self.sc_fc = 0.47
            elif self.shaded_types == 63:
                self.sc_fc = 0.42
            elif self.shaded_types == 64:
                self.sc_fc = 0.64
            elif self.shaded_types == 65:
                self.sc_fc = 0.93
            else:
                self.sc_fc = 1
        elif self.glazed_type == 22:
            if self.shaded_types == 1:
                self.sc_0 = 0.98
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60)*(min((1.2 * float(self.shadow_line)), 60))/60)
            elif self.shaded_types == 2:
                self.sc_0 = 0.98
                self.sc_60 = 0.90
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 3:
                self.sc_0 = 0.86
                self.sc_60 = 0.90
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 4:
                self.sc_0 = 0.89
                self.sc_60 = 0.87
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 5:
                self.sc_0 = 0.83
                self.sc_60 = 0.84
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 6:
                self.sc_0 = 0.98
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 7:
                self.sc_0 = 0.98
                self.sc_60 = 0.84
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 8:
                self.sc_0 = 0.76
                self.sc_60 = 0.84
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 9:
                self.sc_0 = 0.82
                self.sc_60 = 0.76
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 10:
                self.sc_0 = 0.7
                self.sc_60 = 0.7
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 11:
                self.sc_0 = 0.97
                self.sc_60 = 0.96
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 12:
                self.sc_0 = 0.97
                self.sc_60 = 0.77
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 13:
                self.sc_0 = 0.66
                self.sc_60 = 0.77
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 14:
                self.sc_0 = 0.75
                self.sc_60 = 0.66
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 15:
                self.sc_0 = 0.57
                self.sc_60 = 0.57
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 16:
                self.sc_0 = 0.95
                self.sc_60 = 0.95
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 17:
                self.sc_0 = 0.95
                self.sc_60 = 0.55
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 18:
                self.sc_0 = 0.49
                self.sc_60 = 0.55
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 19:
                self.sc_0 = 0.59
                self.sc_60 = 0.52
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 20:
                self.sc_0 = 0.48
                self.sc_60 = 0.51
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 21:
                self.sc_0 = 0.95
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 22:
                self.sc_0 = 0.95
                self.sc_60 = 0.55
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 23:
                self.sc_0 = 0.45
                self.sc_60 = 0.55
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 24:
                self.sc_0 = 0.56
                self.sc_60 = 0.46
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 25:
                self.sc_0 = 0.4
                self.sc_60 = 0.4
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 26:
                self.sc_0 = 0.95
                self.sc_60 = 1
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 27:
                self.sc_0 = 0.95
                self.sc_60 = 0.55
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 28:
                self.sc_0 = 0.42
                self.sc_60 = 0.55
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 29:
                self.sc_0 = 0.56
                self.sc_60 = 0.41
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 30:
                self.sc_0 = 0.33
                self.sc_60 = 0.31
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 31:
                self.sc_0 = 0.93
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 32:
                self.sc_0 = 0.93
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 33:
                self.sc_0 = 0.04
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 34:
                self.sc_0 = 0.2
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 35:
                self.sc_0 = 0.03
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 36:
                self.sc_0 = 0.94
                self.sc_60 = 0.95
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 37:
                self.sc_0 = 0.94
                self.sc_60 = 0.15
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 38:
                self.sc_0 = 0.08
                self.sc_60 = 0.15
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 39:
                self.sc_0 = 0.25
                self.sc_60 = 0.07
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 40:
                self.sc_0 = 0.05
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 41:
                self.sc_0 = 0.95
                self.sc_60 = 1.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 42:
                self.sc_0 = 0.95
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 43:
                self.sc_0 = 0.16
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 44:
                self.sc_0 = 0.33
                self.sc_60 = 0.12
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 45:
                self.sc_0 = 0.08
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 47:
                self.sc_fc = 0.84
            elif self.shaded_types == 48:
                self.sc_fc = 0.75
            elif self.shaded_types == 49:
                self.sc_fc = 0.65
            elif self.shaded_types == 50:
                self.sc_fc = 0.86
            elif self.shaded_types == 51:
                self.sc_fc = 0.79
            elif self.shaded_types == 52:
                self.sc_fc = 0.72
            elif self.shaded_types == 53:
                self.sc_fc = 0.89
            elif self.shaded_types == 54:
                self.sc_fc = 0.82
            elif self.shaded_types == 55:
                self.sc_fc = 0.77
            elif self.shaded_types == 56:
                self.sc_fc = 0.82
            elif self.shaded_types == 57:
                self.sc_fc = 0.64
            elif self.shaded_types == 58:
                self.sc_fc = 0.58
            elif self.shaded_types == 59:
                self.sc_fc = 0.8
            elif self.shaded_types == 60:
                self.sc_fc = 0.77
            elif self.shaded_types == 61:
                self.sc_fc = 0.84
            elif self.shaded_types == 62:
                self.sc_fc = 0.55
            elif self.shaded_types == 63:
                self.sc_fc = 0.5
            elif self.shaded_types == 64:
                self.sc_fc = 0.64
            elif self.shaded_types == 65:
                self.sc_fc = 0.93
            else:
                self.sc_fc = 1
        elif self.glazed_type == 23:
            if self.shaded_types == 1:
                self.sc_0 = 0.98
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60)*(min((1.2 * float(self.shadow_line)), 60))/60)
            elif self.shaded_types == 2:
                self.sc_0 = 0.98
                self.sc_60 = 0.90
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 3:
                self.sc_0 = 0.86
                self.sc_60 = 0.90
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 4:
                self.sc_0 = 0.89
                self.sc_60 = 0.87
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 5:
                self.sc_0 = 0.83
                self.sc_60 = 0.84
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 6:
                self.sc_0 = 0.98
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 7:
                self.sc_0 = 0.98
                self.sc_60 = 0.84
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 8:
                self.sc_0 = 0.75
                self.sc_60 = 0.84
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 9:
                self.sc_0 = 0.72
                self.sc_60 = 0.76
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 10:
                self.sc_0 = 0.70
                self.sc_60 = 0.70
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 11:
                self.sc_0 = 0.97
                self.sc_60 = 0.96
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 12:
                self.sc_0 = 0.97
                self.sc_60 = 0.77
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 13:
                self.sc_0 = 0.65
                self.sc_60 = 0.77
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 14:
                self.sc_0 = 0.74
                self.sc_60 = 0.65
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 15:
                self.sc_0 = 0.57
                self.sc_60 = 0.56
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 16:
                self.sc_0 = 0.95
                self.sc_60 = 0.96
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 17:
                self.sc_0 = 0.95
                self.sc_60 = 0.55
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 18:
                self.sc_0 = 0.49
                self.sc_60 = 0.55
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 19:
                self.sc_0 = 0.58
                self.sc_60 = 0.52
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 20:
                self.sc_0 = 0.47
                self.sc_60 = 0.50
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 21:
                self.sc_0 = 0.95
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 22:
                self.sc_0 = 0.95
                self.sc_60 = 0.54
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 23:
                self.sc_0 = 0.44
                self.sc_60 = 0.54
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 24:
                self.sc_0 = 0.56
                self.sc_60 = 0.45
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 25:
                self.sc_0 = 0.39
                self.sc_60 = 0.39
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 26:
                self.sc_0 = 0.95
                self.sc_60 = 1.01
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 27:
                self.sc_0 = 0.95
                self.sc_60 = 0.55
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 28:
                self.sc_0 = 0.42
                self.sc_60 = 0.55
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 29:
                self.sc_0 = 0.55
                self.sc_60 = 0.40
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 30:
                self.sc_0 = 0.32
                self.sc_60 = 0.30
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 31:
                self.sc_0 = 0.93
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 32:
                self.sc_0 = 0.93
                self.sc_60 = 0.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 33:
                self.sc_0 = 0.03
                self.sc_60 = 0.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 34:
                self.sc_0 = 0.2
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 35:
                self.sc_0 = 0.03
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 36:
                self.sc_0 = 0.94
                self.sc_60 = 0.96
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 37:
                self.sc_0 = 0.94
                self.sc_60 = 0.15
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 38:
                self.sc_0 = 0.08
                self.sc_60 = 0.15
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 39:
                self.sc_0 = 0.25
                self.sc_60 = 0.07
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 40:
                self.sc_0 = 0.04
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 41:
                self.sc_0 = 0.95
                self.sc_60 = 1.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 42:
                self.sc_0 = 0.95
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 43:
                self.sc_0 = 0.16
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 44:
                self.sc_0 = 0.34
                self.sc_60 = 0.12
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 45:
                self.sc_0 = 0.08
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 47:
                self.sc_fc = 0.83
            elif self.shaded_types == 48:
                self.sc_fc = 0.75
            elif self.shaded_types == 49:
                self.sc_fc = 0.64
            elif self.shaded_types == 50:
                self.sc_fc = 0.86
            elif self.shaded_types == 51:
                self.sc_fc = 0.79
            elif self.shaded_types == 52:
                self.sc_fc = 0.72
            elif self.shaded_types == 53:
                self.sc_fc = 0.89
            elif self.shaded_types == 54:
                self.sc_fc = 0.82
            elif self.shaded_types == 55:
                self.sc_fc = 0.77
            elif self.shaded_types == 56:
                self.sc_fc = 0.82
            elif self.shaded_types == 57:
                self.sc_fc = 0.63
            elif self.shaded_types == 58:
                self.sc_fc = 0.57
            elif self.shaded_types == 59:
                self.sc_fc = 0.8
            elif self.shaded_types == 60:
                self.sc_fc = 0.77
            elif self.shaded_types == 61:
                self.sc_fc = 0.84
            elif self.shaded_types == 62:
                self.sc_fc = 0.54
            elif self.shaded_types == 63:
                self.sc_fc = 0.49
            elif self.shaded_types == 64:
                self.sc_fc = 0.64
            elif self.shaded_types == 65:
                self.sc_fc = 0.93
            else:
                self.sc_fc = 1
        elif self.glazed_type == 30:
            if self.shaded_types == 1:
                self.sc_0 = 0.99
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60)*(min((1.2 * float(self.shadow_line)), 60))/60)
            elif self.shaded_types == 2:
                self.sc_0 = 0.99
                self.sc_60 = 0.91
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 3:
                self.sc_0 = 0.87
                self.sc_60 = 0.91
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 4:
                self.sc_0 = 0.90
                self.sc_60 = 0.88
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 5:
                self.sc_0 = 0.85
                self.sc_60 = 0.85
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 6:
                self.sc_0 = 0.98
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 7:
                self.sc_0 = 0.98
                self.sc_60 = 0.83
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 8:
                self.sc_0 = 0.74
                self.sc_60 = 0.83
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 9:
                self.sc_0 = 0.81
                self.sc_60 = 0.74
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 10:
                self.sc_0 = 0.67
                self.sc_60 = 0.67
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 11:
                self.sc_0 = 0.98
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 12:
                self.sc_0 = 0.98
                self.sc_60 = 0.74
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 13:
                self.sc_0 = 0.61
                self.sc_60 = 0.74
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 14:
                self.sc_0 = 0.71
                self.sc_60 = 0.60
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 15:
                self.sc_0 = 0.51
                self.sc_60 = 0.50
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 16:
                self.sc_0 = 0.97
                self.sc_60 = 1.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 17:
                self.sc_0 = 0.97
                self.sc_60 = 0.66
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 18:
                self.sc_0 = 0.59
                self.sc_60 = 0.66
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 19:
                self.sc_0 = 0.67
                self.sc_60 = 0.62
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 20:
                self.sc_0 = 0.57
                self.sc_60 = 0.60
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 21:
                self.sc_0 = 0.97
                self.sc_60 = 1.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 22:
                self.sc_0 = 0.97
                self.sc_60 = 0.61
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 23:
                self.sc_0 = 0.49
                self.sc_60 = 0.61
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 24:
                self.sc_0 = 0.61
                self.sc_60 = 0.49
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 25:
                self.sc_0 = 0.42
                self.sc_60 = 0.42
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 26:
                self.sc_0 = 0.97
                self.sc_60 = 1.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 27:
                self.sc_0 = 0.97
                self.sc_60 = 0.55
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 28:
                self.sc_0 = 0.4
                self.sc_60 = 0.55
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 29:
                self.sc_0 = 0.55
                self.sc_60 = 0.37
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 30:
                self.sc_0 = 0.29
                self.sc_60 = 0.25
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 31:
                self.sc_0 = 0.93
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 32:
                self.sc_0 = 0.93
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 33:
                self.sc_0 = 0.02
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 34:
                self.sc_0 = 0.19
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 35:
                self.sc_0 = 0.02
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 36:
                self.sc_0 = 0.94
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 37:
                self.sc_0 = 0.94
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 38:
                self.sc_0 = 0.07
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 39:
                self.sc_0 = 0.25
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 40:
                self.sc_0 = 0.04
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 41:
                self.sc_0 = 0.95
                self.sc_60 = 1.07
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 42:
                self.sc_0 = 0.95
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 43:
                self.sc_0 = 0.16
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 44:
                self.sc_0 = 0.34
                self.sc_60 = 0.12
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 45:
                self.sc_0 = 0.08
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 47:
                self.sc_fc = 0.85
            elif self.shaded_types == 48:
                self.sc_fc = 0.74
            elif self.shaded_types == 49:
                self.sc_fc = 0.60
            elif self.shaded_types == 50:
                self.sc_fc = 0.88
            elif self.shaded_types == 51:
                self.sc_fc = 0.78
            elif self.shaded_types == 52:
                self.sc_fc = 0.68
            elif self.shaded_types == 53:
                self.sc_fc = 0.9
            elif self.shaded_types == 54:
                self.sc_fc = 0.81
            elif self.shaded_types == 55:
                self.sc_fc = 0.74
            elif self.shaded_types == 56:
                self.sc_fc = 0.80
            elif self.shaded_types == 57:
                self.sc_fc = 0.58
            elif self.shaded_types == 58:
                self.sc_fc = 0.52
            elif self.shaded_types == 59:
                self.sc_fc = 0.8
            elif self.shaded_types == 60:
                self.sc_fc = 0.76
            elif self.shaded_types == 61:
                self.sc_fc = 0.84
            elif self.shaded_types == 62:
                self.sc_fc = 0.46
            elif self.shaded_types == 63:
                self.sc_fc = 0.41
            elif self.shaded_types == 64:
                self.sc_fc = 0.64
            elif self.shaded_types == 65:
                self.sc_fc = 0.94
            else:
                self.sc_fc = 1
        elif self.glazed_type == 31:
            if self.shaded_types == 1:
                self.sc_0 = 0.99
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60)*(min((1.2 * float(self.shadow_line)), 60))/60)
            elif self.shaded_types == 2:
                self.sc_0 = 0.99
                self.sc_60 = 0.91
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 3:
                self.sc_0 = 0.88
                self.sc_60 = 0.91
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 4:
                self.sc_0 = 0.91
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 5:
                self.sc_0 = 0.86
                self.sc_60 = 0.86
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 6:
                self.sc_0 = 0.98
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 7:
                self.sc_0 = 0.98
                self.sc_60 = 0.85
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 8:
                self.sc_0 = 0.76
                self.sc_60 = 0.85
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 9:
                self.sc_0 = 0.83
                self.sc_60 = 0.76
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 10:
                self.sc_0 = 0.70
                self.sc_60 = 0.70
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 11:
                self.sc_0 = 0.98
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 12:
                self.sc_0 = 0.98
                self.sc_60 = 0.76
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 13:
                self.sc_0 = 0.64
                self.sc_60 = 0.76
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 14:
                self.sc_0 = 0.74
                self.sc_60 = 0.64
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 15:
                self.sc_0 = 0.55
                self.sc_60 = 0.54
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 16:
                self.sc_0 = 0.98
                self.sc_60 = 1.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 17:
                self.sc_0 = 0.98
                self.sc_60 = 0.67
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 18:
                self.sc_0 = 0.60
                self.sc_60 = 0.67
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 19:
                self.sc_0 = 0.68
                self.sc_60 = 0.63
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 20:
                self.sc_0 = 0.58
                self.sc_60 = 0.61
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 21:
                self.sc_0 = 0.97
                self.sc_60 = 1.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 22:
                self.sc_0 = 0.97
                self.sc_60 = 0.62
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 23:
                self.sc_0 = 0.50
                self.sc_60 = 0.62
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 24:
                self.sc_0 = 0.62
                self.sc_60 = 0.50
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 25:
                self.sc_0 = 0.43
                self.sc_60 = 0.43
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 26:
                self.sc_0 = 0.97
                self.sc_60 = 1.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 27:
                self.sc_0 = 0.97
                self.sc_60 = 0.56
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 28:
                self.sc_0 = 0.41
                self.sc_60 = 0.56
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 29:
                self.sc_0 = 0.56
                self.sc_60 = 0.39
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 30:
                self.sc_0 = 0.30
                self.sc_60 = 0.27
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 31:
                self.sc_0 = 0.93
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 32:
                self.sc_0 = 0.93
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 33:
                self.sc_0 = 0.02
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 34:
                self.sc_0 = 0.19
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 35:
                self.sc_0 = 0.02
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 36:
                self.sc_0 = 0.94
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 37:
                self.sc_0 = 0.94
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 38:
                self.sc_0 = 0.07
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 39:
                self.sc_0 = 0.25
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 40:
                self.sc_0 = 0.04
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 41:
                self.sc_0 = 0.95
                self.sc_60 = 1.07
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 42:
                self.sc_0 = 0.95
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 43:
                self.sc_0 = 0.16
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 44:
                self.sc_0 = 0.34
                self.sc_60 = 0.12
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 45:
                self.sc_0 = 0.08
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 47:
                self.sc_fc = 0.86
            elif self.shaded_types == 48:
                self.sc_fc = 0.76
            elif self.shaded_types == 49:
                self.sc_fc = 0.64
            elif self.shaded_types == 50:
                self.sc_fc = 0.89
            elif self.shaded_types == 51:
                self.sc_fc = 0.80
            elif self.shaded_types == 52:
                self.sc_fc = 0.71
            elif self.shaded_types == 53:
                self.sc_fc = 0.91
            elif self.shaded_types == 54:
                self.sc_fc = 0.83
            elif self.shaded_types == 55:
                self.sc_fc = 0.76
            elif self.shaded_types == 56:
                self.sc_fc = 0.82
            elif self.shaded_types == 57:
                self.sc_fc = 0.62
            elif self.shaded_types == 58:
                self.sc_fc = 0.56
            elif self.shaded_types == 59:
                self.sc_fc = 0.82
            elif self.shaded_types == 60:
                self.sc_fc = 0.78
            elif self.shaded_types == 61:
                self.sc_fc = 0.85
            elif self.shaded_types == 62:
                self.sc_fc = 0.52
            elif self.shaded_types == 63:
                self.sc_fc = 0.47
            elif self.shaded_types == 64:
                self.sc_fc = 0.64
            elif self.shaded_types == 65:
                self.sc_fc = 0.94
            else:
                self.sc_fc = 1
        elif self.glazed_type == 32:
            if self.shaded_types == 1:
                self.sc_0 = 0.99
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60)*(min((1.2 * float(self.shadow_line)), 60))/60)
            elif self.shaded_types == 2:
                self.sc_0 = 0.99
                self.sc_60 = 0.91
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 3:
                self.sc_0 = 0.88
                self.sc_60 = 0.91
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 4:
                self.sc_0 = 0.91
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 5:
                self.sc_0 = 0.85
                self.sc_60 = 0.86
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 6:
                self.sc_0 = 0.98
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 7:
                self.sc_0 = 0.98
                self.sc_60 = 0.85
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 8:
                self.sc_0 = 0.76
                self.sc_60 = 0.85
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 9:
                self.sc_0 = 0.83
                self.sc_60 = 0.76
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 10:
                self.sc_0 = 0.70
                self.sc_60 = 0.70
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 11:
                self.sc_0 = 0.98
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 12:
                self.sc_0 = 0.98
                self.sc_60 = 0.76
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 13:
                self.sc_0 = 0.64
                self.sc_60 = 0.76
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 14:
                self.sc_0 = 0.74
                self.sc_60 = 0.64
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 15:
                self.sc_0 = 0.55
                self.sc_60 = 0.55
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 16:
                self.sc_0 = 0.96
                self.sc_60 = 0.96
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 17:
                self.sc_0 = 0.96
                self.sc_60 = 0.39
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 18:
                self.sc_0 = 0.33
                self.sc_60 = 0.39
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 19:
                self.sc_0 = 0.46
                self.sc_60 = 0.36
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 20:
                self.sc_0 = 0.32
                self.sc_60 = 0.34
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 21:
                self.sc_0 = 0.96
                self.sc_60 = 1.01
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 22:
                self.sc_0 = 0.96
                self.sc_60 = 0.41
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 23:
                self.sc_0 = 0.31
                self.sc_60 = 0.41
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 24:
                self.sc_0 = 0.45
                self.sc_60 = 0.31
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 25:
                self.sc_0 = 0.25
                self.sc_60 = 0.25
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 26:
                self.sc_0 = 0.97
                self.sc_60 = 1.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 27:
                self.sc_0 = 0.97
                self.sc_60 = 0.45
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 28:
                self.sc_0 = 0.31
                self.sc_60 = 0.45
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 29:
                self.sc_0 = 0.47
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 30:
                self.sc_0 = 0.21
                self.sc_60 = 0.17
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 31:
                self.sc_0 = 0.93
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 32:
                self.sc_0 = 0.93
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 33:
                self.sc_0 = 0.02
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 34:
                self.sc_0 = 0.19
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 35:
                self.sc_0 = 0.02
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 36:
                self.sc_0 = 0.94
                self.sc_60 = 0.99
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 37:
                self.sc_0 = 0.94
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 38:
                self.sc_0 = 0.07
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 39:
                self.sc_0 = 0.25
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 40:
                self.sc_0 = 0.04
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 41:
                self.sc_0 = 0.95
                self.sc_60 = 1.08
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 42:
                self.sc_0 = 0.95
                self.sc_60 = 0.29
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 43:
                self.sc_0 = 0.16
                self.sc_60 = 0.29
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 44:
                self.sc_0 = 0.34
                self.sc_60 = 0.12
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 45:
                self.sc_0 = 0.08
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 47:
                self.sc_fc = 0.86
            elif self.shaded_types == 48:
                self.sc_fc = 0.76
            elif self.shaded_types == 49:
                self.sc_fc = 0.64
            elif self.shaded_types == 50:
                self.sc_fc = 0.88
            elif self.shaded_types == 51:
                self.sc_fc = 0.80
            elif self.shaded_types == 52:
                self.sc_fc = 0.71
            elif self.shaded_types == 53:
                self.sc_fc = 0.91
            elif self.shaded_types == 54:
                self.sc_fc = 0.83
            elif self.shaded_types == 55:
                self.sc_fc = 0.76
            elif self.shaded_types == 56:
                self.sc_fc = 0.82
            elif self.shaded_types == 57:
                self.sc_fc = 0.62
            elif self.shaded_types == 58:
                self.sc_fc = 0.57
            elif self.shaded_types == 59:
                self.sc_fc = 0.82
            elif self.shaded_types == 60:
                self.sc_fc = 0.78
            elif self.shaded_types == 61:
                self.sc_fc = 0.85
            elif self.shaded_types == 62:
                self.sc_fc = 0.52
            elif self.shaded_types == 63:
                self.sc_fc = 0.47
            elif self.shaded_types == 64:
                self.sc_fc = 0.64
            elif self.shaded_types == 65:
                self.sc_fc = 0.94
            else:
                self.sc_fc = 1
        elif self.glazed_type == 33:
            if self.shaded_types == 1:
                self.sc_0 = 0.99
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60)*(min((1.2 * float(self.shadow_line)), 60))/60)
            elif self.shaded_types == 2:
                self.sc_0 = 0.99
                self.sc_60 = 0.92
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 3:
                self.sc_0 = 0.89
                self.sc_60 = 0.92
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 4:
                self.sc_0 = 0.92
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 5:
                self.sc_0 = 0.86
                self.sc_60 = 0.87
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 6:
                self.sc_0 = 0.98
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 7:
                self.sc_0 = 0.98
                self.sc_60 = 0.86
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 8:
                self.sc_0 = 0.79
                self.sc_60 = 0.86
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 9:
                self.sc_0 = 0.84
                self.sc_60 = 0.79
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 10:
                self.sc_0 = 0.73
                self.sc_60 = 0.73
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 11:
                self.sc_0 = 0.98
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 12:
                self.sc_0 = 0.98
                self.sc_60 = 0.79
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 13:
                self.sc_0 = 0.68
                self.sc_60 = 0.79
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 14:
                self.sc_0 = 0.77
                self.sc_60 = 0.68
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 15:
                self.sc_0 = 0.60
                self.sc_60 = 0.60
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 16:
                self.sc_0 = 0.96
                self.sc_60 = 0.96
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 17:
                self.sc_0 = 0.96
                self.sc_60 = 0.40
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 18:
                self.sc_0 = 0.34
                self.sc_60 = 0.40
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 19:
                self.sc_0 = 0.46
                self.sc_60 = 0.37
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 20:
                self.sc_0 = 0.33
                self.sc_60 = 0.35
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 21:
                self.sc_0 = 0.96
                self.sc_60 = 1.01
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 22:
                self.sc_0 = 0.96
                self.sc_60 = 0.42
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 23:
                self.sc_0 = 0.32
                self.sc_60 = 0.42
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 24:
                self.sc_0 = 0.46
                self.sc_60 = 0.32
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 25:
                self.sc_0 = 0.26
                self.sc_60 = 0.26
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 26:
                self.sc_0 = 0.97
                self.sc_60 = 1.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 27:
                self.sc_0 = 0.97
                self.sc_60 = 0.46
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 28:
                self.sc_0 = 0.32
                self.sc_60 = 0.46
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 29:
                self.sc_0 = 0.48
                self.sc_60 = 0.29
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 30:
                self.sc_0 = 0.22
                self.sc_60 = 0.18
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 31:
                self.sc_0 = 0.93
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 32:
                self.sc_0 = 0.93
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 33:
                self.sc_0 = 0.02
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 34:
                self.sc_0 = 0.19
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 35:
                self.sc_0 = 0.02
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 36:
                self.sc_0 = 0.94
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 37:
                self.sc_0 = 0.94
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 38:
                self.sc_0 = 0.07
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 39:
                self.sc_0 = 0.25
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 40:
                self.sc_0 = 0.04
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 41:
                self.sc_0 = 0.95
                self.sc_60 = 1.08
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 42:
                self.sc_0 = 0.95
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 43:
                self.sc_0 = 0.16
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 44:
                self.sc_0 = 0.34
                self.sc_60 = 0.12
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 45:
                self.sc_0 = 0.08
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 47:
                self.sc_fc = 0.87
            elif self.shaded_types == 48:
                self.sc_fc = 0.79
            elif self.shaded_types == 49:
                self.sc_fc = 0.68
            elif self.shaded_types == 50:
                self.sc_fc = 0.89
            elif self.shaded_types == 51:
                self.sc_fc = 0.82
            elif self.shaded_types == 52:
                self.sc_fc = 0.74
            elif self.shaded_types == 53:
                self.sc_fc = 0.91
            elif self.shaded_types == 54:
                self.sc_fc = 0.85
            elif self.shaded_types == 55:
                self.sc_fc = 0.79
            elif self.shaded_types == 56:
                self.sc_fc = 0.84
            elif self.shaded_types == 57:
                self.sc_fc = 0.67
            elif self.shaded_types == 58:
                self.sc_fc = 0.61
            elif self.shaded_types == 59:
                self.sc_fc = 0.83
            elif self.shaded_types == 60:
                self.sc_fc = 0.8
            elif self.shaded_types == 61:
                self.sc_fc = 0.86
            elif self.shaded_types == 62:
                self.sc_fc = 0.58
            elif self.shaded_types == 63:
                self.sc_fc = 0.53
            elif self.shaded_types == 64:
                self.sc_fc = 0.64
            elif self.shaded_types == 65:
                self.sc_fc = 0.94
            else:
                self.sc_fc = 1
        elif self.glazed_type == 34:
            if self.shaded_types == 1:
                self.sc_0 = 0.99
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60)*(min((1.2 * float(self.shadow_line)), 60))/60)
            elif self.shaded_types == 2:
                self.sc_0 = 0.99
                self.sc_60 = 0.92
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 3:
                self.sc_0 = 0.89
                self.sc_60 = 0.92
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 4:
                self.sc_0 = 0.92
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 5:
                self.sc_0 = 0.86
                self.sc_60 = 0.87
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 6:
                self.sc_0 = 0.98
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 7:
                self.sc_0 = 0.98
                self.sc_60 = 0.85
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 8:
                self.sc_0 = 0.77
                self.sc_60 = 0.85
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 9:
                self.sc_0 = 0.83
                self.sc_60 = 0.77
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 10:
                self.sc_0 = 0.71
                self.sc_60 = 0.71
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 11:
                self.sc_0 = 0.98
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 12:
                self.sc_0 = 0.98
                self.sc_60 = 0.77
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 13:
                self.sc_0 = 0.66
                self.sc_60 = 0.77
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 14:
                self.sc_0 = 0.75
                self.sc_60 = 0.66
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 15:
                self.sc_0 = 0.57
                self.sc_60 = 0.57
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 16:
                self.sc_0 = 0.95
                self.sc_60 = 0.95
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 17:
                self.sc_0 = 0.95
                self.sc_60 = 0.41
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 18:
                self.sc_0 = 0.35
                self.sc_60 = 0.41
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 19:
                self.sc_0 = 0.47
                self.sc_60 = 0.38
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 20:
                self.sc_0 = 0.34
                self.sc_60 = 0.36
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 21:
                self.sc_0 = 0.96
                self.sc_60 = 1
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 22:
                self.sc_0 = 0.96
                self.sc_60 = 0.43
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 23:
                self.sc_0 = 0.33
                self.sc_60 = 0.43
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 24:
                self.sc_0 = 0.47
                self.sc_60 = 0.33
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 25:
                self.sc_0 = 0.28
                self.sc_60 = 0.27
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 26:
                self.sc_0 = 0.96
                self.sc_60 = 1.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 27:
                self.sc_0 = 0.97
                self.sc_60 = 0.46
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 28:
                self.sc_0 = 0.33
                self.sc_60 = 0.46
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 29:
                self.sc_0 = 0.49
                self.sc_60 = 0.31
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 30:
                self.sc_0 = 0.24
                self.sc_60 = 0.20
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 31:
                self.sc_0 = 0.93
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 32:
                self.sc_0 = 0.93
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 33:
                self.sc_0 = 0.02
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 34:
                self.sc_0 = 0.19
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 35:
                self.sc_0 = 0.02
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 36:
                self.sc_0 = 0.94
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 37:
                self.sc_0 = 0.94
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 38:
                self.sc_0 = 0.07
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 39:
                self.sc_0 = 0.25
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 40:
                self.sc_0 = 0.04
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 41:
                self.sc_0 = 0.95
                self.sc_60 = 1.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 42:
                self.sc_0 = 0.95
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 43:
                self.sc_0 = 0.16
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 44:
                self.sc_0 = 0.34
                self.sc_60 = 0.12
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 45:
                self.sc_0 = 0.08
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 47:
                self.sc_fc = 0.86
            elif self.shaded_types == 48:
                self.sc_fc = 0.77
            elif self.shaded_types == 49:
                self.sc_fc = 0.66
            elif self.shaded_types == 50:
                self.sc_fc = 0.89
            elif self.shaded_types == 51:
                self.sc_fc = 0.81
            elif self.shaded_types == 52:
                self.sc_fc = 0.72
            elif self.shaded_types == 53:
                self.sc_fc = 0.91
            elif self.shaded_types == 54:
                self.sc_fc = 0.84
            elif self.shaded_types == 55:
                self.sc_fc = 0.77
            elif self.shaded_types == 56:
                self.sc_fc = 0.83
            elif self.shaded_types == 57:
                self.sc_fc = 0.64
            elif self.shaded_types == 58:
                self.sc_fc = 0.59
            elif self.shaded_types == 59:
                self.sc_fc = 0.82
            elif self.shaded_types == 60:
                self.sc_fc = 0.78
            elif self.shaded_types == 61:
                self.sc_fc = 0.86
            elif self.shaded_types == 62:
                self.sc_fc = 0.54
            elif self.shaded_types == 63:
                self.sc_fc = 0.49
            elif self.shaded_types == 64:
                self.sc_fc = 0.64
            elif self.shaded_types == 65:
                self.sc_fc = 0.94
            else:
                self.sc_fc = 1
        elif self.glazed_type == 35:
            if self.shaded_types == 1:
                self.sc_0 = 0.99
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60)*(min((1.2 * float(self.shadow_line)), 60))/60)
            elif self.shaded_types == 2:
                self.sc_0 = 0.99
                self.sc_60 = 0.93
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 3:
                self.sc_0 = 0.90
                self.sc_60 = 0.93
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 4:
                self.sc_0 = 0.92
                self.sc_60 = 0.90
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 5:
                self.sc_0 = 0.87
                self.sc_60 = 0.88
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 6:
                self.sc_0 = 0.98
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 7:
                self.sc_0 = 0.98
                self.sc_60 = 0.87
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 8:
                self.sc_0 = 0.80
                self.sc_60 = 0.87
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 9:
                self.sc_0 = 0.86
                self.sc_60 = 0.81
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 10:
                self.sc_0 = 0.75
                self.sc_60 = 0.75
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 11:
                self.sc_0 = 0.98
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 12:
                self.sc_0 = 0.98
                self.sc_60 = 0.81
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 13:
                self.sc_0 = 0.71
                self.sc_60 = 0.81
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 14:
                self.sc_0 = 0.79
                self.sc_60 = 0.71
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 15:
                self.sc_0 = 0.64
                self.sc_60 = 0.64
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 16:
                self.sc_0 = 0.95
                self.sc_60 = 0.95
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 17:
                self.sc_0 = 0.95
                self.sc_60 = 0.44
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 18:
                self.sc_0 = 0.38
                self.sc_60 = 0.44
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 19:
                self.sc_0 = 0.50
                self.sc_60 = 0.41
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 20:
                self.sc_0 = 0.37
                self.sc_60 = 0.40
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 21:
                self.sc_0 = 0.95
                self.sc_60 = 0.99
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 22:
                self.sc_0 = 0.95
                self.sc_60 = 0.45
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 23:
                self.sc_0 = 0.36
                self.sc_60 = 0.45
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 24:
                self.sc_0 = 0.49
                self.sc_60 = 0.37
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 25:
                self.sc_0 = 0.31
                self.sc_60 = 0.31
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 26:
                self.sc_0 = 0.96
                self.sc_60 = 1.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 27:
                self.sc_0 = 0.96
                self.sc_60 = 0.49
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 28:
                self.sc_0 = 0.37
                self.sc_60 = 0.49
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 29:
                self.sc_0 = 0.61
                self.sc_60 = 0.34
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 30:
                self.sc_0 = 0.27
                self.sc_60 = 0.25
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 31:
                self.sc_0 = 0.93
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 32:
                self.sc_0 = 0.93
                self.sc_60 = 0.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 33:
                self.sc_0 = 0.03
                self.sc_60 = 0.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 34:
                self.sc_0 = 0.19
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 35:
                self.sc_0 = 0.02
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 36:
                self.sc_0 = 0.94
                self.sc_60 = 0.95
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 37:
                self.sc_0 = 0.94
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 38:
                self.sc_0 = 0.07
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 39:
                self.sc_0 = 0.25
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 40:
                self.sc_0 = 0.04
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 41:
                self.sc_0 = 0.95
                self.sc_60 = 1.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 42:
                self.sc_0 = 0.95
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 43:
                self.sc_0 = 0.16
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 44:
                self.sc_0 = 0.33
                self.sc_60 = 0.12
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 45:
                self.sc_0 = 0.08
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 47:
                self.sc_fc = 0.88
            elif self.shaded_types == 48:
                self.sc_fc = 0.70
            elif self.shaded_types == 49:
                self.sc_fc = 0.71
            elif self.shaded_types == 50:
                self.sc_fc = 0.90
            elif self.shaded_types == 51:
                self.sc_fc = 0.83
            elif self.shaded_types == 52:
                self.sc_fc = 0.76
            elif self.shaded_types == 53:
                self.sc_fc = 0.92
            elif self.shaded_types == 54:
                self.sc_fc = 0.86
            elif self.shaded_types == 55:
                self.sc_fc = 0.81
            elif self.shaded_types == 56:
                self.sc_fc = 0.85
            elif self.shaded_types == 57:
                self.sc_fc = 0.69
            elif self.shaded_types == 58:
                self.sc_fc = 0.65
            elif self.shaded_types == 59:
                self.sc_fc = 0.84
            elif self.shaded_types == 60:
                self.sc_fc = 0.81
            elif self.shaded_types == 61:
                self.sc_fc = 0.87
            elif self.shaded_types == 62:
                self.sc_fc = 0.61
            elif self.shaded_types == 63:
                self.sc_fc = 0.57
            elif self.shaded_types == 64:
                self.sc_fc = 0.64
            elif self.shaded_types == 65:
                self.sc_fc = 0.95
            else:
                self.sc_fc = 1
        elif self.glazed_type == 36:
            if self.shaded_types == 1:
                self.sc_0 = 0.99
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60)*(min((1.2 * float(self.shadow_line)), 60))/60)
            elif self.shaded_types == 2:
                self.sc_0 = 0.99
                self.sc_60 = 0.92
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 3:
                self.sc_0 = 0.88
                self.sc_60 = 0.92
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 4:
                self.sc_0 = 0.91
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 5:
                self.sc_0 = 0.86
                self.sc_60 = 0.86
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 6:
                self.sc_0 = 0.98
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 7:
                self.sc_0 = 0.98
                self.sc_60 = 0.85
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 8:
                self.sc_0 = 0.77
                self.sc_60 = 0.85
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 9:
                self.sc_0 = 0.83
                self.sc_60 = 0.77
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 10:
                self.sc_0 = 0.72
                self.sc_60 = 0.71
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 11:
                self.sc_0 = 0.98
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 12:
                self.sc_0 = 0.98
                self.sc_60 = 0.77
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 13:
                self.sc_0 = 0.66
                self.sc_60 = 0.77
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 14:
                self.sc_0 = 0.75
                self.sc_60 = 0.66
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 15:
                self.sc_0 = 0.58
                self.sc_60 = 0.57
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 16:
                self.sc_0 = 0.95
                self.sc_60 = 0.95
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 17:
                self.sc_0 = 0.95
                self.sc_60 = 0.41
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 18:
                self.sc_0 = 0.36
                self.sc_60 = 0.41
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 19:
                self.sc_0 = 0.47
                self.sc_60 = 0.38
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 20:
                self.sc_0 = 0.35
                self.sc_60 = 0.37
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 21:
                self.sc_0 = 0.95
                self.sc_60 = 0.99
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 22:
                self.sc_0 = 0.95
                self.sc_60 = 0.43
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 23:
                self.sc_0 = 0.33
                self.sc_60 = 0.43
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 24:
                self.sc_0 = 0.47
                self.sc_60 = 0.34
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 25:
                self.sc_0 = 0.28
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 26:
                self.sc_0 = 0.96
                self.sc_60 = 1.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 27:
                self.sc_0 = 0.96
                self.sc_60 = 0.47
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 28:
                self.sc_0 = 0.34
                self.sc_60 = 0.47
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 29:
                self.sc_0 = 0.49
                self.sc_60 = 0.31
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 30:
                self.sc_0 = 0.24
                self.sc_60 = 0.21
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 31:
                self.sc_0 = 0.93
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 32:
                self.sc_0 = 0.93
                self.sc_60 = 0.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 33:
                self.sc_0 = 0.03
                self.sc_60 = 0.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 34:
                self.sc_0 = 0.19
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 35:
                self.sc_0 = 0.02
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 36:
                self.sc_0 = 0.94
                self.sc_60 = 0.96
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 37:
                self.sc_0 = 0.94
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 38:
                self.sc_0 = 0.07
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 39:
                self.sc_0 = 0.25
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 40:
                self.sc_0 = 0.04
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 41:
                self.sc_0 = 0.95
                self.sc_60 = 1.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 42:
                self.sc_0 = 0.95
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 43:
                self.sc_0 = 0.16
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 44:
                self.sc_0 = 0.33
                self.sc_60 = 0.12
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 45:
                self.sc_0 = 0.08
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 47:
                self.sc_fc = 0.87
            elif self.shaded_types == 48:
                self.sc_fc = 0.78
            elif self.shaded_types == 49:
                self.sc_fc = 0.66
            elif self.shaded_types == 50:
                self.sc_fc = 0.89
            elif self.shaded_types == 51:
                self.sc_fc = 0.81
            elif self.shaded_types == 52:
                self.sc_fc = 0.73
            elif self.shaded_types == 53:
                self.sc_fc = 0.91
            elif self.shaded_types == 54:
                self.sc_fc = 0.84
            elif self.shaded_types == 55:
                self.sc_fc = 0.78
            elif self.shaded_types == 56:
                self.sc_fc = 0.83
            elif self.shaded_types == 57:
                self.sc_fc = 0.64
            elif self.shaded_types == 58:
                self.sc_fc = 0.59
            elif self.shaded_types == 59:
                self.sc_fc = 0.82
            elif self.shaded_types == 60:
                self.sc_fc = 0.79
            elif self.shaded_types == 61:
                self.sc_fc = 0.86
            elif self.shaded_types == 62:
                self.sc_fc = 0.55
            elif self.shaded_types == 63:
                self.sc_fc = 0.5
            elif self.shaded_types == 64:
                self.sc_fc = 0.64
            elif self.shaded_types == 65:
                self.sc_fc = 0.94
            else:
                self.sc_fc = 1
        elif self.glazed_type == 37:
            if self.shaded_types == 1:
                self.sc_0 = 0.99
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60)*(min((1.2 * float(self.shadow_line)), 60))/60)
            elif self.shaded_types == 2:
                self.sc_0 = 0.99
                self.sc_60 = 0.93
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 3:
                self.sc_0 = 0.90
                self.sc_60 = 0.93
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 4:
                self.sc_0 = 0.92
                self.sc_60 = 0.90
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 5:
                self.sc_0 = 0.87
                self.sc_60 = 0.88
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 6:
                self.sc_0 = 0.98
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 7:
                self.sc_0 = 0.98
                self.sc_60 = 0.87
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 8:
                self.sc_0 = 0.80
                self.sc_60 = 0.87
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 9:
                self.sc_0 = 0.86
                self.sc_60 = 0.81
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 10:
                self.sc_0 = 0.76
                self.sc_60 = 0.75
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 11:
                self.sc_0 = 0.98
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 12:
                self.sc_0 = 0.98
                self.sc_60 = 0.81
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 13:
                self.sc_0 = 0.71
                self.sc_60 = 0.81
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 14:
                self.sc_0 = 0.79
                self.sc_60 = 0.71
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 15:
                self.sc_0 = 0.64
                self.sc_60 = 0.64
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 16:
                self.sc_0 = 0.95
                self.sc_60 = 0.95
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 17:
                self.sc_0 = 0.95
                self.sc_60 = 0.44
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 18:
                self.sc_0 = 0.39
                self.sc_60 = 0.44
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 19:
                self.sc_0 = 0.50
                self.sc_60 = 0.41
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 20:
                self.sc_0 = 0.38
                self.sc_60 = 0.40
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 21:
                self.sc_0 = 0.95
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 22:
                self.sc_0 = 0.95
                self.sc_60 = 0.46
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 23:
                self.sc_0 = 0.37
                self.sc_60 = 0.46
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 24:
                self.sc_0 = 0.50
                self.sc_60 = 0.37
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 25:
                self.sc_0 = 0.32
                self.sc_60 = 0.31
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 26:
                self.sc_0 = 0.95
                self.sc_60 = 1.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 27:
                self.sc_0 = 0.95
                self.sc_60 = 0.49
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 28:
                self.sc_0 = 0.37
                self.sc_60 = 0.49
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 29:
                self.sc_0 = 0.51
                self.sc_60 = 0.35
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 30:
                self.sc_0 = 0.28
                self.sc_60 = 0.25
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 31:
                self.sc_0 = 0.93
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 32:
                self.sc_0 = 0.93
                self.sc_60 = 0.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 33:
                self.sc_0 = 0.03
                self.sc_60 = 0.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 34:
                self.sc_0 = 0.20
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 35:
                self.sc_0 = 0.02
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 36:
                self.sc_0 = 0.94
                self.sc_60 = 0.95
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 37:
                self.sc_0 = 0.94
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 38:
                self.sc_0 = 0.07
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 39:
                self.sc_0 = 0.25
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 40:
                self.sc_0 = 0.04
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 41:
                self.sc_0 = 0.95
                self.sc_60 = 1.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 42:
                self.sc_0 = 0.95
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 43:
                self.sc_0 = 0.16
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 44:
                self.sc_0 = 0.33
                self.sc_60 = 0.12
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 45:
                self.sc_0 = 0.08
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 47:
                self.sc_fc = 0.88
            elif self.shaded_types == 48:
                self.sc_fc = 0.70
            elif self.shaded_types == 49:
                self.sc_fc = 0.71
            elif self.shaded_types == 50:
                self.sc_fc = 0.90
            elif self.shaded_types == 51:
                self.sc_fc = 0.83
            elif self.shaded_types == 52:
                self.sc_fc = 0.77
            elif self.shaded_types == 53:
                self.sc_fc = 0.92
            elif self.shaded_types == 54:
                self.sc_fc = 0.86
            elif self.shaded_types == 55:
                self.sc_fc = 0.81
            elif self.shaded_types == 56:
                self.sc_fc = 0.85
            elif self.shaded_types == 57:
                self.sc_fc = 0.7
            elif self.shaded_types == 58:
                self.sc_fc = 0.65
            elif self.shaded_types == 59:
                self.sc_fc = 0.84
            elif self.shaded_types == 60:
                self.sc_fc = 0.82
            elif self.shaded_types == 61:
                self.sc_fc = 0.88
            elif self.shaded_types == 62:
                self.sc_fc = 0.62
            elif self.shaded_types == 63:
                self.sc_fc = 0.58
            elif self.shaded_types == 64:
                self.sc_fc = 0.64
            elif self.shaded_types == 65:
                self.sc_fc = 0.95
            else:
                self.sc_fc = 1
        elif self.glazed_type == 38:
            if self.shaded_types == 1:
                self.sc_0 = 0.99
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60)*(min((1.2 * float(self.shadow_line)), 60))/60)
            elif self.shaded_types == 2:
                self.sc_0 = 0.99
                self.sc_60 = 0.92
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 3:
                self.sc_0 = 0.88
                self.sc_60 = 0.92
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 4:
                self.sc_0 = 0.91
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 5:
                self.sc_0 = 0.86
                self.sc_60 = 0.86
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 6:
                self.sc_0 = 0.98
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 7:
                self.sc_0 = 0.98
                self.sc_60 = 0.85
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 8:
                self.sc_0 = 0.77
                self.sc_60 = 0.85
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 9:
                self.sc_0 = 0.83
                self.sc_60 = 0.77
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 10:
                self.sc_0 = 0.72
                self.sc_60 = 0.71
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 11:
                self.sc_0 = 0.98
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 12:
                self.sc_0 = 0.98
                self.sc_60 = 0.77
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 13:
                self.sc_0 = 0.66
                self.sc_60 = 0.77
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 14:
                self.sc_0 = 0.75
                self.sc_60 = 0.66
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 15:
                self.sc_0 = 0.58
                self.sc_60 = 0.57
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 16:
                self.sc_0 = 0.95
                self.sc_60 = 0.95
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 17:
                self.sc_0 = 0.95
                self.sc_60 = 0.41
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 18:
                self.sc_0 = 0.36
                self.sc_60 = 0.41
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 19:
                self.sc_0 = 0.47
                self.sc_60 = 0.38
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 20:
                self.sc_0 = 0.35
                self.sc_60 = 0.37
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 21:
                self.sc_0 = 0.95
                self.sc_60 = 0.99
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 22:
                self.sc_0 = 0.95
                self.sc_60 = 0.43
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 23:
                self.sc_0 = 0.33
                self.sc_60 = 0.43
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 24:
                self.sc_0 = 0.47
                self.sc_60 = 0.34
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 25:
                self.sc_0 = 0.28
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 26:
                self.sc_0 = 0.96
                self.sc_60 = 1.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 27:
                self.sc_0 = 0.96
                self.sc_60 = 0.47
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 28:
                self.sc_0 = 0.34
                self.sc_60 = 0.47
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 29:
                self.sc_0 = 0.49
                self.sc_60 = 0.31
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 30:
                self.sc_0 = 0.24
                self.sc_60 = 0.21
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 31:
                self.sc_0 = 0.93
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 32:
                self.sc_0 = 0.93
                self.sc_60 = 0.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 33:
                self.sc_0 = 0.03
                self.sc_60 = 0.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 34:
                self.sc_0 = 0.19
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 35:
                self.sc_0 = 0.02
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 36:
                self.sc_0 = 0.94
                self.sc_60 = 0.96
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 37:
                self.sc_0 = 0.94
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 38:
                self.sc_0 = 0.07
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 39:
                self.sc_0 = 0.25
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 40:
                self.sc_0 = 0.04
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 41:
                self.sc_0 = 0.95
                self.sc_60 = 1.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 42:
                self.sc_0 = 0.95
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 43:
                self.sc_0 = 0.16
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 44:
                self.sc_0 = 0.33
                self.sc_60 = 0.12
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 45:
                self.sc_0 = 0.08
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 47:
                self.sc_fc = 0.87
            elif self.shaded_types == 48:
                self.sc_fc = 0.78
            elif self.shaded_types == 49:
                self.sc_fc = 0.66
            elif self.shaded_types == 50:
                self.sc_fc = 0.89
            elif self.shaded_types == 51:
                self.sc_fc = 0.81
            elif self.shaded_types == 52:
                self.sc_fc = 0.73
            elif self.shaded_types == 53:
                self.sc_fc = 0.91
            elif self.shaded_types == 54:
                self.sc_fc = 0.84
            elif self.shaded_types == 55:
                self.sc_fc = 0.78
            elif self.shaded_types == 56:
                self.sc_fc = 0.83
            elif self.shaded_types == 57:
                self.sc_fc = 0.64
            elif self.shaded_types == 58:
                self.sc_fc = 0.59
            elif self.shaded_types == 59:
                self.sc_fc = 0.82
            elif self.shaded_types == 60:
                self.sc_fc = 0.79
            elif self.shaded_types == 61:
                self.sc_fc = 0.86
            elif self.shaded_types == 62:
                self.sc_fc = 0.55
            elif self.shaded_types == 63:
                self.sc_fc = 0.5
            elif self.shaded_types == 64:
                self.sc_fc = 0.64
            elif self.shaded_types == 65:
                self.sc_fc = 0.94
            else:
                self.sc_fc = 1
        elif self.glazed_type == 39:
            if self.shaded_types == 1:
                self.sc_0 = 0.99
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60)*(min((1.2 * float(self.shadow_line)), 60))/60)
            elif self.shaded_types == 2:
                self.sc_0 = 0.99
                self.sc_60 = 0.93
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 3:
                self.sc_0 = 0.90
                self.sc_60 = 0.93
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 4:
                self.sc_0 = 0.92
                self.sc_60 = 0.90
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 5:
                self.sc_0 = 0.87
                self.sc_60 = 0.88
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 6:
                self.sc_0 = 0.98
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 7:
                self.sc_0 = 0.98
                self.sc_60 = 0.87
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 8:
                self.sc_0 = 0.81
                self.sc_60 = 0.87
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 9:
                self.sc_0 = 0.86
                self.sc_60 = 0.81
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 10:
                self.sc_0 = 0.76
                self.sc_60 = 0.76
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 11:
                self.sc_0 = 0.98
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 12:
                self.sc_0 = 0.98
                self.sc_60 = 0.81
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 13:
                self.sc_0 = 0.72
                self.sc_60 = 0.81
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 14:
                self.sc_0 = 0.79
                self.sc_60 = 0.72
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 15:
                self.sc_0 = 0.64
                self.sc_60 = 0.64
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 16:
                self.sc_0 = 0.95
                self.sc_60 = 0.95
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 17:
                self.sc_0 = 0.95
                self.sc_60 = 0.44
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 18:
                self.sc_0 = 0.39
                self.sc_60 = 0.44
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 19:
                self.sc_0 = 0.50
                self.sc_60 = 0.41
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 20:
                self.sc_0 = 0.38
                self.sc_60 = 0.40
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 21:
                self.sc_0 = 0.95
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 22:
                self.sc_0 = 0.95
                self.sc_60 = 0.46
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 23:
                self.sc_0 = 0.37
                self.sc_60 = 0.46
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 24:
                self.sc_0 = 0.50
                self.sc_60 = 0.37
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 25:
                self.sc_0 = 0.32
                self.sc_60 = 0.32
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 26:
                self.sc_0 = 0.95
                self.sc_60 = 1.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 27:
                self.sc_0 = 0.95
                self.sc_60 = 0.50
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 28:
                self.sc_0 = 0.37
                self.sc_60 = 0.50
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 29:
                self.sc_0 = 0.52
                self.sc_60 = 0.35
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 30:
                self.sc_0 = 0.28
                self.sc_60 = 0.26
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 31:
                self.sc_0 = 0.93
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 32:
                self.sc_0 = 0.93
                self.sc_60 = 0.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 33:
                self.sc_0 = 0.03
                self.sc_60 = 0.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 34:
                self.sc_0 = 0.20
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 35:
                self.sc_0 = 0.02
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 36:
                self.sc_0 = 0.94
                self.sc_60 = 0.95
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 37:
                self.sc_0 = 0.94
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 38:
                self.sc_0 = 0.08
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 39:
                self.sc_0 = 0.25
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 40:
                self.sc_0 = 0.04
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 41:
                self.sc_0 = 0.95
                self.sc_60 = 1.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 42:
                self.sc_0 = 0.95
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 43:
                self.sc_0 = 0.16
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 44:
                self.sc_0 = 0.33
                self.sc_60 = 0.12
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 45:
                self.sc_0 = 0.08
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 47:
                self.sc_fc = 0.88
            elif self.shaded_types == 48:
                self.sc_fc = 0.70
            elif self.shaded_types == 49:
                self.sc_fc = 0.71
            elif self.shaded_types == 50:
                self.sc_fc = 0.90
            elif self.shaded_types == 51:
                self.sc_fc = 0.83
            elif self.shaded_types == 52:
                self.sc_fc = 0.77
            elif self.shaded_types == 53:
                self.sc_fc = 0.92
            elif self.shaded_types == 54:
                self.sc_fc = 0.86
            elif self.shaded_types == 55:
                self.sc_fc = 0.81
            elif self.shaded_types == 56:
                self.sc_fc = 0.85
            elif self.shaded_types == 57:
                self.sc_fc = 0.7
            elif self.shaded_types == 58:
                self.sc_fc = 0.65
            elif self.shaded_types == 59:
                self.sc_fc = 0.84
            elif self.shaded_types == 60:
                self.sc_fc = 0.82
            elif self.shaded_types == 61:
                self.sc_fc = 0.88
            elif self.shaded_types == 62:
                self.sc_fc = 0.62
            elif self.shaded_types == 63:
                self.sc_fc = 0.58
            elif self.shaded_types == 64:
                self.sc_fc = 0.64
            elif self.shaded_types == 65:
                self.sc_fc = 0.95
            else:
                self.sc_fc = 1
        elif self.glazed_type == 40:
            if self.shaded_types == 1:
                self.sc_0 = 0.99
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60)*(min((1.2 * float(self.shadow_line)), 60))/60)
            elif self.shaded_types == 2:
                self.sc_0 = 0.99
                self.sc_60 = 0.93
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 3:
                self.sc_0 = 0.90
                self.sc_60 = 0.93
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 4:
                self.sc_0 = 0.92
                self.sc_60 = 0.90
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 5:
                self.sc_0 = 0.87
                self.sc_60 = 0.88
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 6:
                self.sc_0 = 0.98
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 7:
                self.sc_0 = 0.98
                self.sc_60 = 0.87
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 8:
                self.sc_0 = 0.80
                self.sc_60 = 0.87
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 9:
                self.sc_0 = 0.86
                self.sc_60 = 0.81
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 10:
                self.sc_0 = 0.75
                self.sc_60 = 0.75
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 11:
                self.sc_0 = 0.98
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 12:
                self.sc_0 = 0.98
                self.sc_60 = 0.81
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 13:
                self.sc_0 = 0.71
                self.sc_60 = 0.81
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 14:
                self.sc_0 = 0.79
                self.sc_60 = 0.71
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 15:
                self.sc_0 = 0.64
                self.sc_60 = 0.64
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 16:
                self.sc_0 = 0.95
                self.sc_60 = 0.95
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 17:
                self.sc_0 = 0.95
                self.sc_60 = 0.44
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 18:
                self.sc_0 = 0.38
                self.sc_60 = 0.44
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 19:
                self.sc_0 = 0.49
                self.sc_60 = 0.41
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 20:
                self.sc_0 = 0.37
                self.sc_60 = 0.40
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 21:
                self.sc_0 = 0.95
                self.sc_60 = 0.99
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 22:
                self.sc_0 = 0.95
                self.sc_60 = 0.45
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 23:
                self.sc_0 = 0.36
                self.sc_60 = 0.45
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 24:
                self.sc_0 = 0.49
                self.sc_60 = 0.37
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 25:
                self.sc_0 = 0.31
                self.sc_60 = 0.31
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 26:
                self.sc_0 = 0.96
                self.sc_60 = 1.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 27:
                self.sc_0 = 0.96
                self.sc_60 = 0.49
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 28:
                self.sc_0 = 0.37
                self.sc_60 = 0.49
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 29:
                self.sc_0 = 0.61
                self.sc_60 = 0.34
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 30:
                self.sc_0 = 0.27
                self.sc_60 = 0.25
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 31:
                self.sc_0 = 0.93
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 32:
                self.sc_0 = 0.93
                self.sc_60 = 0.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 33:
                self.sc_0 = 0.03
                self.sc_60 = 0.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 34:
                self.sc_0 = 0.19
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 35:
                self.sc_0 = 0.02
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 36:
                self.sc_0 = 0.94
                self.sc_60 = 0.96
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 37:
                self.sc_0 = 0.94
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 38:
                self.sc_0 = 0.07
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 39:
                self.sc_0 = 0.25
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 40:
                self.sc_0 = 0.04
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 41:
                self.sc_0 = 0.95
                self.sc_60 = 1.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 42:
                self.sc_0 = 0.95
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 43:
                self.sc_0 = 0.16
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 44:
                self.sc_0 = 0.33
                self.sc_60 = 0.12
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 45:
                self.sc_0 = 0.08
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 47:
                self.sc_fc = 0.88
            elif self.shaded_types == 48:
                self.sc_fc = 0.70
            elif self.shaded_types == 49:
                self.sc_fc = 0.71
            elif self.shaded_types == 50:
                self.sc_fc = 0.90
            elif self.shaded_types == 51:
                self.sc_fc = 0.83
            elif self.shaded_types == 52:
                self.sc_fc = 0.76
            elif self.shaded_types == 53:
                self.sc_fc = 0.92
            elif self.shaded_types == 54:
                self.sc_fc = 0.86
            elif self.shaded_types == 55:
                self.sc_fc = 0.81
            elif self.shaded_types == 56:
                self.sc_fc = 0.85
            elif self.shaded_types == 57:
                self.sc_fc = 0.70
            elif self.shaded_types == 58:
                self.sc_fc = 0.65
            elif self.shaded_types == 59:
                self.sc_fc = 0.84
            elif self.shaded_types == 60:
                self.sc_fc = 0.81
            elif self.shaded_types == 61:
                self.sc_fc = 0.87
            elif self.shaded_types == 62:
                self.sc_fc = 0.61
            elif self.shaded_types == 63:
                self.sc_fc = 0.57
            elif self.shaded_types == 64:
                self.sc_fc = 0.64
            elif self.shaded_types == 65:
                self.sc_fc = 0.95
            else:
                self.sc_fc = 1
        elif self.glazed_type == 42:
            if self.shaded_types == 1:
                self.sc_0 = 0.99
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60)*(min((1.2 * float(self.shadow_line)), 60))/60)
            elif self.shaded_types == 2:
                self.sc_0 = 0.99
                self.sc_60 = 0.92
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 3:
                self.sc_0 = 0.89
                self.sc_60 = 0.92
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 4:
                self.sc_0 = 0.92
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 5:
                self.sc_0 = 0.86
                self.sc_60 = 0.87
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 6:
                self.sc_0 = 0.99
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 7:
                self.sc_0 = 0.99
                self.sc_60 = 0.85
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 8:
                self.sc_0 = 0.77
                self.sc_60 = 0.85
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 9:
                self.sc_0 = 0.83
                self.sc_60 = 0.77
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 10:
                self.sc_0 = 0.71
                self.sc_60 = 0.70
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 11:
                self.sc_0 = 0.98
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 12:
                self.sc_0 = 0.98
                self.sc_60 = 0.76
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 13:
                self.sc_0 = 0.64
                self.sc_60 = 0.76
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 14:
                self.sc_0 = 0.74
                self.sc_60 = 0.64
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 15:
                self.sc_0 = 0.54
                self.sc_60 = 0.53
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 16:
                self.sc_0 = 0.98
                self.sc_60 = 1.01
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 17:
                self.sc_0 = 0.98
                self.sc_60 = 0.69
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 18:
                self.sc_0 = 0.63
                self.sc_60 = 0.69
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 19:
                self.sc_0 = 0.71
                self.sc_60 = 0.66
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 20:
                self.sc_0 = 0.61
                self.sc_60 = 0.64
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 21:
                self.sc_0 = 0.97
                self.sc_60 = 1.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 22:
                self.sc_0 = 0.97
                self.sc_60 = 0.65
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 23:
                self.sc_0 = 0.54
                self.sc_60 = 0.65
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 24:
                self.sc_0 = 0.64
                self.sc_60 = 0.54
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 25:
                self.sc_0 = 0.47
                self.sc_60 = 0.47
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 26:
                self.sc_0 = 0.97
                self.sc_60 = 1.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 27:
                self.sc_0 = 0.97
                self.sc_60 = 0.60
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 28:
                self.sc_0 = 0.45
                self.sc_60 = 0.60
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 29:
                self.sc_0 = 0.59
                self.sc_60 = 0.43
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 30:
                self.sc_0 = 0.33
                self.sc_60 = 0.30
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 31:
                self.sc_0 = 0.93
                self.sc_60 = 0.90
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 32:
                self.sc_0 = 0.93
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 33:
                self.sc_0 = 0.02
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 34:
                self.sc_0 = 0.19
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 35:
                self.sc_0 = 0.02
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 36:
                self.sc_0 = 0.94
                self.sc_60 = 1.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 37:
                self.sc_0 = 0.94
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 38:
                self.sc_0 = 0.07
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 39:
                self.sc_0 = 0.25
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 40:
                self.sc_0 = 0.04
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 41:
                self.sc_0 = 0.95
                self.sc_60 = 1.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 42:
                self.sc_0 = 0.95
                self.sc_60 = 0.29
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 43:
                self.sc_0 = 0.17
                self.sc_60 = 0.29
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 44:
                self.sc_0 = 0.33
                self.sc_60 = 0.13
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 45:
                self.sc_0 = 0.08
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 47:
                self.sc_fc = 0.87
            elif self.shaded_types == 48:
                self.sc_fc = 0.77
            elif self.shaded_types == 49:
                self.sc_fc = 0.64
            elif self.shaded_types == 50:
                self.sc_fc = 0.89
            elif self.shaded_types == 51:
                self.sc_fc = 0.80
            elif self.shaded_types == 52:
                self.sc_fc = 0.71
            elif self.shaded_types == 53:
                self.sc_fc = 0.92
            elif self.shaded_types == 54:
                self.sc_fc = 0.83
            elif self.shaded_types == 55:
                self.sc_fc = 0.76
            elif self.shaded_types == 56:
                self.sc_fc = 0.82
            elif self.shaded_types == 57:
                self.sc_fc = 0.61
            elif self.shaded_types == 58:
                self.sc_fc = 0.55
            elif self.shaded_types == 59:
                self.sc_fc = 0.82
            elif self.shaded_types == 60:
                self.sc_fc = 0.78
            elif self.shaded_types == 61:
                self.sc_fc = 0.86
            elif self.shaded_types == 62:
                self.sc_fc = 0.50
            elif self.shaded_types == 63:
                self.sc_fc = 0.44
            elif self.shaded_types == 64:
                self.sc_fc = 0.64
            elif self.shaded_types == 65:
                self.sc_fc = 0.94
            else:
                self.sc_fc = 1
        elif self.glazed_type == 43:
            if self.shaded_types == 1:
                self.sc_0 = 0.99
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60)*(min((1.2 * float(self.shadow_line)), 60))/60)
            elif self.shaded_types == 2:
                self.sc_0 = 0.99
                self.sc_60 = 0.92
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 3:
                self.sc_0 = 0.89
                self.sc_60 = 0.92
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 4:
                self.sc_0 = 0.92
                self.sc_60 = 0.90
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 5:
                self.sc_0 = 0.87
                self.sc_60 = 0.87
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 6:
                self.sc_0 = 0.99
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 7:
                self.sc_0 = 0.99
                self.sc_60 = 0.86
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 8:
                self.sc_0 = 0.79
                self.sc_60 = 0.86
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 9:
                self.sc_0 = 0.84
                self.sc_60 = 0.79
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 10:
                self.sc_0 = 0.73
                self.sc_60 = 0.73
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 11:
                self.sc_0 = 0.98
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 12:
                self.sc_0 = 0.98
                self.sc_60 = 0.78
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 13:
                self.sc_0 = 0.67
                self.sc_60 = 0.78
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 14:
                self.sc_0 = 0.76
                self.sc_60 = 0.67
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 15:
                self.sc_0 = 0.59
                self.sc_60 = 0.58
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 16:
                self.sc_0 = 0.98
                self.sc_60 = 1.01
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 17:
                self.sc_0 = 0.98
                self.sc_60 = 0.70
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 18:
                self.sc_0 = 0.64
                self.sc_60 = 0.70
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 19:
                self.sc_0 = 0.71
                self.sc_60 = 0.7
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 20:
                self.sc_0 = 0.63
                self.sc_60 = 0.65
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 21:
                self.sc_0 = 0.97
                self.sc_60 = 1.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 22:
                self.sc_0 = 0.97
                self.sc_60 = 0.66
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 23:
                self.sc_0 = 0.55
                self.sc_60 = 0.66
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 24:
                self.sc_0 = 0.65
                self.sc_60 = 0.55
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 25:
                self.sc_0 = 0.48
                self.sc_60 = 0.48
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 26:
                self.sc_0 = 0.97
                self.sc_60 = 1.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 27:
                self.sc_0 = 0.97
                self.sc_60 = 0.60
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 28:
                self.sc_0 = 0.46
                self.sc_60 = 0.60
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 29:
                self.sc_0 = 0.59
                self.sc_60 = 0.44
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 30:
                self.sc_0 = 0.34
                self.sc_60 = 0.31
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 31:
                self.sc_0 = 0.93
                self.sc_60 = 0.90
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 32:
                self.sc_0 = 0.93
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 33:
                self.sc_0 = 0.02
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 34:
                self.sc_0 = 0.19
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 35:
                self.sc_0 = 0.02
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 36:
                self.sc_0 = 0.94
                self.sc_60 = 1.01
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 37:
                self.sc_0 = 0.94
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 38:
                self.sc_0 = 0.07
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 39:
                self.sc_0 = 0.25
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 40:
                self.sc_0 = 0.04
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 41:
                self.sc_0 = 0.95
                self.sc_60 = 1.12
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 42:
                self.sc_0 = 0.95
                self.sc_60 = 0.29
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 43:
                self.sc_0 = 0.17
                self.sc_60 = 0.29
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 44:
                self.sc_0 = 0.33
                self.sc_60 = 0.13
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 45:
                self.sc_0 = 0.08
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 47:
                self.sc_fc = 0.88
            elif self.shaded_types == 48:
                self.sc_fc = 0.79
            elif self.shaded_types == 49:
                self.sc_fc = 0.67
            elif self.shaded_types == 50:
                self.sc_fc = 0.90
            elif self.shaded_types == 51:
                self.sc_fc = 0.82
            elif self.shaded_types == 52:
                self.sc_fc = 0.74
            elif self.shaded_types == 53:
                self.sc_fc = 0.92
            elif self.shaded_types == 54:
                self.sc_fc = 0.85
            elif self.shaded_types == 55:
                self.sc_fc = 0.78
            elif self.shaded_types == 56:
                self.sc_fc = 0.83
            elif self.shaded_types == 57:
                self.sc_fc = 0.65
            elif self.shaded_types == 58:
                self.sc_fc = 0.60
            elif self.shaded_types == 59:
                self.sc_fc = 0.84
            elif self.shaded_types == 60:
                self.sc_fc = 0.80
            elif self.shaded_types == 61:
                self.sc_fc = 0.87
            elif self.shaded_types == 62:
                self.sc_fc = 0.55
            elif self.shaded_types == 63:
                self.sc_fc = 0.50
            elif self.shaded_types == 64:
                self.sc_fc = 0.64
            elif self.shaded_types == 65:
                self.sc_fc = 0.95
            else:
                self.sc_fc = 1
        elif self.glazed_type == 44:
            if self.shaded_types == 1:
                self.sc_0 = 0.99
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60)*(min((1.2 * float(self.shadow_line)), 60))/60)
            elif self.shaded_types == 2:
                self.sc_0 = 0.99
                self.sc_60 = 0.92
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 3:
                self.sc_0 = 0.90
                self.sc_60 = 0.93
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 4:
                self.sc_0 = 0.92
                self.sc_60 = 0.90
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 5:
                self.sc_0 = 0.87
                self.sc_60 = 0.88
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 6:
                self.sc_0 = 0.99
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 7:
                self.sc_0 = 0.99
                self.sc_60 = 0.87
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 8:
                self.sc_0 = 0.79
                self.sc_60 = 0.87
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 9:
                self.sc_0 = 0.85
                self.sc_60 = 0.79
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 10:
                self.sc_0 = 0.74
                self.sc_60 = 0.73
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 11:
                self.sc_0 = 0.98
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 12:
                self.sc_0 = 0.98
                self.sc_60 = 0.79
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 13:
                self.sc_0 = 0.69
                self.sc_60 = 0.79
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 14:
                self.sc_0 = 0.77
                self.sc_60 = 0.68
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 15:
                self.sc_0 = 0.60
                self.sc_60 = 0.59
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 16:
                self.sc_0 = 0.96
                self.sc_60 = 0.99
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 17:
                self.sc_0 = 0.96
                self.sc_60 = 0.4
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 18:
                self.sc_0 = 0.34
                self.sc_60 = 0.4
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 19:
                self.sc_0 = 0.47
                self.sc_60 = 0.36
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 20:
                self.sc_0 = 0.33
                self.sc_60 = 0.35
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 21:
                self.sc_0 = 0.97
                self.sc_60 = 1.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 22:
                self.sc_0 = 0.97
                self.sc_60 = 0.42
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 23:
                self.sc_0 = 0.32
                self.sc_60 = 0.42
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 24:
                self.sc_0 = 0.47
                self.sc_60 = 0.31
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 25:
                self.sc_0 = 0.26
                self.sc_60 = 0.25
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 26:
                self.sc_0 = 0.97
                self.sc_60 = 1.12
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 27:
                self.sc_0 = 0.97
                self.sc_60 = 0.46
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 28:
                self.sc_0 = 0.33
                self.sc_60 = 0.46
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 29:
                self.sc_0 = 0.49
                self.sc_60 = 0.29
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 30:
                self.sc_0 = 0.22
                self.sc_60 = 0.17
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 31:
                self.sc_0 = 0.93
                self.sc_60 = 0.90
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 32:
                self.sc_0 = 0.93
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 33:
                self.sc_0 = 0.02
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 34:
                self.sc_0 = 0.19
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 35:
                self.sc_0 = 0.02
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 36:
                self.sc_0 = 0.94
                self.sc_60 = 1.01
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 37:
                self.sc_0 = 0.94
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 38:
                self.sc_0 = 0.07
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 39:
                self.sc_0 = 0.25
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 40:
                self.sc_0 = 0.04
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 41:
                self.sc_0 = 0.95
                self.sc_60 = 1.13
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 42:
                self.sc_0 = 0.95
                self.sc_60 = 0.29
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 43:
                self.sc_0 = 0.17
                self.sc_60 = 0.29
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 44:
                self.sc_0 = 0.33
                self.sc_60 = 0.13
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 45:
                self.sc_0 = 0.08
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 47:
                self.sc_fc = 0.88
            elif self.shaded_types == 48:
                self.sc_fc = 0.79
            elif self.shaded_types == 49:
                self.sc_fc = 0.68
            elif self.shaded_types == 50:
                self.sc_fc = 0.90
            elif self.shaded_types == 51:
                self.sc_fc = 0.82
            elif self.shaded_types == 52:
                self.sc_fc = 0.74
            elif self.shaded_types == 53:
                self.sc_fc = 0.92
            elif self.shaded_types == 54:
                self.sc_fc = 0.85
            elif self.shaded_types == 55:
                self.sc_fc = 0.79
            elif self.shaded_types == 56:
                self.sc_fc = 0.84
            elif self.shaded_types == 57:
                self.sc_fc = 0.66
            elif self.shaded_types == 58:
                self.sc_fc = 0.61
            elif self.shaded_types == 59:
                self.sc_fc = 0.84
            elif self.shaded_types == 60:
                self.sc_fc = 0.80
            elif self.shaded_types == 61:
                self.sc_fc = 0.87
            elif self.shaded_types == 62:
                self.sc_fc = 0.56
            elif self.shaded_types == 63:
                self.sc_fc = 0.51
            elif self.shaded_types == 64:
                self.sc_fc = 0.64
            elif self.shaded_types == 65:
                self.sc_fc = 0.95
            else:
                self.sc_fc = 1
        elif self.glazed_type == 45:
            if self.shaded_types == 1:
                self.sc_0 = 0.99
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60)*(min((1.2 * float(self.shadow_line)), 60))/60)
            elif self.shaded_types == 2:
                self.sc_0 = 0.99
                self.sc_60 = 0.92
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 3:
                self.sc_0 = 0.90
                self.sc_60 = 0.93
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 4:
                self.sc_0 = 0.93
                self.sc_60 = 0.91
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 5:
                self.sc_0 = 0.88
                self.sc_60 = 0.88
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 6:
                self.sc_0 = 0.99
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 7:
                self.sc_0 = 0.99
                self.sc_60 = 0.87
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 8:
                self.sc_0 = 0.81
                self.sc_60 = 0.87
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 9:
                self.sc_0 = 0.86
                self.sc_60 = 0.81
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 10:
                self.sc_0 = 0.75
                self.sc_60 = 0.75
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 11:
                self.sc_0 = 0.98
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 12:
                self.sc_0 = 0.98
                self.sc_60 = 0.81
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 13:
                self.sc_0 = 0.71
                self.sc_60 = 0.81
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 14:
                self.sc_0 = 0.79
                self.sc_60 = 0.71
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 15:
                self.sc_0 = 0.63
                self.sc_60 = 0.62
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 16:
                self.sc_0 = 0.96
                self.sc_60 = 0.99
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 17:
                self.sc_0 = 0.96
                self.sc_60 = 0.4
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 18:
                self.sc_0 = 0.34
                self.sc_60 = 0.4
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 19:
                self.sc_0 = 0.47
                self.sc_60 = 0.37
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 20:
                self.sc_0 = 0.34
                self.sc_60 = 0.36
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 21:
                self.sc_0 = 0.97
                self.sc_60 = 1.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 22:
                self.sc_0 = 0.97
                self.sc_60 = 0.42
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 23:
                self.sc_0 = 0.32
                self.sc_60 = 0.42
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 24:
                self.sc_0 = 0.47
                self.sc_60 = 0.31
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 25:
                self.sc_0 = 0.27
                self.sc_60 = 0.26
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 26:
                self.sc_0 = 0.97
                self.sc_60 = 1.12
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 27:
                self.sc_0 = 0.97
                self.sc_60 = 0.46
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 28:
                self.sc_0 = 0.33
                self.sc_60 = 0.46
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 29:
                self.sc_0 = 0.50
                self.sc_60 = 0.30
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 30:
                self.sc_0 = 0.23
                self.sc_60 = 0.18
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 31:
                self.sc_0 = 0.93
                self.sc_60 = 0.90
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 32:
                self.sc_0 = 0.93
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 33:
                self.sc_0 = 0.02
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 34:
                self.sc_0 = 0.19
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 35:
                self.sc_0 = 0.02
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 36:
                self.sc_0 = 0.94
                self.sc_60 = 1.01
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 37:
                self.sc_0 = 0.94
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 38:
                self.sc_0 = 0.07
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 39:
                self.sc_0 = 0.25
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 40:
                self.sc_0 = 0.04
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 41:
                self.sc_0 = 0.95
                self.sc_60 = 1.12
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 42:
                self.sc_0 = 0.95
                self.sc_60 = 0.29
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 43:
                self.sc_0 = 0.17
                self.sc_60 = 0.29
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 44:
                self.sc_0 = 0.33
                self.sc_60 = 0.13
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 45:
                self.sc_0 = 0.08
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 47:
                self.sc_fc = 0.88
            elif self.shaded_types == 48:
                self.sc_fc = 0.81
            elif self.shaded_types == 49:
                self.sc_fc = 0.70
            elif self.shaded_types == 50:
                self.sc_fc = 0.90
            elif self.shaded_types == 51:
                self.sc_fc = 0.83
            elif self.shaded_types == 52:
                self.sc_fc = 0.76
            elif self.shaded_types == 53:
                self.sc_fc = 0.92
            elif self.shaded_types == 54:
                self.sc_fc = 0.86
            elif self.shaded_types == 55:
                self.sc_fc = 0.81
            elif self.shaded_types == 56:
                self.sc_fc = 0.85
            elif self.shaded_types == 57:
                self.sc_fc = 0.69
            elif self.shaded_types == 58:
                self.sc_fc = 0.64
            elif self.shaded_types == 59:
                self.sc_fc = 0.85
            elif self.shaded_types == 60:
                self.sc_fc = 0.82
            elif self.shaded_types == 61:
                self.sc_fc = 0.88
            elif self.shaded_types == 62:
                self.sc_fc = 0.60
            elif self.shaded_types == 63:
                self.sc_fc = 0.56
            elif self.shaded_types == 64:
                self.sc_fc = 0.64
            elif self.shaded_types == 65:
                self.sc_fc = 0.95
            else:
                self.sc_fc = 1
        elif self.glazed_type == 46:
            if self.shaded_types == 1:
                self.sc_0 = 0.99
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60)*(min((1.2 * float(self.shadow_line)), 60))/60)
            elif self.shaded_types == 2:
                self.sc_0 = 0.99
                self.sc_60 = 0.92
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 3:
                self.sc_0 = 0.90
                self.sc_60 = 0.93
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 4:
                self.sc_0 = 0.93
                self.sc_60 = 0.91
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 5:
                self.sc_0 = 0.88
                self.sc_60 = 0.88
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 6:
                self.sc_0 = 0.99
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 7:
                self.sc_0 = 0.99
                self.sc_60 = 0.87
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 8:
                self.sc_0 = 0.80
                self.sc_60 = 0.87
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 9:
                self.sc_0 = 0.86
                self.sc_60 = 0.81
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 10:
                self.sc_0 = 0.75
                self.sc_60 = 0.75
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 11:
                self.sc_0 = 0.98
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 12:
                self.sc_0 = 0.98
                self.sc_60 = 0.80
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 13:
                self.sc_0 = 0.70
                self.sc_60 = 0.80
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 14:
                self.sc_0 = 0.78
                self.sc_60 = 0.70
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 15:
                self.sc_0 = 0.62
                self.sc_60 = 0.61
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 16:
                self.sc_0 = 0.96
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 17:
                self.sc_0 = 0.96
                self.sc_60 = 0.42
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 18:
                self.sc_0 = 0.36
                self.sc_60 = 0.42
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 19:
                self.sc_0 = 0.48
                self.sc_60 = 0.38
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 20:
                self.sc_0 = 0.35
                self.sc_60 = 0.37
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 21:
                self.sc_0 = 0.96
                self.sc_60 = 1.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 22:
                self.sc_0 = 0.96
                self.sc_60 = 0.44
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 23:
                self.sc_0 = 0.34
                self.sc_60 = 0.44
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 24:
                self.sc_0 = 0.48
                self.sc_60 = 0.34
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 25:
                self.sc_0 = 0.28
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 26:
                self.sc_0 = 0.96
                self.sc_60 = 1.11
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 27:
                self.sc_0 = 0.96
                self.sc_60 = 0.47
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 28:
                self.sc_0 = 0.35
                self.sc_60 = 0.47
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 29:
                self.sc_0 = 0.51
                self.sc_60 = 0.31
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 30:
                self.sc_0 = 0.25
                self.sc_60 = 0.21
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 31:
                self.sc_0 = 0.93
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 32:
                self.sc_0 = 0.93
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 33:
                self.sc_0 = 0.02
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 34:
                self.sc_0 = 0.19
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 35:
                self.sc_0 = 0.02
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 36:
                self.sc_0 = 0.94
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 37:
                self.sc_0 = 0.94
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 38:
                self.sc_0 = 0.07
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 39:
                self.sc_0 = 0.25
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 40:
                self.sc_0 = 0.04
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 41:
                self.sc_0 = 0.95
                self.sc_60 = 1.07
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 42:
                self.sc_0 = 0.95
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 43:
                self.sc_0 = 0.16
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 44:
                self.sc_0 = 0.34
                self.sc_60 = 0.12
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 45:
                self.sc_0 = 0.08
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 47:
                self.sc_fc = 0.88
            elif self.shaded_types == 48:
                self.sc_fc = 0.80
            elif self.shaded_types == 49:
                self.sc_fc = 0.69
            elif self.shaded_types == 50:
                self.sc_fc = 0.90
            elif self.shaded_types == 51:
                self.sc_fc = 0.83
            elif self.shaded_types == 52:
                self.sc_fc = 0.75
            elif self.shaded_types == 53:
                self.sc_fc = 0.92
            elif self.shaded_types == 54:
                self.sc_fc = 0.86
            elif self.shaded_types == 55:
                self.sc_fc = 0.80
            elif self.shaded_types == 56:
                self.sc_fc = 0.85
            elif self.shaded_types == 57:
                self.sc_fc = 0.68
            elif self.shaded_types == 58:
                self.sc_fc = 0.63
            elif self.shaded_types == 59:
                self.sc_fc = 0.85
            elif self.shaded_types == 60:
                self.sc_fc = 0.81
            elif self.shaded_types == 61:
                self.sc_fc = 0.88
            elif self.shaded_types == 62:
                self.sc_fc = 0.58
            elif self.shaded_types == 63:
                self.sc_fc = 0.54
            elif self.shaded_types == 64:
                self.sc_fc = 0.64
            elif self.shaded_types == 65:
                self.sc_fc = 0.95
            else:
                self.sc_fc = 1
        elif self.glazed_type == 47:
            if self.shaded_types == 1:
                self.sc_0 = 0.99
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60)*(min((1.2 * float(self.shadow_line)), 60))/60)
            elif self.shaded_types == 2:
                self.sc_0 = 0.99
                self.sc_60 = 0.92
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 3:
                self.sc_0 = 0.90
                self.sc_60 = 0.93
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 4:
                self.sc_0 = 0.93
                self.sc_60 = 0.91
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 5:
                self.sc_0 = 0.89
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 6:
                self.sc_0 = 0.99
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 7:
                self.sc_0 = 0.99
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 8:
                self.sc_0 = 0.82
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 9:
                self.sc_0 = 0.87
                self.sc_60 = 0.82
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 10:
                self.sc_0 = 0.77
                self.sc_60 = 0.77
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 11:
                self.sc_0 = 0.98
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 12:
                self.sc_0 = 0.98
                self.sc_60 = 0.83
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 13:
                self.sc_0 = 0.73
                self.sc_60 = 0.83
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 14:
                self.sc_0 = 0.80
                self.sc_60 = 0.74
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 15:
                self.sc_0 = 0.66
                self.sc_60 = 0.66
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 16:
                self.sc_0 = 0.95
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 17:
                self.sc_0 = 0.95
                self.sc_60 = 0.44
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 18:
                self.sc_0 = 0.39
                self.sc_60 = 0.44
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 19:
                self.sc_0 = 0.50
                self.sc_60 = 0.41
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 20:
                self.sc_0 = 0.38
                self.sc_60 = 0.40
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 21:
                self.sc_0 = 0.95
                self.sc_60 = 1.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 22:
                self.sc_0 = 0.95
                self.sc_60 = 0.46
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 23:
                self.sc_0 = 0.37
                self.sc_60 = 0.46
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 24:
                self.sc_0 = 0.50
                self.sc_60 = 0.37
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 25:
                self.sc_0 = 0.32
                self.sc_60 = 0.32
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 26:
                self.sc_0 = 0.96
                self.sc_60 = 1.09
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 27:
                self.sc_0 = 0.96
                self.sc_60 = 0.50
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 28:
                self.sc_0 = 0.38
                self.sc_60 = 0.50
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 29:
                self.sc_0 = 0.53
                self.sc_60 = 0.35
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 30:
                self.sc_0 = 0.28
                self.sc_60 = 0.25
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 31:
                self.sc_0 = 0.93
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 32:
                self.sc_0 = 0.93
                self.sc_60 = 0.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 33:
                self.sc_0 = 0.03
                self.sc_60 = 0.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 34:
                self.sc_0 = 0.2
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 35:
                self.sc_0 = 0.02
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 36:
                self.sc_0 = 0.94
                self.sc_60 = 0.96
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 37:
                self.sc_0 = 0.94
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 38:
                self.sc_0 = 0.08
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 39:
                self.sc_0 = 0.25
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 40:
                self.sc_0 = 0.04
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 41:
                self.sc_0 = 0.95
                self.sc_60 = 1.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 42:
                self.sc_0 = 0.95
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 43:
                self.sc_0 = 0.16
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 44:
                self.sc_0 = 0.34
                self.sc_60 = 0.12
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 45:
                self.sc_0 = 0.08
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 47:
                self.sc_fc = 0.89
            elif self.shaded_types == 48:
                self.sc_fc = 0.82
            elif self.shaded_types == 49:
                self.sc_fc = 0.73
            elif self.shaded_types == 50:
                self.sc_fc = 0.91
            elif self.shaded_types == 51:
                self.sc_fc = 0.85
            elif self.shaded_types == 52:
                self.sc_fc = 0.78
            elif self.shaded_types == 53:
                self.sc_fc = 0.93
            elif self.shaded_types == 54:
                self.sc_fc = 0.87
            elif self.shaded_types == 55:
                self.sc_fc = 0.82
            elif self.shaded_types == 56:
                self.sc_fc = 0.86
            elif self.shaded_types == 57:
                self.sc_fc = 0.72
            elif self.shaded_types == 58:
                self.sc_fc = 0.67
            elif self.shaded_types == 59:
                self.sc_fc = 0.86
            elif self.shaded_types == 60:
                self.sc_fc = 0.83
            elif self.shaded_types == 61:
                self.sc_fc = 0.89
            elif self.shaded_types == 62:
                self.sc_fc = 0.63
            elif self.shaded_types == 63:
                self.sc_fc = 0.60
            elif self.shaded_types == 64:
                self.sc_fc = 0.64
            elif self.shaded_types == 65:
                self.sc_fc = 0.95
            else:
                self.sc_fc = 1
        elif self.glazed_type == 48:
            if self.shaded_types == 1:
                self.sc_0 = 0.99
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60)*(min((1.2 * float(self.shadow_line)), 60))/60)
            elif self.shaded_types == 2:
                self.sc_0 = 0.99
                self.sc_60 = 0.92
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 3:
                self.sc_0 = 0.90
                self.sc_60 = 0.94
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 4:
                self.sc_0 = 0.93
                self.sc_60 = 0.91
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 5:
                self.sc_0 = 0.88
                self.sc_60 = 0.88
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 6:
                self.sc_0 = 0.99
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 7:
                self.sc_0 = 0.99
                self.sc_60 = 0.87
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 8:
                self.sc_0 = 0.80
                self.sc_60 = 0.87
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 9:
                self.sc_0 = 0.86
                self.sc_60 = 0.81
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 10:
                self.sc_0 = 0.75
                self.sc_60 = 0.75
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 11:
                self.sc_0 = 0.98
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 12:
                self.sc_0 = 0.98
                self.sc_60 = 0.81
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 13:
                self.sc_0 = 0.70
                self.sc_60 = 0.81
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 14:
                self.sc_0 = 0.78
                self.sc_60 = 0.70
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 15:
                self.sc_0 = 0.62
                self.sc_60 = 0.62
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 16:
                self.sc_0 = 0.96
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 17:
                self.sc_0 = 0.95
                self.sc_60 = 0.42
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 18:
                self.sc_0 = 0.37
                self.sc_60 = 0.42
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 19:
                self.sc_0 = 0.49
                self.sc_60 = 0.39
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 20:
                self.sc_0 = 0.35
                self.sc_60 = 0.37
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 21:
                self.sc_0 = 0.96
                self.sc_60 = 1.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 22:
                self.sc_0 = 0.96
                self.sc_60 = 0.44
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 23:
                self.sc_0 = 0.34
                self.sc_60 = 0.44
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 24:
                self.sc_0 = 0.49
                self.sc_60 = 0.34
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 25:
                self.sc_0 = 0.29
                self.sc_60 = 0.29
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 26:
                self.sc_0 = 0.96
                self.sc_60 = 1.11
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 27:
                self.sc_0 = 0.96
                self.sc_60 = 0.48
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 28:
                self.sc_0 = 0.35
                self.sc_60 = 0.48
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 29:
                self.sc_0 = 0.51
                self.sc_60 = 0.32
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 30:
                self.sc_0 = 0.25
                self.sc_60 = 0.22
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 31:
                self.sc_0 = 0.93
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 32:
                self.sc_0 = 0.93
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 33:
                self.sc_0 = 0.02
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 34:
                self.sc_0 = 0.19
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 35:
                self.sc_0 = 0.02
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 36:
                self.sc_0 = 0.94
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 37:
                self.sc_0 = 0.94
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 38:
                self.sc_0 = 0.07
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 39:
                self.sc_0 = 0.25
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 40:
                self.sc_0 = 0.04
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 41:
                self.sc_0 = 0.95
                self.sc_60 = 1.07
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 42:
                self.sc_0 = 0.95
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 43:
                self.sc_0 = 0.16
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 44:
                self.sc_0 = 0.34
                self.sc_60 = 0.12
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 45:
                self.sc_0 = 0.08
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 47:
                self.sc_fc = 0.88
            elif self.shaded_types == 48:
                self.sc_fc = 0.80
            elif self.shaded_types == 49:
                self.sc_fc = 0.69
            elif self.shaded_types == 50:
                self.sc_fc = 0.90
            elif self.shaded_types == 51:
                self.sc_fc = 0.83
            elif self.shaded_types == 52:
                self.sc_fc = 0.75
            elif self.shaded_types == 53:
                self.sc_fc = 0.92
            elif self.shaded_types == 54:
                self.sc_fc = 0.86
            elif self.shaded_types == 55:
                self.sc_fc = 0.80
            elif self.shaded_types == 56:
                self.sc_fc = 0.85
            elif self.shaded_types == 57:
                self.sc_fc = 0.68
            elif self.shaded_types == 58:
                self.sc_fc = 0.63
            elif self.shaded_types == 59:
                self.sc_fc = 0.85
            elif self.shaded_types == 60:
                self.sc_fc = 0.81
            elif self.shaded_types == 61:
                self.sc_fc = 0.88
            elif self.shaded_types == 62:
                self.sc_fc = 0.59
            elif self.shaded_types == 63:
                self.sc_fc = 0.54
            elif self.shaded_types == 64:
                self.sc_fc = 0.64
            elif self.shaded_types == 65:
                self.sc_fc = 0.95
            else:
                self.sc_fc = 1
        elif self.glazed_type == 49:
            if self.shaded_types == 1:
                self.sc_0 = 0.99
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60)*(min((1.2 * float(self.shadow_line)), 60))/60)
            elif self.shaded_types == 2:
                self.sc_0 = 0.99
                self.sc_60 = 0.94
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 3:
                self.sc_0 = 0.91
                self.sc_60 = 0.94
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 4:
                self.sc_0 = 0.93
                self.sc_60 = 0.91
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 5:
                self.sc_0 = 0.89
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 6:
                self.sc_0 = 0.99
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 7:
                self.sc_0 = 0.99
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 8:
                self.sc_0 = 0.82
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 9:
                self.sc_0 = 0.87
                self.sc_60 = 0.83
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 10:
                self.sc_0 = 0.78
                self.sc_60 = 0.78
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 11:
                self.sc_0 = 0.98
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 12:
                self.sc_0 = 0.98
                self.sc_60 = 0.83
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 13:
                self.sc_0 = 0.74
                self.sc_60 = 0.83
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 14:
                self.sc_0 = 0.81
                self.sc_60 = 0.74
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 15:
                self.sc_0 = 0.67
                self.sc_60 = 0.66
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 16:
                self.sc_0 = 0.95
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 17:
                self.sc_0 = 0.95
                self.sc_60 = 0.45
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 18:
                self.sc_0 = 0.39
                self.sc_60 = 0.44
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 19:
                self.sc_0 = 0.51
                self.sc_60 = 0.42
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 20:
                self.sc_0 = 0.38
                self.sc_60 = 0.40
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 21:
                self.sc_0 = 0.95
                self.sc_60 = 1.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 22:
                self.sc_0 = 0.95
                self.sc_60 = 0.46
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 23:
                self.sc_0 = 0.37
                self.sc_60 = 0.46
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 24:
                self.sc_0 = 0.51
                self.sc_60 = 0.37
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 25:
                self.sc_0 = 0.32
                self.sc_60 = 0.32
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 26:
                self.sc_0 = 0.96
                self.sc_60 = 1.09
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 27:
                self.sc_0 = 0.96
                self.sc_60 = 0.50
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 28:
                self.sc_0 = 0.38
                self.sc_60 = 0.50
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 29:
                self.sc_0 = 0.53
                self.sc_60 = 0.35
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 30:
                self.sc_0 = 0.29
                self.sc_60 = 0.26
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 31:
                self.sc_0 = 0.93
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 32:
                self.sc_0 = 0.93
                self.sc_60 = 0.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 33:
                self.sc_0 = 0.03
                self.sc_60 = 0.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 34:
                self.sc_0 = 0.2
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 35:
                self.sc_0 = 0.02
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 36:
                self.sc_0 = 0.94
                self.sc_60 = 0.96
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 37:
                self.sc_0 = 0.94
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 38:
                self.sc_0 = 0.08
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 39:
                self.sc_0 = 0.25
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 40:
                self.sc_0 = 0.04
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 41:
                self.sc_0 = 0.95
                self.sc_60 = 1.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 42:
                self.sc_0 = 0.95
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 43:
                self.sc_0 = 0.16
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 44:
                self.sc_0 = 0.34
                self.sc_60 = 0.12
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 45:
                self.sc_0 = 0.08
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 47:
                self.sc_fc = 0.89
            elif self.shaded_types == 48:
                self.sc_fc = 0.82
            elif self.shaded_types == 49:
                self.sc_fc = 0.73
            elif self.shaded_types == 50:
                self.sc_fc = 0.91
            elif self.shaded_types == 51:
                self.sc_fc = 0.85
            elif self.shaded_types == 52:
                self.sc_fc = 0.78
            elif self.shaded_types == 53:
                self.sc_fc = 0.93
            elif self.shaded_types == 54:
                self.sc_fc = 0.87
            elif self.shaded_types == 55:
                self.sc_fc = 0.82
            elif self.shaded_types == 56:
                self.sc_fc = 0.86
            elif self.shaded_types == 57:
                self.sc_fc = 0.72
            elif self.shaded_types == 58:
                self.sc_fc = 0.67
            elif self.shaded_types == 59:
                self.sc_fc = 0.86
            elif self.shaded_types == 60:
                self.sc_fc = 0.83
            elif self.shaded_types == 61:
                self.sc_fc = 0.89
            elif self.shaded_types == 62:
                self.sc_fc = 0.64
            elif self.shaded_types == 63:
                self.sc_fc = 0.60
            elif self.shaded_types == 64:
                self.sc_fc = 0.64
            elif self.shaded_types == 65:
                self.sc_fc = 0.95
            else:
                self.sc_fc = 1
        elif self.glazed_type == 50:
            if self.shaded_types == 1:
                self.sc_0 = 0.99
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60)*(min((1.2 * float(self.shadow_line)), 60))/60)
            elif self.shaded_types == 2:
                self.sc_0 = 0.99
                self.sc_60 = 0.92
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 3:
                self.sc_0 = 0.90
                self.sc_60 = 0.94
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 4:
                self.sc_0 = 0.93
                self.sc_60 = 0.91
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 5:
                self.sc_0 = 0.88
                self.sc_60 = 0.88
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 6:
                self.sc_0 = 0.99
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 7:
                self.sc_0 = 0.99
                self.sc_60 = 0.87
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 8:
                self.sc_0 = 0.80
                self.sc_60 = 0.87
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 9:
                self.sc_0 = 0.86
                self.sc_60 = 0.81
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 10:
                self.sc_0 = 0.75
                self.sc_60 = 0.75
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 11:
                self.sc_0 = 0.98
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 12:
                self.sc_0 = 0.98
                self.sc_60 = 0.81
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 13:
                self.sc_0 = 0.70
                self.sc_60 = 0.81
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 14:
                self.sc_0 = 0.78
                self.sc_60 = 0.70
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 15:
                self.sc_0 = 0.62
                self.sc_60 = 0.62
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 16:
                self.sc_0 = 0.96
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 17:
                self.sc_0 = 0.95
                self.sc_60 = 0.42
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 18:
                self.sc_0 = 0.37
                self.sc_60 = 0.42
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 19:
                self.sc_0 = 0.49
                self.sc_60 = 0.39
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 20:
                self.sc_0 = 0.35
                self.sc_60 = 0.37
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 21:
                self.sc_0 = 0.96
                self.sc_60 = 1.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 22:
                self.sc_0 = 0.96
                self.sc_60 = 0.44
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 23:
                self.sc_0 = 0.34
                self.sc_60 = 0.44
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 24:
                self.sc_0 = 0.49
                self.sc_60 = 0.34
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 25:
                self.sc_0 = 0.29
                self.sc_60 = 0.29
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 26:
                self.sc_0 = 0.96
                self.sc_60 = 1.11
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 27:
                self.sc_0 = 0.96
                self.sc_60 = 0.48
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 28:
                self.sc_0 = 0.35
                self.sc_60 = 0.48
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 29:
                self.sc_0 = 0.51
                self.sc_60 = 0.32
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 30:
                self.sc_0 = 0.25
                self.sc_60 = 0.22
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 31:
                self.sc_0 = 0.93
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 32:
                self.sc_0 = 0.93
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 33:
                self.sc_0 = 0.02
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 34:
                self.sc_0 = 0.19
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 35:
                self.sc_0 = 0.02
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 36:
                self.sc_0 = 0.94
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 37:
                self.sc_0 = 0.94
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 38:
                self.sc_0 = 0.07
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 39:
                self.sc_0 = 0.25
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 40:
                self.sc_0 = 0.04
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 41:
                self.sc_0 = 0.95
                self.sc_60 = 1.07
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 42:
                self.sc_0 = 0.95
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 43:
                self.sc_0 = 0.16
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 44:
                self.sc_0 = 0.34
                self.sc_60 = 0.12
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 45:
                self.sc_0 = 0.08
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 47:
                self.sc_fc = 0.88
            elif self.shaded_types == 48:
                self.sc_fc = 0.80
            elif self.shaded_types == 49:
                self.sc_fc = 0.69
            elif self.shaded_types == 50:
                self.sc_fc = 0.90
            elif self.shaded_types == 51:
                self.sc_fc = 0.83
            elif self.shaded_types == 52:
                self.sc_fc = 0.75
            elif self.shaded_types == 53:
                self.sc_fc = 0.92
            elif self.shaded_types == 54:
                self.sc_fc = 0.86
            elif self.shaded_types == 55:
                self.sc_fc = 0.80
            elif self.shaded_types == 56:
                self.sc_fc = 0.85
            elif self.shaded_types == 57:
                self.sc_fc = 0.68
            elif self.shaded_types == 58:
                self.sc_fc = 0.63
            elif self.shaded_types == 59:
                self.sc_fc = 0.85
            elif self.shaded_types == 60:
                self.sc_fc = 0.81
            elif self.shaded_types == 61:
                self.sc_fc = 0.88
            elif self.shaded_types == 62:
                self.sc_fc = 0.59
            elif self.shaded_types == 63:
                self.sc_fc = 0.54
            elif self.shaded_types == 64:
                self.sc_fc = 0.64
            elif self.shaded_types == 65:
                self.sc_fc = 0.95
            else:
                self.sc_fc = 1
        elif self.glazed_type == 51:
            if self.shaded_types == 1:
                self.sc_0 = 0.99
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60)*(min((1.2 * float(self.shadow_line)), 60))/60)
            elif self.shaded_types == 2:
                self.sc_0 = 0.99
                self.sc_60 = 0.94
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 3:
                self.sc_0 = 0.91
                self.sc_60 = 0.94
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 4:
                self.sc_0 = 0.93
                self.sc_60 = 0.91
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 5:
                self.sc_0 = 0.89
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 6:
                self.sc_0 = 0.99
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 7:
                self.sc_0 = 0.99
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 8:
                self.sc_0 = 0.82
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 9:
                self.sc_0 = 0.87
                self.sc_60 = 0.83
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 10:
                self.sc_0 = 0.78
                self.sc_60 = 0.78
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 11:
                self.sc_0 = 0.98
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 12:
                self.sc_0 = 0.98
                self.sc_60 = 0.83
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 13:
                self.sc_0 = 0.74
                self.sc_60 = 0.83
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 14:
                self.sc_0 = 0.81
                self.sc_60 = 0.74
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 15:
                self.sc_0 = 0.67
                self.sc_60 = 0.66
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 16:
                self.sc_0 = 0.95
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 17:
                self.sc_0 = 0.95
                self.sc_60 = 0.45
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 18:
                self.sc_0 = 0.39
                self.sc_60 = 0.44
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 19:
                self.sc_0 = 0.51
                self.sc_60 = 0.42
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 20:
                self.sc_0 = 0.38
                self.sc_60 = 0.40
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 21:
                self.sc_0 = 0.95
                self.sc_60 = 1.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 22:
                self.sc_0 = 0.95
                self.sc_60 = 0.47
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 23:
                self.sc_0 = 0.38
                self.sc_60 = 0.47
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 24:
                self.sc_0 = 0.51
                self.sc_60 = 0.37
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 25:
                self.sc_0 = 0.33
                self.sc_60 = 0.32
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 26:
                self.sc_0 = 0.95
                self.sc_60 = 1.09
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 27:
                self.sc_0 = 0.95
                self.sc_60 = 0.50
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 28:
                self.sc_0 = 0.39
                self.sc_60 = 0.50
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 29:
                self.sc_0 = 0.53
                self.sc_60 = 0.36
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 30:
                self.sc_0 = 0.29
                self.sc_60 = 0.26
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 31:
                self.sc_0 = 0.93
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 32:
                self.sc_0 = 0.93
                self.sc_60 = 0.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 33:
                self.sc_0 = 0.03
                self.sc_60 = 0.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 34:
                self.sc_0 = 0.2
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 35:
                self.sc_0 = 0.02
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 36:
                self.sc_0 = 0.94
                self.sc_60 = 0.96
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 37:
                self.sc_0 = 0.94
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 38:
                self.sc_0 = 0.08
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 39:
                self.sc_0 = 0.25
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 40:
                self.sc_0 = 0.04
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 41:
                self.sc_0 = 0.95
                self.sc_60 = 1.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 42:
                self.sc_0 = 0.95
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 43:
                self.sc_0 = 0.16
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 44:
                self.sc_0 = 0.34
                self.sc_60 = 0.12
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 45:
                self.sc_0 = 0.08
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 47:
                self.sc_fc = 0.89
            elif self.shaded_types == 48:
                self.sc_fc = 0.82
            elif self.shaded_types == 49:
                self.sc_fc = 0.73
            elif self.shaded_types == 50:
                self.sc_fc = 0.91
            elif self.shaded_types == 51:
                self.sc_fc = 0.85
            elif self.shaded_types == 52:
                self.sc_fc = 0.78
            elif self.shaded_types == 53:
                self.sc_fc = 0.93
            elif self.shaded_types == 54:
                self.sc_fc = 0.87
            elif self.shaded_types == 55:
                self.sc_fc = 0.82
            elif self.shaded_types == 56:
                self.sc_fc = 0.86
            elif self.shaded_types == 57:
                self.sc_fc = 0.72
            elif self.shaded_types == 58:
                self.sc_fc = 0.68
            elif self.shaded_types == 59:
                self.sc_fc = 0.86
            elif self.shaded_types == 60:
                self.sc_fc = 0.83
            elif self.shaded_types == 61:
                self.sc_fc = 0.89
            elif self.shaded_types == 62:
                self.sc_fc = 0.64
            elif self.shaded_types == 63:
                self.sc_fc = 0.60
            elif self.shaded_types == 64:
                self.sc_fc = 0.64
            elif self.shaded_types == 65:
                self.sc_fc = 0.95
            else:
                self.sc_fc = 1
        elif self.glazed_type == 52:
            if self.shaded_types == 1:
                self.sc_0 = 0.99
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60)*(min((1.2 * float(self.shadow_line)), 60))/60)
            elif self.shaded_types == 2:
                self.sc_0 = 0.99
                self.sc_60 = 0.93
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 3:
                self.sc_0 = 0.91
                self.sc_60 = 0.93
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 4:
                self.sc_0 = 0.93
                self.sc_60 = 0.91
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 5:
                self.sc_0 = 0.89
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 6:
                self.sc_0 = 0.99
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 7:
                self.sc_0 = 0.99
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 8:
                self.sc_0 = 0.82
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 9:
                self.sc_0 = 0.87
                self.sc_60 = 0.83
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 10:
                self.sc_0 = 0.77
                self.sc_60 = 0.77
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 11:
                self.sc_0 = 0.98
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 12:
                self.sc_0 = 0.98
                self.sc_60 = 0.83
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 13:
                self.sc_0 = 0.73
                self.sc_60 = 0.83
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 14:
                self.sc_0 = 0.81
                self.sc_60 = 0.74
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 15:
                self.sc_0 = 0.66
                self.sc_60 = 0.66
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 16:
                self.sc_0 = 0.95
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 17:
                self.sc_0 = 0.95
                self.sc_60 = 0.44
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 18:
                self.sc_0 = 0.39
                self.sc_60 = 0.44
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 19:
                self.sc_0 = 0.50
                self.sc_60 = 0.41
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 20:
                self.sc_0 = 0.38
                self.sc_60 = 0.40
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 21:
                self.sc_0 = 0.95
                self.sc_60 = 1.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 22:
                self.sc_0 = 0.95
                self.sc_60 = 0.46
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 23:
                self.sc_0 = 0.37
                self.sc_60 = 0.46
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 24:
                self.sc_0 = 0.50
                self.sc_60 = 0.37
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 25:
                self.sc_0 = 0.32
                self.sc_60 = 0.32
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 26:
                self.sc_0 = 0.96
                self.sc_60 = 1.09
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 27:
                self.sc_0 = 0.96
                self.sc_60 = 0.50
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 28:
                self.sc_0 = 0.38
                self.sc_60 = 0.50
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 29:
                self.sc_0 = 0.53
                self.sc_60 = 0.35
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 30:
                self.sc_0 = 0.28
                self.sc_60 = 0.25
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 31:
                self.sc_0 = 0.93
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 32:
                self.sc_0 = 0.93
                self.sc_60 = 0.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 33:
                self.sc_0 = 0.03
                self.sc_60 = 0.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 34:
                self.sc_0 = 0.2
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 35:
                self.sc_0 = 0.02
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 36:
                self.sc_0 = 0.94
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 37:
                self.sc_0 = 0.94
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 38:
                self.sc_0 = 0.08
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 39:
                self.sc_0 = 0.25
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 40:
                self.sc_0 = 0.04
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 41:
                self.sc_0 = 0.95
                self.sc_60 = 1.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 42:
                self.sc_0 = 0.95
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 43:
                self.sc_0 = 0.16
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 44:
                self.sc_0 = 0.34
                self.sc_60 = 0.12
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 45:
                self.sc_0 = 0.08
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 47:
                self.sc_fc = 0.89
            elif self.shaded_types == 48:
                self.sc_fc = 0.82
            elif self.shaded_types == 49:
                self.sc_fc = 0.73
            elif self.shaded_types == 50:
                self.sc_fc = 0.91
            elif self.shaded_types == 51:
                self.sc_fc = 0.85
            elif self.shaded_types == 52:
                self.sc_fc = 0.78
            elif self.shaded_types == 53:
                self.sc_fc = 0.93
            elif self.shaded_types == 54:
                self.sc_fc = 0.87
            elif self.shaded_types == 55:
                self.sc_fc = 0.82
            elif self.shaded_types == 56:
                self.sc_fc = 0.86
            elif self.shaded_types == 57:
                self.sc_fc = 0.72
            elif self.shaded_types == 58:
                self.sc_fc = 0.67
            elif self.shaded_types == 59:
                self.sc_fc = 0.86
            elif self.shaded_types == 60:
                self.sc_fc = 0.83
            elif self.shaded_types == 61:
                self.sc_fc = 0.89
            elif self.shaded_types == 62:
                self.sc_fc = 0.64
            elif self.shaded_types == 63:
                self.sc_fc = 0.60
            elif self.shaded_types == 64:
                self.sc_fc = 0.64
            elif self.shaded_types == 65:
                self.sc_fc = 0.95
            else:
                self.sc_fc = 1
        elif self.glazed_type == 54:
            if self.shaded_types == 1:
                self.sc_0 = 0.99
                self.sc_60 = 0.99
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60)*(min((1.2 * float(self.shadow_line)), 60))/60)
            elif self.shaded_types == 2:
                self.sc_0 = 0.99
                self.sc_60 = 0.93
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 3:
                self.sc_0 = 0.90
                self.sc_60 = 0.93
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 4:
                self.sc_0 = 0.93
                self.sc_60 = 0.91
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 5:
                self.sc_0 = 0.88
                self.sc_60 = 0.88
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 6:
                self.sc_0 = 0.99
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 7:
                self.sc_0 = 0.99
                self.sc_60 = 0.87
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 8:
                self.sc_0 = 0.80
                self.sc_60 = 0.87
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 9:
                self.sc_0 = 0.85
                self.sc_60 = 0.80
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 10:
                self.sc_0 = 0.74
                self.sc_60 = 0.74
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 11:
                self.sc_0 = 0.98
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 12:
                self.sc_0 = 0.98
                self.sc_60 = 0.80
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 13:
                self.sc_0 = 0.69
                self.sc_60 = 0.80
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 14:
                self.sc_0 = 0.78
                self.sc_60 = 0.69
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 15:
                self.sc_0 = 0.60
                self.sc_60 = 0.59
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 16:
                self.sc_0 = 0.97
                self.sc_60 = 1
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 17:
                self.sc_0 = 0.97
                self.sc_60 = 0.71
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 18:
                self.sc_0 = 0.66
                self.sc_60 = 0.71
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 19:
                self.sc_0 = 0.73
                self.sc_60 = 0.69
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 20:
                self.sc_0 = 0.65
                self.sc_60 = 0.67
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 21:
                self.sc_0 = 0.97
                self.sc_60 = 1.01
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 22:
                self.sc_0 = 0.97
                self.sc_60 = 0.68
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 23:
                self.sc_0 = 0.58
                self.sc_60 = 0.68
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 24:
                self.sc_0 = 0.68
                self.sc_60 = 0.59
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 25:
                self.sc_0 = 0.52
                self.sc_60 = 0.52
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 26:
                self.sc_0 = 0.97
                self.sc_60 = 1.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 27:
                self.sc_0 = 0.97
                self.sc_60 = 0.65
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 28:
                self.sc_0 = 0.51
                self.sc_60 = 0.65
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 29:
                self.sc_0 = 0.64
                self.sc_60 = 0.50
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 30:
                self.sc_0 = 0.39
                self.sc_60 = 0.36
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 31:
                self.sc_0 = 0.93
                self.sc_60 = 0.92
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 32:
                self.sc_0 = 0.93
                self.sc_60 = 0.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 33:
                self.sc_0 = 0.03
                self.sc_60 = 0.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 34:
                self.sc_0 = 0.2
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 35:
                self.sc_0 = 0.02
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 36:
                self.sc_0 = 0.94
                self.sc_60 = 1.08
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 37:
                self.sc_0 = 0.94
                self.sc_60 = 0.15
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 38:
                self.sc_0 = 0.08
                self.sc_60 = 0.15
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 39:
                self.sc_0 = 0.26
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 40:
                self.sc_0 = 0.04
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 41:
                self.sc_0 = 0.95
                self.sc_60 = 1.25
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 42:
                self.sc_0 = 0.95
                self.sc_60 = 0.3
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 43:
                self.sc_0 = 0.18
                self.sc_60 = 0.30
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 44:
                self.sc_0 = 0.37
                self.sc_60 = 0.13
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 45:
                self.sc_0 = 0.09
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 47:
                self.sc_fc = 0.88
            elif self.shaded_types == 48:
                self.sc_fc = 0.80
            elif self.shaded_types == 49:
                self.sc_fc = 0.68
            elif self.shaded_types == 50:
                self.sc_fc = 0.91
            elif self.shaded_types == 51:
                self.sc_fc = 0.83
            elif self.shaded_types == 52:
                self.sc_fc = 0.75
            elif self.shaded_types == 53:
                self.sc_fc = 0.93
            elif self.shaded_types == 54:
                self.sc_fc = 0.86
            elif self.shaded_types == 55:
                self.sc_fc = 0.79
            elif self.shaded_types == 56:
                self.sc_fc = 0.84
            elif self.shaded_types == 57:
                self.sc_fc = 0.66
            elif self.shaded_types == 58:
                self.sc_fc = 0.60
            elif self.shaded_types == 59:
                self.sc_fc = 0.85
            elif self.shaded_types == 60:
                self.sc_fc = 0.81
            elif self.shaded_types == 61:
                self.sc_fc = 0.88
            elif self.shaded_types == 62:
                self.sc_fc = 0.57
            elif self.shaded_types == 63:
                self.sc_fc = 0.53
            elif self.shaded_types == 64:
                self.sc_fc = 0.64
            elif self.shaded_types == 65:
                self.sc_fc = 0.95
            else:
                self.sc_fc = 1
        elif self.glazed_type == 55:
            if self.shaded_types == 1:
                self.sc_0 = 0.99
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60)*(min((1.2 * float(self.shadow_line)), 60))/60)
            elif self.shaded_types == 2:
                self.sc_0 = 0.99
                self.sc_60 = 0.93
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 3:
                self.sc_0 = 0.91
                self.sc_60 = 0.93
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 4:
                self.sc_0 = 0.93
                self.sc_60 = 0.91
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 5:
                self.sc_0 = 0.89
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 6:
                self.sc_0 = 0.99
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 7:
                self.sc_0 = 0.99
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 8:
                self.sc_0 = 0.82
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 9:
                self.sc_0 = 0.87
                self.sc_60 = 0.83
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 10:
                self.sc_0 = 0.77
                self.sc_60 = 0.77
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 11:
                self.sc_0 = 0.98
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 12:
                self.sc_0 = 0.98
                self.sc_60 = 0.83
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 13:
                self.sc_0 = 0.73
                self.sc_60 = 0.83
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 14:
                self.sc_0 = 0.81
                self.sc_60 = 0.73
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 15:
                self.sc_0 = 0.65
                self.sc_60 = 0.65
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 16:
                self.sc_0 = 0.97
                self.sc_60 = 0.99
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 17:
                self.sc_0 = 0.97
                self.sc_60 = 0.72
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 18:
                self.sc_0 = 0.67
                self.sc_60 = 0.72
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 19:
                self.sc_0 = 0.73
                self.sc_60 = 0.69
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 20:
                self.sc_0 = 0.66
                self.sc_60 = 0.68
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 21:
                self.sc_0 = 0.97
                self.sc_60 = 1
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 22:
                self.sc_0 = 0.97
                self.sc_60 = 0.69
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 23:
                self.sc_0 = 0.60
                self.sc_60 = 0.69
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 24:
                self.sc_0 = 0.69
                self.sc_60 = 0.61
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 25:
                self.sc_0 = 0.54
                self.sc_60 = 0.54
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 26:
                self.sc_0 = 0.97
                self.sc_60 = 1.01
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 27:
                self.sc_0 = 0.97
                self.sc_60 = 0.67
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 28:
                self.sc_0 = 0.53
                self.sc_60 = 0.67
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 29:
                self.sc_0 = 0.65
                self.sc_60 = 0.53
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 30:
                self.sc_0 = 0.42
                self.sc_60 = 0.39
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 31:
                self.sc_0 = 0.93
                self.sc_60 = 0.92
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 32:
                self.sc_0 = 0.93
                self.sc_60 = 0.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 33:
                self.sc_0 = 0.03
                self.sc_60 = 0.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 34:
                self.sc_0 = 0.2
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 35:
                self.sc_0 = 0.02
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 36:
                self.sc_0 = 0.94
                self.sc_60 = 1.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 37:
                self.sc_0 = 0.94
                self.sc_60 = 0.15
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 38:
                self.sc_0 = 0.08
                self.sc_60 = 0.15
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 39:
                self.sc_0 = 0.26
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 40:
                self.sc_0 = 0.04
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 41:
                self.sc_0 = 0.95
                self.sc_60 = 1.21
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 42:
                self.sc_0 = 0.95
                self.sc_60 = 0.3
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 43:
                self.sc_0 = 0.18
                self.sc_60 = 0.3
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 44:
                self.sc_0 = 0.37
                self.sc_60 = 0.13
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 45:
                self.sc_0 = 0.09
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 47:
                self.sc_fc = 0.89
            elif self.shaded_types == 48:
                self.sc_fc = 0.82
            elif self.shaded_types == 49:
                self.sc_fc = 0.72
            elif self.shaded_types == 50:
                self.sc_fc = 0.91
            elif self.shaded_types == 51:
                self.sc_fc = 0.85
            elif self.shaded_types == 52:
                self.sc_fc = 0.78
            elif self.shaded_types == 53:
                self.sc_fc = 0.93
            elif self.shaded_types == 54:
                self.sc_fc = 0.87
            elif self.shaded_types == 55:
                self.sc_fc = 0.82
            elif self.shaded_types == 56:
                self.sc_fc = 0.86
            elif self.shaded_types == 57:
                self.sc_fc = 0.71
            elif self.shaded_types == 58:
                self.sc_fc = 0.66
            elif self.shaded_types == 59:
                self.sc_fc = 0.86
            elif self.shaded_types == 60:
                self.sc_fc = 0.83
            elif self.shaded_types == 61:
                self.sc_fc = 0.89
            elif self.shaded_types == 62:
                self.sc_fc = 0.61
            elif self.shaded_types == 63:
                self.sc_fc = 0.57
            elif self.shaded_types == 64:
                self.sc_fc = 0.65
            elif self.shaded_types == 65:
                self.sc_fc = 0.96
            else:
                self.sc_fc = 1
        elif self.glazed_type == 56:
            if self.shaded_types == 1:
                self.sc_0 = 0.99
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60)*(min((1.2 * float(self.shadow_line)), 60))/60)
            elif self.shaded_types == 2:
                self.sc_0 = 0.99
                self.sc_60 = 0.94
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 3:
                self.sc_0 = 0.92
                self.sc_60 = 0.94
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 4:
                self.sc_0 = 0.94
                self.sc_60 = 0.93
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 5:
                self.sc_0 = 0.90
                self.sc_60 = 0.90
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 6:
                self.sc_0 = 0.99
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 7:
                self.sc_0 = 0.99
                self.sc_60 = 0.91
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 8:
                self.sc_0 = 0.85
                self.sc_60 = 0.91
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 9:
                self.sc_0 = 0.89
                self.sc_60 = 0.85
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 10:
                self.sc_0 = 0.81
                self.sc_60 = 0.81
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 11:
                self.sc_0 = 0.98
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 12:
                self.sc_0 = 0.98
                self.sc_60 = 0.86
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 13:
                self.sc_0 = 0.78
                self.sc_60 = 0.86
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 14:
                self.sc_0 = 0.87
                self.sc_60 = 0.78
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 15:
                self.sc_0 = 0.71
                self.sc_60 = 0.71
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 16:
                self.sc_0 = 0.95
                self.sc_60 = 0.96
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 17:
                self.sc_0 = 0.95
                self.sc_60 = 0.73
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 18:
                self.sc_0 = 0.96
                self.sc_60 = 0.73
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 19:
                self.sc_0 = 0.75
                self.sc_60 = 0.71
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 20:
                self.sc_0 = 0.68
                self.sc_60 = 0.70
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 21:
                self.sc_0 = 0.95
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 22:
                self.sc_0 = 0.95
                self.sc_60 = 0.71
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 23:
                self.sc_0 = 0.64
                self.sc_60 = 0.71
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 24:
                self.sc_0 = 0.71
                self.sc_60 = 0.65
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 25:
                self.sc_0 = 0.59
                self.sc_60 = 0.59
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 26:
                self.sc_0 = 0.95
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 27:
                self.sc_0 = 0.95
                self.sc_60 = 0.7
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 28:
                self.sc_0 = 0.59
                self.sc_60 = 0.70
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 29:
                self.sc_0 = 0.69
                self.sc_60 = 0.59
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 30:
                self.sc_0 = 0.49
                self.sc_60 = 0.47
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 31:
                self.sc_0 = 0.93
                self.sc_60 = 0.90
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 32:
                self.sc_0 = 0.93
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 33:
                self.sc_0 = 0.04
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 34:
                self.sc_0 = 0.2
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 35:
                self.sc_0 = 0.03
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 36:
                self.sc_0 = 0.94
                self.sc_60 = 0.99
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 37:
                self.sc_0 = 0.94
                self.sc_60 = 0.15
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 38:
                self.sc_0 = 0.08
                self.sc_60 = 0.15
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 39:
                self.sc_0 = 0.26
                self.sc_60 = 0.07
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 40:
                self.sc_0 = 0.05
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 41:
                self.sc_0 = 0.95
                self.sc_60 = 1.08
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 42:
                self.sc_0 = 0.95
                self.sc_60 = 0.29
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 43:
                self.sc_0 = 0.17
                self.sc_60 = 0.29
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 44:
                self.sc_0 = 0.35
                self.sc_60 = 0.13
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 45:
                self.sc_0 = 0.08
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 47:
                self.sc_fc = 0.90
            elif self.shaded_types == 48:
                self.sc_fc = 0.85
            elif self.shaded_types == 49:
                self.sc_fc = 0.76
            elif self.shaded_types == 50:
                self.sc_fc = 0.92
            elif self.shaded_types == 51:
                self.sc_fc = 0.87
            elif self.shaded_types == 52:
                self.sc_fc = 0.81
            elif self.shaded_types == 53:
                self.sc_fc = 0.94
            elif self.shaded_types == 54:
                self.sc_fc = 0.89
            elif self.shaded_types == 55:
                self.sc_fc = 0.85
            elif self.shaded_types == 56:
                self.sc_fc = 0.88
            elif self.shaded_types == 57:
                self.sc_fc = 0.75
            elif self.shaded_types == 58:
                self.sc_fc = 0.71
            elif self.shaded_types == 59:
                self.sc_fc = 0.88
            elif self.shaded_types == 60:
                self.sc_fc = 0.86
            elif self.shaded_types == 61:
                self.sc_fc = 0.90
            elif self.shaded_types == 62:
                self.sc_fc = 0.68
            elif self.shaded_types == 63:
                self.sc_fc = 0.64
            elif self.shaded_types == 64:
                self.sc_fc = 0.64
            elif self.shaded_types == 65:
                self.sc_fc = 0.96
            else:
                self.sc_fc = 1
        elif self.glazed_type == 58:
            if self.shaded_types == 1:
                self.sc_0 = 0.99
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60)*(min((1.2 * float(self.shadow_line)), 60))/60)
            elif self.shaded_types == 2:
                self.sc_0 = 0.99
                self.sc_60 = 0.95
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 3:
                self.sc_0 = 0.92
                self.sc_60 = 0.95
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 4:
                self.sc_0 = 0.94
                self.sc_60 = 0.93
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 5:
                self.sc_0 = 0.90
                self.sc_60 = 0.91
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 6:
                self.sc_0 = 0.99
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 7:
                self.sc_0 = 0.99
                self.sc_60 = 0.91
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 8:
                self.sc_0 = 0.85
                self.sc_60 = 0.91
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 9:
                self.sc_0 = 0.89
                self.sc_60 = 0.86
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 10:
                self.sc_0 = 0.82
                self.sc_60 = 0.82
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 11:
                self.sc_0 = 0.98
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 12:
                self.sc_0 = 0.98
                self.sc_60 = 0.86
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 13:
                self.sc_0 = 0.78
                self.sc_60 = 0.86
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 14:
                self.sc_0 = 0.87
                self.sc_60 = 0.79
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 15:
                self.sc_0 = 0.72
                self.sc_60 = 0.72
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 16:
                self.sc_0 = 0.94
                self.sc_60 = 0.95
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 17:
                self.sc_0 = 0.94
                self.sc_60 = 0.73
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 18:
                self.sc_0 = 0.70
                self.sc_60 = 0.73
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 19:
                self.sc_0 = 0.75
                self.sc_60 = 0.72
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 20:
                self.sc_0 = 0.69
                self.sc_60 = 0.71
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 21:
                self.sc_0 = 0.94
                self.sc_60 = 0.96
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 22:
                self.sc_0 = 0.94
                self.sc_60 = 0.72
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 23:
                self.sc_0 = 0.65
                self.sc_60 = 0.72
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 24:
                self.sc_0 = 0.72
                self.sc_60 = 0.66
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 25:
                self.sc_0 = 0.60
                self.sc_60 = 0.60
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 26:
                self.sc_0 = 0.94
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 27:
                self.sc_0 = 0.94
                self.sc_60 = 0.71
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 28:
                self.sc_0 = 0.60
                self.sc_60 = 0.71
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 29:
                self.sc_0 = 0.69
                self.sc_60 = 0.60
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 30:
                self.sc_0 = 0.51
                self.sc_60 = 0.49
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 31:
                self.sc_0 = 0.93
                self.sc_60 = 0.90
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 32:
                self.sc_0 = 0.93
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 33:
                self.sc_0 = 0.04
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 34:
                self.sc_0 = 0.2
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 35:
                self.sc_0 = 0.03
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 36:
                self.sc_0 = 0.94
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 37:
                self.sc_0 = 0.94
                self.sc_60 = 0.15
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 38:
                self.sc_0 = 0.08
                self.sc_60 = 0.15
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 39:
                self.sc_0 = 0.26
                self.sc_60 = 0.07
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 40:
                self.sc_0 = 0.05
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 41:
                self.sc_0 = 0.95
                self.sc_60 = 1.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 42:
                self.sc_0 = 0.95
                self.sc_60 = 0.29
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 43:
                self.sc_0 = 0.17
                self.sc_60 = 0.29
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 44:
                self.sc_0 = 0.35
                self.sc_60 = 0.13
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 45:
                self.sc_0 = 0.09
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 47:
                self.sc_fc = 0.91
            elif self.shaded_types == 48:
                self.sc_fc = 0.85
            elif self.shaded_types == 49:
                self.sc_fc = 0.77
            elif self.shaded_types == 50:
                self.sc_fc = 0.92
            elif self.shaded_types == 51:
                self.sc_fc = 0.87
            elif self.shaded_types == 52:
                self.sc_fc = 0.82
            elif self.shaded_types == 53:
                self.sc_fc = 0.94
            elif self.shaded_types == 54:
                self.sc_fc = 0.89
            elif self.shaded_types == 55:
                self.sc_fc = 0.85
            elif self.shaded_types == 56:
                self.sc_fc = 0.89
            elif self.shaded_types == 57:
                self.sc_fc = 0.77
            elif self.shaded_types == 58:
                self.sc_fc = 0.72
            elif self.shaded_types == 59:
                self.sc_fc = 0.88
            elif self.shaded_types == 60:
                self.sc_fc = 0.86
            elif self.shaded_types == 61:
                self.sc_fc = 0.91
            elif self.shaded_types == 62:
                self.sc_fc = 0.69
            elif self.shaded_types == 63:
                self.sc_fc = 0.65
            elif self.shaded_types == 64:
                self.sc_fc = 0.64
            elif self.shaded_types == 65:
                self.sc_fc = 0.96
            else:
                self.sc_fc = 1
        elif self.glazed_type == 59:
            if self.shaded_types == 1:
                self.sc_0 = 0.99
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60)*(min((1.2 * float(self.shadow_line)), 60))/60)
            elif self.shaded_types == 2:
                self.sc_0 = 0.99
                self.sc_60 = 0.94
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 3:
                self.sc_0 = 0.92
                self.sc_60 = 0.94
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 4:
                self.sc_0 = 0.94
                self.sc_60 = 0.92
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 5:
                self.sc_0 = 0.90
                self.sc_60 = 0.90
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 6:
                self.sc_0 = 0.99
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 7:
                self.sc_0 = 0.99
                self.sc_60 = 0.90
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 8:
                self.sc_0 = 0.85
                self.sc_60 = 0.90
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 9:
                self.sc_0 = 0.89
                self.sc_60 = 0.85
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 10:
                self.sc_0 = 0.80
                self.sc_60 = 0.80
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 11:
                self.sc_0 = 0.98
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 12:
                self.sc_0 = 0.98
                self.sc_60 = 0.85
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 13:
                self.sc_0 = 0.77
                self.sc_60 = 0.85
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 14:
                self.sc_0 = 0.83
                self.sc_60 = 0.77
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 15:
                self.sc_0 = 0.7069
                self.sc_60 = 0.71
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 16:
                self.sc_0 = 0.96
                self.sc_60 = 0.96
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 17:
                self.sc_0 = 0.96
                self.sc_60 = 0.73
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 18:
                self.sc_0 = 0.96
                self.sc_60 = 0.73
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 19:
                self.sc_0 = 0.75
                self.sc_60 = 0.71
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 20:
                self.sc_0 = 0.68
                self.sc_60 = 0.70
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 21:
                self.sc_0 = 0.95
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 22:
                self.sc_0 = 0.95
                self.sc_60 = 0.71
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 23:
                self.sc_0 = 0.63
                self.sc_60 = 0.71
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 24:
                self.sc_0 = 0.71
                self.sc_60 = 0.64
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 25:
                self.sc_0 = 0.58
                self.sc_60 = 0.58
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 26:
                self.sc_0 = 0.95
                self.sc_60 = 0.99
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 27:
                self.sc_0 = 0.95
                self.sc_60 = 0.69
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 28:
                self.sc_0 = 0.68
                self.sc_60 = 0.69
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 29:
                self.sc_0 = 0.68
                self.sc_60 = 0.58
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 30:
                self.sc_0 = 0.48
                self.sc_60 = 0.46
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 31:
                self.sc_0 = 0.93
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 32:
                self.sc_0 = 0.93
                self.sc_60 = 0.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 33:
                self.sc_0 = 0.03
                self.sc_60 = 0.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 34:
                self.sc_0 = 0.2
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 35:
                self.sc_0 = 0.03
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 36:
                self.sc_0 = 0.94
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 37:
                self.sc_0 = 0.94
                self.sc_60 = 0.15
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 38:
                self.sc_0 = 0.08
                self.sc_60 = 0.15
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 39:
                self.sc_0 = 0.25
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 40:
                self.sc_0 = 0.04
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 41:
                self.sc_0 = 0.95
                self.sc_60 = 1.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 42:
                self.sc_0 = 0.95
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 43:
                self.sc_0 = 0.17
                self.sc_60 = 0.28
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 44:
                self.sc_0 = 0.34
                self.sc_60 = 0.12
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 45:
                self.sc_0 = 0.08
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 47:
                self.sc_fc = 0.90
            elif self.shaded_types == 48:
                self.sc_fc = 0.84
            elif self.shaded_types == 49:
                self.sc_fc = 0.76
            elif self.shaded_types == 50:
                self.sc_fc = 0.92
            elif self.shaded_types == 51:
                self.sc_fc = 0.86
            elif self.shaded_types == 52:
                self.sc_fc = 0.81
            elif self.shaded_types == 53:
                self.sc_fc = 0.94
            elif self.shaded_types == 54:
                self.sc_fc = 0.89
            elif self.shaded_types == 55:
                self.sc_fc = 0.84
            elif self.shaded_types == 56:
                self.sc_fc = 0.88
            elif self.shaded_types == 57:
                self.sc_fc = 0.74
            elif self.shaded_types == 58:
                self.sc_fc = 0.70
            elif self.shaded_types == 59:
                self.sc_fc = 0.87
            elif self.shaded_types == 60:
                self.sc_fc = 0.85
            elif self.shaded_types == 61:
                self.sc_fc = 0.90
            elif self.shaded_types == 62:
                self.sc_fc = 0.66
            elif self.shaded_types == 63:
                self.sc_fc = 0.62
            elif self.shaded_types == 64:
                self.sc_fc = 0.64
            elif self.shaded_types == 65:
                self.sc_fc = 0.96
            else:
                self.sc_fc = 1
        elif self.glazed_type == 61:
            if self.shaded_types == 1:
                self.sc_0 = 0.99
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60)*(min((1.2 * float(self.shadow_line)), 60))/60)
            elif self.shaded_types == 2:
                self.sc_0 = 0.99
                self.sc_60 = 0.92
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 3:
                self.sc_0 = 0.88
                self.sc_60 = 0.92
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 4:
                self.sc_0 = 0.91
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 5:
                self.sc_0 = 0.86
                self.sc_60 = 0.87
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 6:
                self.sc_0 = 0.98
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 7:
                self.sc_0 = 0.98
                self.sc_60 = 0.86
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 8:
                self.sc_0 = 0.77
                self.sc_60 = 0.86
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 9:
                self.sc_0 = 0.83
                self.sc_60 = 0.78
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 10:
                self.sc_0 = 0.71
                self.sc_60 = 0.72
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 11:
                self.sc_0 = 0.98
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 12:
                self.sc_0 = 0.98
                self.sc_60 = 0.78
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 13:
                self.sc_0 = 0.66
                self.sc_60 = 0.78
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 14:
                self.sc_0 = 0.75
                self.sc_60 = 0.67
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 15:
                self.sc_0 = 0.57
                self.sc_60 = 0.58
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 16:
                self.sc_0 = 0.97
                self.sc_60 = 1.01
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 17:
                self.sc_0 = 0.97
                self.sc_60 = 0.44
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 18:
                self.sc_0 = 0.36
                self.sc_60 = 0.44
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 19:
                self.sc_0 = 0.48
                self.sc_60 = 0.41
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 20:
                self.sc_0 = 0.36
                self.sc_60 = 0.41
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 21:
                self.sc_0 = 0.97
                self.sc_60 = 1.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 22:
                self.sc_0 = 0.97
                self.sc_60 = 0.45
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 23:
                self.sc_0 = 0.33
                self.sc_60 = 0.45
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 24:
                self.sc_0 = 0.47
                self.sc_60 = 0.35
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 25:
                self.sc_0 = 0.28
                self.sc_60 = 0.29
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 26:
                self.sc_0 = 0.97
                self.sc_60 = 1.11
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 27:
                self.sc_0 = 0.97
                self.sc_60 = 0.48
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 28:
                self.sc_0 = 0.32
                self.sc_60 = 0.48
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 29:
                self.sc_0 = 0.48
                self.sc_60 = 0.31
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 30:
                self.sc_0 = 0.22
                self.sc_60 = 0.19
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 31:
                self.sc_0 = 0.93
                self.sc_60 = 0.90
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 32:
                self.sc_0 = 0.93
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 33:
                self.sc_0 = 0.02
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 34:
                self.sc_0 = 0.19
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 35:
                self.sc_0 = 0.02
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 36:
                self.sc_0 = 0.94
                self.sc_60 = 1
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 37:
                self.sc_0 = 0.94
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 38:
                self.sc_0 = 0.07
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 39:
                self.sc_0 = 0.24
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 40:
                self.sc_0 = 0.04
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 41:
                self.sc_0 = 0.95
                self.sc_60 = 1.11
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 42:
                self.sc_0 = 0.95
                self.sc_60 = 0.29
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 43:
                self.sc_0 = 0.16
                self.sc_60 = 0.29
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 44:
                self.sc_0 = 0.33
                self.sc_60 = 0.13
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 45:
                self.sc_0 = 0.08
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 47:
                self.sc_fc = 0.86
            elif self.shaded_types == 48:
                self.sc_fc = 0.77
            elif self.shaded_types == 49:
                self.sc_fc = 0.65
            elif self.shaded_types == 50:
                self.sc_fc = 0.89
            elif self.shaded_types == 51:
                self.sc_fc = 0.81
            elif self.shaded_types == 52:
                self.sc_fc = 0.81
            elif self.shaded_types == 53:
                self.sc_fc = 0.72
            elif self.shaded_types == 54:
                self.sc_fc = 0.91
            elif self.shaded_types == 55:
                self.sc_fc = 0.84
            elif self.shaded_types == 56:
                self.sc_fc = 0.77
            elif self.shaded_types == 57:
                self.sc_fc = 0.83
            elif self.shaded_types == 58:
                self.sc_fc = 0.64
            elif self.shaded_types == 59:
                self.sc_fc = 0.58
            elif self.shaded_types == 60:
                self.sc_fc = 0.82
            elif self.shaded_types == 61:
                self.sc_fc = 0.78
            elif self.shaded_types == 62:
                self.sc_fc = 0.86
            elif self.shaded_types == 63:
                self.sc_fc = 0.48
            elif self.shaded_types == 64:
                self.sc_fc = 0.64
            elif self.shaded_types == 65:
                self.sc_fc = 0.94
            else:
                self.sc_fc = 1
        elif self.glazed_type == 62:
            if self.shaded_types == 1:
                self.sc_0 = 0.99
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60)*(min((1.2 * float(self.shadow_line)), 60))/60)
            elif self.shaded_types == 2:
                self.sc_0 = 0.99
                self.sc_60 = 0.93
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 3:
                self.sc_0 = 0.89
                self.sc_60 = 0.93
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 4:
                self.sc_0 = 0.92
                self.sc_60 = 0.90
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 5:
                self.sc_0 = 0.87
                self.sc_60 = 0.88
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 6:
                self.sc_0 = 0.98
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 7:
                self.sc_0 = 0.98
                self.sc_60 = 0.87
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 8:
                self.sc_0 = 0.80
                self.sc_60 = 0.87
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 9:
                self.sc_0 = 0.85
                self.sc_60 = 0.81
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 10:
                self.sc_0 = 0.74
                self.sc_60 = 0.75
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 11:
                self.sc_0 = 0.98
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 12:
                self.sc_0 = 0.98
                self.sc_60 = 0.81
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 13:
                self.sc_0 = 0.70
                self.sc_60 = 0.81
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 14:
                self.sc_0 = 0.78
                self.sc_60 = 0.71
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 15:
                self.sc_0 = 0.62
                self.sc_60 = 0.64
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 16:
                self.sc_0 = 0.97
                self.sc_60 = 1.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 17:
                self.sc_0 = 0.97
                self.sc_60 = 0.46
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 18:
                self.sc_0 = 0.38
                self.sc_60 = 0.46
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 19:
                self.sc_0 = 0.50
                self.sc_60 = 0.43
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 20:
                self.sc_0 = 0.38
                self.sc_60 = 0.43
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 21:
                self.sc_0 = 0.98
                self.sc_60 = 1.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 22:
                self.sc_0 = 0.98
                self.sc_60 = 0.47
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 23:
                self.sc_0 = 0.34
                self.sc_60 = 0.47
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 24:
                self.sc_0 = 0.49
                self.sc_60 = 0.37
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 25:
                self.sc_0 = 0.29
                self.sc_60 = 0.31
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 26:
                self.sc_0 = 0.98
                self.sc_60 = 1.11
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 27:
                self.sc_0 = 0.98
                self.sc_60 = 0.49
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 28:
                self.sc_0 = 0.33
                self.sc_60 = 0.49
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 29:
                self.sc_0 = 0.49
                self.sc_60 = 0.32
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 30:
                self.sc_0 = 0.23
                self.sc_60 = 0.21
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 31:
                self.sc_0 = 0.93
                self.sc_60 = 0.90
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 32:
                self.sc_0 = 0.93
                self.sc_60 = 0.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 33:
                self.sc_0 = 0.02
                self.sc_60 = 0.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 34:
                self.sc_0 = 0.19
                self.sc_60 = 0.03
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 35:
                self.sc_0 = 0.02
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 36:
                self.sc_0 = 0.94
                self.sc_60 = 0.99
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 37:
                self.sc_0 = 0.94
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 38:
                self.sc_0 = 0.07
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 39:
                self.sc_0 = 0.25
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 40:
                self.sc_0 = 0.04
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 41:
                self.sc_0 = 0.95
                self.sc_60 = 1.1
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 42:
                self.sc_0 = 0.95
                self.sc_60 = 0.29
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 43:
                self.sc_0 = 0.16
                self.sc_60 = 0.29
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 44:
                self.sc_0 = 0.33
                self.sc_60 = 0.13
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 45:
                self.sc_0 = 0.08
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 47:
                self.sc_fc = 0.87
            elif self.shaded_types == 48:
                self.sc_fc = 0.80
            elif self.shaded_types == 49:
                self.sc_fc = 0.69
            elif self.shaded_types == 50:
                self.sc_fc = 0.90
            elif self.shaded_types == 51:
                self.sc_fc = 0.83
            elif self.shaded_types == 52:
                self.sc_fc = 0.76
            elif self.shaded_types == 53:
                self.sc_fc = 0.92
            elif self.shaded_types == 54:
                self.sc_fc = 0.85
            elif self.shaded_types == 55:
                self.sc_fc = 0.8
            elif self.shaded_types == 56:
                self.sc_fc = 0.85
            elif self.shaded_types == 57:
                self.sc_fc = 0.68
            elif self.shaded_types == 58:
                self.sc_fc = 0.63
            elif self.shaded_types == 59:
                self.sc_fc = 0.84
            elif self.shaded_types == 60:
                self.sc_fc = 0.81
            elif self.shaded_types == 61:
                self.sc_fc = 0.87
            elif self.shaded_types == 62:
                self.sc_fc = 0.59
            elif self.shaded_types == 63:
                self.sc_fc = 0.55
            elif self.shaded_types == 64:
                self.sc_fc = 0.64
            elif self.shaded_types == 65:
                self.sc_fc = 0.95
            else:
                self.sc_fc = 1
        elif self.glazed_type == 64:
            if self.shaded_types == 1:
                self.sc_0 = 0.99
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60)*(min((1.2 * float(self.shadow_line)), 60))/60)
            elif self.shaded_types == 2:
                self.sc_0 = 0.99
                self.sc_60 = 0.94
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 3:
                self.sc_0 = 0.90
                self.sc_60 = 0.94
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 4:
                self.sc_0 = 0.93
                self.sc_60 = 0.91
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 5:
                self.sc_0 = 0.88
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 6:
                self.sc_0 = 0.99
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 7:
                self.sc_0 = 0.99
                self.sc_60 = 0.88
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 8:
                self.sc_0 = 0.80
                self.sc_60 = 0.88
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 9:
                self.sc_0 = 0.85
                self.sc_60 = 0.81
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 10:
                self.sc_0 = 0.75
                self.sc_60 = 0.76
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 11:
                self.sc_0 = 0.98
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 12:
                self.sc_0 = 0.98
                self.sc_60 = 0.81
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 13:
                self.sc_0 = 0.69
                self.sc_60 = 0.81
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 14:
                self.sc_0 = 0.77
                self.sc_60 = 0.71
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 15:
                self.sc_0 = 0.61
                self.sc_60 = 0.63
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 16:
                self.sc_0 = 0.98
                self.sc_60 = 1.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 17:
                self.sc_0 = 0.98
                self.sc_60 = 0.62
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 18:
                self.sc_0 = 0.52
                self.sc_60 = 0.62
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 19:
                self.sc_0 = 0.62
                self.sc_60 = 0.58
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 20:
                self.sc_0 = 0.51
                self.sc_60 = 0.57
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 21:
                self.sc_0 = 0.98
                self.sc_60 = 1.08
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 22:
                self.sc_0 = 0.98
                self.sc_60 = 0.58
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 23:
                self.sc_0 = 0.44
                self.sc_60 = 0.58
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 24:
                self.sc_0 = 0.57
                self.sc_60 = 0.47
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 25:
                self.sc_0 = 0.38
                self.sc_60 = 0.40
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 26:
                self.sc_0 = 0.97
                self.sc_60 = 1.11
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 27:
                self.sc_0 = 0.97
                self.sc_60 = 0.55
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 28:
                self.sc_0 = 0.38
                self.sc_60 = 0.55
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 29:
                self.sc_0 = 0.54
                self.sc_60 = 0.37
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 30:
                self.sc_0 = 0.27
                self.sc_60 = 0.24
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 31:
                self.sc_0 = 0.93
                self.sc_60 = 0.90
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 32:
                self.sc_0 = 0.93
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 33:
                self.sc_0 = 0.02
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 34:
                self.sc_0 = 0.19
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 35:
                self.sc_0 = 0.01
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 36:
                self.sc_0 = 0.94
                self.sc_60 = 0.99
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 37:
                self.sc_0 = 0.94
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 38:
                self.sc_0 = 0.07
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 39:
                self.sc_0 = 0.24
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 40:
                self.sc_0 = 0.03
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 41:
                self.sc_0 = 0.95
                self.sc_60 = 1.10
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 42:
                self.sc_0 = 0.95
                self.sc_60 = 0.29
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 43:
                self.sc_0 = 0.16
                self.sc_60 = 0.29
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 44:
                self.sc_0 = 0.33
                self.sc_60 = 0.12
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 45:
                self.sc_0 = 0.08
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 47:
                self.sc_fc = 0.89
            elif self.shaded_types == 48:
                self.sc_fc = 0.80
            elif self.shaded_types == 49:
                self.sc_fc = 0.69
            elif self.shaded_types == 50:
                self.sc_fc = 0.91
            elif self.shaded_types == 51:
                self.sc_fc = 0.83
            elif self.shaded_types == 52:
                self.sc_fc = 0.75
            elif self.shaded_types == 53:
                self.sc_fc = 0.93
            elif self.shaded_types == 54:
                self.sc_fc = 0.86
            elif self.shaded_types == 55:
                self.sc_fc = 0.80
            elif self.shaded_types == 56:
                self.sc_fc = 0.84
            elif self.shaded_types == 57:
                self.sc_fc = 0.67
            elif self.shaded_types == 58:
                self.sc_fc = 0.62
            elif self.shaded_types == 59:
                self.sc_fc = 0.85
            elif self.shaded_types == 60:
                self.sc_fc = 0.81
            elif self.shaded_types == 61:
                self.sc_fc = 0.88
            elif self.shaded_types == 62:
                self.sc_fc = 0.57
            elif self.shaded_types == 63:
                self.sc_fc = 0.53
            elif self.shaded_types == 64:
                self.sc_fc = 0.64
            elif self.shaded_types == 65:
                self.sc_fc = 0.95
            else:
                self.sc_fc = 1
        elif self.glazed_type == 65:
            if self.shaded_types == 1:
                self.sc_0 = 0.99
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60)*(min((1.2 * float(self.shadow_line)), 60))/60)
            elif self.shaded_types == 2:
                self.sc_0 = 0.99
                self.sc_60 = 0.94
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 3:
                self.sc_0 = 0.91
                self.sc_60 = 0.94
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 4:
                self.sc_0 = 0.93
                self.sc_60 = 0.92
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 5:
                self.sc_0 = 0.89
                self.sc_60 = 0.90
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 6:
                self.sc_0 = 0.99
                self.sc_60 = 0.98
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 7:
                self.sc_0 = 0.99
                self.sc_60 = 0.90
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 8:
                self.sc_0 = 0.83
                self.sc_60 = 0.90
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 9:
                self.sc_0 = 0.87
                self.sc_60 = 0.84
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 10:
                self.sc_0 = 0.78
                self.sc_60 = 0.79
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 11:
                self.sc_0 = 0.98
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 12:
                self.sc_0 = 0.98
                self.sc_60 = 0.84
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 13:
                self.sc_0 = 0.74
                self.sc_60 = 0.84
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 14:
                self.sc_0 = 0.81
                self.sc_60 = 0.75
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 15:
                self.sc_0 = 0.67
                self.sc_60 = 0.68
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 16:
                self.sc_0 = 0.98
                self.sc_60 = 1.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 17:
                self.sc_0 = 0.98
                self.sc_60 = 0.63
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 18:
                self.sc_0 = 0.54
                self.sc_60 = 0.63
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 19:
                self.sc_0 = 0.64
                self.sc_60 = 0.60
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 20:
                self.sc_0 = 0.53
                self.sc_60 = 0.58
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 21:
                self.sc_0 = 0.98
                self.sc_60 = 1.08
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 22:
                self.sc_0 = 0.98
                self.sc_60 = 0.60
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 23:
                self.sc_0 = 0.46
                self.sc_60 = 0.60
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 24:
                self.sc_0 = 0.59
                self.sc_60 = 0.48
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 25:
                self.sc_0 = 0.40
                self.sc_60 = 0.41
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 26:
                self.sc_0 = 0.98
                self.sc_60 = 1.11
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 27:
                self.sc_0 = 0.98
                self.sc_60 = 0.56
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 28:
                self.sc_0 = 0.39
                self.sc_60 = 0.56
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 29:
                self.sc_0 = 0.55
                self.sc_60 = 0.38
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 30:
                self.sc_0 = 0.29
                self.sc_60 = 0.26
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 31:
                self.sc_0 = 0.93
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 32:
                self.sc_0 = 0.93
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 33:
                self.sc_0 = 0.02
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 34:
                self.sc_0 = 0.19
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 35:
                self.sc_0 = 0.02
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 36:
                self.sc_0 = 0.94
                self.sc_60 = 0.99
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 37:
                self.sc_0 = 0.94
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 38:
                self.sc_0 = 0.07
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 39:
                self.sc_0 = 0.24
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 40:
                self.sc_0 = 0.04
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 41:
                self.sc_0 = 0.95
                self.sc_60 = 1.08
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 42:
                self.sc_0 = 0.95
                self.sc_60 = 0.29
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 43:
                self.sc_0 = 0.16
                self.sc_60 = 0.29
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 44:
                self.sc_0 = 0.33
                self.sc_60 = 0.12
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 45:
                self.sc_0 = 0.08
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 47:
                self.sc_fc = 0.90
            elif self.shaded_types == 48:
                self.sc_fc = 0.83
            elif self.shaded_types == 49:
                self.sc_fc = 0.72
            elif self.shaded_types == 50:
                self.sc_fc = 0.92
            elif self.shaded_types == 51:
                self.sc_fc = 0.85
            elif self.shaded_types == 52:
                self.sc_fc = 0.79
            elif self.shaded_types == 53:
                self.sc_fc = 0.93
            elif self.shaded_types == 54:
                self.sc_fc = 0.87
            elif self.shaded_types == 55:
                self.sc_fc = 0.83
            elif self.shaded_types == 56:
                self.sc_fc = 0.87
            elif self.shaded_types == 57:
                self.sc_fc = 0.72
            elif self.shaded_types == 58:
                self.sc_fc = 0.68
            elif self.shaded_types == 59:
                self.sc_fc = 0.87
            elif self.shaded_types == 60:
                self.sc_fc = 0.84
            elif self.shaded_types == 61:
                self.sc_fc = 0.89
            elif self.shaded_types == 62:
                self.sc_fc = 0.64
            elif self.shaded_types == 63:
                self.sc_fc = 0.61
            elif self.shaded_types == 64:
                self.sc_fc = 0.64
            elif self.shaded_types == 65:
                self.sc_fc = 0.96
            else:
                self.sc_fc = 1
        elif self.glazed_type == 66:
            if self.shaded_types == 1:
                self.sc_0 = 1
                self.sc_60 = 1
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60)*(min((1.2 * float(self.shadow_line)), 60))/60)
            elif self.shaded_types == 2:
                self.sc_0 = 1
                self.sc_60 = 0.96
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 3:
                self.sc_0 = 0.93
                self.sc_60 = 0.96
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 4:
                self.sc_0 = 0.95
                self.sc_60 = 0.93
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 5:
                self.sc_0 = 0.91
                self.sc_60 = 0.91
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 6:
                self.sc_0 = 0.99
                self.sc_60 = 0.99
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 7:
                self.sc_0 = 0.99
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 8:
                self.sc_0 = 0.81
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 9:
                self.sc_0 = 0.86
                self.sc_60 = 0.82
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 10:
                self.sc_0 = 0.76
                self.sc_60 = 0.76
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 11:
                self.sc_0 = 0.99
                self.sc_60 = 0.99
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 12:
                self.sc_0 = 0.99
                self.sc_60 = 0.81
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 13:
                self.sc_0 = 0.69
                self.sc_60 = 0.81
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 14:
                self.sc_0 = 0.77
                self.sc_60 = 0.70
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 15:
                self.sc_0 = 0.60
                self.sc_60 = 0.62
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 16:
                self.sc_0 = 0.97
                self.sc_60 = 1.01
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 17:
                self.sc_0 = 0.97
                self.sc_60 = 0.40
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 18:
                self.sc_0 = 0.32
                self.sc_60 = 0.40
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 19:
                self.sc_0 = 0.45
                self.sc_60 = 0.37
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 20:
                self.sc_0 = 0.32
                self.sc_60 = 0.37
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 21:
                self.sc_0 = 0.97
                self.sc_60 = 1.07
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 22:
                self.sc_0 = 0.97
                self.sc_60 = 0.42
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 23:
                self.sc_0 = 0.30
                self.sc_60 = 0.42
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 24:
                self.sc_0 = 0.45
                self.sc_60 = 0.32
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 25:
                self.sc_0 = 0.25
                self.sc_60 = 0.27
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 26:
                self.sc_0 = 0.98
                self.sc_60 = 1.12
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 27:
                self.sc_0 = 0.98
                self.sc_60 = 0.47
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 28:
                self.sc_0 = 0.31
                self.sc_60 = 0.47
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 29:
                self.sc_0 = 0.47
                self.sc_60 = 0.30
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 30:
                self.sc_0 = 0.21
                self.sc_60 = 0.18
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 31:
                self.sc_0 = 0.93
                self.sc_60 = 0.90
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 32:
                self.sc_0 = 0.93
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 33:
                self.sc_0 = 0.02
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 34:
                self.sc_0 = 0.19
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 35:
                self.sc_0 = 0.02
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 36:
                self.sc_0 = 0.94
                self.sc_60 = 1
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 37:
                self.sc_0 = 0.94
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 38:
                self.sc_0 = 0.07
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 39:
                self.sc_0 = 0.24
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 40:
                self.sc_0 = 0.03
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 41:
                self.sc_0 = 0.95
                self.sc_60 = 1.11
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 42:
                self.sc_0 = 0.95
                self.sc_60 = 0.29
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 43:
                self.sc_0 = 0.15
                self.sc_60 = 0.29
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 44:
                self.sc_0 = 0.33
                self.sc_60 = 0.13
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 45:
                self.sc_0 = 0.08
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 47:
                self.sc_fc = 0.91
            elif self.shaded_types == 48:
                self.sc_fc = 0.82
            elif self.shaded_types == 49:
                self.sc_fc = 0.69
            elif self.shaded_types == 50:
                self.sc_fc = 0.93
            elif self.shaded_types == 51:
                self.sc_fc = 0.84
            elif self.shaded_types == 52:
                self.sc_fc = 0.75
            elif self.shaded_types == 53:
                self.sc_fc = 0.95
            elif self.shaded_types == 54:
                self.sc_fc = 0.87
            elif self.shaded_types == 55:
                self.sc_fc = 0.80
            elif self.shaded_types == 56:
                self.sc_fc = 0.85
            elif self.shaded_types == 57:
                self.sc_fc = 0.67
            elif self.shaded_types == 58:
                self.sc_fc = 0.62
            elif self.shaded_types == 59:
                self.sc_fc = 0.87
            elif self.shaded_types == 60:
                self.sc_fc = 0.82
            elif self.shaded_types == 61:
                self.sc_fc = 0.90
            elif self.shaded_types == 62:
                self.sc_fc = 0.57
            elif self.shaded_types == 63:
                self.sc_fc = 0.52
            elif self.shaded_types == 64:
                self.sc_fc = 0.64
            elif self.shaded_types == 65:
                self.sc_fc = 0.95
            else:
                self.sc_fc = 1
        elif self.glazed_type == 67:
            if self.shaded_types == 1:
                self.sc_0 = 1
                self.sc_60 = 1
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60)*(min((1.2 * float(self.shadow_line)), 60))/60)
            elif self.shaded_types == 2:
                self.sc_0 = 1
                self.sc_60 = 0.96
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 3:
                self.sc_0 = 0.93
                self.sc_60 = 0.96
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 4:
                self.sc_0 = 0.95
                self.sc_60 = 0.94
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 5:
                self.sc_0 = 0.92
                self.sc_60 = 0.92
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 6:
                self.sc_0 = 1
                self.sc_60 = 1
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 7:
                self.sc_0 = 1
                self.sc_60 = 0.91
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 8:
                self.sc_0 = 0.83
                self.sc_60 = 0.91
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 9:
                self.sc_0 = 0.88
                self.sc_60 = 0.84
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 10:
                self.sc_0 = 0.79
                self.sc_60 = 0.80
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 11:
                self.sc_0 = 0.99
                self.sc_60 = 0.99
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 12:
                self.sc_0 = 0.99
                self.sc_60 = 0.83
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 13:
                self.sc_0 = 0.73
                self.sc_60 = 0.83
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 14:
                self.sc_0 = 0.80
                self.sc_60 = 0.74
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 15:
                self.sc_0 = 0.66
                self.sc_60 = 0.67
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 16:
                self.sc_0 = 0.98
                self.sc_60 = 1.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 17:
                self.sc_0 = 0.98
                self.sc_60 = 0.42
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 18:
                self.sc_0 = 0.32
                self.sc_60 = 0.42
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 19:
                self.sc_0 = 0.47
                self.sc_60 = 0.40
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 20:
                self.sc_0 = 0.34
                self.sc_60 = 0.40
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 21:
                self.sc_0 = 0.98
                self.sc_60 = 1.07
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 22:
                self.sc_0 = 0.97
                self.sc_60 = 0.44
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 23:
                self.sc_0 = 0.32
                self.sc_60 = 0.44
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 24:
                self.sc_0 = 0.47
                self.sc_60 = 0.35
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 25:
                self.sc_0 = 0.27
                self.sc_60 = 0.29
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 26:
                self.sc_0 = 0.98
                self.sc_60 = 1.12
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 27:
                self.sc_0 = 0.98
                self.sc_60 = 0.48
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 28:
                self.sc_0 = 0.32
                self.sc_60 = 0.48
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 29:
                self.sc_0 = 0.49
                self.sc_60 = 0.32
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 30:
                self.sc_0 = 0.22
                self.sc_60 = 0.20
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 31:
                self.sc_0 = 0.93
                self.sc_60 = 0.90
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 32:
                self.sc_0 = 0.93
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 33:
                self.sc_0 = 0.02
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 34:
                self.sc_0 = 0.19
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 35:
                self.sc_0 = 0.02
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 36:
                self.sc_0 = 0.94
                self.sc_60 = 1
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 37:
                self.sc_0 = 0.94
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 38:
                self.sc_0 = 0.07
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 39:
                self.sc_0 = 0.24
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 40:
                self.sc_0 = 0.03
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 41:
                self.sc_0 = 0.95
                self.sc_60 = 1.10
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 42:
                self.sc_0 = 0.95
                self.sc_60 = 0.29
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 43:
                self.sc_0 = 0.15
                self.sc_60 = 0.29
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 44:
                self.sc_0 = 0.33
                self.sc_60 = 0.13
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 45:
                self.sc_0 = 0.08
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 47:
                self.sc_fc = 0.92
            elif self.shaded_types == 48:
                self.sc_fc = 0.84
            elif self.shaded_types == 49:
                self.sc_fc = 0.73
            elif self.shaded_types == 50:
                self.sc_fc = 0.94
            elif self.shaded_types == 51:
                self.sc_fc = 0.86
            elif self.shaded_types == 52:
                self.sc_fc = 0.79
            elif self.shaded_types == 53:
                self.sc_fc = 0.95
            elif self.shaded_types == 54:
                self.sc_fc = 0.88
            elif self.shaded_types == 55:
                self.sc_fc = 0.82
            elif self.shaded_types == 56:
                self.sc_fc = 0.87
            elif self.shaded_types == 57:
                self.sc_fc = 0.71
            elif self.shaded_types == 58:
                self.sc_fc = 0.67
            elif self.shaded_types == 59:
                self.sc_fc = 0.89
            elif self.shaded_types == 60:
                self.sc_fc = 0.85
            elif self.shaded_types == 61:
                self.sc_fc = 0.91
            elif self.shaded_types == 62:
                self.sc_fc = 0.63
            elif self.shaded_types == 63:
                self.sc_fc = 0.59
            elif self.shaded_types == 64:
                self.sc_fc = 0.64
            elif self.shaded_types == 65:
                self.sc_fc = 0.95
            else:
                self.sc_fc = 1
        elif self.glazed_type == 68:
            if self.shaded_types == 1:
                self.sc_0 = 1
                self.sc_60 = 1
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60)*(min((1.2 * float(self.shadow_line)), 60))/60)
            elif self.shaded_types == 2:
                self.sc_0 = 1
                self.sc_60 = 0.96
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 3:
                self.sc_0 = 0.94
                self.sc_60 = 0.96
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 4:
                self.sc_0 = 0.92
                self.sc_60 = 0.93
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 5:
                self.sc_0 = 0.99
                self.sc_60 = 1
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 6:
                self.sc_0 = 0.99
                self.sc_60 = 0.91
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 7:
                self.sc_0 = 0.83
                self.sc_60 = 0.91
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 8:
                self.sc_0 = 0.88
                self.sc_60 = 0.84
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 9:
                self.sc_0 = 0.78
                self.sc_60 = 0.80
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 10:
                self.sc_0 = 0.99
                self.sc_60 = 0.99
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 11:
                self.sc_0 = 0.99
                self.sc_60 = 0.83
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 12:
                self.sc_0 = 0.72
                self.sc_60 = 0.83
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 13:
                self.sc_0 = 0.80
                self.sc_60 = 0.74
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 14:
                self.sc_0 = 0.65
                self.sc_60 = 0.66
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 15:
                self.sc_0 = 0.98
                self.sc_60 = 1.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 16:
                self.sc_0 = 0.98
                self.sc_60 = 1.01
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 17:
                self.sc_0 = 0.98
                self.sc_60 = 0.57
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 18:
                self.sc_0 = 0.48
                self.sc_60 = 0.57
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 19:
                self.sc_0 = 0.58
                self.sc_60 = 0.54
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 20:
                self.sc_0 = 0.46
                self.sc_60 = 0.53
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 21:
                self.sc_0 = 0.98
                self.sc_60 = 1.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 22:
                self.sc_0 = 0.98
                self.sc_60 = 0.57
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 23:
                self.sc_0 = 0.48
                self.sc_60 = 0.57
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 24:
                self.sc_0 = 0.58
                self.sc_60 = 0.54
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 25:
                self.sc_0 = 0.46
                self.sc_60 = 0.53
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 26:
                self.sc_0 = 0.98
                self.sc_60 = 1.09
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 27:
                self.sc_0 = 0.98
                self.sc_60 = 0.55
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 28:
                self.sc_0 = 0.41
                self.sc_60 = 0.55
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 29:
                self.sc_0 = 0.55
                self.sc_60 = 0.44
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 30:
                self.sc_0 = 0.35
                self.sc_60 = 0.37
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 31:
                self.sc_0 = 0.98
                self.sc_60 = 1.12
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 32:
                self.sc_0 = 0.98
                self.sc_60 = 0.54
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 33:
                self.sc_0 = 0.02
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 34:
                self.sc_0 = 0.19
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 35:
                self.sc_0 = 0.02
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 36:
                self.sc_0 = 0.94
                self.sc_60 = 1
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 37:
                self.sc_0 = 0.94
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 38:
                self.sc_0 = 0.07
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 39:
                self.sc_0 = 0.24
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 40:
                self.sc_0 = 0.03
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 41:
                self.sc_0 = 0.95
                self.sc_60 = 1.11
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 42:
                self.sc_0 = 0.95
                self.sc_60 = 0.29
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 43:
                self.sc_0 = 0.15
                self.sc_60 = 0.29
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 44:
                self.sc_0 = 0.33
                self.sc_60 = 0.13
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 45:
                self.sc_0 = 0.08
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 47:
                self.sc_fc = 0.93
            elif self.shaded_types == 48:
                self.sc_fc = 0.84
            elif self.shaded_types == 49:
                self.sc_fc = 0.73
            elif self.shaded_types == 50:
                self.sc_fc = 0.94
            elif self.shaded_types == 51:
                self.sc_fc = 0.86
            elif self.shaded_types == 52:
                self.sc_fc = 0.78
            elif self.shaded_types == 53:
                self.sc_fc = 0.96
            elif self.shaded_types == 54:
                self.sc_fc = 0.88
            elif self.shaded_types == 55:
                self.sc_fc = 0.82
            elif self.shaded_types == 56:
                self.sc_fc = 0.86
            elif self.shaded_types == 57:
                self.sc_fc = 0.7
            elif self.shaded_types == 58:
                self.sc_fc = 0.67
            elif self.shaded_types == 59:
                self.sc_fc = 0.89
            elif self.shaded_types == 60:
                self.sc_fc = 0.85
            elif self.shaded_types == 61:
                self.sc_fc = 0.91
            elif self.shaded_types == 62:
                self.sc_fc = 0.61
            elif self.shaded_types == 63:
                self.sc_fc = 0.58
            elif self.shaded_types == 64:
                self.sc_fc = 0.64
            elif self.shaded_types == 65:
                self.sc_fc = 0.96
            else:
                self.sc_fc = 1
        elif self.glazed_type == 69:
            if self.shaded_types == 1:
                self.sc_0 = 1
                self.sc_60 = 1
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60)*(min((1.2 * float(self.shadow_line)), 60))/60)
            elif self.shaded_types == 2:
                self.sc_0 = 1
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 3:
                self.sc_0 = 0.95
                self.sc_60 = 0.97
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 4:
                self.sc_0 = 0.96
                self.sc_60 = 0.95
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 5:
                self.sc_0 = 0.93
                self.sc_60 = 0.94
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 6:
                self.sc_0 = 1
                self.sc_60 = 1
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 7:
                self.sc_0 = 1
                self.sc_60 = 0.92
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 8:
                self.sc_0 = 0.86
                self.sc_60 = 0.92
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 9:
                self.sc_0 = 0.90
                self.sc_60 = 0.87
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 10:
                self.sc_0 = 0.82
                self.sc_60 = 0.83
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 11:
                self.sc_0 = 0.99
                self.sc_60 = 0.99
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 12:
                self.sc_0 = 0.99
                self.sc_60 = 0.86
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 13:
                self.sc_0 = 0.77
                self.sc_60 = 0.86
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 14:
                self.sc_0 = 0.83
                self.sc_60 = 0.77
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 15:
                self.sc_0 = 0.71
                self.sc_60 = 0.72
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 16:
                self.sc_0 = 0.99
                self.sc_60 = 1.05
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 17:
                self.sc_0 = 0.99
                self.sc_60 = 0.60
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 18:
                self.sc_0 = 0.50
                self.sc_60 = 0.60
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 19:
                self.sc_0 = 0.60
                self.sc_60 = 0.57
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 20:
                self.sc_0 = 0.49
                self.sc_60 = 0.55
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 21:
                self.sc_0 = 0.99
                self.sc_60 = 1.09
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 22:
                self.sc_0 = 0.99
                self.sc_60 = 0.57
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 23:
                self.sc_0 = 0.43
                self.sc_60 = 0.57
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 24:
                self.sc_0 = 0.56
                self.sc_60 = 0.46
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 25:
                self.sc_0 = 0.37
                self.sc_60 = 0.39
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 26:
                self.sc_0 = 0.99
                self.sc_60 = 1.12
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 27:
                self.sc_0 = 0.99
                self.sc_60 = 0.55
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 28:
                self.sc_0 = 0.38
                self.sc_60 = 0.55
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 29:
                self.sc_0 = 0.54
                self.sc_60 = 0.37
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 30:
                self.sc_0 = 0.28
                self.sc_60 = 0.25
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 31:
                self.sc_0 = 0.93
                self.sc_60 = 0.89
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 32:
                self.sc_0 = 0.93
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 33:
                self.sc_0 = 0.02
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 34:
                self.sc_0 = 0.19
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 35:
                self.sc_0 = 0.01
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 36:
                self.sc_0 = 0.94
                self.sc_60 = 0.99
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 37:
                self.sc_0 = 0.94
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 38:
                self.sc_0 = 0.07
                self.sc_60 = 0.14
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 39:
                self.sc_0 = 0.24
                self.sc_60 = 0.06
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 40:
                self.sc_0 = 0.03
                self.sc_60 = 0.02
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 41:
                self.sc_0 = 0.95
                self.sc_60 = 1.09
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 42:
                self.sc_0 = 0.95
                self.sc_60 = 0.29
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 43:
                self.sc_0 = 0.15
                self.sc_60 = 0.29
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 44:
                self.sc_0 = 0.33
                self.sc_60 = 0.12
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 45:
                self.sc_0 = 0.08
                self.sc_60 = 0.04
                self.sc_fc = self.sc_0 + ((self.sc_0 - self.sc_60) * (min((1.2 * float(self.shadow_line)), 60)) / 60)
            elif self.shaded_types == 47:
                self.sc_fc = 0.94
            elif self.shaded_types == 48:
                self.sc_fc = 0.87
            elif self.shaded_types == 49:
                self.sc_fc = 0.77
            elif self.shaded_types == 50:
                self.sc_fc = 0.95
            elif self.shaded_types == 51:
                self.sc_fc = 0.89
            elif self.shaded_types == 52:
                self.sc_fc = 0.82
            elif self.shaded_types == 53:
                self.sc_fc = 0.96
            elif self.shaded_types == 54:
                self.sc_fc = 0.90
            elif self.shaded_types == 55:
                self.sc_fc = 0.85
            elif self.shaded_types == 56:
                self.sc_fc = 0.89
            elif self.shaded_types == 57:
                self.sc_fc = 0.75
            elif self.shaded_types == 58:
                self.sc_fc = 0.72
            elif self.shaded_types == 59:
                self.sc_fc = 0.91
            elif self.shaded_types == 60:
                self.sc_fc = 0.87
            elif self.shaded_types == 61:
                self.sc_fc = 0.92
            elif self.shaded_types == 62:
                self.sc_fc = 0.68
            elif self.shaded_types == 63:
                self.sc_fc = 0.65
            elif self.shaded_types == 64:
                self.sc_fc = 0.64
            elif self.shaded_types == 65:
                self.sc_fc = 0.96
            else:
                self.sc_fc = 1
        else:
            self.sc_fc = 1

        return self.sc_fc

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
        self.lineEdit_5.clear()

    def reset_shgc_installation_factor(self):
        self.comboBox_2.setCurrentIndex(0)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add Fenestration Area Properties"))
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
        self.comboBox_4.setItemText(1, _translate("Dialog", "Northeast/Northwest"))
        self.comboBox_4.setItemText(2, _translate("Dialog", "East/West"))
        self.comboBox_4.setItemText(3, _translate("Dialog", "Southeast/Southwest"))
        self.comboBox_4.setItemText(4, _translate("Dialog", "South"))
        self.comboBox_4.setItemText(5, _translate("Dialog", "Horizontal"))
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
        self.comboBox_7.setItemText(1, _translate("Dialog", "Louvered-Indoor side-reflection 0.15-slat angle worst"))
        self.comboBox_7.setItemText(2, _translate("Dialog", "Louvered-Indoor side-reflection 0.15-slat angle 0"))
        self.comboBox_7.setItemText(3, _translate("Dialog", "Louvered-Indoor side-reflection 0.15-slat angle negative"))
        self.comboBox_7.setItemText(4, _translate("Dialog", "Louvered-Indoor side-reflection 0.15-slat angle 45"))
        self.comboBox_7.setItemText(5, _translate("Dialog", "Louvered-Indoor side-reflection .015-slat angle closed"))
        self.comboBox_7.setItemText(6, _translate("Dialog", "Louvered-Indoor side-reflection 0.5-slat angle worst"))
        self.comboBox_7.setItemText(7, _translate("Dialog", "Louvered-Indoor side-reflection 0.5-slat angle 0"))
        self.comboBox_7.setItemText(8, _translate("Dialog", "Louvered-Indoor side-reflection 0.5-slat angle negative"))
        self.comboBox_7.setItemText(9, _translate("Dialog", "Louvered-Indoor side-reflection 0.5-slat angle 45"))
        self.comboBox_7.setItemText(10, _translate("Dialog", "Louvered-Indoor side-reflection 0.5-slat angle closed"))
        self.comboBox_7.setItemText(11, _translate("Dialog", "Louvered-Indoor side-reflection 0.8-slat angle worst"))
        self.comboBox_7.setItemText(12, _translate("Dialog", "Louvered-Indoor side-reflection 0.8-slat angle 0"))
        self.comboBox_7.setItemText(13, _translate("Dialog", "Louvered-Indoor side-reflection 0.8-slat angle negative"))
        self.comboBox_7.setItemText(14, _translate("Dialog", "Louvered-Indoor side-reflection 0.8-slat angle 45"))
        self.comboBox_7.setItemText(15, _translate("Dialog", "Louvered-Indoor side-reflection 0.8-slat angle closed"))
        self.comboBox_7.setItemText(16, _translate("Dialog", "Louvered-Between Glazing-reflection 0.15-slat angle worst"))
        self.comboBox_7.setItemText(17, _translate("Dialog", "Louvered-Between Glazing-reflection 0.15-slat angle 0"))
        self.comboBox_7.setItemText(18, _translate("Dialog", "Louvered-Between Glazing-reflection 0.15-slat angle negative"))
        self.comboBox_7.setItemText(19, _translate("Dialog", "Louvered-Between Glazing-reflection 0.15-slat angle 45"))
        self.comboBox_7.setItemText(20, _translate("Dialog", "Louvered-Between Glazing-reflection .015-slat angle closed"))
        self.comboBox_7.setItemText(21, _translate("Dialog", "Louvered-Between Glazing-reflection 0.5-slat angle worst"))
        self.comboBox_7.setItemText(22, _translate("Dialog", "Louvered-Between Glazing-reflection 0.5-slat angle 0"))
        self.comboBox_7.setItemText(23, _translate("Dialog", "Louvered-Between Glazing-reflection 0.5-slat angle negative"))
        self.comboBox_7.setItemText(24, _translate("Dialog", "Louvered-Between Glazing-reflection 0.5-slat angle 45"))
        self.comboBox_7.setItemText(25, _translate("Dialog", "Louvered-Between Glazing-reflection 0.5-slat angle closed"))
        self.comboBox_7.setItemText(26, _translate("Dialog", "Louvered-Between Glazing-reflection 0.8-slat angle worst"))
        self.comboBox_7.setItemText(27, _translate("Dialog", "Louvered-Between Glazing-reflection 0.8-slat angle 0"))
        self.comboBox_7.setItemText(28, _translate("Dialog", "Louvered-Between Glazing-reflection 0.8-slat angle negative"))
        self.comboBox_7.setItemText(29, _translate("Dialog", "Louvered-Between Glazing-reflection 0.8-slat angle 45"))
        self.comboBox_7.setItemText(30, _translate("Dialog", "Louvered-Between Glazing-reflection 0.8-slat angle closed"))
        self.comboBox_7.setItemText(31, _translate("Dialog", "Louvered-Outdoor Side-reflection 0.15-slat angle worst"))
        self.comboBox_7.setItemText(32, _translate("Dialog", "Louvered-Outdoor Side-reflection 0.15-slat angle 0"))
        self.comboBox_7.setItemText(33, _translate("Dialog", "Louvered-Outdoor Side-reflection 0.15-slat angle negative"))
        self.comboBox_7.setItemText(34, _translate("Dialog", "Louvered-Outdoor Side-reflection 0.15-slat angle 45"))
        self.comboBox_7.setItemText(35, _translate("Dialog", "Louvered-Outdoor Side-reflection .015-slat angle closed"))
        self.comboBox_7.setItemText(36, _translate("Dialog", "Louvered-Outdoor Side-reflection 0.5-slat angle worst"))
        self.comboBox_7.setItemText(37, _translate("Dialog", "Louvered-Outdoor Side-reflection 0.5-slat angle 0"))
        self.comboBox_7.setItemText(38, _translate("Dialog", "Louvered-Outdoor Side-reflection 0.5-slat angle negative"))
        self.comboBox_7.setItemText(39, _translate("Dialog", "Louvered-Outdoor Side-reflection 0.5-slat angle 45"))
        self.comboBox_7.setItemText(40, _translate("Dialog", "Louvered-Outdoor Side-reflection 0.5-slat angle closed"))
        self.comboBox_7.setItemText(41, _translate("Dialog", "Louvered-Outdoor Side-reflection 0.8-slat angle worst"))
        self.comboBox_7.setItemText(42, _translate("Dialog", "Louvered-Outdoor Side-reflection 0.8-slat angle 0"))
        self.comboBox_7.setItemText(43, _translate("Dialog", "Louvered-Outdoor Side-reflection 0.8-slat angle negative"))
        self.comboBox_7.setItemText(44, _translate("Dialog", "Louvered-Outdoor Side-reflection 0.8-slat angle 45"))
        self.comboBox_7.setItemText(45, _translate("Dialog", "Louvered-Outdoor Side-reflection 0.8-slat angle closed"))
        self.comboBox_7.setItemText(46, _translate("Dialog", "Louvered-Sheer"))
        self.comboBox_7.setItemText(47, _translate("Dialog", "Drapery-Dark Closed Weave-Fabric Designator III"))
        self.comboBox_7.setItemText(48, _translate("Dialog", "Drapery-Medium Closed Weave-Fabric Designator III"))
        self.comboBox_7.setItemText(49, _translate("Dialog", "Drapery-Light Closed Weave-Fabric Designator III"))
        self.comboBox_7.setItemText(50, _translate("Dialog", "Drapery-Dark Closed Weave-Fabric Designator II"))
        self.comboBox_7.setItemText(51, _translate("Dialog", "Drapery-Medium Closed Weave-Fabric Designator II"))
        self.comboBox_7.setItemText(52, _translate("Dialog", "Drapery-Light Closed Weave-Fabric Designator II"))
        self.comboBox_7.setItemText(53, _translate("Dialog", "Drapery-Dark Closed Weave-Fabric Designator I"))
        self.comboBox_7.setItemText(54, _translate("Dialog", "Drapery-Medium Closed Weave-Fabric Designator I"))
        self.comboBox_7.setItemText(55, _translate("Dialog", "Drapery-Light Closed Weave-Fabric Designator I"))
        self.comboBox_7.setItemText(56, _translate("Dialog", "Drapery-Sheer"))
        self.comboBox_7.setItemText(57, _translate("Dialog", "Roller-Light Translucent-Openness 0.14"))
        self.comboBox_7.setItemText(58, _translate("Dialog", "Roller Screen-White Opaque-Openness 0"))
        self.comboBox_7.setItemText(59, _translate("Dialog", "Roller Screen-Dark Opaque-Openness 0"))
        self.comboBox_7.setItemText(60, _translate("Dialog", "Roller Screen-Light Gray Translucent-Openness 0.1"))
        self.comboBox_7.setItemText(61, _translate("Dialog", "Roller Screen-Dark Gray Translucent-Openness 0.14"))
        self.comboBox_7.setItemText(62, _translate("Dialog", "Roller Screen-Reflective White Opaque-Openness 0"))
        self.comboBox_7.setItemText(63, _translate("Dialog", "Roller Screen-Reflective White Translucent-Openness 0.07"))
        self.comboBox_7.setItemText(64, _translate("Dialog", "Outdoor Insect Screen"))
        self.comboBox_7.setItemText(65, _translate("Dialog", "Indoor Insect Screen"))
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
        self.label_12.setText(_translate("Dialog", "Shading Profile Angle :"))


