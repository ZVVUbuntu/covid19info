"""Protect module"""
from PyQt5.QtWidgets import QFrame, QLabel, QVBoxLayout, QHBoxLayout, QScrollArea
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
from . import flowbox


class Protect_yourself(QScrollArea):
	"""Protect yourself class"""
	def __init__(self):
		super().__init__()
		self.setWidgetResizable(True)
		self.create_widgets()
		
	def create_widgets(self):
		"""Create widgets"""
		self.PROTECT_STEPS = [
				(self.tr('Wash your hands often with soap and water for at least 20 seconds especially after you have been in a public place, or after blowing your nose, coughing, or sneezing.'), './icons/clean_hands.png', ),
				(self.tr('Avoid close contact with people who are sick.'), './icons/distance.png', ),
				(self.tr('Stay home if you are sick, except to get medical care.'), './icons/stay_home.png', ),
				(self.tr('Cover your mouth and nose with a tissue when you cough or sneeze.'), './icons/cover_coughs.png', ),
				(self.tr('Wear a facemask if you are sick.'), './icons/wear_facemask.png', ),
				(self.tr('Clean AND disinfect frequently touched surfaces daily.'), './icons/clean_room.png', ),
			]
	#main_widget
		self.main_widget = QFrame()
		self.setWidget(self.main_widget)
	#vbox_main
		self.vbox_main = QVBoxLayout()
		self.main_widget.setLayout(self.vbox_main)
	#flow_box_steps
		self.flow_box_steps = flowbox.Window()
		self.vbox_main.addWidget(self.flow_box_steps)
		#set_items
		for item in self.PROTECT_STEPS:
			text, icon = item
			self.label = My_label()
			self.label.set_info(text, icon)
			self.flow_box_steps.flowLayout.addWidget(self.label) 
			
####################################################################################

class My_label(QLabel):
	"""MyLabel class"""
	def __init__(self):
		super().__init__()
		self.create_widgets()
		
	def create_widgets(self):
		"""Create widgets"""
		#hbox_main
		self.hbox_main = QHBoxLayout()
		self.setLayout(self.hbox_main)
		#label_icon
		self.label_icon = QLabel()
		self.label_icon.setScaledContents(True)
		self.label_icon.setAlignment(Qt.AlignCenter)
		self.label_icon.setFixedSize(120, 120)
		self.hbox_main.addWidget(self.label_icon)
		#label_text
		self.label_text = QLabel()
		self.label_text.setAlignment(Qt.AlignCenter)
		self.label_text.setWordWrap(True)
		self.hbox_main.addWidget(self.label_text)
		###
		self.setObjectName('Symptome_label')
		self.setFixedSize(300, 200)
		
	def set_info(self, text='', icon=None):
		"""Set info"""
		self.label_icon.setPixmap(QPixmap(icon))
		self.label_text.setText(text)
