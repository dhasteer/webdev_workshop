from flask import Flask, redirect, url_for, render_template, request
#from fileinput import filename
#from classify.imgclassify import img_classify

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

"""
@app.route('/about.html')
def loadabout():
    return render_template('about.html')

@app.route('/index.html')
def loadindex():
    return render_template('index.html')

@app.route('/services.html')
def loadservices():
    return render_template('services.html')
    # return render_template('services2.html')

@app.route('/portfolio.html')
def loadportfolio():
    return render_template('portfolio.html')

@app.route('/pricing.html')
def loadpricing():
    return render_template('pricing.html')

@app.route('/contact.html')
def loadcontact():
    return render_template('contact.html')

@app.route('/classify', methods=['POST'])
def loadclassify():
    if request.method == 'POST':
        f = request.files['upload']
        fpath = f'static/img/{f.filename}'
        f.save(fpath)
        classification = img_classify(fpath)
    return render_template('services2.html', result=classification, path=fpath)
"""

if __name__=='__main__':
    app.run(debug=True)
