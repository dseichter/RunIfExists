#!/usr/bin/env python3

import sys
import os
import time
import threading
import subprocess
import webbrowser
from PySide6.QtWidgets import QApplication, QMessageBox

from gui import MainWindow, AboutDialog
import helper

class WatcherThread(threading.Thread):
    def __init__(self, parent, startfile, runfile):
        threading.Thread.__init__(self)
        self._parent = parent
        self._startfile = startfile
        self._runfile = runfile
        self.daemon = True

    def run(self):
        while not os.path.exists(self._startfile):
            time.sleep(1)
        
        env = os.environ.copy()
        subprocess.Popen(self._runfile, env=env)
        
        try:
            os.remove(self._startfile)
        except:
            pass

class RunIfExistsApp(MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(f"{helper.NAME} {helper.VERSION}")
        
    def activate(self):
        if not self.start_file_path or not self.run_file_path:
            QMessageBox.warning(self, "Warning", "Please select both run file and start file.")
            return
            
        worker = WatcherThread(self, self.start_file_path, self.run_file_path)
        worker.start()
        QMessageBox.information(self, "Watcher started", "Watcher started.")

    def create_desktop_link(self):
        if not self.start_file_path or not self.run_file_path:
            QMessageBox.warning(self, "Warning", "Please select both run file and start file.")
            return
            
        if os.name == 'nt':
            desktop = os.path.join(os.environ['USERPROFILE'], 'Desktop')
            shellscript = os.path.join(desktop, 'RunIfExists.bat')
            with open(shellscript, 'w') as f:
                f.write(f'{sys.executable} "{self.run_file_path}" "{self.start_file_path}"\n')
        else:
            desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
            shellscript = os.path.join(desktop, 'RunIfExists.sh')
            with open(shellscript, 'w') as f:
                f.write('#!/bin/bash\n')
                f.write(f'{sys.executable} "{self.run_file_path}" "{self.start_file_path}"\n')
        
        QMessageBox.information(self, "Desktop link", "Desktop file created.")

    def show_support(self):
        webbrowser.open_new_tab('https://github.com/dseichter/RunIfExists')

    def check_updates(self):
        if helper.check_for_new_release():
            reply = QMessageBox.question(self, "Update available", 
                                       "A new release is available.\nWould you like to open the download page?",
                                       QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                webbrowser.open_new_tab(helper.RELEASES)
        else:
            QMessageBox.information(self, "No update", "No new release available.")

    def show_about(self):
        dlg = AboutDialog(self)
        dlg.name_label.setText(f"{helper.NAME} {helper.VERSION}")
        dlg.license_label.setText(f"Licensed under {helper.LICENCE}")
        dlg.exec()

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("RunIfExists")
    
    window = RunIfExistsApp()
    window.show()
    
    sys.exit(app.exec())

if __name__ == '__main__':
    main()