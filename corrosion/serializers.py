class AnalysisSerializer(serializers.ModelSerializer):
    translation_task = TranslationTaskSerializer(read_only=True)
    
    class Meta:
        model = Analysis
        fields = ['id', 'translation_task', 'c_execution_time', 'rust_execution_time',
                  'c_memory_usage', 'rust_memory_usage', 'result_summary', 'created_at']