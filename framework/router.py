"""Serverless: stateless functions triggered by events, invoked on demand.
No servers to manage; function runs when an event fires."""
import time


class EventRouter:
    def __init__(self):
        self.routes = {}  # event_type -> [function]

    def on(self, event_type):
        def decorator(fn):
            self.routes.setdefault(event_type, []).append(fn)
            return fn
        return decorator

    def emit(self, event_type, payload):
        results = []
        for fn in self.routes.get(event_type, []):
            started = time.monotonic()
            out = fn(payload)
            elapsed = (time.monotonic() - started) * 1000
            results.append((fn.__name__, out, f"{elapsed:.1f}ms"))
        return results
