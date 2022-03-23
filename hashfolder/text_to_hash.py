#!/usr/bin/python3
# -*- coding: utf-8 -*-

import hashlib

def texttohash(text):
  return hashlib.sha256(text)

if __name__ == "__main__":
  print(text_to_hash("Hello universe i am from world"))
