# -*- coding: utf-8 -*-

# #########################################################################
# # Python code generated with wxFormBuilder (version 4.1.0-69d57cd9)
# # http://www.wxformbuilder.org/
# #
# # PLEASE DO *NOT* EDIT THIS FILE!
# #########################################################################

import wx
import wx.xrc

ID_CLOSE = 1000
ID_GET_HELP = 1001
ID_CHECK_FOR_UPDATES = 1002
ID_ABOUT = 1003


# #########################################################################
# # Class frameMain
# #########################################################################


class frameMain(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"RunIfExists", pos=wx.DefaultPosition, size=wx.Size(738, 210), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.m_menubar1 = wx.MenuBar(0)
        self.menuitemFile = wx.Menu()
        self.menuitemFileClose = wx.MenuItem(self.menuitemFile, ID_CLOSE, u"Close", wx.EmptyString, wx.ITEM_NORMAL)
        self.menuitemFile.Append(self.menuitemFileClose)

        self.m_menubar1.Append(self.menuitemFile, u"File")

        self.menuitemHelp = wx.Menu()
        self.menuitemHelpSupport = wx.MenuItem(self.menuitemHelp, ID_GET_HELP, u"Support...", wx.EmptyString, wx.ITEM_NORMAL)
        self.menuitemHelp.Append(self.menuitemHelpSupport)

        self.menuitemHelpUpdate = wx.MenuItem(self.menuitemHelp, ID_CHECK_FOR_UPDATES, u"Check for updates", wx.EmptyString, wx.ITEM_NORMAL)
        self.menuitemHelp.Append(self.menuitemHelpUpdate)

        self.menuitemHelpAbout = wx.MenuItem(self.menuitemHelp, ID_ABOUT, u"About...", wx.EmptyString, wx.ITEM_NORMAL)
        self.menuitemHelp.Append(self.menuitemHelpAbout)

        self.m_menubar1.Append(self.menuitemHelp, u"Help")

        self.SetMenuBar(self.m_menubar1)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        fgSizer1 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer1.AddGrowableCol(1)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)


        fgSizer1.Add((0, 0), 1, wx.EXPAND, 5)
        self.m_staticText1 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Select the file to run,...", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)

        self.m_staticText1.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))

        fgSizer1.Add(self.m_staticText1, 1, wx.ALL | wx.EXPAND, 5)
        self.m_staticText2 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Run:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)

        fgSizer1.Add(self.m_staticText2, 0, wx.ALL, 5)
        self.m_filePicker1 = wx.FilePickerCtrl(self.m_panel1, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE)
        fgSizer1.Add(self.m_filePicker1, 1, wx.ALL | wx.EXPAND, 5)

        fgSizer1.Add((0, 0), 1, wx.EXPAND, 5)
        self.m_staticText3 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"...if the following file exists.", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)

        self.m_staticText3.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))

        fgSizer1.Add(self.m_staticText3, 1, wx.ALL | wx.EXPAND, 5)
        self.m_staticText4 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Startfile:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)

        fgSizer1.Add(self.m_staticText4, 0, wx.ALL, 5)
        self.m_filePicker2 = wx.FilePickerCtrl(self.m_panel1, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE)
        fgSizer1.Add(self.m_filePicker2, 1, wx.ALL | wx.EXPAND, 5)

        fgSizer1.Add((0, 0), 1, wx.EXPAND, 5)
        fgSizer2 = wx.FlexGridSizer(0, 3, 0, 0)
        fgSizer2.SetFlexibleDirection(wx.BOTH)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.buttonCreateStartfile = wx.Button(self.m_panel1, wx.ID_ANY, u"Create Startfile", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer2.Add(self.buttonCreateStartfile, 0, wx.ALL, 5)
        self.buttonActivate = wx.Button(self.m_panel1, wx.ID_ANY, u"Activate", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer2.Add(self.buttonActivate, 0, wx.ALL, 5)
        self.buttonCreateLink = wx.Button(self.m_panel1, wx.ID_ANY, u"Create Link on Desktop", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer2.Add(self.buttonCreateLink, 0, wx.ALL, 5)
        fgSizer1.Add(fgSizer2, 1, wx.EXPAND, 5)
        self.m_panel1.SetSizer(fgSizer1)
        self.m_panel1.Layout()
        fgSizer1.Fit(self.m_panel1)
        bSizer2.Add(self.m_panel1, 1, wx.EXPAND | wx.ALL, 5)
        self.SetSizer(bSizer2)
        self.Layout()
        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_SHOW, self.onShow)
        self.Bind(wx.EVT_MENU, self.miFileClose, id=self.menuitemFileClose.GetId())
        self.Bind(wx.EVT_MENU, self.miHelpSupport, id=self.menuitemHelpSupport.GetId())
        self.Bind(wx.EVT_MENU, self.miHelpUpdate, id=self.menuitemHelpUpdate.GetId())
        self.Bind(wx.EVT_MENU, self.miHelpAbout, id=self.menuitemHelpAbout.GetId())
        self.buttonCreateStartfile.Bind(wx.EVT_BUTTON, self.createStartfile)
        self.buttonActivate.Bind(wx.EVT_BUTTON, self.activate)
        self.buttonCreateLink.Bind(wx.EVT_BUTTON, self.createDesktopLink)

    def __del__(self):
        pass
    # Virtual event handlers, override them in your derived class

    def onShow(self, event):
        event.Skip()

    def miFileClose(self, event):
        event.Skip()

    def miHelpSupport(self, event):
        event.Skip()

    def miHelpUpdate(self, event):
        event.Skip()

    def miHelpAbout(self, event):
        event.Skip()

    def createStartfile(self, event):
        event.Skip()

    def activate(self, event):
        event.Skip()

    def createDesktopLink(self, event):
        event.Skip()

# #########################################################################
# # Class dialogAbout
# #########################################################################


class dialogAbout(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"About RunIfExists", pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.bitmapLogo = wx.StaticBitmap(self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.bitmapLogo, 0, wx.ALL, 5)
        self.staticTextName = wx.StaticText(self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticTextName.Wrap(-1)

        bSizer2.Add(self.staticTextName, 0, wx.ALL, 5)
        self.staticTextLicence = wx.StaticText(self, wx.ID_ANY, u"Licenced under", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticTextLicence.Wrap(-1)

        bSizer2.Add(self.staticTextLicence, 0, wx.ALL, 5)
        self.staticTextGithub = wx.StaticText(self, wx.ID_ANY, u"More on GitHub", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticTextGithub.Wrap(-1)

        self.staticTextGithub.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, wx.EmptyString))
        self.staticTextGithub.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        bSizer2.Add(self.staticTextGithub, 0, wx.ALL, 5)
        self.staticTextIcon8 = wx.StaticText(self, wx.ID_ANY, u"Icons by Icons8.com", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticTextIcon8.Wrap(-1)

        self.staticTextIcon8.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_GRAYTEXT))

        bSizer2.Add(self.staticTextIcon8, 0, wx.ALL, 5)
        m_sdbSizer2 = wx.StdDialogButtonSizer()
        self.m_sdbSizer2OK = wx.Button(self, wx.ID_OK)
        m_sdbSizer2.AddButton(self.m_sdbSizer2OK)
        self.m_sdbSizer2Cancel = wx.Button(self, wx.ID_CANCEL)
        m_sdbSizer2.AddButton(self.m_sdbSizer2Cancel)
        m_sdbSizer2.Realize()
        bSizer2.Add(m_sdbSizer2, 1, wx.EXPAND, 5)
        self.SetSizer(bSizer2)
        self.Layout()
        bSizer2.Fit(self)
        self.Centre(wx.BOTH)

        # Connect Events
        self.staticTextGithub.Bind(wx.EVT_LEFT_DOWN, self.openGithub)
        self.staticTextIcon8.Bind(wx.EVT_LEFT_DOWN, self.openIcons8)

    def __del__(self):
        pass
    # Virtual event handlers, override them in your derived class

    def openGithub(self, event):
        event.Skip()

    def openIcons8(self, event):
        event.Skip()
