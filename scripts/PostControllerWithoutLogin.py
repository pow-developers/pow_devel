#
#
# DO NOT EDIT THIS FILE.
# This file was autogenerated by python_on_wheels.
# Any manual edits may be overwritten without notification.
#
# 
# date created: 	2012-07-22
import sys
import os
from mako.template import Template
from mako.lookup import TemplateLookup
import datetime

sys.path.append( os.path.abspath(os.path.join( os.path.dirname(os.path.abspath(__file__)), "../lib" )))
sys.path.append( os.path.abspath(os.path.join( os.path.dirname(os.path.abspath(__file__)), "../models" )))
sys.path.append( os.path.abspath(os.path.join( os.path.dirname(os.path.abspath(__file__)), "../controllers" )) )

import powlib, pow_web_lib
import PowObject
import BaseController
import Post

class PostController(BaseController.BaseController):
    def __init__(self):
        self.modelname = "Post"
        BaseController.BaseController.__init__(self)
        self.login_required = []
        
    def list( self, powdict ):
        res = self.model.find_all()
        return self.render(model=self.model, powdict=powdict, list=res)
    
    def blog( self, powdict ):
        res = self.model.find_all()
        return self.render(model=self.model, powdict=powdict, list=res)
    
    def show( self,powdict ):
        res = self.model.find_by("id",powdict["REQ_PARAMETERS"]["id"])
        return self.render(model=res, powdict=powdict)
        
    def new( self, powdict ):
        self.model.__init__()
        dict = powdict["REQ_PARAMETERS"]
        if dict.has_key("title"):
            self.model.set("title", dict["title"])
        if dict.has_key("content"):
            self.model.set("content", dict["content"])
            
        ofiledir  = os.path.normpath("./public/img/blog/")
        if pow_web_lib.get_form_image_data( "image", dict, ofiledir):
            # if form contains file data AND file could be written, update model
            self.model.set("image", dict["image"].filename )   
        else:
            # dont update model
            self.model.set("image","")     
        self.model.create()
        return self.render(model=self.model, powdict=powdict)
    
    def create( self, powdict):
        self.model.__init__()
        return self.render(model=self.model, powdict=powdict)
    
    def edit( self, powdict ):
        res = self.model.find_by("id",powdict["REQ_PARAMETERS"]["id"])
        return self.render(model=res, powdict=powdict)
    
    def update( self, powdict ):
        self.model.__init__()
        #print powdict["REQ_PARAMETERS"]
        self.model = self.model.find_by("id",powdict["REQ_PARAMETERS"]["id"])
        #print self.model
        dict = powdict["REQ_PARAMETERS"]
        if dict.has_key("title"):
            self.model.set("title", dict["title"])
        if dict.has_key("content"):
            self.model.set("content", dict["content"])
        #print dir(powdict["REQ_BODY"])  
        
        ofiledir  = os.path.normpath("./public/img/blog/")
        if pow_web_lib.get_form_image_data( "image", dict, ofiledir):
            # if form contains file data AND file could be written, update model
            self.model.set("image", dict["image"].filename )     
        else:
            # dont update model
            pass
        self.model.update()
        return self.render(model=self.model, powdict=powdict)
    
    def delete( self, powdict ):
        self.model.__init__()
        self.model = self.model.find_by("id",powdict["REQ_PARAMETERS"]["id"])
        self.model.delete(self.model.get_id())
        return self.render(model=self.model, powdict=powdict)
