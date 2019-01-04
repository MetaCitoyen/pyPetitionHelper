import wx


class myCheckBox(wx.CheckBox):
    def AcceptsFocusFromKeyboard(self):
        return False
