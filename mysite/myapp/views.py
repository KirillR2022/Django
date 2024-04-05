from django.http import HttpResponse
from django.template.loader import get_template

import logging

logger = logging.getLogger(__name__)


def index(request):
    template = get_template('index.html')
    html = template.render()

    logger.info("Посетили главную страницу")
    return HttpResponse(html)


def about(request):
    template = get_template('about.html')
    html = template.render()

    logger.info("Посетили страницу 'О себе'")
    return HttpResponse(html)
