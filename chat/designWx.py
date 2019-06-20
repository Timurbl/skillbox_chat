import wx


class TestWindow(wx.Frame):
    chat_box: wx.TextCtrl
    msg_box: wx.TextCtrl
    submit_btn: wx.Button

    def __init__(self):
        super().__init__(
            None,
            title="My chat",
            size=wx.Size(350, 500)
        )

        self.build_msg_dialog()

    def build_msg_dialog(self):
        box = wx.TextEntryDialog(None, "Enter your login", "Welcome to the chat!")
        if box.ShowModal() == wx.ID_OK:
            answer = box.GetValue()
            if answer == answer:  # checking reservation
                self.build_chat()
                self.build_handlers()
        else:
            box.Destroy()

    def build_chat(self):
        panel = wx.BoxSizer(wx.VERTICAL)

        self.chat_box = wx.TextCtrl(self, style=wx.TE_READONLY | wx.TE_MULTILINE)
        self.msg_box = wx.TextCtrl(self)
        self.submit_btn = wx.Button(self, label="Send message")

        panel.Add(self.chat_box, wx.SizerFlags(1).Expand())
        panel.Add(self.msg_box, wx.SizerFlags(0).Expand().Border(wx.ALL, 10))
        panel.Add(self.submit_btn, wx.SizerFlags(0).Expand().Border(wx.LEFT | wx.RIGHT | wx.BOTTOM, 10))

        self.SetSizer(panel)

    def build_handlers(self):
        self.submit_btn.Bind(wx.EVT_BUTTON, self.on_btn_click)
        self.msg_box.Bind(wx.EVT_TEXT_ENTER, self.on_btn_click)

    def on_btn_click(self, event):
        message = self.msg_box.GetValue()
        self.chat_box.WriteText(f"{message}\n")

        self.msg_box.SetValue("")


if __name__ == "__main__":
    app = wx.App()
    window = TestWindow()
    window.Show()
    app.MainLoop()
