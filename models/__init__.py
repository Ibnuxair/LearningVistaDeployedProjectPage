#!/usr/bin/python3
"""
initialize the models package
"""

from os import getenv


storage_t = getenv("LV_TYPE_STORAGE")

if not storage_t:
    raise EnvironmentError("LV_TYPE_STORAGE is not set.")
elif storage_t == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    raise ValueError(f"Unsupported storage type: {storage_t}")
