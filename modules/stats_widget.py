"""Stats module"""
import urllib.parse
import urllib.request
from urllib.request import Request, urlopen, FancyURLopener
from PyQt5.QtWidgets import (QFrame, QLabel, QVBoxLayout, QHBoxLayout, 
							 QTableWidget, QTableWidgetItem, QAbstractItemView, 
							 QHeaderView, QTableView, QLineEdit)
from PyQt5.QtGui import QIcon, QColor, QFont, QStandardItem, QStandardItemModel
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QSize, QThread, QCoreApplication, QSortFilterProxyModel
from . import zbutton


class Stats_widget(QFrame):
	"""Stats widget class"""
	def __init__(self):
		super().__init__()
		self.create_widgets()
		
	def create_widgets(self):
		"""Create widgets"""
		self.MAIN_URL = 'https://www.worldometers.info/coronavirus/'
		self.PARSER = 'html.parser'
		self.TABLE_HEADERS = (self.tr('Country'), self.tr('Total cases'), self.tr('New cases'), 
						self.tr('Total deaths'), self.tr('New deaths'), self.tr('Total recovered'), 
						self.tr('Active cases'), self.tr('Serious, critical'), self.tr('Total cases per 1M'),
						self.tr('Total deaths per 1M'), )
	#vbox_main
		self.vbox_main = QVBoxLayout()
		self.setLayout(self.vbox_main)
	#hbox_tools
		self.hbox_tools = QHBoxLayout()
		self.vbox_main.addLayout(self.hbox_tools)
		#
		self.hbox_tools.addStretch()
		#line_filter
		self.line_filter = QLineEdit()
		self.line_filter.addAction(QIcon('./icons/filter_icon.png'), QLineEdit.LeadingPosition)
		self.line_filter.setFixedSize(300, 40)
		self.line_filter.setPlaceholderText('Country')
		self.line_filter.textChanged.connect(self.press_search)
		self.hbox_tools.addWidget(self.line_filter)
		#
		self.hbox_tools.addStretch()
		#button_reload_info
		self.button_reload_info = zbutton.Zbutton()
		self.button_reload_info.set_info(icon='./icons/refresh_icon.png', tool_tip=self.tr('Refresh info'))
		self.button_reload_info.clicked.connect(self.press_refresh_button)
		self.hbox_tools.addWidget(self.button_reload_info)
	#model
		self.model = QStandardItemModel()
		self.model.setHorizontalHeaderLabels(self.TABLE_HEADERS)
		#sort_model
		self.sort_model = QSortFilterProxyModel()
		self.sort_model.setSourceModel(self.model)
		self.sort_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
		self.sort_model.setFilterKeyColumn(0)
	#table_view
		self.table_view = QTableView()
		self.table_view.setModel(self.sort_model)
		self.table_view.setSelectionBehavior(QAbstractItemView.SelectRows)
		self.table_view.setSelectionMode(QAbstractItemView.SingleSelection)
		self.table_view.sortByColumn(1, Qt.DescendingOrder)
		self.table_view.verticalHeader().hide()
		self.table_view.setShowGrid(True)
		self.table_view.setIconSize(QSize(32, 32))
		self.table_view.setFocusPolicy(Qt.NoFocus)
		self.table_view.setObjectName('Main_table')
		self.vbox_main.addWidget(self.table_view)
		for i in range(0, 10):
			self.table_view.horizontalHeader().setSectionResizeMode(i, QHeaderView.Stretch)
		
		#thread
		self.my_thread = MyThread()
		self.my_thread.notifyProgress.connect(self.update_progress)
		self.my_thread.start()
###############################################################################

	def press_refresh_button(self):
		"""Press refresh button"""
		self.model.removeRows(0, self.model.rowCount())
		if not self.my_thread.isRunning():
			self.my_thread.start()

	def update_progress(self, soup):
		#soup = BS(webpage, self.PARSER)
		try:
			table_today = soup.find('table', attrs={'id':'main_table_countries_today'})
			total_row = table_today.find('tr', attrs={'class':'total_row'})
			total_items = total_row.find_all('td')
			self.add_row(total_items, 'headers')
			all_rows = table_today.tbody.find_all('tr')
			for r in all_rows:
				items = r.find_all('td')
				self.add_row(items)
		except:
			pass

	def add_row(self, items, row_type='row'):
		"""Add one row"""
		items = items[:-1]
		list_items = []
		for item in items:
			index = items.index(item)
			data = item.text
			if index == 1: data = int(data.replace(',', ''))
			self.item = MyItem()
			if row_type == 'headers': self.item.set_total_info(data)
			else: self.item.set_info(data, index)
			list_items.append(self.item)
		self.model.appendRow(list_items)
		
	def press_search(self, text):
		"""Press search"""
		self.sort_model.setFilterRegExp(text)
		
############################################################################################################

class MyItem(QStandardItem):
	"""My Item class"""
	def __init__(self):
		super().__init__()
		self.setFlags(Qt.ItemIsEnabled)
		
	def set_info(self, data, index):
		"""set info"""
		if index == 2 and data:
			font = self.font()
			font.setBold(True)
			self.setBackground(QColor('lightyellow'))
			self.setFont(font)
		if index == 4 and data:
			font = self.font()
			font.setBold(True)
			self.setForeground(QColor('white'))
			self.setBackground(QColor('red'))
			self.setFont(font)
		self.setData(data, Qt.EditRole)
		
	def set_total_info(self, data):
		"""Set total info"""
		font = self.font()
		font.setBold(True)
		self.setFont(font)
		self.setBackground(QColor('#d6eeff'))
		self.setData(data, Qt.EditRole)

############################################################################################################

class MyThread(QThread):
	"""MyThread class"""
	#notifyProgress = QtCore.pyqtSignal(bytes)
	notifyProgress = QtCore.pyqtSignal(object)
	def __init__(self):
		super().__init__()
		self.MAIN_URL = 'https://www.worldometers.info/coronavirus/'
		self.PARSER = 'html.parser'

	def run(self):
		try:
			import bs4
			from bs4 import BeautifulSoup
			myopener = MyOpener()
			webpage = myopener.open(self.MAIN_URL)
			self.soup = BeautifulSoup(webpage, self.PARSER)
			#self.notifyProgress.emit(webpage.read())
			self.notifyProgress.emit(self.soup)
		except:
			pass

############################################################################################################

class MyOpener(FancyURLopener):
	version = ('Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36 OPR/53.0.2907.106')
