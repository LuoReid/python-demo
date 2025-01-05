#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module by reid'

from threading import Thread
import selectors
import sys
from time import sleep, time
from typing import Tuple
from fib import timed_fib


def process_input(stream):
    text = stream.readline()
    n = int(text.strip())
    print('fib({}) = {}'.format(n, timed_fib(n)))


def print_hello():
    while True:
        print("{} - Hello world:)".format(int(time())))
        # sleep(3)


def read_and_process_input():
    while True:
        n = int(input())
        print('fib({}) = {}'.format(n, timed_fib(n)))


def main():
    t = Thread(target=print_hello)
    t.daemon = True
    t.start()
    read_and_process_input()


def main1():
    selector = selectors.DefaultSelector()
    selector.register(sys.stdin, selectors.EVENT_READ)
    last_hello = 0
    while True:
        for [event, mask,t] in selector.select(0.1):
            print(event,mask,t)
            process_input(event.fileobj)
        if time() - last_hello > 3000000:
            last_hello = time()
            print_hello()

def main2():
    args = sys.argv
    print('args:',args)

if __name__ == '__main__':
    main2()
