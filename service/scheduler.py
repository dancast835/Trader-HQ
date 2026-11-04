from datetime import timezone
from zoneinfo import ZoneInfo
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from service.strategy_vault import *

scheduler = AsyncIOScheduler(
    timezone=ZoneInfo("America/New_York")
)

def configure_scheduler():
    scheduler.add_job(
        up_and_down,
        trigger="cron",
        day_of_week="mon-fri",
        hour=9,
        minute=35,
        id="up_and_down_market_open",
        replace_existing=True,
        coalesce=True,
        max_instances=1,
        misfire_grace_time=60,
    )
