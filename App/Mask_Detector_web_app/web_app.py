from pywebio.input import file_upload
from pywebio.output import put_image
from pywebio import start_server


def main():
    # File Upload
    img = file_upload("Select a image:", accept="image/*")
    put_image(img['content'], width='224px', height='224px')


if __name__ == "__main__":
    start_server(main, port=8080, debug=True)
