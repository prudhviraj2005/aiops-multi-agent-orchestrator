class NotifierTool:
    def notify(self, channel: str, message: str):
        return {
            "channel": channel,
            "message": message,
            "status": "SENT"
        }
