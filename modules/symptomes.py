"""Symptomes module"""
from PyQt5.QtWidgets import QFrame, QLabel, QVBoxLayout, QHBoxLayout, QScrollArea
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
from . import flowbox


class Symptomes(QScrollArea):
	"""Stats widget class"""
	def __init__(self):
		super().__init__()
		self.setWidgetResizable(True)
		self.create_widgets()
		
	def create_widgets(self):
		"""Create widgets"""
		self.COMMON_SYMPTOMES = [
				(self.tr('Fever'), './icons/fever.png', ),
				(self.tr('Dry cough'), './icons/cough.png', ),
				(self.tr('Shortness of breath'), './icons/shortness_breath.png', ),
				(self.tr('Fatigue'), './icons/fatigue.png', ),
			]
		self.UNCOMMON_SYMPTOMES = [
				(self.tr('Headache'), './icons/headache.png', ), 
				(self.tr('Nasal congestion'), './icons/nose.png', ), 
				(self.tr('Sore throat'), './icons/sore_throat.png', ), 
				(self.tr('Chills'), './icons/chills.png', ), 
				(self.tr('Pain in muscules or joints'), './icons/pain.png', ), 
			]
	#main_widget
		self.main_widget = QFrame()
		self.setWidget(self.main_widget)
	#vbox_main
		self.vbox_main = QVBoxLayout()
		self.main_widget.setLayout(self.vbox_main)
	#label_common_title
		self.label_common_title = QLabel()
		self.label_common_title.setText(self.tr('Common symptoms'))
		self.label_common_title.setFixedHeight(40)
		self.label_common_title.setObjectName('Title_label')
		self.vbox_main.addWidget(self.label_common_title)
		#flow_box_common
		self.flow_box_common = flowbox.Window()
		self.vbox_main.addWidget(self.flow_box_common)
		#set_items
		for item in self.COMMON_SYMPTOMES:
			text, icon = item
			self.label = My_label()
			self.label.set_info(text, icon)
			self.flow_box_common.flowLayout.addWidget(self.label)
	#label_uncommon_title
		self.label_uncommon_title = QLabel()
		self.label_uncommon_title.setText(self.tr('Uncommon symptoms'))
		self.label_uncommon_title.setFixedHeight(40)
		self.label_uncommon_title.setObjectName('Title_label')
		self.vbox_main.addWidget(self.label_uncommon_title)
		#flow_box_uncommon
		self.flow_box_uncommon = flowbox.Window()
		self.vbox_main.addWidget(self.flow_box_uncommon)
		#set_items
		for item in self.UNCOMMON_SYMPTOMES:
			text, icon = item
			self.label = My_label()
			self.label.set_info(text, icon)
			self.flow_box_uncommon.flowLayout.addWidget(self.label)
			
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
		self.label_icon.setFixedSize(150, 150)
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
