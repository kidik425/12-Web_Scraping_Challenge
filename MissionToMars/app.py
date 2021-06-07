from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars as scrape

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def home():
    mars_data = mongo.db.collection.find_one()
    return render_template("index.html", mars=mars_data)


@app.route("/scrape")
def scraper():
    mars_data = scrape.scrape()

    mongo.db.collection.update({}, mars_data, upsert=True)
    
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
