#!/usr/bin/env python
"""
Very simple HTTP server in python.

Usage::
    ./dummy-web-server.py [<port>]

Send a GET request::
    curl http://localhost

Send a HEAD request::
    curl -I http://localhost

Send a POST request::
    curl -d "foo=bar&bin=baz" http://localhost

"""
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import os

global cur_string
cur_string = ""
global cur_list
cur_list = []

def update_cur_string(new_string):
    global cur_string
    cur_string = cur_string + new_string

def get_cur_string():
    return cur_string

def update_cur_list(new_item):
    global cur_list
    cur_list.append(new_item)

def get_cur_list():
    return cur_list

def split_path(path_str):
    return_map = {}

    path_str = path_str[2:]
    path_list = path_str.split('&')
    for item in path_list:
        split_list = item.split('=')
        split_list[1] = split_list[1].replace('%20', ' ')
        split_list[1] = split_list[1].replace('+', ' ')
        split_list[1] = split_list[1].replace('%27', '\'')
        split_list[1] = split_list[1].replace('%24', '$')
        return_map[split_list[0]] = split_list[1]

    return return_map

class S(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_OPTIONS(self):
        self._set_headers()
        self.wfile.write("<html><body><h1>hi!</h1></body></html>")

    def do_GET(self):
        """
        self._set_headers()
        if (get_name_index() == len(get_names_list())):
            self.wfile.write('-1')
        else:
	    self.wfile.write(str(get_names_list()[get_name_index()]))
        inc_name_index()
        """
        self._set_headers()
        #self.wfile.write(get_cur_list())
        for item in get_cur_list():
            self.wfile.write(item[0] + ',' + item[1] + ';')

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        """
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        email_file = open('emails.txt', 'a')
        email_file.write(post_data + '\n')
        email_file.close()
        """
        self._set_headers()
        params = split_path(self.path)

        """ Determine what we put in the string """
        """
        if 'title' in params:
            #update_cur_string('<h1>' + params['title'] + '</h1><br>')
        elif 'question' in params:
            update_cur_string('<p style="font-weight: bold">Question: ' + params['question'] + '</p>')
        elif 'answer' in params:
            update_cur_string('<p>' + params['answer'] + '</p>')
        elif 'section' in params:
            update_cur_string('<h3>' + params['section'] + '</h3><br>')
        elif 'note' in params:
            update_cur_string('<p>Note: ' + params['note'])
        """
        for item in params:
            update_cur_list([item, params[item]])

def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
