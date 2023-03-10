from flask import Flask, render_template, request, redirect, url_for, session, flash
from wtforms.validators import DataRequired
from testing import *
import torch

import torch, torchdata, torchtext
from torch import nn
import torch.nn.functional as F

import random, math, time

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
SEED = 1234
torch.manual_seed(SEED)
torch.backends.cudnn.deterministic = True

variants = 'general'
save_path = './models/Seq2SeqPackedAttention.pt'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'
app.config['UPLOAD_FOLDER'] = 'static/files' 

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/mt', methods = ['GET','POST'])
def machinetranslation():
    if request.method == 'POST':
        source = request.form.get('source')
        predict = translation(source, variants, save_path, device)
        #predict = translation(source, variants, save_path, map_location=torch.device(device))

    else:
        source = ' '
        predict = ' '
    data = {"source":source, "predict":predict}
    return render_template("mt.html", data = data)

if __name__ == "__main__":
    app.run(debug=True)
