from flask import Flask, render_template, redirect, url_for, request, make_response, session, abort
#from .session_interface import MySessionInterface
from itsdangerous import Signer, BadSignature
app = Flask(__name__)
app.secret_key = b"gfdgd"
#app.session_interface = MySessionInterface()
##app.run() çalıştırma seçeneği

def get_current_username():
    email = ""
    login_auth = False
    if 'email' in session:  # login.html e yönlendirilmiştir.
        email = session['email']
        login_auth = True
    return email, login_auth

@app.route("/")
def Index():
    email, login_auth = get_current_username() #Kullanıcı doğru paraola ve şifre girdidğinde her sayfayı ziyaret etmesi sağlanır.
    return render_template("index.html", email=email, login_auth=login_auth) #index.html döndürmek için


@app.route("/about")
def About():
    email, login_auth = get_current_username()
    return render_template("about.html", email=email, login_auth=login_auth)


@app.route("/projects")
def Projects():
    email, login_auth = get_current_username()
    return render_template("projects.html", email=email, login_auth=login_auth)


@app.route("/contact")
def Contact():
    email, login_auth = get_current_username()
    return render_template("contact.html", email=email, login_auth=login_auth)


@app.route("/contactlist") #Yönlendirilecek linkler.
def ContactList():
    email, login_auth = get_current_username()
    return render_template("contact_list.html", email=email, login_auth=login_auth)


@app.route("/landscaping") #Yönlendirilecek linkler.
def Landscaping():
    email, login_auth = get_current_username()
    return render_template("landscaping.html", email=email, login_auth=login_auth)


# Kullanıcıyı Login işleminde sonra sayfalara yönlendiren fonk...
@app.route("/login", methods=['GET', 'POST'])
def Login():
    if request.method == 'POST':
        if request.form:
            if 'email' in request.form and 'password' == request.form:
                email = request.form['email'] # email değeri alınır, fonksiyona atanır.
                password = request.form['password'] # loginden alının email ve pass. değişken olarak atanır.
                if email == 'admin' and password == 'admin':
                    session['email']=email #sessionda görüyorsak login olmuştur, göremiyorsak olamamıştır.
                    return redirect(url_for('Index')) # Index fonk. yönlendirir.
                else:
                    return redirect(url_for('Login'))
        abort(400) # hata kodu döndürür.
    email, login_auth = get_current_username()
    return render_template("login.html", email = email, login_auth=login_auth)