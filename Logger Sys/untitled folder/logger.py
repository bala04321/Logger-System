#Code by Nallapati Bala Yashaswini
from datetime import datetime, time
from log_node import LogNode

class Logger:
    def __init__(self, capacity=8*60):  # Assuming each log entry represents a minute
        self.head = None
        self.tail = None
        self.count = 0
        self.capacity = capacity

    def log(self, timestamp, severity, message):
        if not self._is_within_operating_hours():
            return False  # Not within operating hours
        if self.count == self.capacity:
            # Overwrite the oldest log entry if at capacity
            self.tail.next = LogNode(timestamp, severity, message, self.head.next)
            self.head = self.head.next
        else:
            new_node = LogNode(timestamp, severity, message)
            if not self.head:
                self.head = new_node
                self.tail = new_node
                new_node.next = new_node  # Circular link
            else:
                new_node.next = self.head
                self.tail.next = new_node
                self.tail = new_node
            self.count += 1
        return True

    def get_logs(self):
        results = []
        current = self.head
        if not current:
            return results
        while True:
            results.append({
                'timestamp': current.timestamp,
                'severity': current.severity,
                'message': current.message
            })
            current = current.next
            if current == self.head:
                break
        return results

    def _is_within_operating_hours(self):
        now = datetime.now().time()
        start_time = time(9, 0)  # 9:00 AM
        end_time = time(17, 0)   # 5:00 PM
        return start_time <= now <= end_time
