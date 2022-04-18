from typing import List
from domain.events.actions import IEmailNotifier
from domain.events.events import Event


class FakeNotifier(IEmailNotifier):
    def send_notification(self, event: Event, receivers: List[str]):
        print(
            f"Se lanzó la notificación de la actualizacion del product {event.product_id} para los emails: {','.join(receivers)}"
        )
        print(self.generate_html(event))

    def generate_html(self, event_data):
        return f"""
            <html>
                <head></head>
                <h1 style='text-align:center'>This is an update notification</h1>
                <p>The product with id <{event_data.product_id}> has been updated the user with id <{event_data.user_id}></p><br/>
                <p>Changes:</p><br/>
                <p>{event_data.change}</p>
                </body>
            </html>
        
        """
