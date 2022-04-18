from domain.events.actions import EmailNotifierService, InformationSaverService
from infrastructure.database.models.product import ProductQueries
from domain.productManagment.productService import ProductService
from domain.userManagment.userService import UserService
from infrastructure.database.models.user import UserQueries
from infrastructure.auth.jwt import JWT
from infrastructure.notification.test import FakeNotifier
from infrastructure.database.models.product_views import InformationSaver

def get_user_services() -> UserService:
    return UserService(UserQueries(), JWT())

def get_product_services() -> UserService:
    return ProductService(ProductQueries())

def get_email_notifier_service() -> EmailNotifierService:
    return EmailNotifierService(FakeNotifier())

def get_info_saver_service() -> InformationSaverService:
    return InformationSaverService(InformationSaver())