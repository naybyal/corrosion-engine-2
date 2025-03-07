from rest_framework import serializers
from .models import Analysis, TranslationTask
from .serializers import TranslationTaskSerializer

class TranslationTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TranslationTask
        fields = ['id', 'source_code', 'status', 'created_at']

class AnalysisSerializer(serializers.ModelSerializer):
    translation_task = TranslationTaskSerializer(read_only=True)
    
    class Meta:
        model = Analysis
        fields = ['id', 'translation_task', 'c_execution_time', 'rust_execution_time',
                  'c_memory_usage', 'rust_memory_usage', 'result_summary', 'created_at']