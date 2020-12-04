mkdir sketchKeras/weights
curl -sc /tmp/cookie "https://drive.google.com/uc?export=download&id=1Zo88NmWoAitO7DnyBrRhKXPcHyMAZS97" > /dev/null
CODE="$(awk '/_warning_/ {print $NF}' /tmp/cookie)"
curl -Lb /tmp/cookie "https://drive.google.com/uc?export=download&confirm=${CODE}&id=1Zo88NmWoAitO7DnyBrRhKXPcHyMAZS97" -o sketchKeras/weights/model.pth