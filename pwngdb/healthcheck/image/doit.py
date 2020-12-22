#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socketio

sio = socketio.Client()

success = False

@sio.event
def connect():
    print('connection established')
    sio.emit('start')

@sio.event
def regs(data):
    pass

@sio.event
def mem(data):
    pass

@sio.event
def maps(data):
    pass

@sio.event
def breakpoints(data):
    pass

@sio.event
def search_result(data):
    pass

@sio.event
def asm(data):
    global success
    print('received asm')
    success = True
    sio.disconnect()

@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://localhost:1337')
sio.sleep(1)
exit(0 if success else 1)
