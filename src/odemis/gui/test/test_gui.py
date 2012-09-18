# This file was automatically generated by pywxrc.
# -*- coding: UTF-8 -*-

import wx
import wx.xrc as xrc

__res = None

def get_resources():
    """ This function provides access to the XML resources in this module."""
    global __res
    if __res == None:
        __init_resources()
    return __res




class xrcstream_frame(wx.Frame):
#!XRCED:begin-block:xrcstream_frame.PreCreate
    def PreCreate(self, pre):
        """ This function is called during the class's initialization.

        Override it for custom setup before the window is created usually to
        set additional window styles using SetWindowStyle() and SetExtraStyle().
        """
        pass

#!XRCED:end-block:xrcstream_frame.PreCreate

    def __init__(self, parent):
        # Two stage creation (see http://wiki.wxpython.org/index.cgi/TwoStageCreation)
        pre = wx.PreFrame()
        self.PreCreate(pre)
        get_resources().LoadOnFrame(pre, parent, "stream_frame")
        self.PostCreate(pre)

        # Define variables for the controls, bind event handlers
        self.scrwin = xrc.XRCCTRL(self, "scrwin")
        self.fpb = xrc.XRCCTRL(self, "fpb")
        self.stream_panel = xrc.XRCCTRL(self, "stream_panel")



class xrctext_frame(wx.Frame):
#!XRCED:begin-block:xrctext_frame.PreCreate
    def PreCreate(self, pre):
        """ This function is called during the class's initialization.

        Override it for custom setup before the window is created usually to
        set additional window styles using SetWindowStyle() and SetExtraStyle().
        """
        pass

#!XRCED:end-block:xrctext_frame.PreCreate

    def __init__(self, parent):
        # Two stage creation (see http://wiki.wxpython.org/index.cgi/TwoStageCreation)
        pre = wx.PreFrame()
        self.PreCreate(pre)
        get_resources().LoadOnFrame(pre, parent, "text_frame")
        self.PostCreate(pre)

        # Define variables for the controls, bind event handlers
        self.txt_suggest = xrc.XRCCTRL(self, "txt_suggest")





# ------------------------ Resource data ----------------------

def __init_resources():
    global __res
    __res = xrc.EmptyXmlResource()

    wx.FileSystem.AddHandler(wx.MemoryFSHandler())

    test_gui_xrc = '''\
<?xml version="1.0" ?><resource version="2.5.3.0" xmlns="http://www.wxwidgets.org/wxxrc">
  <object class="wxFrame" name="stream_frame">
    <object class="wxBoxSizer">
      <orient>wxVERTICAL</orient>
      <object class="sizeritem">
        <object class="wxScrolledWindow" name="scrwin">
          <object class="wxBoxSizer">
            <orient>wxVERTICAL</orient>
            <object class="sizeritem">
              <object class="FoldPanelBar" name="fpb">
                <object class="FoldPanelItem">
                  <object class="wxPanel" name="stream_panel" subclass="odemis.gui.comp.stream.StreamPanel">
                    <fg>#7F7F7F</fg>
                    <bg>#333333</bg>
                    <font>
                      <size>9</size>
                      <style>normal</style>
                      <weight>normal</weight>
                      <underlined>0</underlined>
                      <family>default</family>
                      <face>Ubuntu</face>
                      <encoding>UTF-8</encoding>
                    </font>
                    <XRCED>
                      <assign_var>1</assign_var>
                    </XRCED>
                  </object>
                  <label>STREAMS</label>
                  <XRCED>
                    <assign_var>1</assign_var>
                  </XRCED>
                </object>
                <spacing>0</spacing>
                <leftspacing>0</leftspacing>
                <rightspacing>0</rightspacing>
                <bg>#4D4D4D</bg>
                <XRCED>
                  <assign_var>1</assign_var>
                </XRCED>
              </object>
              <flag>wxEXPAND</flag>
            </object>
          </object>
          <bg>#A52A2A</bg>
          <XRCED>
            <assign_var>1</assign_var>
          </XRCED>
        </object>
        <option>1</option>
        <flag>wxEXPAND</flag>
        <minsize>400,400</minsize>
      </object>
    </object>
    <size>400,400</size>
    <title>Stream panel test frame</title>
  </object>
  <object class="wxFrame" name="text_frame">
    <object class="wxPanel">
      <object class="wxBoxSizer">
        <orient>wxVERTICAL</orient>
        <object class="sizeritem">
          <object class="SuggestTextCtrl" name="txt_suggest">
            <size>200,-1</size>
            <value>suggest text field</value>
            <XRCED>
              <assign_var>1</assign_var>
            </XRCED>
          </object>
          <option>0</option>
          <flag>wxALL|wxALIGN_CENTRE</flag>
          <border>10</border>
        </object>
        <object class="sizeritem">
          <object class="UnitIntegerCtrl">
            <size>200,-1</size>
            <value>9</value>
            <min>-10</min>
            <max>10</max>
            <unit>cm</unit>
          </object>
          <flag>wxALL|wxALIGN_CENTRE</flag>
          <border>10</border>
        </object>
        <object class="sizeritem">
          <object class="UnitIntegerCtrl">
            <size>200,-1</size>
            <value>0</value>
            <min>-10</min>
            <max>10</max>
            <unit>μm</unit>
          </object>
          <flag>wxALL|wxALIGN_CENTRE</flag>
          <border>10</border>
        </object>
        <object class="sizeritem">
          <object class="UnitFloatCtrl">
            <size>200,-1</size>
            <value>4.44</value>
            <unit>kg</unit>
          </object>
          <flag>wxALL|wxALIGN_CENTRE</flag>
          <border>10</border>
        </object>
      </object>
      <fg>#E6E6FA</fg>
      <bg>#A52A2A</bg>
    </object>
    <size>400,400</size>
  </object>
</resource>'''

    wx.MemoryFSHandler.AddFile('XRC/test_gui/test_gui_xrc', test_gui_xrc)
    __res.Load('memory:XRC/test_gui/test_gui_xrc')

