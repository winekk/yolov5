import sys
from PySide6 import QtWidgets

main_window = QtWidgets.QApplication(sys.argv)
widget_1 = QtWidgets.QWidget()
widget_1.resize(640, 480)
widget_1.setWindowTitle("主窗口")
widget_1.show()
sys.exit(main_window.exec())
