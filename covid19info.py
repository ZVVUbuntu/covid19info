"""Covid19 info main module""" 
import sys
import os
from PyQt5.QtWidgets import QApplication, QFrame, QLabel, QVBoxLayout, QHBoxLayout, QTabWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QTranslator, QLocale
from modules import stats_widget, symptomes, protect_yourself


class Covid19_info(QFrame):
	"""Covid19 info class"""
	def __init__(self):
		super().__init__()
		self.create_widgets()
		
	def create_widgets(self):
		"""Create widgets"""
	#vbox_main
		self.vbox_main = QVBoxLayout()
		self.setLayout(self.vbox_main)
	#TABBER
		self.TABBER = QTabWidget()
		self.vbox_main.addWidget(self.TABBER)
		#stats_tab
		self.stats_tab = stats_widget.Stats_widget()
		self.TABBER.addTab(self.stats_tab, 'Stats')
		#symptomes_tab
		self.symptomes_tab = symptomes.Symptomes()
		self.TABBER.addTab(self.symptomes_tab, 'Symptoms')
		#protect_tab
		self.protect_tab = protect_yourself.Protect_yourself()
		self.TABBER.addTab(self.protect_tab, 'Protect')
	###
		self.setWindowIcon(QIcon('./icons/app_icon.jpg'))
		self.setWindowTitle('Covid19 info')
		self.showMaximized()
		self.show()
		
##############################################################

def get_lang_file(lang):
	lang_file = ''
	if lang == 'system':
		system_lang = QLocale.system().name()
		if 'ru' in system_lang: lang_file = './langs/ru.qm'
		if 'uk' in system_lang: lang_file = './langs/ua.qm'
	return lang_file

APP = QApplication(sys.argv)
file_css = os.path.join(os.getcwd(), 'styles', 'main.css')
if os.path.exists(file_css):
	with open(file_css, 'r') as file_open:
		data = file_open.read()
		APP.setStyleSheet(data)
lang = get_lang_file('system')
if os.path.exists(lang):
	TRANSLATOR = QTranslator()
	TRANSLATOR.load(lang)
	APP.installTranslator(TRANSLATOR)
WIN = Covid19_info()
APP.exec_()
