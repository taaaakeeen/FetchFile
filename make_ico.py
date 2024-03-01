from PIL import Image

PNG_FILE_NAME = "FetchFile.png"
ICO_FILE_NAME = "FetchFile.ico"
img = Image.open(PNG_FILE_NAME)
img.save(ICO_FILE_NAME, format="ICO", sizes=[(256, 256)])