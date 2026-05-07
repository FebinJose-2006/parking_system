from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import ParkingLot, Slot, Booking
from .forms import BookingForm


@login_required
def dashboard(request):
    lots = ParkingLot.objects.all()

    return render(request, 'parking/dashboard.html', {
        'lots': lots
    })


@login_required
def slot_list(request, lot_id):
    lot = get_object_or_404(ParkingLot, id=lot_id)
    slots = Slot.objects.filter(lot=lot)

    return render(request, 'parking/slots.html', {
        'lot': lot,
        'slots': slots
    })


@login_required
def book_slot(request, slot_id):
    slot = get_object_or_404(Slot, id=slot_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)

        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.slot = slot
            booking.save()

            slot.status = 'booked'
            slot.save()

            return redirect('dashboard')

    else:
        form = BookingForm()

    return render(request, 'parking/book_slot.html', {
        'form': form,
        'slot': slot
    })