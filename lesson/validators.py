from rest_framework.serializers import ValidationError


class LinkValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field)
        if 'youtube.com' not in tmp_val:
            raise ValidationError('The link is not valid')
