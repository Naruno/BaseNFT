#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
import argparse
from doctest import Example
import sys
import flask
from flask import jsonify
from flask import request
from waitress import serve

from hash_functions.text_to_hash import texttohash

app = flask.Flask(__name__)

@app.route("/nft/<text>", methods=["GET"])
def nft_text(text):
    return jsonify(texttohash(str(text)))

def start():
    """
    Start the API server.
    """

    parser = argparse.ArgumentParser(
        description=
        "The NFT Creator"
    )

    parser.add_argument("-p", "--port", default=8000, type=int, help="Add new UNL node")

    args = parser.parse_args()



    serve(app, host="0.0.0.0", port=args.port)


if __name__ == "__main__":
    start()







