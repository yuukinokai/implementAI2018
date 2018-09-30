import requests
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

# Replace <Subscription Key> with your valid subscription key.
subscription_key = "fb2a1d4c0ddc4948b6c15bbf8c774423"
assert subscription_key

def getDescription(img):

    # You must use the same region in your REST call as you used to get your
    # subscription keys. For example, if you got your subscription keys from
    # westus, replace "westcentralus" in the URI below with "westus".
    #
    # Free trial subscription keys are generated in the westcentralus region.
    # If you use a free trial subscription key, you shouldn't need to change
    # this region.
    vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v2.0/"

    analyze_url = vision_base_url + "analyze"

    # Read the image into a byte array
    image_data = open("./" + img, "rb").read()
    print(image_data)
    headers    = {'Ocp-Apim-Subscription-Key': subscription_key,
                  'Content-Type': 'application/octet-stream'}
    params     = {'visualFeatures': 'Categories,Description,Color'}
    response = requests.post(
        analyze_url, headers=headers, params=params, data=image_data)
    response.raise_for_status()

    # The 'analysis' object contains various fields that describe the image. The most
    # relevant caption for the image is obtained from the 'description' property.
    analysis = response.json()
    #print(analysis)
    image_caption = analysis["description"]["captions"][0]["text"].capitalize()
    return image_caption

    # # Display the image and overlay it with the caption.
    # image = Image.open(BytesIO(image_data))
    # plt.imshow(image)
    # plt.axis("off")
    # _ = plt.title(image_caption, size="x-large", y=-0.1)