from flask import Flask, render_template
from search import SearchForm
import os
import pandas as pd

df=pd.read_csv('rankingExample.csv')
print(df)
docs= df.loc[df["query"].str.contains("mathematician" ,"docid")]
print(docs)
app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/')
def index():
    return render_template('index.html')

@app.context_processor
def base():
	form = SearchForm()
	return dict(form=form)

@app.route('/search', methods=["POST"])
def search():
	form = SearchForm()
	print(form.searched)
	#doclist = df["query"].str.contains(form.searched)
	# dbsearch = dbsearch.query
	if form.validate_on_submit():
		# Get data from submitted form
	
		#Query the Database
		

		print("test")

	return render_template("search.html",
		 form=form,
		 searched = form.searched.data,
		#docs= ("test"))
		# should be between 31- 43 if validate and submit
		docs= df.loc[df["query"].str.contains(form.searched.data)].to_string())


	






	