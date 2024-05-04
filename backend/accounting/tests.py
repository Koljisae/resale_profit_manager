from django.test import TestCase
from django.contrib.auth.models import User

from accounting.management.commands.command_filter_query import FILTER_TICKETS
from accounting.models import Ticket, TicketFilter
from datetime import datetime


class TestTicketModels(TestCase):
    def setUp(self):
        self.bought = 7.56
        self.sold = 8.53
        self.profit = self.sold - self.bought
        self.today = datetime.now()
        self.user_object = User.objects.create_user(
            username='test_user',
            password='password',
        )
        self.ticket_object = Ticket.objects.create(
            user=self.user_object,
            title='Ticket title',
            bought=self.bought,
        )

    def test_ticket_exists(self):
        ticket = Ticket.objects.filter(title=self.ticket_object.title).first()
        self.assertEqual(ticket.user, self.user_object)
        self.assertEqual(ticket.title, self.ticket_object.title)
        self.assertEqual(ticket.closed, 'False')
        self.assertEqual(ticket.bought, 7.56)
        self.assertIsNone(ticket.sold)
        self.assertIsNone(ticket.profit)
        self.assertIsNone(ticket.category)
        self.assertEqual(ticket.created_at.date(), self.today.date())
        self.assertEqual(ticket.closed_at.date(), self.today.date())
        self.assertEqual(ticket.deleted, 'False')

    def test_ticket_update(self):
        ticket = Ticket.objects.filter(title=self.ticket_object.title).first()
        ticket.title = 'Ticket'
        ticket.sold = self.sold
        ticket.profit = self.profit
        ticket.save()
        self.assertEqual(ticket.title, 'Ticket')
        self.assertEqual(ticket.sold, self.sold)
        self.assertEqual(ticket.profit, self.profit)

    def test_get_update_url(self):
        self.assertEqual(Ticket.get_update_url(self.ticket_object), f'/update/{self.ticket_object.pk}')

    def test_get_delete_url(self):
        self.assertEqual(Ticket.get_delete_url(self.ticket_object), f'/delete/{self.ticket_object.pk}')

    def test_str_method(self):
        self.assertEqual(Ticket.__str__(self.ticket_object), self.ticket_object.title)


class TestTicketFilterModel(TestCase):
    def setUp(self):
        for filter_dict in FILTER_TICKETS:
            filter_model = TicketFilter(**filter_dict)
            filter_model.save()

    def test_ticket_filter(self):
        for filter_dict in FILTER_TICKETS:
            ticket_filter = TicketFilter.objects.filter(**filter_dict).first()
            self.assertEqual(ticket_filter.pk, filter_dict.get('pk'))
            self.assertEqual(ticket_filter.title, filter_dict.get('title'))
            self.assertEqual(ticket_filter.url_value, filter_dict.get('url_value'))
            self.assertEqual(ticket_filter.annotation, filter_dict.get('annotation'))
            self.assertEqual(ticket_filter.color, filter_dict.get('color'))
