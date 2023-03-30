import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import simpledialog
import socket
import threading
import re
import mysql.connector
import datetime
import hashlib


VERY_LITTLE = ('Terminal', 8)
LITTLE = ('Terminal', 14)
MEDIUM = ('Terminal', 40)

HOST = '127.0.0.1'
PORT = 9000