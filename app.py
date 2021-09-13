from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///invoice.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Jiggidiboo(db.Model):
    
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200),nullable =False)
    org = db.Column(db.String(200),nullable =False)
    addr = db.Column(db.String(200),nullable =False)
    phone = db.Column(db.String(200),nullable =False)
    desc1 = db.Column(db.String(200),nullable =False)
    qnt1 = db.Column(db.Integer,nullable =False)
    up1 = db.Column(db.Integer,nullable =False)

    desc2 = db.Column(db.String(200),nullable =False)
    qnt2 = db.Column(db.Integer,nullable =False)
    up2 = db.Column(db.Integer,nullable =False)
    desc3 = db.Column(db.String(200),nullable =False)
    qnt3 = db.Column(db.Integer,nullable =False)
    up3 = db.Column(db.Integer,nullable =False)
    desc4 = db.Column(db.String(200),nullable =False)
    qnt4 = db.Column(db.Integer,nullable =False)
    up4 = db.Column(db.Integer,nullable =False)
    desc5 = db.Column(db.String(200),nullable =False)
    qnt5 = db.Column(db.Integer,nullable =False)
    up5 = db.Column(db.Integer,nullable =False)
    desc6 = db.Column(db.String(200),nullable =False)
    qnt6 = db.Column(db.Integer,nullable =False)
    up6 = db.Column(db.Integer,nullable =False)
    desc7 = db.Column(db.String(200),nullable =False)
    qnt7 = db.Column(db.Integer,nullable =False)
    up7 = db.Column(db.Integer,nullable =False)
    desc8 = db.Column(db.String(200),nullable =False)
    qnt8 = db.Column(db.Integer,nullable =False)
    up8 = db.Column(db.Integer,nullable =False)
    desc9 = db.Column(db.String(200),nullable =False)
    qnt9 = db.Column(db.Integer,nullable =False)
    up9 = db.Column(db.Integer,nullable =False)
    desc10 = db.Column(db.String(200),nullable =False)
    qnt10 = db.Column(db.Integer,nullable =False)
    up10 = db.Column(db.Integer,nullable =False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    tot_am = db.Column(db.Integer,nullable =False)
    perc = db.Column(db.Integer,nullable =False)
    tot_tot = db.Column(db.Integer,nullable =False)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.name} - {self.org} - {self.addr} - {self.phone} - {self.desc1} - {self.qnt1} - {self.up1} - {self.am1} - {self.desc2} - {self.qnt2} - {self.up2} - {self.am2}-{self.desc3} - {self.qnt3} - {self.up3} - {self.am3} - {self.desc4} - {self.qnt4}- {self.up4}-{self.am4}"



@app.route("/invoice", methods=['GET','POST'])
def Invoice():

    if request.method == 'POST':
        name = request.form['name']
        org = request.form['org']
        addr = request.form['addr']
        phone = request.form['phone']
        desc1 = request.form['desc1'] 
        qnt1 = request.form['qnt1']
        up1 = request.form['up1']
        desc2 = request.form['desc2'] 
        qnt2 =request.form['qnt2']
        up2 = request.form['up2']
        desc3 = request.form['desc3'] 
        qnt3 =request.form['qnt3']
        up3 = request.form['up3']
        desc4 = request.form['desc4'] 
        qnt4 = request.form['qnt4']
        up4 = request.form['up4']

        desc5 = request.form['desc5'] 
        qnt5 = request.form['qnt5']
        up5 = request.form['up5']
        desc6 = request.form['desc6'] 
        qnt6 = request.form['qnt6']
        up6 = request.form['up6']
        desc7 = request.form['desc7'] 
        qnt7 = request.form['qnt7']
        up7 = request.form['up7']
        desc8 = request.form['desc8'] 
        qnt8 =request.form['qnt8']
        up8 = request.form['up8']

        desc9 = request.form['desc9'] 
        qnt9 =request.form['qnt9']
        up9 = request.form['up9']

        desc10 = request.form['desc10'] 
        qnt10 = request.form['qnt10']
        up10 = request.form['up10']

        perc = request.form['tax-info']
        amount1 = int(qnt1) * int(up1)
        amount2 = int(qnt2) * int(up2)
        amount3 = int(qnt3) * int(up3)
        amount4 = int(qnt4) * int(up4)
        amount5 = int(qnt5) * int(up5)
        amount6 = int(qnt6) * int(up6)
        amount7 = int(qnt7) * int(up7)
        amount8 = int(qnt8) * int(up8)
        amount9 = int(qnt9) * int(up9)
        amount10 = int(qnt10) * int(up10)

        tot_am = amount1 + amount2 + amount3 + amount4 + amount5 + amount6 + amount7 + amount8 + amount9 + amount10

        tot_perc = (float(perc)/100) * float(tot_am)

        tot_tot = tot_perc + tot_am

        invoicec = Jiggidiboo(name=name, org=org, addr=addr, phone=phone, desc1=desc1,desc2=desc2,desc3=desc3,desc4=desc4,desc5=desc5,desc6=desc6,desc7=desc7,desc8=desc8,desc9=desc9,desc10=desc10,qnt1=qnt1,qnt2=qnt2,qnt3=qnt3,qnt4=qnt4,qnt5=qnt5,qnt6=qnt6,qnt7=qnt7,qnt8=qnt8,qnt9=qnt9,qnt10=qnt10,up1=up1,up2=up2,up3=up3,up4=up4,up5=up5,up6=up6,up7=up7,up8=up8,up9=up9,up10=up10,tot_am=tot_am, tot_tot=tot_tot,perc=perc)
        db.session.add(invoicec)
        db.session.commit()
    allInv = Jiggidiboo.query.all()
    print(Jiggidiboo)
    return render_template('invoice.html', allInv=allInv)

@app.route("/open/<int:sno>", methods=['GET','POST'])
def Open(sno):
    In = Jiggidiboo.query.filter_by(sno=sno).first()
    return render_template('open.html', In=In)




@app.route("/delete/<int:sno>", methods=['GET','POST'])
def delete(sno):
    In = Jiggidiboo.query.filter_by(sno=sno).first()
    db.session.delete(In)
    db.session.commit()
    return redirect('/invoice')













if __name__ == "__main__":
    app.run(debug=True)