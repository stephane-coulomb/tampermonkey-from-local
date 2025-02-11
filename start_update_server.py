from flask import Flask
from flask_autoindex import AutoIndex
import os

print("#### Starting update server...")
print("#### You can now trigger update your files from http://localhost:5008/")


app = Flask(__name__)

ppath = os.getcwd()  # Update your own parent directory here

AutoIndex(app, browse_root=os.path.join(ppath,"scripts"))

if __name__ == "__main__":
    app.run(debug=True, port=5008)
