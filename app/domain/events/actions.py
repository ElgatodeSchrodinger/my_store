from abc import abstractmethod

from domain.events.events import Event


class INotifier:
    pass


class IEmailNotifier(INotifier):

    @abstractmethod
    def send_notification(self, event: Event):
        raise NotImplementedError

class EmailNotifierService:

    def __init__(self, email_service, user_service) -> None:
        self.__email_service = email_service
        self.__user_service = user_service

    def send_notification_to_admins(self, event: Event):
        receivers = self.__user_service.get_admin_emails()
        self.__email_service.send_notification(event, receivers)


class IInformationSaver:

    @abstractmethod
    def save_details(self, event: Event):
        raise NotImplementedError
    
class InformationSaverService:

    def __init__(self, saver_service) -> None:
        self.__saver_service = saver_service

    def save_details(self, event: Event):
        self.__saver_service.save_details(event)