# questions/context_processors.py
from .views import POPULAR_TAGS, BEST_MEMBERS  # импортируем ваши списки

def global_sidebar_data(request):
    return {
        'popular_tags': POPULAR_TAGS,
        'best_members': BEST_MEMBERS,
    }
