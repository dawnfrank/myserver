#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from flask import Flask

class MyFlask(Flask):
    def wsgi_app(self,environ, start_response):
        urlInfo = environ.get('PATH_INFO')
        urlPath = "%s/%s" % (os.getcwd(), urlInfo)
        if urlInfo and self.static_folder and not os.path.exists(urlPath):
            staticPath = self.static_folder.replace(os.getcwd(),"")
            staticPath = staticPath.replace("\\","/")
            urlPath = "%s%s"%(staticPath,urlInfo)
            if os.path.exists(urlPath):
                environ['PATH_INFO'] = urlPath
        return super(MyFlask,self).wsgi_app(environ, start_response)