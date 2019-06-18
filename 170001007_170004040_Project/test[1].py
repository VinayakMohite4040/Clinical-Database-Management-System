from flask import Flask, render_template, request
import mysql.connector
import datetime

app = Flask(__name__)


mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="username",
    passwd="password",
    database="test"
)

mycursor = mydb.cursor()


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/search")
def search():
    return render_template('search.html')

@app.route("/search/patient")
def search_patient():
    return render_template('search_patient.html')

@app.route("/search/patient/name", methods = ['GET', 'POST'])
def search_patient_name():
    if request.method == 'POST':
        P_name = request.form['P_name']
        mycursor.execute("select * from Patient where P_name = '%s'" % P_name)
        result = mycursor.fetchall()
        return render_template('display_patient.html', result = result)
    return render_template('search_patient_name.html')

@app.route("/search/patient/city", methods = ['GET', 'POST'])
def search_patient_city():
    if request.method == 'POST':
        city = request.form['city']
        mycursor.execute("select * from Patient where Add_city = '%s'" % city)
        result = mycursor.fetchall()
        return render_template('display_patient.html', result = result)
    return render_template('search_patient_city.html')

@app.route("/search/patient/state", methods = ['GET', 'POST'])
def search_patient_state():
    if request.method == 'POST':
        state = request.form['state']
        mycursor.execute("select * from Patient where Add_state = '%s'" % state)
        result = mycursor.fetchall()
        return render_template('display_patient.html', result = result)
    return render_template('search_patient_state.html')



@app.route("/search/staff")
def search_staff():
    return render_template('search_staff.html')

@app.route("/search/staff/name", methods = ['GET', 'POST'])
def search_staff_name():
    if request.method == 'POST':
        P_name = request.form['P_name']
        mycursor.execute("select * from Staff where S_name = '%s'" % P_name)
        result = mycursor.fetchall()
        return render_template('display_staff.html', result = result)
    return render_template('search_staff_name.html')

@app.route("/search/staff/city", methods = ['GET', 'POST'])
def search_staff_city():
    if request.method == 'POST':
        city = request.form['city']
        mycursor.execute("select * from Staff where Add_city = '%s'" % city)
        result = mycursor.fetchall()
        return render_template('display_staff.html', result = result)
    return render_template('search_staff_city.html')

@app.route("/search/staff/state", methods = ['GET', 'POST'])
def search_staff_state():
    if request.method == 'POST':
        state = request.form['state']
        mycursor.execute("select * from Staff where Add_state = '%s'" % state)
        result = mycursor.fetchall()
        return render_template('display_staff.html', result = result)
    return render_template('search_staff_state.html')


@app.route("/search/visit", methods=['GET', 'POST'])
def search_visit():
    if request.method == 'POST':
        date = request.form['date']
        mycursor.execute("select * from Visit where Visit_date = '%s'" % date)
        result = mycursor.fetchall()
        return render_template('display_visit.html', result = result)
    return render_template('search_visit.html')


@app.route("/search/payment")
def search_payment():
    return render_template('search_payment.html')

@app.route("/search/payment/date", methods=['GET', 'POST'])
def search_payment_date():
    if request.method == 'POST':
        date = request.form['date']
        mycursor.execute("select * from Payment where Paid_date = '%s'" % date)
        result = mycursor.fetchall()
        return render_template('display_payment.html', result=result)
    return render_template('search_payment_date.html')

@app.route("/search/payment/id", methods=['GET', 'POST'])
def search_payment_id():
    if request.method == 'POST':
        id = request.form['id']
        mycursor.execute("select * from Payment where Visit_id = '%s'" % id)
        result = mycursor.fetchall()
        return render_template('display_payment.html', result=result)
    return render_template('search_payment_id.html')



@app.route('/display')
def display():
    return render_template('display.html')

@app.route('/display/patient')
def display_patient():
    mycursor.execute("select * from Patient")
    result = mycursor.fetchall()
    return render_template('display_patient.html', result = result)

@app.route('/display/staff')
def display_staff():
    mycursor.execute("select * from Staff")
    result = mycursor.fetchall()
    return render_template('display_staff.html', result = result)

@app.route('/display/test')
def display_test():
    mycursor.execute("select * from test_details")
    result = mycursor.fetchall()
    return render_template('display_test.html', result = result)

@app.route('/display/visit')
def display_visit():
    mycursor.execute("select * from Visit")
    result = mycursor.fetchall()
    return render_template('display_visit.html', result = result)

@app.route('/display/payment')
def display_payment():
    mycursor.execute("select * from Payment")
    result = mycursor.fetchall()
    return render_template('display_payment.html', result = result)



@app.route('/insert')
def insert():
    return render_template('insert.html')

