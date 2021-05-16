from apps.order.models import Order


class ScannerService:
    @staticmethod
    def scan_image(order_id: int) -> None:
        order = Order.objects.get(pk=order_id)
        order.status = order.PROCESSING

        order.save()
