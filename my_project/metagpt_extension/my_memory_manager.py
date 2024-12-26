"""
my_memory_manager.py
A minimal JSON-based memory manager.
"""
import os
import time
import json

class MemoryManager:
    def __init__(self, store_path="./memory_store.json"):
        self.store_path = store_path
        self.data = {}
        if os.path.exists(store_path):
            with open(store_path, "r") as f:
                try:
                    self.data = json.load(f)
                except:
                    self.data = {}

    def add_entry(self, role_name: str, content: str):
        timestamp = time.time()
        entry = {
            "timestamp": timestamp,
            "role": role_name,
            "content": content
        }
        self.data[str(timestamp)] = entry
        self._save()

    def query_latest(self, role_name: str=None, limit=5):
        items = list(self.data.items())
        items.sort(key=lambda x: float(x[0]), reverse=True)
        if role_name:
            filtered = [v for _,v in items if v["role"]==role_name]
        else:
            filtered = [v for _,v in items]
        return filtered[:limit]

    def _save(self):
        with open(self.store_path, "w") as f:
            json.dump(self.data, f, indent=2)
