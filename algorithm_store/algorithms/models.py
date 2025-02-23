from django.db import models

class Algorithm(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    visualization_code = models.TextField()  # Can store the code for visualizations (e.g., D3.js code)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
