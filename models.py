# corrosion/models.py

from django.db import models
from django.contrib.auth.models import User

class SourceCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="source_codes", null=True, blank=True)
    code = models.TextField(help_text="The original C code submission.")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"SourceCode {self.id}"

class TranslationTask(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]
    source_code = models.ForeignKey(SourceCode, on_delete=models.CASCADE, related_name="translation_tasks")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"TranslationTask {self.id} - {self.status}"

class TranslationResult(models.Model):
    translation_task = models.OneToOneField(TranslationTask, on_delete=models.CASCADE, related_name="result")
    rust_code = models.TextField(null=True, blank=True, help_text="The generated Rust code.")
    compilation_logs = models.TextField(null=True, blank=True, help_text="Compilation logs or errors.")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"TranslationResult for Task {self.translation_task.id}"

class Analysis(models.Model):
    """
    Stores performance analysis for the translation task.
    It will compare the execution of the original C code and the generated Rust code.
    """
    translation_task = models.OneToOneField(TranslationTask, on_delete=models.CASCADE, related_name="analysis")
    c_execution_time = models.FloatField(help_text="Execution time in seconds for the C program")
    rust_execution_time = models.FloatField(help_text="Execution time in seconds for the Rust program")
    c_memory_usage = models.FloatField(null=True, blank=True, help_text="Memory usage in MB for the C program")
    rust_memory_usage = models.FloatField(null=True, blank=True, help_text="Memory usage in MB for the Rust program")
    result_summary = models.TextField(null=True, blank=True, help_text="Summary of performance differences")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Analysis for Task {self.translation_task.id}"
