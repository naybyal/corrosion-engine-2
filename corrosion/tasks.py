# corrosion/tasks.py

from celery import shared_task
from .models import TranslationTask, Analysis
from .utils.performance import perform_analysis

@shared_task
def run_performance_analysis(task_id, c_binary_path, rust_binary_path):
    """
    Run performance analysis on the given binaries and store the results.
    """
    try:
        # Get the TranslationTask instance
        task = TranslationTask.objects.get(id=task_id)
        
        # Perform the analysis using the utility function
        results = perform_analysis(c_binary_path, rust_binary_path)
        
        # Create and save an Analysis record linked to the translation task
        Analysis.objects.create(
            translation_task=task,
            c_execution_time=results["c_execution_time"],
            rust_execution_time=results["rust_execution_time"],
            c_memory_usage=results["c_memory_usage"],
            rust_memory_usage=results["rust_memory_usage"],
            result_summary=results["result_summary"]
        )
        return "Analysis completed successfully."
    except Exception as e:
        # Log exception details here (or update the TranslationTask status if needed)
        return f"Analysis failed: {str(e)}"
