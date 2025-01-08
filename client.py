from flask import Flask, request, Response
from gtts import gTTS
app = Flask(__name__)

# 다건 gtts 저장
@app.route('/gtts/list', methods=['POST'])
def gtts_list_post():
  params = request.get_json()

  for param in params:
    text = param['text']
    lang = param['lang']
    save_path = param['savePath']

    gtts_save(text, lang, save_path)

  return Response(status=201)

# 단건 gtts 저장
@app.route('/gtts', methods=['POST'])
def gtts_post():
  params = request.get_json()
  print(params)

  text = params['text']
  lang = params['lang']
  save_path = params['savePath']

  gtts_save(text, lang, save_path)

  return Response(status=201)

def gtts_save(text, lang, save_path):
  result = gTTS(
    text=text,
    lang=lang,
    slow=False,
    tld="com"
  )

  result.save(save_path)

def gtts_save(text, lang, save_path):
  result = gTTS(
    text=text,
    lang=lang,
    slow=False,
    tld="com"
  )

  result.save(save_path)

if __name__ == '__main__':
  app.run(port=6000, host="0.0.0.0")