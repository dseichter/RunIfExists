# Copyright (c) 2024 Daniel Seichter
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

# importing wx files
import wx
# import the newly created GUI file
import gui
# import common libraries
import webbrowser
import subprocess
import os
import sys
import time
import threading
# import workdir specific libraries
import about_ui
import helper
import icons


class WatcherThread(threading.Thread):
    def __init__(self, parent, startfile, runfile):
        threading.Thread.__init__(self)
        self._parent = parent
        self._startfile = startfile
        self._runfile = runfile

    def run(self):
        # global variable to check if the program is active
        active = True
        while not os.path.exists(self._startfile) and active is True:
            time.sleep(1)

        active = False
        env = os.environ.copy()
        subprocess.Popen(self._runfile, env=env)


class RunIfExistsFrame(gui.frameMain):
    # constructor
    def __init__(self, parent):
        # initialize parent class
        gui.frameMain.__init__(self, parent)

        # specify all the icons
        gui.frameMain.SetIcon(self, icons.track_and_field.GetIcon())
        self.menuitemFileClose.SetBitmap(icons.cancel.GetBitmap().ConvertToImage().Rescale(16, 16).ConvertToBitmap())
        self.menuitemHelpSupport.SetBitmap(icons.get_help.GetBitmap().ConvertToImage().Rescale(16, 16).ConvertToBitmap())
        self.menuitemHelpUpdate.SetBitmap(icons.restart.GetBitmap().ConvertToImage().Rescale(16, 16).ConvertToBitmap())
        self.menuitemHelpAbout.SetBitmap(icons.info.GetBitmap().ConvertToImage().Rescale(16, 16).ConvertToBitmap())

    def onShow(self, event):
        # add the version to the label
        self.SetTitle(helper.NAME + ' ' + helper.VERSION)

        self.Layout()
        self.Fit()

    def createStartfile(self, event):
        if self.filepickerStartfile.GetPath() != '':
            if os.path.exists(self.filepickerStartfile.GetPath()):
                wx.MessageBox('File already exists.', 'File exists', wx.OK | wx.ICON_INFORMATION)
            else:
                with open(self.filepickerStartfile.GetPath(), 'w') as f:
                    f.write('')
                wx.MessageBox('File created.', 'File created', wx.OK | wx.ICON_INFORMATION)

    def activate(self, event):
        worker = WatcherThread(self, self.filepickerStartfile.GetPath(), self.filepickerRun.GetPath())
        worker.start()
        wx.MessageBox('Watcher started.', 'Watcher started', wx.OK | wx.ICON_INFORMATION)

    def createDesktopLink(self, event):
        # create a batch file to start the program
        if os.name == 'nt':
            # Windows
            desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
            shellscript = os.path.join(desktop, 'RunIfExists.bat')
            with open(shellscript, 'w') as f:
                f.write(sys.executable + ' "' + self.filepickerRun.GetPath() + '" "' + self.filepickerStartfile.GetPath() + '"' + '\n')
        else:
            # Linux
            desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
            shellscript = os.path.join(desktop, 'RunIfExists.sh')
            with open(shellscript, 'w') as f:
                f.write('#!/bin/bash\n')
                f.write(sys.executable + ' "' + self.filepickerRun.GetPath() + '" "' + self.filepickerStartfile.GetPath() + '"' + '\n')
        wx.MessageBox('Desktop file created.', 'Desktop link', wx.OK | wx.ICON_INFORMATION)

    def miFileClose(self, event):
        self.Close()

    def miHelpSupport(self, event):
        webbrowser.open_new_tab('https://github.com/dseichter/RunIfExists')  # Add the URL of the GitHub repository

    def miHelpUpdate(self, event):
        if helper.check_for_new_release():
            result = wx.MessageBox('A new release is available.\nWould you like to open the download page?', 'Update available', wx.YES_NO | wx.ICON_INFORMATION)
            if result == wx.YES:
                webbrowser.open_new_tab(helper.RELEASES)
        else:
            wx.MessageBox('No new release available.', 'No update', wx.OK | wx.ICON_INFORMATION)

    def miHelpAbout(self, event):
        # open the about dialog
        dlg = about_ui.DialogAbout(self)
        dlg.ShowModal()
        dlg.Destroy()


# mandatory in wx, create an app, False stands for not deteriction stdin/stdout
# refer manual for details
app = wx.App(False)

# create an object of CalcFrame
frame = RunIfExistsFrame(None)

# show the frame
frame.Show(True)

# start the applications
app.MainLoop()
