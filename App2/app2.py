from flask import Flask, render_template, request

app = Flask(__name__,template_folder="html")

@app.route('/', methods=["GET", "POST"])
def home():
  if request.method == "POST":
    nft = request.form.get("nft")
    recipient = request.form.get("recipient")
    key = request.form.get("key")
    
    if not nft or not recipient or not key:
      error = "all form fields required..."
      return error
    print(f"key: {key}, recipient: {recipient}, nft: {nft}")
  return render_template("home.html")

if __name__ == "__main__":
  app.run(debug=True)