#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import hashlib

def texttohash(text):
  return hashlib.sha256(str(text).encode('utf-8')).hexdigest()

if __name__ == "__main__":
  print(text_to_hash("Hello universe i am from world"))
