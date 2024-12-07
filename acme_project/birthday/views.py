# # birthday/views.py
# from django.shortcuts import render

# # Импортируем класс BirthdayForm, чтобы создать экземпляр формы.
# from .forms import BirthdayForm
# from .utils import calculate_birthday_countdown

# from .models import Birthday


# def birthday(request):
#     form = BirthdayForm(request.POST or None)
#     # Создаём словарь контекста сразу после инициализации формы.
#     context = {'form': form}
#     # Если форма валидна...
#     if form.is_valid():
#         form.save() # Добавим строчку с вызовом метода
#         # ...вызовем функцию подсчёта дней:
#         birthday_countdown = calculate_birthday_countdown(
#             # ...и передаём в неё дату из словаря cleaned_data.
#             form.cleaned_data['birthday']
#         )
#         # Обновляем словарь контекста: добавляем в него новый элемент.
#         context.update({'birthday_countdown': birthday_countdown})
#     return render(request, 'birthday/birthday.html', context)


# def birthday_list(request):
#     # Получаем все объекты модели Birthday из БД.
#     birthdays = Birthday.objects.all()
#     # Передаём их в контекст шаблона.
#     context = {'birthdays': birthdays}
#     return render(request, 'birthday/birthday_list.html', context)

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

from django.shortcuts import get_object_or_404, redirect, render

from .forms import BirthdayForm
from .models import Birthday
from .utils import calculate_birthday_countdown
# Импортируем класс пагинатора.
from django.core.paginator import Paginator

from django.views.generic import ListView


# Добавим опциональный параметр pk.
def birthday(request, pk=None):
    # Если в запросе указан pk (если получен запрос на редактирование объекта):
    if pk is not None:
        # Получаем объект модели или выбрасываем 404 ошибку.
        instance = get_object_or_404(Birthday, pk=pk)
    # Если в запросе не указан pk
    # (если получен запрос к странице создания записи):
    else:
        # Связывать форму с объектом не нужно, установим значение None.
        instance = None
    # Передаём в форму либо данные из запроса, либо None.
    # В случае редактирования прикрепляем объект модели.
    form = BirthdayForm(request.POST or None,
                        files=request.FILES or None, instance=instance)
    # Остальной код без изменений.
    context = {'form': form}
    # Сохраняем данные, полученные из формы, и отправляем ответ:
    if form.is_valid():
        form.save()
        birthday_countdown = calculate_birthday_countdown(
            form.cleaned_data['birthday']
        )
        context.update({'birthday_countdown': birthday_countdown})
    return render(request, 'birthday/birthday.html', context)


# def birthday_list(request):
#     # Получаем все объекты модели Birthday из БД.
#     birthdays = Birthday.objects.all()
#     # Передаём их в контекст шаблона.
#     context = {'birthdays': birthdays}
#     return render(request, 'birthday/birthday_list.html', context)

# def birthday_list(request):
#     # Получаем список всех объектов с сортировкой по id.
#     birthdays = Birthday.objects.order_by('id')
#     # Создаём объект пагинатора с количеством 10 записей на страницу.
#     paginator = Paginator(birthdays, 2)

#     # Получаем из запроса значение параметра page.
#     page_number = request.GET.get('page')
#     # Получаем запрошенную страницу пагинатора.
#     # Если параметра page нет в запросе или его значение не приводится к числу,
#     # вернётся первая страница.
#     page_obj = paginator.get_page(page_number)
#     # Вместо полного списка объектов передаём в контекст
#     # объект страницы пагинатора
#     context = {'page_obj': page_obj}
#     return render(request, 'birthday/birthday_list.html', context)

# Наследуем класс от встроенного ListView:
class BirthdayListView(ListView):
    # Указываем модель, с которой работает CBV...
    model = Birthday
    # ...сортировку, которая будет применена при выводе списка объектов:
    ordering = 'id'
    # ...и даже настройки пагинации:
    paginate_by = 2


def delete_birthday(request, pk):
    # Получаем объект модели или выбрасываем 404 ошибку.
    instance = get_object_or_404(Birthday, pk=pk)
    # В форму передаём только объект модели;
    # передавать в форму параметры запроса не нужно.
    form = BirthdayForm(instance=instance)
    context = {'form': form}
    # Если был получен POST-запрос...
    if request.method == 'POST':
        # ...удаляем объект:
        instance.delete()
        # ...и переадресовываем пользователя на страницу со списком записей.
        return redirect('birthday:list')
    # Если был получен GET-запрос — отображаем форму.
    return render(request, 'birthday/birthday.html', context)
