import random
from log_generator import logger_obj

users_count = 10
workflow_total_steps = 20
min_time_in_ms = 10
max_time_in_ms = 100

for user_id in range(1, users_count+1):
    current_step = 0
    end_step = workflow_total_steps
    while(current_step < end_step):
        next_step = random.randint(current_step+1, end_step)
        step_time = random.randint(min_time_in_ms, max_time_in_ms)

        log_message = f"user_{user_id},button_{current_step},button_{next_step},{step_time}ms"
        logger_obj.info(log_message)

        current_step = next_step