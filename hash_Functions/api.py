#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
import argparse
import sys
import flask
from blockchain.block.create_block import CreateBlock
from blockchain.block.get_block import GetBlockFromOtherNode
from flask import jsonify
from flask import request
from lib.export import export_the_transactions
from lib.settings_system import debug_mode
from lib.settings_system import test_mode
from lib.settings_system import the_settings
from lib.status import Status
from node.node_connection import ndconnect
from node.node_connection import ndconnectmixdb
from node.node_connection import ndid
from node.node_connection import ndstart
from node.node_connection import ndstop
from node.unl import save_new_unl_node
from transactions.get_my_transaction import GetMyTransaction
from transactions.send import send
from waitress import serve
from wallet.create_a_wallet import create_a_wallet
from wallet.delete_current_wallet import delete_current_wallet
from wallet.print_balance import print_balance
from wallet.print_wallets import print_wallets
from wallet.wallet_selector import wallet_selector

app = flask.Flask(__name__)

@app.route("/nft/<sha256>", methods=["GET"])
def wallet_change_page(sha256):
    wallet_selector(sha256)
    return jsonify(print_wallets())

def start():
    """
    Start the API server.
    """

    parser = argparse.ArgumentParser(
        description=
        "This is an open source decentralized application network. In this network, you can develop and publish decentralized applications."
    )

    parser.add_argument("-p", "--port", type=int, help="Add new UNL node")

    args = parser.parse_args()

    if len(sys.argv) < 2:
        serve(app, host="0.0.0.0", port=8000)
    else:
        serve(app, host="0.0.0.0", port=args.port)


if __name__ == "__main__":
    start()







