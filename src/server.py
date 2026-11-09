# This file contains the main server API for handling horse and race data requests

from flask import Flask, jsonify
from init import init_horses, init_races
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

