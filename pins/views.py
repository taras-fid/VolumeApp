from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from Volume.models import Pin

# Create your views here.
def explore(request):
    pins = []
    if request.method == 'POST':
        pass
    else:
        if request.GET.get('sort'):
            if request.GET.get('sort') == 'justAdded':
                #  TODO: можна додати прикол типу шо тіки ті шо сьодні додались чи шось таке, якщо хо.
                pins = Pin.objects.order_by('updated_at')
            elif request.GET.get('sort') == 'lowToHigh':
                pins = Pin.objects.order_by('price')
            elif request.GET.get('sort') == 'highToLow':
                pins = Pin.objects.order_by('-price')
            elif request.GET.get('sort') == 'mostLiked':
                pins = Pin.objects.order_by('-likes')
            elif request.GET.get('sort') == 'leastLike':
                pins = Pin.objects.order_by('likes')
            else:
                pins = Pin.objects.order_by('updated_at')
    return render(request, 'pins/explore.html', {'pins': pins})


def add_like(request, pinId):
    pin = get_object_or_404(Pin, id=int(pinId))
    pin.increase_likes()
    return HttpResponse(status=200)

