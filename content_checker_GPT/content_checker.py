import json
import requests

def remove_first_and_last_line(s):
    lines = s.split('\n')
    if len(lines) <= 2:
        return '' 
    return '\n'.join(lines[1:-1])
def gpt_api(base64_image,data,api_key, i_test=0):
    print("checking content")
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"}
    payload = {
        "model": "gpt-4o",
        "messages": [
          {
            "role": "user",
            "content": [
              {
                "type": "text",
                "text": f"""
                    the included image is a scanned invoice, can u check if this data is contained in it and valid	:
                    {data}
                    answer should be field_name:true/false, if it doesn't appear on the invoice check if it can be deducted from the context and set it true,
                    the response should be in json format without comments
                """
          },
          {
            "type": "image_url",
            "image_url": {
              "url": f"data:image/jpeg;base64,{base64_image}"
            }
          }
        ]
      }
    ],
    "max_tokens": 300
    }
    try:
      response_GPT = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
      try:
          response=remove_first_and_last_line(response_GPT.json()['choices'][0]['message']['content'])   
          print(response_GPT)
          response=json.loads(response)
          return response,200
      except:
          if i_test==3:
              return "Error, while trying to connect to OpenAi .\nPlease check your Key",400
          return gpt_api(base64_image,data,api_key,i_test+1)
    except:
      return "please check your internet connection",400

     