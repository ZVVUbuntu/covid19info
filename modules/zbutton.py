"""Zbutton module"""
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize


class Zbutton(QPushButton):
	"""My button class"""
	def __init__(self):
		super().__init__()
		self.setCursor(Qt.PointingHandCursor)
		self.setFocusPolicy(Qt.NoFocus)
		self.INFO = None
		self.set_size()
		
	def set_size(self, width=40, height=40):
		"""Set size"""
		self.setFixedSize(width, height)
		self.setIconSize(QSize(height-4, height-4))
		
	def set_info(self, icon=None, text='', tool_tip=''):
		"""Set info"""
		if icon: self.setIcon(QIcon(icon))
		if text: self.setText(text)
		if tool_tip: self.setToolTip(tool_tip)
