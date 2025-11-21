import sys

if len(sys.argv) == 3:
    filename = sys.argv[1]
    extension = sys.argv[2]
else:
    filename = "program1"
    extension = "pdf"

if extension == "jpeg" or extension == "png":
    print("It is an image!!")
elif extension == "HDR" or extension == "mp4":
    print("It is a video!!")
elif extension == "pdf" or extension == "txt":
    print("It is a document!!")
else:
    print("Invalid output")
