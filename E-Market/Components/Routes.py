#? Routes 
# @app.route("/")
# def home():
#     return "<p>Hello This is My First WebSite created in Flask-Python</p>"

# @app.route("/about/<username>")
# def about(username):
#     return f'<h1> This is about page  of {username}</h1>'

from Components import app
from flask import render_template,redirect,url_for,flash,request
from Components.Models import Item, User
from Components.Forms import RegisterForm,LoginForm,PurchaseItemForm,SellItemForm
from Components import db
from flask_login import login_user,logout_user,login_required,current_user
#? Templates
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

#* sending data form route to template using jinja syntax
@app.route('/market',methods=['GET', 'POST'])
@login_required
def market():
            #---Purchase Logic ---
    purchase_form=PurchaseItemForm()
    selling_form=SellItemForm()

    if request.method=="POST":
        purchased_item=request.form.get('purchased_item')
        p_item_obj=Item.query.filter_by(name=purchased_item).first()

        if p_item_obj:
            if current_user.can_purchase(p_item_obj):
               p_item_obj.buy(current_user)
               flash(f"Congratulations! you bought {p_item_obj.name} for {p_item_obj.price}$",category='success')
            else:
                flash(f"Unfortunately, You don't have enough money to purchase {p_item_obj.name}",category='danger')

            # --- SELL LOGIC ---
        sold_item = request.form.get('sold_item')
        s_item_obj = Item.query.filter_by(name=sold_item).first()

        if s_item_obj:
            if current_user.can_sell(s_item_obj):
                s_item_obj.sell(current_user)
                flash(f"You sold {s_item_obj.name} back to the market!", category='success')
            else:
                flash(f"Something went wrong... You don't own {s_item_obj.name}", category='danger')


        return redirect(url_for('market'))
    
    if request.method=="GET":
          items=Item.query.filter_by(owner=None).all()
          owned_items=Item.query.filter_by(owner=current_user.id).all()
          return render_template('market.html', items=items,purchase_form=purchase_form, owned_items=owned_items, selling_form=selling_form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        user_to_create = User(
            userName=form.username.data,
            email_address=form.email_address.data,
            password_encrypt=form.password1.data
        )
        db.session.add(user_to_create)
        db.session.commit()
        flash('Account created successfully! Please log in.', category='success')
        return redirect(url_for('market'))

    if form.errors:
        for field_errors in form.errors.values():
            for error in field_errors:
                flash(f'There was an error creating your account: {error}', category='danger')

    return render_template('register.html', form=form)




@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(userName=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data ):
            login_user(attempted_user)
            flash(f'Success! You are logged in as {attempted_user.userName}',category='success')
            return redirect(url_for('market'))
        else:
            flash('Username and Password are not match! Please try again. ',category='danger')
    

    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    flash('You Have been Logged Out.',category='info')
    return redirect(url_for('home'))



    
if __name__ == '__main__':
    app.run(debug=True)