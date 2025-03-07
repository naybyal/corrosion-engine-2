import subprocess
import time

def run_program(binary_path):
    """
    Runs the given binary and returns the execution time.
    For a real-world scenario, consider using more robust measurement tools.
    """
    start_time = time.time()
    subprocess.run([binary_path], check=True)
    end_time = time.time()
    return end_time - start_time

def perform_analysis(c_binary, rust_binary):
    """
    Run both the C and Rust binaries and return their execution times.
    In a production setting, add error handling and memory usage measurement.
    """
    c_time = run_program(c_binary)
    rust_time = run_program(rust_binary)
    
    # Dummy memory usage values; replace with actual measurements if needed.
    c_memory = 50.0   # example in MB
    rust_memory = 45.0
    
    summary = f"C is slower by {c_time - rust_time:.4f} seconds." if c_time > rust_time else f"Rust is slower by {rust_time - c_time:.4f} seconds."
    return {
        "c_execution_time": c_time,
        "rust_execution_time": rust_time,
        "c_memory_usage": c_memory,
        "rust_memory_usage": rust_memory,
        "result_summary": summary,
    }
