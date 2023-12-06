from django.contrib import admin
from movie_app.models import Director, Movie, Review

admin.site.register(Director)
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'duration', 'description')
    list_filter = ('director',)
    search_fields = ('title',)
    # readonly_fields = ('',)
    list_per_page = 1
    ordering = ('title',)


admin.site.register(Review)

