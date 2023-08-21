from django.db import models
from django.db.models import Sum
from django.utils.functional import cached_property

class Module(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null= True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    @property
    def module_total_number_of_students(self):
        return self.diversity.aggregate(total_students=Sum('student_count'))['total_students']
    
    @cached_property
    def get_total_students_by_ethnic_group(self, ethnic_group):
        try:
            diversity = Diversity.objects.get(module=self, ethnic_group=ethnic_group)
            return diversity.student_count
        except Diversity.DoesNotExist:
            return 0

    
class Diversity(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='diversity')
    ethnic_group = models.CharField(max_length=50)
    student_count = models.IntegerField()
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ethnic_group} - {self.module}"