
from users.models import User
from django import template
register = template.Library()




@register.simple_tag
def get_profile(request):
    user=request.user
    return User.objects.get(user=user)