@app.route('/insert/patient', methods=['GET', 'POST'])
def insert_patient():
    if request.method == 'POST':
        name = request.form['name']
        DOB = request.form['DOB']
        gender = request.form['gender']
        blood_grp = request.form['blood_grp']
        phone_1 = request.form['phone_1']
        phone_2 = request.form['phone_2']
        house_no = request.form['house_no']
        street = request.form['street']
        city = request.form['city']
        state = request.form['state']
        insert_data = "insert into patient(P_name, DOB, Gender, P_phone_1, P_phone_2, Blood_group, Add_house_no, Add_street, Add_city, Add_state) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        input_data = (name, DOB, gender, phone_1, phone_2, blood_grp, house_no, street, city, state)
        mycursor.execute(insert_data, input_data)
        mydb.commit()
        return render_template('home.html')
    return render_template('insert_patient.html')

@app.route('/insert/staff', methods=['GET', 'POST'])
def insert_staff():
    if request.method == 'POST':
        name = request.form['name']
        joining = request.form['joining']
        gender = request.form['gender']
        phone_1 = request.form['phone_1']
        phone_2 = request.form['phone_2']
        department = request.form['department']
        post = request.form['post']
        salary = request.form['salary']
        visiting_hrs = request.form['visiting_hrs']
        house_no = request.form['house_no']
        street = request.form['street']
        city = request.form['city']
        state = request.form['state']
        insert_data = "insert into Staff(S_name, Joining_date, Gender, S_phone_1, S_phone_2, Department, Post, Salary, Visiting_hrs, Add_house_no, Add_street, Add_city, Add_state) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        input_data = (name, joining, gender, phone_1, phone_2, department, post, salary, visiting_hrs, house_no, street, city, state)
        mycursor.execute(insert_data, input_data)
        mydb.commit()
        return render_template('home.html')
    return render_template('insert_staff.html')

@app.route('/insert/visit', methods = ['GET', 'POST'])
def insert_visit():
    if request.method == 'POST':
        patient_id = request.form['P_id']
        mycursor.execute("select inject(%s)" % patient_id)
        result = mycursor.fetchone()
        for x in result:
            count = x
        if (count == 0):
            return render_template('insert_patient.html')
        reason = request.form['Reason_for_visit']
        mycursor.execute("insert into Visit(P_id, Reason_for_visit, bill_amount, Amount_pending) values (%s, '%s', 0, 0)" % (patient_id, reason))
        mydb.commit()
        return render_template('home.html')
    return render_template('insert_visit.html')

@app.route('/visit', methods = ['GET', 'POST'])
def edit_visit():
    if request.method == 'POST':
        visit_id = request.form['visit_id']
        staff_id = request.form['S_id']
        test_1 = request.form['test_1']
        test_2 = request.form['test_2']
        test_3 = request.form['test_3']
        test_4 = request.form['test_4']
        due_date = request.form['Due_date']
        mycursor.execute("update Visit set S_id = %s, Due_date = '%s' where Visit_id = %s" % (staff_id, due_date, visit_id))
        x = 0
        amount = 0
        while(x < 4):
            if x==0 :
                mycursor.execute("update Visit set test_1=%s where Visit_id = %s" % (test_1, visit_id))
                mycursor.execute("select test_cost from test_details where Test_id=%s" % test_1)
                result = mycursor.fetchone()
                for y in result:
                    add_amnt = y
                amount = amount + add_amnt
            elif x==1 :
                mycursor.execute("update Visit set test_2=%s where Visit_id = %s" % (test_2, visit_id))
                mycursor.execute("select test_cost from test_details where Test_id=%s" % test_2)
                result = mycursor.fetchone()
                for y in result:
                    add_amnt = y
                amount = amount + add_amnt
            elif x==2 :
                mycursor.execute("update Visit set test_3=%s where Visit_id = %s" % (test_3, visit_id))
                mycursor.execute("select test_cost from test_details where Test_id=%s" % test_3)
                result = mycursor.fetchone()
                for y in result:
                    add_amnt = y
                amount = amount + add_amnt
            elif x==3 :
                mycursor.execute("update Visit set test_4=%s where Visit_id = %s" % (test_4, visit_id))
                mycursor.execute("select test_cost from test_details where Test_id=%s" % test_4)
                result = mycursor.fetchone()
                for y in result:
                    add_amnt = y
                amount = amount + add_amnt
            x=x+1

        mycursor.execute("update Visit set bill_amount = %s, Amount_pending = %s where Visit_id = %s" % (amount, amount, visit_id))
        mydb.commit()
        return render_template('home.html')
    return render_template('visit.html')

