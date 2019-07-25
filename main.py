from flask import Flask, render_template, redirect, url_for
from forms.phoneForm import Phone
from dao.myhelper import Helper



app = Flask(__name__)
app.secret_key = 'development key'


@app.route('/', methods=['GET', 'POST'])
def root():
    form = Phone()
    return render_template('phone.html', form=form)



@app.route('/edit_phone/<phone_id>', methods=['GET','POST'])
def edit_phone(phone_id):
    print('phone_id:', phone_id)
    form = Phone()

    helper = Helper()

    phone_data = helper.Get_phone(phone_id)

    form.phone_date.data = phone_data[0][0]
    form.phone_vendor.data = phone_data[0][1]
    form.phone_model.data = phone_data[0][2]
    form.phone_price.data = phone_data[0][3]


    return render_template('phone.html', form=form, action="save_phone")

@app.route('/save_phone', methods=['GET', 'POST'])
def save_phone():
    form = Phone()

    if not form.validate():
        return render_template('phone.html', form=form, form_name="Edit phone", action="save_phone")
    else:

        helper = Helper()
        helper.Update_phone(form.phone_id.data, form.phone_model.data, form.phone_vendor.data, form.phone_price.data, form.phone_date.data)

        return redirect(url_for('root'))



if __name__ == '__main__':
    app.run(debug=True, port=5001)
