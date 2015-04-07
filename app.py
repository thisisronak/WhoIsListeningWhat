from flask import Flask, render_template

import json, urllib

app = Flask(__name__)

TOP_TRACKS_URL = "http://ws.audioscrobbler.com/2.0/?method=user.getTopTracks&api_key=f03a9ec80e3af7e86173f2a2c5036728&format=json&limit=10&user="


@app.route('/render/topTracks/<user>')
def getTopTracks(user):
  global TOP_TRACKS_URL
  url = TOP_TRACKS_URL+user
  data   = urllib.urlopen(url).read()  
  tracks = json.loads(data)
  print tracks.keys()
  if "error" in tracks.keys():
    return "Following user does not exist"
  # if tracks["toptracks"]["totalPages"]==0:
  #   return "bar"

  topTracks = []
  upto = None
  if len(tracks["toptracks"]["track"])>10:
    upto =10
  else:
    upto = len(tracks["toptracks"]["track"])
  for i in xrange(upto):
    d= {}
    d["name"] = tracks["toptracks"]["track"][i]["name"]
    if "image" in tracks["toptracks"]["track"][i].keys():
      d["img"] = tracks["toptracks"]["track"][i]["image"][0]["#text"]
    else:
      d["img"] = "http://userserve-ak.last.fm/serve/34s/102537525.png"
    d["artist"] = tracks["toptracks"]["track"][i]["artist"]["name"]
    d["url"] = tracks["toptracks"]["track"][i]["url"]
    topTracks.append(d)

  return json.dumps(topTracks) 

@app.route('/')
def index():
  return render_template("base.html")

if __name__ == "__main__":
  app.run(debug=True)
