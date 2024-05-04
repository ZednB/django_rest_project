from rest_framework.serializers import ValidationError


class UrlValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        url = 'https://www.youtube.com/'
        if url not in str(value):
            raise ValidationError('Вы не можете прикреплять ссылки на сторонние ресурсы')
