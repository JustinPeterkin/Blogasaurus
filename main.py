#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import logging

HOMEPAGE = """<html>
 <head>
   <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
   <script src ="Project.js"></script>
    <link rel="stylesheet" href = "Project.css">
   <center><title>About Me</title></center>
</head>
 <body>
   <h1><u>About Me</u></h1>
    <h2>Justin Peterkin</h2>
     <p>I was born in Staten Island, New York and have lived there my whole life. I graduated from Curtis High School, and will attend the Macaualy Honors College at the College of Staten Island.</p>
  <div id="wall">
    <div class="frame" id = "curtis">
      <a href="https://sites.google.com/a/curtishs.org/home/Home"> <img src = "http://static.hudl.com/users/prod/322887_e2845c25393e4603ae3dd783112f505e.jpg"/></a>
    </div>
   <div id = "csi">
      <a href="https://www.csi.cuny.edu/academics-and-research/specialized-programs/honors-programs/macaulay-honors-college"><img id = "logo" src = "https://pbs.twimg.com/profile_images/469282330184400896/0i4N5Bsf_400x400.jpeg"/></a>
    </div>
<h3>How I Spent My Summer</h3>
  <p>This summer I will be attending Google's CSSI, which will teach me about computer science.</p>
 </body>

</html>"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(HOMEPAGE)


app = webapp2.WSGIApplication([
    ('/', MainHandler)



], debug=True)
