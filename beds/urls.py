from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView, UpdateView

from models import Restaurant, Dish
from forms import RestaurantForm, DishForm
from views import RestaurantCreate, DishCreate, RestaurantDetail, RestaurantList

urlpatterns = patterns('',
    # List latest 5 restaurants: /beds/
    url(r'^$',
        RestaurantList.as_view(),
        name='restaurant_list'),
    # List restaurants: /beds/restaurants.json
    url(r'^restaurants\.(?P<extension>(json|xml))$',
        RestaurantList.as_view(),
        name='restaurant_list_conneg'),

    # Restaurant details, ex.: /beds/restaurants/1/
    url(r'^restaurants/(?P<pk>\d+)/$',
        RestaurantDetail.as_view(),
        name='restaurant_detail'),
    # Restaurant details, ex.: /beds/restaurants/1.json
    url(r'^restaurants/(?P<pk>\d+)\.(?P<extension>(json|xml))$',
        RestaurantDetail.as_view(),
        name='restaurant_detail_conneg'),

    # Create a restaurant: /beds/restaurants/create/
    url(r'^restaurants/create/$',
        RestaurantCreate.as_view(),
        name='restaurant_create'),

    # Edit restaurant details, ex: /beds/restaurants/1/edit/
    url(r'^restaurants/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model=Restaurant,
            form_class=RestaurantForm,
            template_name='beds/form.html'),
        name='restaurant_edit'),

    # Restaurant dish details, ex: /beds/restaurants/1/dishes/1/
    url(r'^restaurants/(?P<pkr>\d+)/dishes/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Dish,
            template_name='beds/dish_detail.html'),
        name='dish_detail'),

    # Create a restaurant dish, ex: /beds/restaurants/1/dishes/create/
    url(r'^restaurants/(?P<pk>\d+)/dishes/create/$',
        DishCreate.as_view(),
        name='dish_create'),

    # Edit restaurant dish details, ex: /beds/restaurants/1/dishes/1/edit/
    url(r'^restaurants/(?P<pkr>\d+)/dishes/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model=Dish,
            form_class=DishForm,
            template_name='beds/form.html'),
        name='dish_edit'),

    # Create a restaurant review using function, ex: /beds/restaurants/1/reviews/create/
    url(r'^restaurants/(?P<pk>\d+)/reviews/create/$',
        'beds.views.review',
        name='review_create'),
)
