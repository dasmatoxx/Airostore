from django.urls import path


from applications.ticket.views import TicketCreateView, TicketView

urlpatterns = [
    path('type-class/',  TicketView.as_view()),
    path('user-ticket/',  TicketView.as_view()),
    path('create-ticket/',  TicketCreateView.as_view()),
]