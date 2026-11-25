from django.shortcuts import render
from django.http import Http404
from datetime import datetime, timedelta
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

QUESTION_LIST = [
    {
        'id': 1,
        'header': 'Почему в Django возникает ошибка SynchronousOnlyOperation при работе с async/await?',
        'text': 'Пытаюсь использовать асинхронные вьюхи в Django, но при обращении к ORM вылетает ошибка SynchronousOnlyOperation. Читал документацию, но не до конца понял, нужно ли переписывать все запросы на sync_to_async, или есть какой-то более элегантный способ настроить работу с базой данных в асинхронном режиме. Как правильно организовать этот процесс?',
        'tag': ['Python', 'Django'],
        'author': 'user_123',
        'rating': 12,
        'date': datetime.now() - timedelta(hours=2),
    },
    {
        'id': 2,
        'header': 'Как избежать утечки памяти при использовании std::shared_ptr в C++?',
        'text': 'В моем проекте класс Parent и класс Child хранят друг на друга умные указатели std::shared_ptr. После выхода из области видимости объекты не уничтожаются. Я понимаю, что это циклическая ссылка, но как правильно разорвать эту связь с помощью std::weak_ptr? В каких конкретно местах его лучше применять, чтобы не сломать логику работы приложения?',
        'tag': ['C++', 'Asm'],
        'author': 'student_42',
        'rating': 8,
        'date': datetime.now() - timedelta(days=1),
    },
    {
        'id': 3,
        'header': 'Как прижать футер к низу страницы, если контента мало?',
        'text': 'Столкнулся с проблемой верстки: если контента на странице мало, футер "всплывает" наверх. Пробовал использовать position: absolute и bottom: 0, но тогда он перекрывает основной контент при прокрутке. Интересует современное и надежное решение на Flexbox или CSS Grid, которое будет корректно работать во всех браузерах.',
        'tag': ['HTML', 'CSS'],
        'author': 'dev_007',
        'rating': 25,
        'date': datetime.now() - timedelta(days=3),
    },
    {
        'id': 4,
        'header': 'Оценка сложности алгоритма быстрой сортировки в худшем случае',
        'text': 'Знаю, что средняя сложность QuickSort — это O(n log n). Однако в некоторых источниках указано, что при неудачном выборе опорного элемента (pivot) сложность может деградировать до O(n^2). Какую стратегию выбора pivot лучше использовать на практике, чтобы минимизировать вероятность такого сценария при сортировке почти отсортированных массивов?',
        'tag': ['Алгоритмы', 'Python'],
        'author': 'Mr Freeman',
        'rating': 42,
        'date': datetime.now() - timedelta(days=5),
    },
    {
        'id': 5,
        'header': 'Как безопасно удалить коммит из удаленного репозитория Git?',
        'text': 'Случайно закоммитил и запушил файл с секретными ключами в общую ветку develop. Знаю про команду git revert, но она создает новый коммит, и файл остается в истории. Можно ли как-то переписать историю с помощью git reset и force push, чтобы полностью стереть эти данные? Какие есть риски для коллег?',
        'tag': ['Git'],
        'author': 'Bender',
        'rating': 15,
        'date': datetime.now() - timedelta(days=10),
    }
]

ANSWERS = [
    {
        'question_id': 1, # Привязка к ID вопроса
        'content': 'Для работы с ORM в асинхронном режиме используйте sync_to_async из модуля asgiref.sync. Это позволит выполнять синхронные запросы к БД внутри асинхронных вьюх без блокировки event loop.',
        'author': 'Mr Freeman',
        'date': datetime.now() - timedelta(minutes=30),
        'rating': 8,
        'is_correct': True, # Помечаем как правильный ответ
    },
    {
        'question_id': 1,
        'content': 'Можно также использовать асинхронные методы ORM (например, `aget()`), которые появились в Django 4.1+, если ваша версия позволяет.',
        'author': 'Dr House',
        'date': datetime.now() - timedelta(minutes=15),
        'rating': 3,
        'is_correct': False,
    },
    {
        'question_id': 2,
        'content': 'Вам нужно использовать std::weak_ptr для одной из связей. Обычно Parent владеет Child через shared_ptr, а Child хранит weak_ptr на Parent. Тогда цикла не будет.',
        'author': 'dev_007',
        'date': datetime.now() - timedelta(hours=5),
        'rating': 12,
        'is_correct': True,
    },
    {
        'question_id': 3,
        'content': 'Самый современный способ — использовать CSS Grid. Задайте body `display: grid; grid-template-rows: auto 1fr auto;`. Это прижмет футер к низу.',
        'author': 'student_42',
        'date': datetime.now() - timedelta(days=1),
        'rating': 20,
        'is_correct': False,
    }
]

POPULAR_TAGS = [
    {'name': 'C++'},
    {'name': 'Python'},
    {'name': 'Django'},
    {'name': 'Git'},
    {'name': 'Алгоритмы'},
    {'name': 'HTML'},
    {'name': 'CSS'},
    {'name': 'Asm'},
]

BEST_MEMBERS = [
    {'username': 'Mr Freeman'},
    {'username': 'Dr House'},
    {'username': 'Bender'},
    {'username': 'Queen Victoria'},
    {'username': 'V Pupkin'},
]

def paginate(objects_list, request, per_page=2):
    # Создаем пагинатор
    paginator = Paginator(objects_list, per_page)

    # Получаем номер страницы из GET-запроса (если нет, то 1)
    page_number = request.GET.get('page', 1)

    try:
        # Пытаемся получить нужную страницу
        page = paginator.page(page_number)
    except PageNotAnInteger:
        # Если передали НЕ число (например, ?page=abc), отдаем первую страницу
        page = paginator.page(1)
    except EmptyPage:
        # Если передали число, но такой страницы нет (например, ?page=9999),
        # отдаем ПОСЛЕДНЮЮ страницу
        page = paginator.page(paginator.num_pages)

    return page

# 2. Ваши вьюхи (функции)
def base(request):
    sorted_questions = sorted(QUESTION_LIST, key=lambda q: q['date'], reverse=True)

    page_obj = paginate(sorted_questions, request, per_page=2)

    context = {
        'questions': page_obj.object_list,
        'page_obj': page_obj
    }
    return render(request, 'questions/base.html', context)

def hot(request):
    sorted_questions = sorted(QUESTION_LIST, key=lambda q: q['rating'], reverse=True)

    page_obj = paginate(sorted_questions, request, per_page=2)

    context = {
        'hot_questions': page_obj.object_list,
        'page_obj': page_obj
    }
    return render(request, 'questions/hot.html', context)

def ask(request):
    return render(request, 'questions/ask.html')

def index(request, question_id):
    question_data = None
    for q in QUESTION_LIST:
        if q['id'] == question_id:
            question_data = q
            break

    if question_data is None:
        raise Http404("Вопрос не найден")

    question_answers = [a for a in ANSWERS if a['question_id'] == question_id]

    sorted_answers = sorted(question_answers, key=lambda a: (a['is_correct'], a['rating']), reverse=True)

    context = {
        'question': question_data,
        'answers': sorted_answers, # Передаем ответы в шаблон
    }

    return render(request, 'questions/index.html', context)

def tags(request, tag):
    filtered_questions = [q for q in QUESTION_LIST if tag in q['tag']]

    sorted_questions = sorted(filtered_questions, key=lambda q: q['rating'], reverse=True)

    page_obj = paginate(sorted_questions, request, per_page=2)

    context = {
        'questions': sorted_questions,
        'current_tag': tag
    }
    return render(request, 'questions/tags.html', context)
