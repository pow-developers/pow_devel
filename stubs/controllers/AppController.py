#
#
# DO NOT EDIT THIS FILE.
# This file was autogenerated by python_on_wheels.
# Any manual edits may be overwritten without notification.
#
# 

# date created:     2011-06-21

import sys
import os


sys.path.append( os.path.abspath(os.path.join( os.path.dirname(os.path.abspath(__file__)), "../lib" )))
sys.path.append( os.path.abspath(os.path.join( os.path.dirname(os.path.abspath(__file__)), "../models" )))
sys.path.append( os.path.abspath(os.path.join( os.path.dirname(os.path.abspath(__file__)), "../models/powmodels" )))
sys.path.append( os.path.abspath(os.path.join( os.path.dirname(os.path.abspath(__file__)), "../controllers" )) )

import powlib
from powlib import mixin, uc
from BaseController import BaseController
import datetime

#import AuthController 

#@mixin(AuthController.AuthController)
class AppController(BaseController):
    
    def __init__(self):
        # it is needed to set a Modelname before calling the BaseControllers init
        self.modelname = "App"
        BaseController.__init__(self)
        
        self.login_required = []
        # example of locked actions and the redirections.
        self.locked_actions = {}
    
    def ajax( self, powdict ):
        print "AJAX-Request"
        now = datetime.datetime.now()
        now = now.strftime("%Y-%m-%d %H:%M:%S")
        ret_str = uc("""<div class="alert alert-success">
                <button type="button" class="close" data-dismiss="alert">&times;</button>
                <strong>Yeah! AJAX with python rocks totally now:</strong>&nbsp %s &nbsp; %s 
              </div>""" % (now, powdict["REQ_BODY"] ))
        return ret_str 
        
    
    def welcome( self,powdict ):
        #example of setting a special_template for an action not following the Controller_action.tmpl convention
        #return self.render(special_tmpl="hero.tmpl",model=self.model, powdict=powdict)
        return self.render(model=self.model, powdict=powdict)
        
    def thanks( self ):
        print "Das ist die thanks action"
        
    def howto_start( self,powdict ):
        return self.render(model=self.model, powdict=powdict)
    
    
        
    
