from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html',
                         title='Home Page',
                         msg = 'This is my Message')

@app.route('/user/info')
def info():
  return render_template('info.html',
                         title='Info Page',
                         name='Pimonpan Jantaramanee',
                         email='std.67122420326@ubru.ac.th',
                         mobile='081-111-1111',
                         age=21)

@app.route('/favorite/sports')
def fav_sports():
  sports = ['Football','Basketball','Volleyball']
  return render_template('favorite_sports.html',
                         title='Favorite Sports Page',
                         sports=sports)

@app.route('/favorite/foods')
def fav_foods():
  title = 'Favorite Foods Page'
  foods = ['ข้าวหน้าเป็ด','บะหมี่','ไก่ย่าง','ส้มตำ','ผัดไทย','ข้าวผัด','ข้าวมันไก่']
  return render_template('favorite_foods.html',
                         title=title,
                         foods=foods)