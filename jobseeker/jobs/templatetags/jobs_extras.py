from django import template

#the below allows us to register this django 'filter'
register = template.Library()

#define the 'filter'
def trim_string(some_str):
    return some_str[:25]

#register the filter
register.filter('trim_string', trim_string)