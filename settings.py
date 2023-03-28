import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import simpledialog
import socket
import threading
import re
import bcrypt
import mysql.connector

VERY_LITTLE = ('Terminal', 8)
LITTLE = ('Terminal', 14)
MEDIUM = ('Terminal', 40)
