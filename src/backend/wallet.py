from flask import request, session
from flask_restx import Resource, abort, Namespace
from wallet import Wallet





ns_wallet = Namespace('wallet', 'Endpoints for managing a wallet balance')
wallet = Wallet()
@ns_wallet.route("/")
class Wallet(Resource):
    def get(self):
        return "Wallet contains {}".format(wallet.balance)

@ns_wallet.route("/add_funds/<amount>")
@ns_wallet.doc(params={'amount': 'Amount to top up wallet'})
class Wallet(Resource):
    def post(self, amount):
        wallet.add_cash(float(amount))
        # Return results
        return "Wallet now contains {}".format(wallet.balance)

@ns_wallet.route("/spend_funds/<amount>")
@ns_wallet.doc(params={'amount': 'Amount to spend from wallet'})
class Wallet(Resource):
    def post(self, amount):
        wallet.spend_cash(float(amount))
        # Return results
        return "Wallet now contains {}".format(wallet.balance)