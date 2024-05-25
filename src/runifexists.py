# importing wx files
import wx
# import the newly created GUI file
import gui
# import common libraries
import webbrowser
import subprocess
import os
# import workdir specific libraries
import about_ui
import helper
import icons


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
        event.Skip()

    def activate(self, event):
        event.Skip()

    def createDesktopLink(self, event):
        event.Skip()

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
        dlg = about_ui.dialogAbout(self)
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