@app.route('/insert/payment', methods=['GET', 'POST'])
def insert_payment():
    if request.method == 'POST':
        visit_id = request.form['visit_id']
        amount = request.form['amount']
        method = request.form['method']
        mycursor.execute("insert into Payment(Visit_id, amt_paid, Payment_method) values(%s, %s, '%s')" % (
        visit_id, amount, method))
        mycursor.execute("select Amount_pending from Visit where Visit_id = %s" % visit_id)
        result = mycursor.fetchone()
        for x in result:
            pending_amnt = x - int(amount)
        mycursor.execute("update Visit set Amount_pending = %d where Visit_id = %s" % (pending_amnt, visit_id))
        if pending_amnt <= 0:
			mycursor.execute("update Visit set Amount_pending = 0 where Visit_id = %s" % visit_id)
            mycursor.execute("update Visit set Payment_status = 'completed' where Visit_id = %s" % visit_id)
        mydb.commit()
        return render_template('home.html')
    return render_template('insert_payment.html')

@app.route('/insert/test', methods=['GET', 'POST'])
def insert_test():
    if request.method == 'POST':
        name = request.form['name']
        room = request.form['room']
        cost = request.form['cost']
        mycursor.execute("insert into test_details(Room_no, Name, test_cost) values('%s', '%s', '%s')" % (room, name, cost))
        mydb.commit()
        return render_template('home.html')
    return render_template('insert_test.html')


@app.route('/delete')
def delete():
    return render_template('delete.html')

@app.route('/delete/patient', methods=['GET', 'POST'])
def delete_patient():
    if request.method == 'POST':
        id = request.form['id']
        mycursor.execute("delete from patient where P_id = (%s)" % id)
        mydb.commit()
        return render_template('home.html')
    return render_template('delete_patient.html')

@app.route('/delete/patient/all')
def delete_all_patient():
    mycursor.execute("delete from patient")
    mydb.commit()
    return render_template('home.html')

@app.route('/delete/staff', methods=['GET', 'POST'])
def delete_staff():
    if request.method == 'POST':
        id = request.form['id']
        mycursor.execute("delete from Staff where S_id = (%s)" % id)
        mydb.commit()
        return render_template('home.html')
    return render_template('delete_staff.html')

@app.route('/delete/staff/all')
def delete_all_staff():
    mycursor.execute("delete from Staff")
    mydb.commit()
    return render_template('home.html')

@app.route('/delete/visit', methods=['GET', 'POST'])
def delete_visit():
    if request.method == 'POST':
        id = request.form['id']
        mycursor.execute("delete from Visit where Visit_id = (%s)" % id)
        mydb.commit()
        return render_template('home.html')
    return render_template('delete_visit.html')

@app.route('/delete/visit/all')
def delete_all_visit():
    mycursor.execute("delete from Visit")
    mydb.commit()
    return render_template('home.html')

@app.route('/delete/test', methods=['GET', 'POST'])
def delete_test():
    if request.method == 'POST':
        id = request.form['id']
        mycursor.execute("delete from test_details where Test_id = (%s)" % id)
        mydb.commit()
        return render_template('home.html')
    return render_template('delete_test.html')

@app.route('/delete/patient/all')
def delete_all_test():
    mycursor.execute("delete from test_details")
    mydb.commit()
    return render_template('home.html')

@app.route('/delete/payment', methods=['GET', 'POST'])
def delete_payment():
    if request.method == 'POST':
        id = request.form['id']
        mycursor.execute("delete from Payment where Payment_id = (%s)" % id)
        mydb.commit()
        return render_template('home.html')
    return render_template('delete_payment.html')

@app.route('/delete/payment/all')
def delete_all_payment():
    mycursor.execute("delete from Payment")
    mydb.commit()
    return render_template('home.html')


@app.route('/update')
def update():
    return render_template('update.html')

@app.route('/update/patient', methods=['GET', 'POST'])
def update_patient():
    if request.method == 'POST':
        id = request.form['id']
        choice = request.form['choice']
        change = request.form['change']
        mycursor.execute("update Patient set %s = '%s' where P_id = %s" % (choice, change, id))
        mydb.commit()
        return render_template('home.html')
    return render_template('update_patient.html')

@app.route('/update/staff', methods=['GET', 'POST'])
def update_staff():
    if request.method == 'POST':
        id = request.form['id']
        choice = request.form['choice']
        change = request.form['change']
        mycursor.execute("update Staff set %s = '%s' where S_id = %s" % (choice, change, id))
        mydb.commit()
        return render_template('home.html')
    return render_template('update_staff.html')

@app.route('/update/test', methods=['GET', 'POST'])
def update_test():
    if request.method == 'POST':
        id = request.form['id']
        choice = request.form['choice']
        change = request.form['change']
        mycursor.execute("update test_details set %s = '%s' where test_id = %s" % (choice, change, id))
        mydb.commit()
        return render_template('home.html')
    return render_template('update_test.html')

def end():
    mycursor.close()
    mydb.close()


if __name__ == "__main__":
    app.run(debug=True)
