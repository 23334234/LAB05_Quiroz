from django.contrib import admin, messages

# Register your models here.
from .models import Categoria, Producto, Cliente

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pub_date') 
    search_fields = ('nombre', 'pub_date')
    ordering = ('-nombre',)
    date_hierarchy = 'pub_date'

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos','dni', 'telefono')
    search_fields = ('nombres', 'dni')

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'stock', 'pub_date')
    list_display_links = ('nombre',)
    list_filter = ('categoria', 'pub_date')
    search_fields = ('nombre', 'categoria')
    ordering = ('pub_date',)
    list_per_page = 3
    
    
    actions = ['actualizar_stock']
    
    def actualizar_stock(self, request, queryset):
        """
        Acción personalizada para actualizar el stock de los productos seleccionados a 20.
        """
        total_actualizado = queryset.update(stock=20)
        self.message_user(request, f"Se ha actualizado el stock de {total_actualizado} productos a 20 unidades.", messages.SUCCESS)

    actualizar_stock.short_description = "Actualizar stock a 20 unidades"

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Producto, ProductoAdmin)


admin.site.site_header = 'Mi Panel de Administración'
admin.site.index_title = 'Panel de control de Mi App'
admin.site.site_title = 'Gestión de Mi App'

