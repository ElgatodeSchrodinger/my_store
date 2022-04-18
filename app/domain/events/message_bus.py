from typing import List, Dict, Callable, Type
from domain.events import events
from api.utils import get_email_notifier_service, get_info_saver_service


def handle(event: events.Event):
    for handler in HANDLERS[type(event)]:
        handler(event)


def save_view_product_by_anon_user(event: events.ViewProductByAnon):
    saver_service = get_info_saver_service()
    saver_service.save_details(event=event)


def send_update_product_notification(event: events.UpdateProduct):
    email_notifier = get_email_notifier_service()
    email_notifier.send_notification(event=event)

HANDLERS = {
    events.ViewProductByAnon: [save_view_product_by_anon_user],
    events.UpdateProduct: [send_update_product_notification]
}  # type: Dict[Type[events.Event], List[Callable]]