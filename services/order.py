from django.contrib.auth import get_user_model
from django.db import transaction
from db.models import Order, Ticket
User = get_user_model()


@transaction.atomic
def create_order(tickets: list, username: str, date: str = None) -> Order:
    user = User.objects.get(username=username)
    order = Order.objects.create(created_at=date, user=user)
    for data in tickets:
        Ticket.objects.create(movie_session=data["movie_session"],
                              order=order,
                              row=data["row"],
                              seat=data["seat"])
    return order


def get_orders(username: str = None) -> Order:
    if username:
        return Order.objects.filter(user__username=username)
    return Order.objects.all()
