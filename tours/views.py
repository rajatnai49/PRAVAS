from django.shortcuts import render, redirect
from .models import Destination, Tour, TourBooking
from pravas.models import user
from django.contrib import messages


def see_tour(request):
    if request.method == "POST":
        tour_id = request.POST["tour_id"]
        tour = Tour.objects.get(id=tour_id)
        destination = tour.destinations.all()
        context = {'tour': tour, 'destination': destination}
        return render(request=request, template_name="tours/see_tour.html", context=context)


def book_tour(request):
    if request.method == "POST":
        tour_id = request.POST["tour_id"]
        tour = Tour.objects.get(id=tour_id)
        user = request.user
        date_booked = request.POST["date_booked"]
        number_of_pass = request.POST["number_of_pass"]
        new_booking = TourBooking(
            tour=tour, user=user, date=date_booked, num_passengers=number_of_pass)
        new_booking.save()
        messages.success(request, 'Tour is booked')
        return redirect("pravas:home")
