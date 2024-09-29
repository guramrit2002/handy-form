import html


def get_field_type_choices(FIELD_TYPE_CHOICES):
    return [key for key, _ in FIELD_TYPE_CHOICES]


def clean_html(raw_html):
    return  html.unescape(raw_html)


