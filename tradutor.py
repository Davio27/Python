# import requests
# from api_key import api_key

# url = "https://text-translator2.p.rapidapi.com/translate"

# text = input('Insira o texto para ser traduzido: ')

# payload = {
#     "sourcer_language": "pt",
#     "target_language": "en",
#     "text": text
# }

# headers = {
#     "content-type": "application/x-www-form-urlencoded",
#     "X-RapidAPI-Key": api_key,
#     "X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
# }

# response = requests.post(url, data=payload, headers=headers)
# print(response.json()['data']['translatedText'])
import requests

url = "https://google-translate1.p.rapidapi.com/language/translate/v2/detect"

payload = { "q": "English is hard, but detectably so" }
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"Accept-Encoding": "application/gzip",
	"X-RapidAPI-Key": "a1ad93f3d0mshf6eb937f40dfc2fp1a50cfjsnd14caf1ccd9f",
	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
}

response = requests.post(url, data=payload, headers=headers)

print(response.json())
