from quart import Quart, request, send_file, render_template
import MinePI
import io

def booler(arg):
	if arg.upper().lower() == "false":
		return False
	elif arg.upper().lower() == "true":
		return True

app = Quart(__name__)

@app.route("/minecraft/skin/<username>")
async def minecraft_skin(username):
	vr = int(request.args.get("vr", -25))
	hr = int(request.args.get("hr", 35))
	hrh = int(request.args.get("hrh", 0))
	vrll = int(request.args.get("vrll", 0))
	vrrl = int(request.args.get("vrrl", 0))
	vrla = int(request.args.get("vrla", 0))
	vrra = int(request.args.get("vrra", 0))
	ratio = int(request.args.get("ratio", 12))
	overlay = booler(request.args.get("overlay", "true"))
	aa = booler(request.args.get("aa", "true"))
	
	img = await MinePI.render_3d_skin(username, vr=vr, hr=hr, hrh=hrh, vrll=vrll, vrrl=vrrl, vrla=vrla, vrra=vrra, ratio=ratio, display_second_layer=overlay, aa=aa)
	img_byte_arr = io.BytesIO()
	img.save(img_byte_arr, format='PNG')
	return await send_file(img_byte_arr, mimetype="image/png", as_attachment=False, attachment_filename='skin.png')

@app.route("/minecraft/head/<username>")
async def minecraft_head(username):
	vr = int(request.args.get("vr", -25))
	hr = int(request.args.get("hr", 35))
	ratio = int(request.args.get("ratio", 12))
	overlay = booler(request.args.get("overlay", "true"))
	aa = booler(request.args.get("aa", "true"))
	
	img = await MinePI.render_3d_head(username, vr=vr, hr=hr, ratio=ratio, display_hair=overlay, aa=aa)
	img_byte_arr = io.BytesIO()
	img.save(img_byte_arr, format='PNG')
	return await send_file(img_byte_arr, mimetype="image/png", as_attachment=False, attachment_filename='head.png')

@app.route("/")
async def index():
	return render_template("index.html")

if __name__ == "name":
  app.run(host="0.0.0.0")
