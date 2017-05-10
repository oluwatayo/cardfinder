from django.contrib import admin
from .models import Card, Specs , CardFound, SpecsFound

admin.site.register(Card)
admin.site.register(Specs)
admin.site.register(CardFound)
admin.site.register(SpecsFound)