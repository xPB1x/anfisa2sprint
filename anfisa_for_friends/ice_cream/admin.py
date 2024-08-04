from django.contrib import admin
from .models import Category, Topping, Wrapper, IceCream


class IceCreamAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper',
    )
    list_editable = (
        'is_published',
        'is_on_main',
        'category'
    )
    search_fields = ('title',) 
    list_filter = ('category',)
    list_display_links = ('title',)
    filter_horizontal = ('toppings',)


class IceCreamInline(admin.StackedInline):
    model = IceCream
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        IceCreamInline,
    ]


class WrapperAdmin(admin.ModelAdmin):
    inlines = [IceCreamInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Topping)
admin.site.register(Wrapper, WrapperAdmin)
admin.site.register(IceCream, IceCreamAdmin)
admin.site.empty_value_display = 'Не задано'
