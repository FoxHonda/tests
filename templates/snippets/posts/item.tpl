{% load static %}
<div class="item">
	<a href="{% url 'details' pk=item.id %}">
	{% if item.image %}
		<img src="/media/{{ item.image }}" alt="{{ item.image }}">
	{% else %}
		<img src="{% static 'pictures/def.png' %}" alt="default picture">
	{% endif %}
	<h4>{{ item.title }}</h4>
	{% if item.theme %}
		<label>{{ item.theme }}</label>
	{% else	%}	
		<label>&nbsp;</label>
	{% endif %}
	<p>{{ item.description }}</p>
	</a>
</div>