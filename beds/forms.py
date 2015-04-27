from django.forms import ModelForm
from beds.models import Restaurant, Dish

class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        exclude = ('user', 'date',)

class DishForm(ModelForm):
    class Meta:
        model = Dish
        exclude = ('restaurant', 'user', 'date',)