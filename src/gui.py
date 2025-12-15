from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                               QGridLayout, QLabel, QPushButton, QFileDialog, 
                               QMessageBox, QDialog, QDialogButtonBox)
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
import os
import icons

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RunIfExists")
        self.setFixedSize(738, 210)
        self.setWindowIcon(icons.get_icon('directions_run_48dp_8B1A10_FILL0_wght400_GRAD0_opsz48'))
        
        self.init_ui()
        self.run_file_path = ""
        self.start_file_path = ""
        
    def init_ui(self):
        self.create_menu_bar()
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout(central_widget)
        content_widget = QWidget()
        main_layout.addWidget(content_widget)
        
        grid_layout = QGridLayout(content_widget)
        
        header_label = QLabel("Select the file to run,...")
        header_label.setStyleSheet("font-weight: bold;")
        grid_layout.addWidget(QWidget(), 0, 0)
        grid_layout.addWidget(header_label, 0, 1)
        
        run_label = QLabel("Run:")
        self.run_file_button = QPushButton("Select a file")
        self.run_file_button.clicked.connect(self.select_run_file)
        grid_layout.addWidget(run_label, 1, 0)
        grid_layout.addWidget(self.run_file_button, 1, 1)
        
        header_label2 = QLabel("...if the following file exists.")
        header_label2.setStyleSheet("font-weight: bold;")
        grid_layout.addWidget(QWidget(), 2, 0)
        grid_layout.addWidget(header_label2, 2, 1)
        
        start_label = QLabel("Startfile:")
        self.start_file_button = QPushButton("Select a file")
        self.start_file_button.clicked.connect(self.select_start_file)
        grid_layout.addWidget(start_label, 3, 0)
        grid_layout.addWidget(self.start_file_button, 3, 1)
        
        button_layout = QHBoxLayout()
        self.create_startfile_btn = QPushButton("Create Startfile")
        self.activate_btn = QPushButton("Activate")
        self.create_link_btn = QPushButton("Create Link on Desktop")
        
        self.create_startfile_btn.clicked.connect(self.create_startfile)
        self.activate_btn.clicked.connect(self.activate)
        self.create_link_btn.clicked.connect(self.create_desktop_link)
        
        button_layout.addWidget(self.create_startfile_btn)
        button_layout.addWidget(self.activate_btn)
        button_layout.addWidget(self.create_link_btn)
        
        button_widget = QWidget()
        button_widget.setLayout(button_layout)
        grid_layout.addWidget(QWidget(), 4, 0)
        grid_layout.addWidget(button_widget, 4, 1)
        
        grid_layout.setColumnStretch(1, 1)
        
    def create_menu_bar(self):
        menubar = self.menuBar()
        
        file_menu = menubar.addMenu("File")
        close_action = QAction(icons.get_icon('logout_24dp_8B1A10_FILL0_wght400_GRAD0_opsz24'), "Close", self)
        close_action.triggered.connect(self.close)
        file_menu.addAction(close_action)
        
        help_menu = menubar.addMenu("Help")
        
        support_action = QAction(icons.get_icon('globe_24dp_8B1A10_FILL0_wght400_GRAD0_opsz24'), "Support...", self)
        support_action.triggered.connect(self.show_support)
        help_menu.addAction(support_action)
        
        update_action = QAction(icons.get_icon('update_24dp_8B1A10_FILL0_wght400_GRAD0_opsz24'), "Check for updates", self)
        update_action.triggered.connect(self.check_updates)
        help_menu.addAction(update_action)
        
        about_action = QAction(icons.get_icon('info_24dp_8B1A10_FILL0_wght400_GRAD0_opsz24'), "About...", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)
        
    def select_run_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select a file", "", "All Files (*.*)")
        if file_path:
            self.run_file_path = file_path
            self.run_file_button.setText(os.path.basename(file_path))
            
    def select_start_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select a file", "", "All Files (*.*)")
        if file_path:
            self.start_file_path = file_path
            self.start_file_button.setText(os.path.basename(file_path))
    
    def create_startfile(self):
        if not self.start_file_path:
            QMessageBox.warning(self, "Warning", "Please select a start file first.")
            return
            
        if os.path.exists(self.start_file_path):
            QMessageBox.information(self, "File exists", "File already exists.")
        else:
            with open(self.start_file_path, 'w') as f:
                f.write('')
            QMessageBox.information(self, "File created", "File created.")
    
    def activate(self):
        pass
    
    def create_desktop_link(self):
        pass
    
    def show_support(self):
        pass
    
    def check_updates(self):
        pass
    
    def show_about(self):
        pass


class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("About RunIfExists")
        self.setWindowIcon(icons.get_icon('info_24dp_8B1A10_FILL0_wght400_GRAD0_opsz24'))
        self.setModal(True)
        
        layout = QVBoxLayout(self)
        
        self.logo_label = QLabel()
        layout.addWidget(self.logo_label)
        
        self.name_label = QLabel("RunIfExists")
        layout.addWidget(self.name_label)
        
        self.license_label = QLabel("Licensed under GPL-3.0")
        layout.addWidget(self.license_label)
        
        self.github_label = QLabel('<a href="https://github.com/dseichter/RunIfExists">More on GitHub</a>')
        self.github_label.setOpenExternalLinks(True)
        layout.addWidget(self.github_label)
        
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)