from django.contrib import admin
from .models import User,Instruction

# Register your models here.
admin.site.register(User)
class InstructionAdmin(admin.ModelAdmin):
    list=['state']

admin.site.register(Instruction,InstructionAdmin)
