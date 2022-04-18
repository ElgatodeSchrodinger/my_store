from typing import List
from domain.events.actions import IEmailNotifier
from domain.events.events import Event
from core.config import settings
import boto3


class SESNotifier(IEmailNotifier):
    def __init__(self) -> None:
        self.ses_client = boto3.client(
            "ses",
            region_name=settings.AWS_SES_REGION,
            aws_access_key_id=settings.AWS_SES_ACCESS_KEY,
            aws_secret_access_key=settings.AWS_SES_SECRET_KEY,
        )

    def verify_email_identity(self):

        response = self.ses_client.verify_email_identity(
            EmailAddress="admin@example.com"
        )
        print(response)

    def send_notification(self, event: Event, receivers: List[str]):
        sender = "Administrator <admin@example.com>"
        self.ses_client.send_email(
            Destination={
                "ToAddresses": receivers,
            },
            Message={
                "Body": {
                    "Html": {
                        "Charset": "UTF-8",
                        "Data": self.generate_html(event),
                    },
                },
                "Subject": {
                    "Charset": "UTF-8",
                    "Data": f"Event Notification: {type(event)}",
                },
            },
            Source=sender,
        )

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
