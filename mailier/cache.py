from django.conf import settings
from django.core.cache import cache
from mailier.models import Msg


def get_cached_msg():
    if settings.CACHE_ENABLED:
        key = 'msg_list'
        msg_list = cache.get(key)
        if msg_list is None:
            msg_list = Msg.objects.all()
            cache.set(key, msg_list)
            return msg_list
        return msg_list