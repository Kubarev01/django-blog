from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from comments.form import CommentForm
from comments.models import Comment
from posts.models import Post

# Create your views here.



# def leave_comment(request):

#     if request.method == 'POST':

#         form = CommentForm(request.POST)

#         if form.is_valid():
#             # Сохранение формы
#             form.save()

#             # Редирект на ту же страницу
#             return HttpResponseRedirect(request.path_info)
#             # return redirect(request.get_full_path())

#     else:
#     # метод GET

#         form = CommentForm()

#         # Получение всех имен из БД.
#     comments = Comment.objects.all()
#     context={
#         'form':form,
#         'comments':comments
#     }

#     # И добавляем names в контекст, чтобы плучить к ним доступ в шаблоне
#     return render(request, 'main/blog.html', context)



def leave_comment(request, post_slug):
    # Получаем пост по его ID
    post = get_object_or_404(Post, slug=post_slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            # Создаем новый комментарий, связанный с постом
            text=form.cleaned_data['text']
            comment = Comment(text=text, author=request.user, post=post)
            comment.save()
            

            # Редирект на страницу поста
            return redirect('main:post', post_slug=post.slug)  # Замените 'post_detail' на имя вашего маршрута для просмотра поста

    else:
        form = CommentForm()

    # Получаем все комментарии для данного поста
    comments = post.comments.all()  # Предполагается, что у вас есть обратная связь в модели Comment

    context = {
        'form': form,
        'comments': comments,
        'post': post  # Передаем пост в контекст, если нужно отображать его в шаблоне
    }

    return render(request, 'main/blog.html', context)
