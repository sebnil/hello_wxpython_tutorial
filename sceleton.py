__author__ = 'sebnil'

import wx
import gui

# Extend the gui with some new functionality
class MyFrame(gui.MainFrame):
    def __init__(self, parent, title):
        gui.MainFrame.__init__(self, parent)

    # this is the event we defined in wxformbuilder, and now override from gui.py
    def on_button_click_event(self, event):
        print('on_button_click_event')

# Create wxpython app
class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, "Hello Wxpython")
        self.SetTopWindow(self.frame)
        self.frame.Show(True)
        print("wxApp created.")

        return True

if __name__ == "__main__":
    app = MyApp(redirect=False) # do not redirect stdout to the gui
    app.MainLoop() # render gui continuously