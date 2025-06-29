from flask import Flask, render_template, redirect, session, request
from moralis import sol_api
import random
import datetime
import stripe
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label="Log In")


stripe.api_key = "MY_STRIPE_API_KEY"
api_key = "MY_MORALIS_API_KEY"
CHAIN = "solana"
COLLECTION_ADDRESS ="*********************"
DOMAIN = "http://127.0.0.1:5000/"


app = Flask(__name__)
app.config['SECRET_KEY'] = 'add-secret-key-here'


@app.route("/", methods=["GET", "POST"])
def home():
    if 'random_sol_price' not in session:
        session['random_sol_price'] = random.randint(30, 40)
        session['convert_sol'] = get_sol_price_in_usd(session['random_sol_price'])

    current_year = datetime.datetime.now().year
    nft_data = get_wallet_nft()

    return render_template("index.html",
                           price=session['random_sol_price'],
                           year=current_year,
                           all_nfts=nft_data,
                           sol_to_usd=session['convert_sol'])


def get_wallet_nft():
    params = {
      "nft_metadata": True,
      "media_items": False,
      "exclude_spam": False,
      "network": "mainnet",
      "address": COLLECTION_ADDRESS
    }

    result = sol_api.account.get_nfts(
      api_key=api_key,
      params=params,
    )

    # GET Mint address for Metadata
    nft_list = []

    for i, nft in enumerate(result[:12]):
        params = {
            "network": "mainnet",
            "address": nft['mint']
        }

        nft_result = sol_api.nft.get_nft_metadata(
            api_key=api_key,
            params=params,
        )

        nft_list.append({
            "id": i,
            "name": nft_result['name'],
            "symbol": nft_result['symbol'],
            "url": nft_result['imageOriginalUrl']
        })

    return nft_list


def get_sol_price_in_usd(sol: float) -> float:
    params = {
        "network": "mainnet",
        "address": "So11111111111111111111111111111111111111112"  # SOL token mint
    }
    result = sol_api.token.get_token_price(
        api_key=api_key,
        params=params)
    price = float(result["usdPrice"])
    return round(sol * price, 2)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/checkout/<int:index>', methods=['GET', 'POST'])
def checkout(index):
    checkout_item = None
    for nft in nft_data:
        if nft["id"] == index:
            checkout_item = nft
    return render_template('checkout.html',
                           checkout_nft=checkout_item,
                           sol_to_usd=session.get('convert_sol', 'Unknown'))
      

@app.route('/checkout')
def generic_checkout():
    return render_template('checkout.html', checkout_nft=None)


@app.route('/create-checkout-session/<int:index>', methods=['GET', 'POST'])
def create_checkout_session(index):
    checkout_item = None
    for nft in nft_data:
        if nft["id"] == index:
            checkout_item = nft
    sol_to_usd = session.get('convert_sol', 0)

    # Store data in session
    session['checkout_nft'] = checkout_item
    session['sol_to_usd'] = sol_to_usd
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'unit_amount': int(float(sol_to_usd) * 100),
                    'product_data': {
                        'name': checkout_item['name'],
                    },
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=DOMAIN + 'success',
            cancel_url=DOMAIN + 'cancel',
        )

    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)


@app.route('/success')
def success():
    checkout_nft = session.pop('checkout_nft', None)
    return render_template('success.html', checkout_nft=checkout_nft)


@app.route('/cancel')
def cancel():
    return render_template('cancel.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return render_template("login_success.html", logged_in=True, name=form.email.data, password=form.password.data)
    return render_template("login.html", form=form)


nft_data = get_wallet_nft()


if __name__ == '__main__':
    app.run(debug=True)







