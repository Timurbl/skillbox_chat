from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor


class Client(Protocol):
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
        self.transport.write(notification.encode())


        #for message in self.factory.chat_history:
        #   self.transport.write(message.encode())


    def dataReceived(self, data: bytes):
        """
        Обработчик нового сообщения от клиента
        :param data:
        """
        message = data.decode().replace('\n', '')



        if self.login is not None:
            server_message = f"{self.login}: {message}"
            self.factory.notify_all_users(server_message)
            self.factory.chat_history.append(server_message)

            print(server_message)
        else:

            self.login = message.replace("login:", "")
            self.factory.chat_login.append(self.login)

            if self.factory.chat_login.count(self.login) > 1:
                self.transport.write(f"login: '{self.login}' is reserved\n".encode())
                self.transport.write("Your login >>> ".encode())
                self.factory.chat_login.remove(self.login)
                self.login = None
            else:
                notification = f"New user connected: {self.login}"
                self.factory.notify_all_users(notification)

                #self.factory.chat_history.append(notification)
                #self.transport.write("Welcome to the chat v0.1\n".encode())
                for message in self.factory.chat_history:
                    self.transport.write((str(message) + "\n").encode())


                #print(notification)

    def connectionLost(self, reason=None):
        """
        Обработчик отключения клиента
        :param reason:
        """
        self.factory.clients.remove(self)
        print(f"Client disconnected: {self.ip}")


class Chat(Factory):
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
        return Client(self)

    def notify_all_users(self, data: str):
        """
        Отправка сообщений всем текущим пользователям
        :param data:
        :return:
        """
        for user in self.clients:
            user.transport.write(f"{data}\n".encode())


if __name__ == '__main__':
    reactor.listenTCP(7410, Chat())
    reactor.run()