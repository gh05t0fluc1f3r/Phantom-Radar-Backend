from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess

scheduler = BlockingScheduler()

@scheduler.scheduled_job('interval', hours=12)
def scheduled_job():
    print("🕒 Scheduled job running...")
    subprocess.call(["python3", "scripts/fetch_nvd.py"])
    subprocess.call(["python3", "scripts/enrich_threats.py"])

if __name__ == "__main__":
    print("🚀 Starting Phantom Radar Scheduler...")
    scheduler.start()

