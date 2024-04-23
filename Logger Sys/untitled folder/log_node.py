#Code by Nallapati Bala Yashaswini
class LogNode:
    def __init__(self, timestamp, severity, message, next=None):
        self.timestamp = timestamp
        self.severity = severity
        self.message = message
        self.next = next
