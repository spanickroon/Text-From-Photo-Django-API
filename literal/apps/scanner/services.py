import io
import json
import os
from typing import Optional

import cv2
import requests
from rest_framework.response import Response

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

        url: Optional[str] = os.environ.get("OCR_API_URL")

        result: Response = requests.post(
            url,  # type: ignore
            files={f"screenshot{order.extension}": file_bytes},
            data={"apikey": os.environ.get("OCR_API_KEY")},
        )

        result = json.loads(result.content.decode())

        parsed_results = result.get("ParsedResults")[0]
        text_detected = parsed_results.get("ParsedText")

        order.text = text_detected
        order.save()
