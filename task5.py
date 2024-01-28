from apscheduler.schedulers.blocking import BlockingScheduler

def task_to_be_scheduled():
    print("Task executed!")

# Create a scheduler
scheduler = BlockingScheduler()

# Schedule the task to run every 5 seconds
scheduler.add_job(task_to_be_scheduled, 'interval', seconds=5)

# Schedule the task to run daily at a specific time (change the hour and minute accordingly)
scheduler.add_job(task_to_be_scheduled, 'cron', hour=12, minute=0)

# Start the scheduler
try:
    print("Scheduler started. Press Ctrl+C to exit.")
    scheduler.start()
except KeyboardInterrupt:
    print("Scheduler stopped.")
