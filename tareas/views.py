from django.contrib.auth.decorators import login_required
# from django.core.exceptions import PermissionDenied
from django.shortcuts import render

@login_required
def index(request):
    """
    Home.
    """
    return render(request, 'index.html')

# @login_required
# def map(request):
#     print(request.user.has_perm('managers'))
#     if request.user.has_perm('managers'):
#         return render(request, 'map.html')
#     else:
#         raise PermissionDenied
