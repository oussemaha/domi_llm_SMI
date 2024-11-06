import torch
from PIL import Image
from transformers import AutoModel, AutoTokenizer
import base64

def load_CPM():
    model = AutoModel.from_pretrained("./Model", trust_remote_code=True)  
    tokenizer = AutoTokenizer.from_pretrained("./Model", trust_remote_code=True)  
    return model, tokenizer

def base64_to_image_PIL(base64_image):
    image_data = base64.b64decode(base64_string)
    image_bytes = BytesIO(image_data)
    image = Image.open(image_bytes)
    return image

def minicpm_api(base64_image,data,model,tokenizer):
    image = base64_to_image_PIL(base64_image)
    question = f"""
        the included image is a scanned invoice, can u check if this data is contained in it and valid :
        {data}
        answer should be field_name:true/false, if it doesn't appear on the invoice check if it can be deducted from the context and set it true,
         the response should be without comments and in JSON format
    """
    msgs = [{'role': 'user', 'content': [image, question]}]
    res = model.chat(
        image=None,
        msgs=msgs,
        tokenizer=tokenizer
        )   
    return res,200