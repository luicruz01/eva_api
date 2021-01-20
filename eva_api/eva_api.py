import requests
import logging

from PIL import Image, UnidentifiedImageError
from io import BytesIO
from flask import Flask, request, send_file

application = Flask(__name__)

logging.basicConfig()
logger = logging.getLogger('main')
logger.setLevel(logging.DEBUG)


@application.route("/image.jpg")
def image():
    log = {
        "session": request.headers.get("X-SESSION-NAME"),
        "side": request.args.get("side"),
        "temperature": 0,
        "error": False
    }
    url = "https://fake-img-endpoint.vercel.app/api/image"
    try:
        response = requests.get(url)
        if response.status_code >= 500:
            log["error"] = True
            logger.error(log)
            return
        im = Image.open(BytesIO(response.content))
        center = im.getpixel((int(im.size[0] / 2), int(im.size[1] / 2)))
        log["temperature"] = (center * 0.04) - 273.15
        im.mode = 'I'
        im.point(lambda i: i * (1. / 256)).convert('L').save("image.jpeg")
        logger.info(log)
        return send_file("image.jpeg", mimetype="image/jpg")
    except UnidentifiedImageError:
        log["error"] = True
        logger.error(log)
        return
    except Exception as e:
        logger.error(e)


if __name__ == '__main__':
    application.run()
