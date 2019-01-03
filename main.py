# -*- coding: utf-8 -*-

import wx
import winMain


if __name__ == '__main__':
    app = wx.App(False)
    win = winMain.winMain(None)
    win.Show(True)
    app.MainLoop()
