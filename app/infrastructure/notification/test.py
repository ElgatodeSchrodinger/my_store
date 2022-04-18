
from typing import List
from domain.events.actions import IEmailNotifier
from domain.events.events import Event


class FakeNotifier(IEmailNotifier):
    
    def send_notification(self, event: Event, receivers: List[str]):
        print(f"Se lanzó la notificación de la actualizacion del product {event.product_id} para los emails: {','.join(receivers)}")