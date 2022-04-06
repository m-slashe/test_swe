from flask import Flask, Response, send_from_directory
import aiofiles
import tempfile
import os
import logging

default_format = '%(asctime)s - %(levelname)s - %(message)s'
formatter = logging.Formatter(default_format)

logging.basicConfig(format=default_format,
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

logger = logging.getLogger()

file_handler = logging.FileHandler('test_two.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

app = Flask(__name__)


def get_ok_file_path():
    temp_folder = tempfile.gettempdir()
    return os.path.join(temp_folder, 'ok')


@app.route("/ping")
async def get_ping():
    ok_file_path = get_ok_file_path()
    try:
        async with aiofiles.open(ok_file_path, mode='r') as _:
            pass
        return {'message': 'OK'}
    except:
        return Response(status=503)


@app.route("/img")
async def get_img():
    logger.info('Gif image recovered!')
    return send_from_directory(app.root_path, 'img.gif')
