# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class winMain
###########################################################################

class winMain ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Petition Helper", pos = wx.DefaultPosition, size = wx.Size( 468,488 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Nom", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.m_LastName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_LastName, 1, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Prénom", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer3.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		self.m_FirstName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_FirstName, 1, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer3, 0, wx.EXPAND, 5 )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Code postale", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer4.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		self.m_TownCode = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_TownCode.SetMaxLength( 5 ) 
		bSizer4.Add( self.m_TownCode, 1, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer4, 0, wx.EXPAND, 5 )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Commune", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		bSizer5.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		self.m_Town = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_Town, 1, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer5, 0, wx.EXPAND, 5 )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Mail", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		bSizer6.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		self.m_Mail = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_Mail, 2, wx.ALL, 5 )
		
		self.m_staticText24 = wx.StaticText( self, wx.ID_ANY, u"@", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )
		bSizer6.Add( self.m_staticText24, 0, wx.ALL, 5 )
		
		self.m_MailServer = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_MailServer, 1, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer6, 0, wx.EXPAND, 5 )
		
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Phone", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		bSizer7.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		self.m_Phone = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_Phone.SetMaxLength( 10 ) 
		bSizer7.Add( self.m_Phone, 1, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer7, 0, wx.EXPAND, 5 )
		
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Ref", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		bSizer8.Add( self.m_staticText7, 0, wx.ALL, 5 )
		
		self.m_Ref = wx.TextCtrl( self, wx.ID_ANY, u"PetitionHelper.csv", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_Ref, 1, wx.ALL, 5 )
		
		self.m_Page = wx.TextCtrl( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_Page, 0, wx.ALL, 5 )
		
		self.m_Line = wx.TextCtrl( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_Line, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer8, 0, wx.EXPAND, 5 )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Enregistrer", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_button1, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_List = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
		bSizer1.Add( self.m_List, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.onValidate )
		self.m_List.Bind( wx.EVT_LEFT_UP, self.onLeftUpTab )
		self.m_List.Bind( wx.EVT_RIGHT_DOWN, self.onRightDownTab )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onValidate( self, event ):
		event.Skip()
	
	def onLeftUpTab( self, event ):
		event.Skip()
	
	def onRightDownTab( self, event ):
		event.Skip()
	

