import wx
from twisted.internet import wxreactor

wxreactor.install()

from twisted.internet import reactor
from twisted.internet.protocol import ClientFactory
from twisted.protocols.basic import LineOnlyReceiver


class ChatClient(LineOnlyReceiver):
    """
    Класс для работы с подключением
    """
    factory: 'ChatFactory'

    def __init__(self, factory):
        """
        Запоминаем фабрику для последующего обращения
        :param factory:
        """
        self.factory = factory

    def connectionMade(self):
        """
        Обработчик установки соединения с сервером
        :return:
        """
        self.factory.window.protocol = self  # записали в окно приложения текущий протокол

    def lineReceived(self, line):
        """
        Обработчик получения новой строки от сервера
        :param line:
        :return:
        """
        message = line.decode()  # раскодируем
        print(message)
        self.factory.window.chat_box.AppendText(f"{message}\n")  # добавим в поле сообщений


class ChatFactory(ClientFactory):
    """
    Класс для создания подключения
    """
    window: 'ChatWindow'

    def __init__(self, window):
        """
        Запоминаем окно приложения в конструкторе для обращения
        :param window:
        """
        self.window = window

    def buildProtocol(self, addr):
        """
        Обработчик создания подключения
        :param addr:
        :return:
        """
        return ChatClient(self)


class ChatWindow(wx.Frame):
    protocol: ChatClient

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
        # log in
        box = wx.TextEntryDialog(None, "Enter your login", "Welcome to the chat!")
        if box.ShowModal() == wx.ID_OK:
            login = box.GetValue()
            # self.protocol.sendLine(login.encode())

            if login:  # checking reservation
                self.build_chat()
                self.build_handlers()
        else:
            box.Destroy()

    def build_chat(self):
        panel = wx.BoxSizer(wx.VERTICAL)

        self.chat_box = wx.TextCtrl(self, style=wx.TE_READONLY | wx.TE_MULTILINE)
        self.msg_box = wx.TextCtrl(self)
        self.msg_box.SetHint("Your message")
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
        print(message)
        self.protocol.sendLine(message.encode())
        # self.protocol.sendLine(message.encode())
        # self.chat_box.WriteText(f"{message}\n")
        self.msg_box.SetValue("")


if __name__ == "__main__":
    app = wx.App()
    window = ChatWindow()
    window.Show()

    reactor.registerWxApp(app)
    reactor.connectTCP(
        "localhost",
        7410,
        ChatFactory(window)
    )
    reactor.run()
