import torch
from PIL import Image
from transformers import AutoModel, AutoTokenizer
import base64
from io import BytesIO

question = """
            the included image is a scanned invoice, can u check if this data is contained in it and valid :
            {data}
            answer should be field_name:true/false, if it doesn't appear on the invoice check if it can be deducted from the context and set it true,
             the response should be without comments and in JSON format
        """
class ContentCheckerMiniCPM:
    def __init__(self):
        self.model, self.tokenizer = None, None
        self.load_CPM("./Model")

    def load_CPM(self,model_path):
        self.model = AutoModel.from_pretrained(f"./{model_path}", trust_remote_code=True)  
        self.tokenizer = AutoTokenizer.from_pretrained(f"./{model_path}", trust_remote_code=True)  


    def base64_to_image_PIL(base64_image):
        image_data = base64.b64decode(base64_image)
        image_bytes = BytesIO(image_data)
        image = Image.open(image_bytes)
        return image
    
    def process_data(self,imageFile,data,prompt_text=question):
        image = Image.open(imageFile)
        msgs = [{'role': 'user', 'content': [image, question.format(data=data)]}]
        try:
            res = self.model.chat(
                image=None,
                msgs=msgs,
                tokenizer=tokenizer
                )      
        except Exception as e:
            print(e)
            return "Error in processing data with CPM error" , 400
        return res,200