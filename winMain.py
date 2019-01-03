# -*- coding: utf-8 -*-
import wx
import screens
import firstnames
import lastnames
import towns
import towncodes


class winMain(screens.winMain):
    def __init__(self, parent):
        screens.winMain.__init__(self, parent)
        self.m_LastName.AutoComplete(lastnames.lastnames)
        self.m_FirstName.AutoComplete(firstnames.firstnames)
        self.m_Town.AutoComplete(towns.towns)
        self.m_TownCode.AutoComplete(towncodes.towncodes)
        self.m_MailServer.AutoComplete(["orange.fr", "free.fr", "live.fr", "gmail.com", "outlook.fr",
        "hotmail.fr", "hotmail.com", "sfr.fr", "wanadoo.fr", "laposte.net", "libertysurf.fr",
        "yahoo.fr", "bbox.fr"])
        self.m_List.InsertColumn(0, u"Nom")
        self.m_List.InsertColumn(1, u"Prénom")
        self.m_List.InsertColumn(2, u"Code postale")
        self.m_List.InsertColumn(3, u"mail")
        self.m_List.InsertColumn(4, u"Téléphone")

    def error(self, title, msg):
        dlg = wx.MessageDialog(self,
                               msg,
                               title,
                               wx.OK | wx.ICON_ERROR
                               )
        dlg.ShowModal()
        dlg.Destroy()

    def onValidate( self, event ):
        self.m_LastName.SetValue(self.m_LastName.GetValue().upper().strip())
        self.m_FirstName.SetValue(self.m_FirstName.GetValue().lower().strip())
        phone = self.m_Phone.GetValue().strip()
        if phone != "":
            if len(phone) != 10:
                self.error("Problème sur le téléphone", "Il doit faire 10 caractères")
                return
            if phone[0] != "0":
                self.error("Problème sur le téléphone", "Il doit commencer par 0")
                return
            if not phone.isnumeric():
                self.error("Problème sur le téléphone", "Il doit être numérique")
                return
        town = self.m_Town.GetValue()
        if town == "":
            town = self.m_TownCode.GetValue()
        mail = "%s@%s" % (self.m_Mail.GetValue(), self.m_MailServer.GetValue())
        if mail == "@":
            mail = ""
        index = self.m_List.InsertItem(0, self.m_LastName.GetValue())
        self.m_List.SetItem(index, 1, self.m_FirstName.GetValue())
        self.m_List.SetItem(index, 2, town)
        self.m_List.SetItem(index, 3, mail)
        self.m_List.SetItem(index, 4, self.m_Phone.GetValue())
        f = open(self.m_Ref.GetValue(), "a+t")
        f.write('"%s";"%s";"%s";"%s";"%s";"%s";"%s"\n' % (
                self.m_Page.GetValue(),
                self.m_Line.GetValue(),
                self.m_LastName.GetValue(),
                self.m_FirstName.GetValue(),
                mail,
                town,
                self.m_Phone.GetValue()))
        f.close()
        self.m_FirstName.Clear()
        self.m_LastName.Clear()
        self.m_TownCode.Clear()
        self.m_Town.Clear()
        self.m_Phone.Clear()
        self.m_Mail.Clear()
        self.m_MailServer.Clear()
        self.m_Line.SetValue(str(int(self.m_Line.GetValue())+1))
        self.m_LastName.SetFocus()

    def onQuit(self, event):
        self.Close()
