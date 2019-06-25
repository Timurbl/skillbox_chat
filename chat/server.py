from time import ctime
from twisted.internet import reactor
from twisted.internet.protocol import ServerFactory
from twisted.protocols.basic import LineOnlyReceiver


class Client(LineOnlyReceiver):
    ip: str = None
    login: str = None
    factory: 'Chat'

    def __init__(self, factory):
        """
        Инициализация фабрики клиента
        :param factory:
        """
        self.factory = factory

    def connectionMade(self):
        """
        Обработчик подключения нового клиента
        """

        self.ip = self.transport.getPeer().host
        self.factory.clients.append(self)
        self.factory.chat_login.append(self.login)

        print(f"Client connected: {self.ip}")

        notification = "Welcome to the chat v0.1\n"
        self.sendLine(notification.encode())

        notification = "Enter your login"
        self.sendLine(notification.encode())

    def lineReceived(self, data: bytes):
        """
        Обработчик нового сообщения от клиента
        :param data:
        """
        message = data.decode().replace('\n', '')
        print("line received: ", message)

        if self.login is not None:
            time = ctime().split()[3]
            server_message = f"[{time}] {self.login}: {message}"
            self.factory.notify_all_users(server_message)
            self.factory.chat_history.append(server_message)

            # print("ser_msg", server_message)
        else:

            self.login = message
            self.factory.chat_login.append(self.login)

            if self.factory.chat_login.count(self.login) > 1:

                # pass
                # TODO: login reservation

                self.sendLine(f"login: '{self.login}' is reserved\n".encode())
                self.sendLine("Enter your login again".encode())
                self.factory.chat_login.remove(self.login)
                self.login = None

            else:
                self.sendLine("__del_all_hist".encode())

                notification = "Welcome to the chat v0.1\n"
                self.sendLine(notification.encode())
                # self.factory.chat_history.append(notification)
                # self.transport.write("Welcome to the chat v0.1\n".encode())
                for message in self.factory.chat_history:
                    self.transport.write((str(message) + "\n").encode())

                notification = f"New user connected: {self.login}"
                self.factory.chat_history.append(notification)
                self.factory.notify_all_users(notification)

    def connectionLost(self, reason=None):
        """
        Обработчик отключения клиента
        :param reason:
        """
        self.factory.clients.remove(self)
        self.factory.chat_login.remove(self.login)

        notification = f"Chat member disconnected: {self.login}"
        self.factory.notify_all_users(notification)
        print(notification)


class Chat(ServerFactory):
    window: 'ChatWindow'

    clients: list
    chat_login: list
    chat_history: list

    def __init__(self):
        """
        Инициализация сервера
        """
        self.clients = []
        self.chat_history = []
        self.chat_login = []
        print("*" * 10, "\nStart server \nCompleted [OK]")

    def startFactory(self):
        """
        Запуск процесса ожидания новых клиентов
        :return:
        """
        print("\n\nStart listening for the clients...")

    def buildProtocol(self, addr):
        """
        Инициализация нового клиента
        :param addr:
        :return:
        """
        print("new user")
        return Client(self)

    def notify_all_users(self, data: str):
        """
        Отправка сообщений всем текущим пользователям
        :param data:
        :return:
        """

        data.encode()
        data = data.replace("\r", "")
        data = data.replace("\n", "")
        print("data", data)
        for user in self.clients:
            # user.transport.write(f"{data}\n".encode())
            user.sendLine(data.encode())


if __name__ == '__main__':
    reactor.listenTCP(1720, Chat())
    reactor.run()
