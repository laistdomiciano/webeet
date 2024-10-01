from flask import Flask, jsonify, request, abort
import json

app = Flask(__name__)

with open('characters.json', 'r') as file:
    characters = json.load(file)


