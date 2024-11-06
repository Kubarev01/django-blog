from django import template
from posts.models import Post



register = template.Library()



@register.simple_tag
def get_posts():
    return Post.objects.all()



@register.simple_tag
def get_posts_for_carousel():
     return Post.objects.order_by('?')[:3]