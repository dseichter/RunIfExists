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
ID_ABOUT = 1001


# #########################################################################
# # Class frameMain
# #########################################################################


class frameMain(wx.Frame):

	def __init__(self, parent):
		wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"RunIfExists", pos=wx.DefaultPosition, size=wx.Size(738, 210), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

		self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

		fgSizer1 = wx.FlexGridSizer(0, 2, 0, 0)
		fgSizer1.AddGrowableCol(1)
		fgSizer1.SetFlexibleDirection(wx.BOTH)
		fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)


		fgSizer1.Add((0, 0), 1, wx.EXPAND, 5)
		self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"Select the file to run,...", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText1.Wrap(-1)

		self.m_staticText1.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))

		fgSizer1.Add(self.m_staticText1, 1, wx.ALL | wx.EXPAND, 5)
		self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, u"Run:", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText2.Wrap(-1)

		fgSizer1.Add(self.m_staticText2, 0, wx.ALL, 5)
		self.m_filePicker1 = wx.FilePickerCtrl(self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE)
		fgSizer1.Add(self.m_filePicker1, 1, wx.ALL | wx.EXPAND, 5)

		fgSizer1.Add((0, 0), 1, wx.EXPAND, 5)
		self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, u"...if the following file exists.", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText3.Wrap(-1)

		self.m_staticText3.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))

		fgSizer1.Add(self.m_staticText3, 1, wx.ALL | wx.EXPAND, 5)
		self.m_staticText4 = wx.StaticText(self, wx.ID_ANY, u"Startfile:", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText4.Wrap(-1)

		fgSizer1.Add(self.m_staticText4, 0, wx.ALL, 5)
		self.m_filePicker2 = wx.FilePickerCtrl(self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE)
		fgSizer1.Add(self.m_filePicker2, 1, wx.ALL | wx.EXPAND, 5)

		fgSizer1.Add((0, 0), 1, wx.EXPAND, 5)
		fgSizer2 = wx.FlexGridSizer(0, 3, 0, 0)
		fgSizer2.SetFlexibleDirection(wx.BOTH)
		fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

		self.buttonCreateStartfile = wx.Button(self, wx.ID_ANY, u"Create Startfile", wx.DefaultPosition, wx.DefaultSize, 0)
		fgSizer2.Add(self.buttonCreateStartfile, 0, wx.ALL, 5)
		self.buttonActivate = wx.Button(self, wx.ID_ANY, u"Activate", wx.DefaultPosition, wx.DefaultSize, 0)
		fgSizer2.Add(self.buttonActivate, 0, wx.ALL, 5)
		self.buttonCreateLink = wx.Button(self, wx.ID_ANY, u"Create Link on Desktop", wx.DefaultPosition, wx.DefaultSize, 0)
		fgSizer2.Add(self.buttonCreateLink, 0, wx.ALL, 5)
		fgSizer1.Add(fgSizer2, 1, wx.EXPAND, 5)
		self.SetSizer(fgSizer1)
		self.Layout()
		self.m_menubar1 = wx.MenuBar(0)
		self.menuitemFile = wx.Menu()
		self.menuitemFileClose = wx.MenuItem(self.menuitemFile, ID_CLOSE, u"Close", wx.EmptyString, wx.ITEM_NORMAL)
		self.menuitemFile.Append(self.menuitemFileClose)

		self.m_menubar1.Append(self.menuitemFile, u"File")

		self.menuitemHelp = wx.Menu()
		self.menuitemHelpAbout = wx.MenuItem(self.menuitemHelp, ID_ABOUT, u"About", wx.EmptyString, wx.ITEM_NORMAL)
		self.menuitemHelp.Append(self.menuitemHelpAbout)

		self.m_menubar1.Append(self.menuitemHelp, u"Help")

		self.SetMenuBar(self.m_menubar1)

		self.Centre(wx.BOTH)

		# Connect Events
		self.Bind(wx.EVT_SHOW, self.onShow)
		self.buttonCreateStartfile.Bind(wx.EVT_BUTTON, self.createStartfile)
		self.buttonActivate.Bind(wx.EVT_BUTTON, self.activate)
		self.buttonCreateLink.Bind(wx.EVT_BUTTON, self.createDesktopLink)
		self.Bind(wx.EVT_MENU, self.menuitemFileClose, id=self.menuitemFileClose.GetId())
		self.Bind(wx.EVT_MENU, self.menuitemHelpAbout, id=self.menuitemHelpAbout.GetId())

	def __del__(self):
		pass
	# Virtual event handlers, override them in your derived class

	def onShow(self, event):
		event.Skip()

	def createStartfile(self, event):
		event.Skip()

	def activate(self, event):
		event.Skip()

	def createDesktopLink(self, event):
		event.Skip()

	def menuitemFileClose(self, event):
		event.Skip()

	def menuitemHelpAbout(self, event):
		event.Skip()
