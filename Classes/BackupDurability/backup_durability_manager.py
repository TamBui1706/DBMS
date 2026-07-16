class BackupDurabilityManager:
    def __init__(self):
        self.backupManager = None
        self.restoreManager = None
        self.recoveryManager = None
        self.checkpointMgr = None

