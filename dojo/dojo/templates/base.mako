<!DOCTYPE html>
<html>
<head>
  
  <title>${self.title()}</title>
  <meta name="viewport"
      content="width=device-width,initial-scale=1,maximum-scale=1,minimum-scale=1,user-scalable=no"/>
  <meta name="apple-mobile-web-app-capable" content="yes" />
  ${self.meta()}
  
  <link rel="shortcut icon" href="${request.static_url('dojo:static/favicon.ico')}" />
  <link rel="stylesheet" href="${request.static_url('dojo:static/pylons.css')}" type="text/css" media="screen" charset="utf-8" />
  <link rel="stylesheet" href="http://static.pylonsproject.org/fonts/nobile/stylesheet.css" media="screen" />
  <link rel="stylesheet" href="http://static.pylonsproject.org/fonts/neuton/stylesheet.css" media="screen" />
  <!--[if lte IE 6]>
  <link rel="stylesheet" href="${request.static_url('dojo:static/ie6.css')}" type="text/css" media="screen" charset="utf-8" />
  <![endif]-->
  <script src="${request.static_url('dojo:static/js/dojo/dojo.js')}" data-dojo-config="async:true"></script>
  <script type="text/javascript">
      // Load the widget parser and mobile base
      require(["dojox/mobile/parser", "dojox/mobile/deviceTheme", "dojox/mobile/compat", "dojox/mobile"],
          function(parser, deviceTheme) {
       
              // Parse the page for widgets!
              parser.parse();
          }
      );
  </script>
  ${self.javascript()}
</head>

<body>
  ${self.body()}
</body>
</html>

<%def name="title()">Home Controller</%def>

<%def name="meta()">
  <meta http-equiv="Content-Type" content="text/html;charset=UTF-8"/>
  <meta name="keywords" content="python web application" />
  <meta name="description" content="PyCK web application" />
</%def>

<%def name="javascript()">
</%def>
    


