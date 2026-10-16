"""Demo: serverless functions triggered by events."""
from framework.router import EventRouter


def main():
    router = EventRouter()

    @router.on("order.created")
    def send_email(evt):
        return f"email sent to {evt['user_id']} for order {evt['order_id']}"

    @router.on("order.created")
    def update_inventory(evt):
        return f"inventory deducted for order {evt['order_id']}"

    @router.on("payment.received")
    def confirm_order(evt):
        return f"order {evt['order_id']} confirmed after payment"

    print("--- Emit order.created: two functions run ---")
    for name, out, ms in router.emit("order.created", {"order_id": "o_1", "user_id": "alice"}):
        print(f"  [{name}] {out} ({ms})")

    print("\n--- Emit payment.received: confirm function runs ---")
    for name, out, ms in router.emit("payment.received", {"order_id": "o_1"}):
        print(f"  [{name}] {out} ({ms})")

    print("\n== all cases done ==")


if __name__ == "__main__":
    main()
