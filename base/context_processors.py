#context_processors.py
from .models import  User, Vacation
from django.db.models import Q

def counter(request):
    no_unactive_requests = User.objects.filter(is_active=False).count()

    no_pending_vacations=0
    try:
        user = User.objects.get(id=request.user.id)        
        no_pending_vacations = Vacation.objects.filter(
        status=0,
        employee__department__department_id = user.department.department_id
    ).count()
    except:
        pass

    context = {
        'no_unactive_requests' : no_unactive_requests,
        'no_pending_vacations' : no_pending_vacations,
    }
    return context