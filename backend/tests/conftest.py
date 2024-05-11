import pytest
import random

from django.test import Client
from django.contrib.auth.models import User

from user.management.commands.command_settings_query import CURRENCY, PAGINATION
from user.models import UserSettings, UserProfile, CommandCurrency, CommandPagination
from accounting.models import Ticket, TicketFilter
from accounting.management.commands.command_filter_query import FILTER_TICKETS


TEST_USERNAME = 'user'
TEST_PASSWORD = 'a9Jd2o9gLe2axs'
TEST_EMAIL = 'user@user.com'


@pytest.fixture
def client():
    client = Client()
    return client


@pytest.fixture
def created_user():
    user = User.objects.create_user(
        username=TEST_USERNAME,
        email=TEST_EMAIL,
        password=TEST_PASSWORD,
    )
    UserSettings.objects.create(user=user)
    UserProfile.objects.create(user=user)
    return user


@pytest.fixture
def login_user(client):
    client.login(
        username=TEST_USERNAME,
        password=TEST_PASSWORD,
    )


@pytest.fixture
def ticket(created_user):
    ticket_waiting = Ticket.objects.create(
        user=created_user,
        title='Ticket of Waiting',
        bought=1.25,
        sold=None,
        profit=None,
    )
    return ticket_waiting


@pytest.fixture
def add_ten_tickets(created_user):
    for value in range(1, 11):
        bought = random.randrange(1, 50)
        sold = random.randrange(10, 60)
        profit = sold - bought
        Ticket.objects.create(
            user=created_user,
            title=f'Ticket number {value}',
            bought=bought,
            sold=sold,
            profit=profit,
        )


@pytest.fixture
def ticket_success(created_user):
    ticket_success = Ticket.objects.create(
        user=created_user,
        title='Ticket of Success',
        bought=5.12,
        sold=6.22,
        profit=1.10,
    )
    return ticket_success


@pytest.fixture
def ticket_failure(created_user):
    ticket_failure = Ticket.objects.create(
        user=created_user,
        title='Ticket of Failure',
        bought=5.12,
        sold=2.00,
        profit=-3.12,
    )
    return ticket_failure


@pytest.fixture
def ticket_without_profit(created_user):
    ticket_nothing = Ticket.objects.create(
        user=created_user,
        title='Ticket of Nothing',
        bought=2.78,
        sold=2.78,
        profit=0,
    )
    return ticket_nothing


@pytest.fixture
def add_ticket_filter():
    for filter_dict in FILTER_TICKETS:
        filter_model = TicketFilter(**filter_dict)
        filter_model.save()


@pytest.fixture
def add_currency_symbols():
    for currency_dict in CURRENCY:
        currency_model = CommandCurrency(**currency_dict)
        currency_model.save()


@pytest.fixture
def add_pagination_values():
    for pagination_dict in PAGINATION:
        paginate_by_model = CommandPagination(**pagination_dict)
        paginate_by_model.save()
