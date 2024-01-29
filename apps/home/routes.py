

from apps.home import blueprint
from flask import render_template, request,redirect,url_for
from flask_login import login_required, current_user
from jinja2 import TemplateNotFound
from fileinput import filename
import os
from datetime import datetime
import sqlite3
from werkzeug.utils import secure_filename



current_directory = os.getcwd()

print("Current Directory:", current_directory)
global jsonath2
new=os.path.join(current_directory,'apps')
jsonath1=os.path.join(new,'data.sqlite3')

dd=datetime.today().strftime('%Y-%m-%d')
DB_NAME=jsonath1



@blueprint.route('/index')
@login_required
def index():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    query = 'SELECT * FROM videodata'
    cursor.execute(query)
    data = cursor.fetchall()

    


    return render_template('home/dashboard.html', 
                           segment='index', 
                           user_id=current_user.id,data=data)




@blueprint.route('/<template>')
@login_required
def route_template(template):

    print(current_user)

    conn1 = sqlite3.connect(DB_NAME)
    cursor1 = conn1.cursor()
    query1 = f"SELECT * FROM videodata WHERE user='{current_user}'"
    cursor1.execute(query1)
    data1 = cursor1.fetchall()

    conn2 = sqlite3.connect(DB_NAME)
    cursor2 = conn2.cursor()
    query2=f"SELECT count(*) FROM videodata WHERE user='{current_user}'"
    cursor2.execute(query2)
    data2 = cursor2.fetchall()
    datax=data2[:-3]
    print(datax)

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment,data1=data1,current_user=current_user,data3=str(data2)[2:-3])

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500



@blueprint.route('/uploads',methods=['GET','POST'])
@login_required
def uploads():
    
    current_datetime = datetime.now()

    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S.%f")

    print(formatted_datetime)
    n = request.form.get('Cotegary')
    n1 = request.form.get('name')
    n2 = request.form.get('desc')
    n3 = request.files['video']  # Use square brackets to access files, not parentheses
    n4 = request.files['thumb']  # Similarly here


    n3.save(f"apps/static/videos/{n3.filename}")

    n4.save(f'apps/static/Thumpnails/{n4.filename}')

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    query = f"INSERT INTO videodata (videoid,user,time,thumnail,categary,desc) VALUES ('static/videos/{n3.filename}', '{current_user}','{formatted_datetime}', 'static/Thumpnails/{n4.filename}', '{n}','{n2}')"
    cursor.execute(query)
    data = cursor.fetchall()
    conn.commit()


    return redirect(url_for('home_blueprint.route_template', template='upload'))

def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
