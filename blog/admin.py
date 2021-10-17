from django.contrib import admin
from .models import Category, Post

# video del curso para crear las entradas y categorias
# se quiere filtrar por entradas y categorias

# 1.- mover vista a las vistas dentro de blog
# crear una carpeta template, mover la template

# 2.- crear una carpeta templates en app blog y mover blog.html
#  y una entrada url html y moverlo blog.html (quitar blog de core)
# en ur blog, 
# crear una entrad en el url de la app blog para dejarlo apuntando en la raiz de url de blog
# en los url del core apuntarlo con el include

# importar los post en en la vista blog; recuperarn todos los post post.objects.all() y se pasan en el direccionario 
# de contexto

# ir al template blog y editar (el original) que viene estático haciendo un bucle





# en web empresa el include del path /blog


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('title','author','published','post_categories')
    ordering = ('author','published')
    list_filter = ('author__username','category__name')
    search_fields = ('title', 'author__username','category__name')

    def post_categories(self, obj):
        return ",".join([c.name for c in obj.category.all().order_by("name")])

    #sobreescribir el motodo para que en vez de categorais en el encabezamiento aparezca categorias
    post_categories.short_description = "categorias"


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
