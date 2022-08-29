from flask import Flask

from pywebio.input import file_upload
from pywebio.output import put_image
from pywebio.platform.flask import webio_view


app = Flask(__name__)


def predict(img):
    ...


def main():
    # File Upload
    img = file_upload("Select a image:", accept="image/*")
    put_image(img['content'], width='224px', height='224px')


app.add_url_rule('/', 'webio_view', webio_view(main), methods=['GET', 'POST'])


if __name__ == "__main__":
    app.run(host='localhost', port=8080)
