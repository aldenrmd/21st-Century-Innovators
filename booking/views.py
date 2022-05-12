from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Sender, Receiver
from track.models import Tracker
from track.views import track_code_generator


# Create your views here.
TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)


def booking(request):
    today = datetime.datetime.now().date()
    if request.method == 'POST':
        track_code = track_code_generator()
        sender_first_name = request.POST['sender_first_name']
        sender_last_name = request.POST['sender_last_name']
        sender_address = request.POST['sender_address']
        sender_city = request.POST['sender_city']
        sender_state = request.POST['sender_state']
        sender_zip = request.POST['sender_zip']
        sender_email = request.POST['sender_email']
        sender_number = request.POST['sender_number']
        sender_country = request.POST['sender_country']
        receiver_first_name = request.POST['receiver_first_name']
        receiver_last_name = request.POST['receiver_last_name']
        receiver_address = request.POST['receiver_address']
        receiver_city = request.POST['receiver_city']
        receiver_state = request.POST['receiver_state']
        receiver_zip = request.POST['receiver_zip']
        receiver_email = request.POST['receiver_email']
        receiver_number = request.POST['receiver_number']
        receiver_country = request.POST['receiver_country']
        my1 = Receiver(receiver_first_name=receiver_first_name, receiver_last_name=receiver_last_name, receiver_address=receiver_address, receiver_city=receiver_city, receiver_state=receiver_state, receiver_zip=receiver_zip, receiver_email=receiver_email, receiver_number=receiver_number, receiver_country=receiver_country, trackingcode=track_code)
        my2 = Sender(sender_first_name=sender_first_name, sender_last_name=sender_last_name, sender_address=sender_address, sender_city=sender_city, sender_state=sender_state, sender_zip=sender_zip, sender_email=sender_email, sender_number=sender_number, sender_country=sender_country, trackingcode=track_code)
        track_model = Tracker(trackingcode=track_code, status=0)
        my1.save()
        my2.save()
        track_model.save()
        return render(request, "admin_access/dashboard.html")
    return render(request, "booking/booking.html")

def update(request):
    query=None
    track=[]
    sender=[]
    receiver=[]
    if request.method == 'GET':
        query = request.GET.get('search')
        if Tracker.objects.filter(trackingcode=query):
            track=Tracker.objects.filter(trackingcode=query)
            if Sender.objects.filter(trackingcode=query):
                sender= Sender.objects.filter(trackingcode=query)
            if Receiver.objects.filter(trackingcode=query):
                receiver= Receiver.objects.filter(trackingcode=query)
        return render(request,  'booking/update.html', {'query':query,'track':track, 'sender':sender, 'receiver':receiver})
    if request.method == '#':
        pass
        #something
    else:
        return render(request, 'booking/update.html',{})

def search(request):
    return render(request, "booking/search.html")
