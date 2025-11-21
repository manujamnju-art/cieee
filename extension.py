import sys

if len(sys.argv) == 3:
    filename = sys.argv[1]
    extension = sys.argv[2]
else:
    filename = "program1"
    extension = "pdf"

if extension in ["jpeg", "png"]:
    print("It is an image!!")
elif extension in ["HDR", "mp4"]:
    print("It is a video!!")
elif extension in ["pdf", "txt"]:
    print("It is a document!!")
else:
    print("Invalid output")