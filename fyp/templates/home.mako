<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:ice="http://ns.adobe.com/incontextediting">
<head>
<meta http-equiv="content-type" content="text/html; charset=utf-8" />
<title>Home Controller</title>
<meta name="keywords" content="" />
<meta name="description" content="" />
<link href="${request.static_url('fyp:static/css/default.css')}" rel="stylesheet" type="text/css" media="screen" />
<script src="includes/ice/ice.js" type="text/javascript"></script>
<script src="SpryAssets/SpryCollapsiblePanel.js" type="text/javascript"></script>
<style type="text/css">
#apDiv1 {
    position:absolute;
    width:118px;
    height:109px;
    z-index:1;
    left: 227px;
    top: 146px;
}
#apDiv2 {
    position:absolute;
    width:122px;
    height:77px;
    z-index:2;
    left: 226px;
    top: 367px;
}
#apDiv3 {
    position:absolute;
    width:118px;
    height:110px;
    z-index:3;
    left: 227px;
    top: 264px;
}
#apDiv4 {
    position:absolute;
    width:126px;
    height:84px;
    z-index:4;
    left: 228px;
    top: 572px;
}
#apDiv5 {
    position:absolute;
    width:124px;
    height:93px;
    z-index:5;
    left: 226px;
    top: 481px;
    font-weight: bold;
}
</style>
<link href="SpryAssets/SpryCollapsiblePanel.css" rel="stylesheet" type="text/css" />
<style type="text/css">
#apDiv6 {
    position:absolute;
    width:124px;
    height:137px;
    z-index:6;
    left: 210px;
    top: -17px;
}
#apDiv7 {
    position:absolute;
    width:597px;
    height:115px;
    z-index:7;
    left: 140px;
    top: 13px;
}
#apDiv8 {
    position:absolute;
    width:200px;
    height:80px;
    z-index:8;
    left: 719px;
    top: 29px;
}
#apDiv9 {
    position:absolute;
    width:57px;
    height:29px;
    z-index:9;
    left: 394px;
    top: 196px;
}
#apDiv10 {
    position:absolute;
    width:54px;
    height:29px;
    z-index:10;
    left: 398px;
    top: 415px;
}
#apDiv11 {
    position:absolute;
    width:70px;
    height:31px;
    z-index:11;
    left: 396px;
    top: 308px;
}
#apDiv12 {
    position:absolute;
    width:65px;
    height:35px;
    z-index:12;
    left: 398px;
    top: 603px;
}
#apDiv13 {
    position:absolute;
    width:62px;
    height:32px;
    z-index:13;
    left: 397px;
    top: 513px;
}
</style>
</head>
<body background = "${request.static_url('fyp:static/images/img12.jpg')}">
<!-- start header -->
 
<div id="header">
  <div id="logo">
    <h1>&nbsp;</h1>
<p>&nbsp;</p>
<div id="apDiv8"><A HREF = "${request.route_url('home')}"><img src="${request.static_url('fyp:static/images/cap1.PNG')}" alt="" width="217" height="91" /></A></div>
<p>&nbsp;</p>
<p>&nbsp;</p>
        <p>&nbsp;</p>
    <p>&nbsp;</p>
    <p>&nbsp;</p>
    <p>&nbsp;</p>
    <p>&nbsp;</p>
    <p>&nbsp;</p>
    <p>&nbsp;</p>
    <p>&nbsp;</p>
    <div id="apDiv7">
      <h1>&nbsp;</h1>
      <h1>Home Controller</h1>
    </div>
    <p>&nbsp;</p>
<h1><a href="#"></a> </h1>
        <p>&nbsp;</p>
  </div>
    

  <p>&nbsp;</p>
  <p>&nbsp;</p>
  
    <div class="CollapsiblePanelTab" tabindex="0"></div>
    <div class="CollapsiblePanelContent">
      <div id="apDiv9"><a href="${request.route_url('control')}"><strong>CONTROL</strong></a></div>
      <div id="apDiv10"><a href="${request.route_url('audio')}"><strong>AUDIO</strong></a></div>
      <div id="apDiv12"><a href="${request.route_url('status')}"><strong>STATUS</strong></a></div>
      <p>&nbsp;</p>
      <div id="apDiv11"><a href="${request.route_url('security')}"><strong>SECURITY</strong></a></div>
      <p>&nbsp;</p>
      <p>&nbsp;</p>
      <p>&nbsp;</p>
      <div id="apDiv13"><a href="${request.route_url('settings')}"><strong>SETTINGS</strong></a></div>
      <p>&nbsp;</p>
  </div>
    <p>&nbsp;</p>
    <p>&nbsp;</p>
    <p>&nbsp;</p>
</div>
 
  <div id="page">
    <div id="content">
      <div class="post">
        <div></div>
        <div>
          <div align="center">
            <div id="apDiv1">
              <p><img src="${request.static_url('fyp:static/images/bulb.PNG')}" alt="" width="84" height="103" /></p>
            </div>
            <div id="apDiv2">
              <p><img src="${request.static_url('fyp:static/images/BACK.PNG')}" alt="" width="78" height="89" /></p>
            </div>
          </div>
        </div>
        <div id="apDiv3">
          <p align="center"> <img src="${request.static_url('fyp:static/images/security.PNG')}" alt="" width="81" height="81" /></p>
</div>
        <div id="apDiv4">
          <p align="center"><img src="${request.static_url('fyp:static/images/status.PNG')}" alt="" width="77" height="80" /></p>
        </div>
        <div id="apDiv5">
          <div align="center">
            <p><img src="${request.static_url('fyp:static/images/settings77.PNG')}" alt="" width="86" height="92" /></p>
</div>
        </div>
<!-- end footer --></div>
</div>
    </div>
  </div>
</div>

</body>
</html>
