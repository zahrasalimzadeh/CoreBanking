import time
from datetime import datetime
from decimal import Decimal
from prometheus_client import Counter, Histogram, Gauge
from DataAccess.Config.database import create_session
from DataAccess.Models.performance_logger import PerformanceLogger

FUNCTION_CALLS = Counter(
    "app_function_calls_total", "Total number of function calls", ["function", "status"]
)
FUNCTION_DURATION = Histogram(
    "app_function_duration_seconds", "Function execution time in seconds", ["function"]
)
LAST_DURATION = Gauge(
    "app_function_last_duration_seconds", "Execution time of the most recent call", ["function"]
)
LAST_CALL_TIMESTAMP = Gauge(
    "app_function_last_call_timestamp_seconds", "Unix timestamp of the most recent call", ["function"]
)


def performance_logger(main_function):
    def wrapper(*args, **kwargs):
        function_name = main_function.__name__
        start_time = time.time()
        output = main_function(*args, **kwargs)
        end_time = time.time()

        execution_time = end_time - start_time

        call_date_time = datetime.now()

        print("Performance Logger")
        print(f"\tFunction Name: '{function_name}'")
        print(f"\tExecution Time: '{execution_time}'")
        print(f"\tCall Date Time: '{call_date_time}'")

        FUNCTION_CALLS.labels(function=function_name, status="success").inc()
        FUNCTION_DURATION.labels(function=function_name).observe(execution_time)
        LAST_DURATION.labels(function=function_name).set(execution_time)
        LAST_CALL_TIMESTAMP.labels(function=function_name).set(end_time)

        with create_session() as session:
            session.add(PerformanceLogger(
                function_name=function_name,
                execution_time=Decimal(f"{execution_time:.10f}"),
                call_date_time=call_date_time
            ))

        return output

    return wrapper