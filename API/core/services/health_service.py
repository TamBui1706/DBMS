import time
from Classes.Core.database_server import DatabaseServer

class HealthService:
    def __init__(self):
        self.server = DatabaseServer()
        self.server.serverId = "DBMS-Server-01"
        self.server.status = "running"
        self.start_time = time.time()

    def check_health(self):
        return {
            "serverId": self.server.serverId,
            "status": self.server.status,
            "uptime_seconds": int(time.time() - self.start_time),
            "version": "1.0.0-Beta"
        }
