{% load static %}
<div class="item">
	<a href="{% url 'details' pk=id %}">
	{% if image %}
		<img src="/media/{{ image }}" alt="{{ image }}">
	{% else %}
		<img src="{% static 'pictures/def.png' %}" alt="default picture">
	{% endif %}
	<h4>{{ title }}</h4>
	<p>{{ description }}</p>
	</a>
</div>