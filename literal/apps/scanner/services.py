import io
import json
import os

import cv2
import requests

from apps.order.models import Order


class ScannerService:
    @staticmethod
    def scan_image(order_id: int) -> None:
        order = Order.objects.get(pk=order_id)
        order.status = order.PROCESSING

        order.save()

        img = cv2.imread(order.image.path)
        height, width, _ = img.shape
        roi = img[0:height, 0:width]

        _, compressed_image = cv2.imencode(order.extension, roi, [1, 90])
        file_bytes = io.BytesIO(compressed_image)

        result = requests.post(
            os.environ.get("OCR_API_URL"),
            files={"screenshot.jpg": file_bytes},
            data={"apikey": os.environ.get("OCR_API_KEY"), "language": order.language},
        )

        result = result.content.decode()
        result = json.loads(result)

        parsed_results = result.get("ParsedResults")[0]
        text_detected = parsed_results.get("ParsedText")

        order.text = text_detected
        order.save()
