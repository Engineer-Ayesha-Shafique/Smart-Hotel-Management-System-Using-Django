from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q
from .forms import ReservationForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from .render import Render
from django.db.models import Sum

import random
import string

from parking_zones.models import Parking_Zone, Reservation

from django.contrib import messages

def index(request):
    today = timezone.now()
    context = {
        'all_parking_zones':Parking_Zone.objects.all(),
        'reservations': Reservation.objects.filter(customer=request.user),
        'today': today,
    }
    return render(request, 'parking_zones/index.html', context)

def adminreservationview(request):
    today = timezone.now()

    # sum = Parking_Zone.objects.aggregate(Sum('num_of_slots'))
    context = {
        'all_parking_zones':Parking_Zone.objects.all(),
        'reservations': Reservation.objects.all(),
        'today': today,

    }
    return render(request, 'parking_zones/adminview.html', context)

def parking_status(request, slug):
    all_parking_zones = Parking_Zone.objects.all()
    parking_zone = all_parking_zones.get(slug=slug)
    context = {
        'parking_zone': parking_zone,
    }
    return render(request, 'parking_zones/status.html', context)

def create_ticket_code():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))

class ReservationView(View):
    def get(self, request):
        try:
            user_reservation = Reservation.objects.get(customer=request.user, checked_out=False)
            if user_reservation:
                messages.warning(self.request, 'Please Check Out Your Previous Reservation')
                return redirect('index')
        except ObjectDoesNotExist:
            pass   
                
        reservation = ReservationForm()

        return render(request, 'parking_zones/booking.html', {'form': reservation})

    def post(self, request):
        try:
            user_reservation = Reservation.objects.get(customer=request.user, checked_out=False)
            if user_reservation:
                messages.warning(self.request, 'Please Check Out Your Previous Reservation')
                return redirect('index')

        except ObjectDoesNotExist:
            pass    

        reservation_form = ReservationForm(data=request.POST)

        if reservation_form.is_valid():
            start_date = reservation_form.cleaned_data['start_date']
            finish_date = reservation_form.cleaned_data['finish_date']
            parking_zone = reservation_form.cleaned_data['parking_zone']
            plate_number = reservation_form.cleaned_data['plate_number']

            parkingzone = Parking_Zone.objects.get(name=parking_zone)
            if parkingzone.vacant_slots == 0:
                messages.warning(self.request, 'Parking Zone Full!')
                return redirect('index')

            reservation = reservation_form.save(commit=False)
            reservation.customer = request.user
            reservation.parking_zone = parking_zone
            reservation.ticket_code = create_ticket_code()
            reservation.save()
            #parkingzone = Parking_Zone.objects.get(name=parking_zone)
            parkingzone.occupied_slots += 1
            parkingzone.save()
            vacantslots = int(parkingzone.num_of_slots) - int(parkingzone.occupied_slots)
            parkingzone.vacant_slots = vacantslots
            parkingzone.save()
            messages.info(request, 'Successfully Booked')
            return redirect('index')

        return render(request, 'parking_zones/booking.html', {'form': reservation_form})

class Ticket_Pdf(View):

    def get(self, request):
        
        today = timezone.now()
        reservation = Reservation.objects.filter(Q(customer=request.user, checked_out=False) | Q(customer=request.user, checked_out=True)).first()
        if reservation:
            params = {
                'today': today,
                'reservation': reservation,
                'request': request
            }
            return Render.render('parking_zones/ticket.html', params)
        else:
            messages.warning(self.request, f'No Parking reservation exists for {self.request.user}')
            return redirect('index')    

@login_required
def check_out(request):
    try:
        reservation = Reservation.objects.get(customer=request.user, checked_out=False)
        if reservation:
            reservation.checked_out = True
            reservation.save()
            parking_zone_name = reservation.parking_zone.name
            parking_zone = Parking_Zone.objects.get(name=parking_zone_name)
            parking_zone.occupied_slots -= 1
            parking_zone.vacant_slots += 1
            parking_zone.save()
            messages.info(request, 'Successfully Checked Out')
        
    except ObjectDoesNotExist:
            messages.warning(request, f'No Parking reservation exists for {request.user}')        

    return redirect('index')      
