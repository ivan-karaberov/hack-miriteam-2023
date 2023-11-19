import datetime

from services.checkDB import get_daily_stat

import config


async def stat():
    stat = await get_daily_stat()
    zones = [0]*3

    for s in stat:
        zones[s["now_status"]] += 1

    info = {
        "doc_cat": "Производство-склад",
        "doc_created": f"Документ сформирован в: {datetime.datetime.now().strftime(config.DATETIME_FORMAT)}",
        "all": f"Всего произведено - {sum(zones)}",
        "z0": f"В зоне 0 - {zones[0]}",
        "z1": f"В зоне 1 - {zones[1]}",
        "z2": f"В зоне 2 - {zones[2]}"
    }

    return  {"info": info, "stat": stat}