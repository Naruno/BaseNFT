#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import hashlib
####################    CONVERT TO SHA348 ####################
enterfilepath = "Screen Shot 2022-03-23 at 20.05.05.png";#for ex
with open(enterfilepath,"rb") as f: #here we use any loop 
    bytes = f.read()
    convert_To_sha384 = hashlib.sha384(bytes).hexdigest();
print(convert_To_sha384)
####################    CONVERT TO sha1 #################### 
enterFilePath = "Screen Shot 2022-03-23 at 20.05.14.png"
with open(enterFilePath,"rb") as trvl:
    bytes = trvl.read()
    convertTosha1 = hashlib.sha1(bytes).hexdigest();
print(convertTosha1)
####################    CONVERT TO sha224 ####################
filePath = "Screen Shot 2022-03-23 at 20.06.41.png"
with open(filePath,"rb") as trvlg:
    bytes = trvlg.readline()
    converttosha224 = hashlib.sha224(bytes).hexdigest();
print(converttosha224)








