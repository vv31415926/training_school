from django.contrib import admin
from .models import *

admin.site.register( Task )
admin.site.register( Version )
admin.site.register( Lesson )
admin.site.register( Theme )
admin.site.register( Partition )
admin.site.register( Level )