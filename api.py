#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
import argparse
import sys
import flask
from flask import jsonify
from flask import request

app = flask.Flask(__name__)

@app.route("/nft/<sha256>", methods=["GET"])
def nft(sha256):
    return jsonify(sha256)

def start():
    """
    Start the API server.
    """

    parser = argparse.ArgumentParser(
        description=
        "The NFT Creator"
    )

    parser.add_argument("-p", "--port", type=int, help="Add new UNL node")

    args = parser.parse_args()

    if len(sys.argv) < 2:
        serve(app, host="0.0.0.0", port=8000)
    else:
        serve(app, host="0.0.0.0", port=args.port)


if __name__ == "__main__":
    start()







