#!/usr/bin/env python3

import sys
import os
import time
import threading
import subprocess
import webbrowser
import signal
from PySide6.QtWidgets import QApplication, QMessageBox, QFileDialog

from gui import MainWindow, AboutDialog
from about_ui import DialogAbout
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
        except OSError:
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
            
        try:
            if os.name == 'nt':
                filename = "RunIfExists.bat"
                filter_str = "Batch files (*.bat)"
            else:
                filename = "RunIfExists.sh"
                filter_str = "Shell scripts (*.sh)"
            
            file_path, _ = QFileDialog.getSaveFileName(
                self, "Save desktop link", 
                os.path.join(os.path.expanduser('~'), filename),
                filter_str
            )
            
            if not file_path:
                return
            
            with open(file_path, 'w') as f:
                if os.name == 'nt':
                    f.write(f'{sys.executable} "{self.run_file_path}" "{self.start_file_path}"\n')
                else:
                    f.write('#!/bin/bash\n')
                    f.write(f'{sys.executable} "{self.run_file_path}" "{self.start_file_path}"\n')
                    
            if os.name != 'nt':
                os.chmod(file_path, 0o755)
            
            QMessageBox.information(self, "Desktop link", f"Script created: {file_path}")
        except (OSError, PermissionError) as e:
            QMessageBox.critical(self, "Error", f"Failed to create script: {str(e)}")

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
        dlg = DialogAbout(self)
        dlg.exec()

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("RunIfExists")
    
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    
    window = RunIfExistsApp()
    window.show()
    
    sys.exit(app.exec())

if __name__ == '__main__':
    main()