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
        "yahoo.fr", "bbox.fr", "club-internet.fr"])
        self.m_List.InsertColumn(0, u"Nom")
        self.m_List.InsertColumn(1, u"Prénom")
        self.m_List.InsertColumn(2, u"mail")
        self.m_List.InsertColumn(3, u"Code postale")
        self.m_List.InsertColumn(4, u"Téléphone")

    def onToggleMail( self, event ):
        self.m_Mail.Enable(not self.m_Mail.IsEnabled())
        self.m_MailServer.Enable(self.m_Mail.IsEnabled())
        self.m_Mail.SetValue("")
        self.m_MailServer.SetValue("")

    def onTogglePhone( self, event ):
        self.m_Phone.Enable(not self.m_Phone.IsEnabled())
        self.m_Phone.SetValue("")

    def onToggleTown( self, event ):
        self.m_Town.Enable(not self.m_Town.IsEnabled())
        self.m_Town.SetValue("")

    def onToggleTownCode( self, event ):
        self.m_TownCode.Enable(not self.m_TownCode.IsEnabled())

    def error(self, title, msg):
        dlg = wx.MessageDialog(self,
                               msg,
                               title,
                               wx.OK | wx.ICON_ERROR
                               )
        dlg.ShowModal()
        dlg.Destroy()

    def onValidate(self, event):
        self.AddOrUpdateItem()


    def onLeftUpTab(self, event):
        for i in range(self.m_List.GetItemCount()):
            if self.m_List.IsSelected(i):
                self.m_FirstName.SetValue(self.m_List.GetItemText(i, 0))
                self.m_LastName.SetValue(self.m_List.GetItemText(i, 1))
                mail = self.m_List.GetItemText(i, 2)
                if "@" in mail:
                    mail, mailserver = mail.split("@", 2)
                else:
                    mailserver = ""
                self.m_Mail.SetValue(mail)
                self.m_MailServer.SetValue(mailserver)
                towncodes = self.m_List.GetItemText(i, 3)
                if " " in towncodes:
                    towncodes, towns = towncodes.split(" ", 2)
                    self.m_TownCode.Clear()
                    self.m_Town.SetValue("%s %s" % (towncodes, towns))
                else:
                    self.m_TownCode.SetValue(towncodes)
                    self.m_Town.Clear()
                self.m_Phone.SetValue(self.m_List.GetItemText(i, 4))
                return

    def onRightDownTab(self, event):
        menu = wx.Menu()
        menu.Append(1, "Copier dans le presse papier")
        menu.Bind(wx.EVT_MENU, self.CopyItems, id=1)
        menu.Append(2, "Mise à jour")
        menu.Bind(wx.EVT_MENU, self.UpdateItem, id=2)
        menu.Append(3, "Effacer")
        menu.Bind(wx.EVT_MENU, self.ClearTab, id=3)
        self.PopupMenu(menu)

    def CopyItems(self, event):
        selectedItems = []
        for i in range(self.m_List.GetItemCount()):
            l = []
            for j in range(0, 5):
                l.append(self.m_List.GetItemText(i, j))
            selectedItems.append("\t".join(l))

        clipdata = wx.TextDataObject()
        clipdata.SetText("\n".join(selectedItems))
        wx.TheClipboard.Open()
        wx.TheClipboard.SetData(clipdata)
        wx.TheClipboard.Close()

    def UpdateItem(self, event):
        for i in range(self.m_List.GetItemCount()):
            if self.m_List.IsSelected(i):
                self.AddOrUpdateItem(i)
                return

    def AddOrUpdateItem(self, index=None):
        self.m_LastName.SetValue(self.m_LastName.GetValue().upper().strip())
        self.m_FirstName.SetValue(self.m_FirstName.GetValue().lower().strip())
        self.m_MailServer.SetValue(self.m_MailServer.GetValue().lower().strip())
        self.m_Mail.SetValue(self.m_Mail.GetValue().lower().strip())
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
        if index == None:
            index = self.m_List.InsertItem(0, self.m_LastName.GetValue())
        else:
            self.m_List.SetItem(index, 0, self.m_LastName.GetValue())
        self.m_List.SetItem(index, 1, self.m_FirstName.GetValue())
        self.m_List.SetItem(index, 2, mail)
        self.m_List.SetItem(index, 3, town)
        self.m_List.SetItem(index, 4, self.m_Phone.GetValue())
        f = open("PetitionHelper.log", "a+t")
        f.write('"%s";"%s";"%s";"%s";"%s";"%s";"%s";"%s"\n' % (
                self.m_Ref.GetValue(),
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

    def ClearTab(self, event):
        dlg = wx.MessageDialog(self,
                               "Confirmation",
                               "Etes-vous certain de vouloir supprimer les éléments ?",
                               wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION
                               )
        if dlg.ShowModal() == wx.ID_YES:
            self.m_List.DeleteAllItems()
        dlg.Destroy()


    def onQuit(self, event):
        self.Close()
