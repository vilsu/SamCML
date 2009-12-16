{% extends "homepage.html" %}

{% block title %}Codes{% endblock %}

{% block headline %}Sam codes{% endblock %}

{% block link %} Send Your Answer {% endblock %}

{% block content %}
    <ul>
    {% for code in codes %}<li>{{ code }}</li>{% endfor %}
    </ul>
{% endblock %}
