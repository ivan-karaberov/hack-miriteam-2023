import datetime
import pytz

import db
import config


async def check_in_db(val: str):
    sql = f"SELECT * FROM pallet WHERE id=?"
    return await db.fetch_one(sql=sql, params=[val])


async def add_to_db(val: str, status: int):
    if await check_in_db(val) is None:
        sql = """INSERT INTO pallet(id, now_status, changed)VALUES (?, ?, ?)"""
        await db.execute(sql, [val, status, _get_now_formatted()])
        return {"status": 200}
    return {"status": 0}


async def update_in_db(id: str, status: int):
    if await check_in_db(id) is not None:
        sql="UPDATE pallet SET now_status=? WHERE id=?"
        await db.execute(sql, [status, id])
        return {"status": 200}
    return {"status": 0}


async def delete_from_db(id: str):
    if await check_in_db(id) is not None:
        sql = "DELETE FROM pallet WHERE id=?"
        await db.execute(sql, [id])
        return {"status": 200}
    return {"status": 0}


async def get_daily_stat():
    now = _get_now_datetime()
    today = f'{now.year:04d}-{now.month:02d}-{now.day}'
    sql = f"""SELECT id, now_status, changed FROM pallet
              WHERE changed >= '{today}' ORDER BY now_status"""
    row = await db.fetch_all(sql)
    return row


def _get_now_formatted() -> str:
    """Возвращает настоящую Дату и время строкой"""
    return _get_now_datetime().strftime(config.DATETIME_FORMAT)


def _get_now_datetime() -> datetime.datetime:
    """Возвращает настоящую Дату и время"""
    tz = pytz.timezone(config.TIMEZONE)
    return datetime.datetime.now(tz)