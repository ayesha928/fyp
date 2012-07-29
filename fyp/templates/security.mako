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
	width:121px;
	height:140px;
	z-index:1;
	left: 430px;
	top: 162px;
}
#apDiv2 {
	position:absolute;
	width:62px;
	height:86px;
	z-index:2;
	left: 127px;
	top: 571px;
}
#apDiv3 {
	position:absolute;
	width:65px;
	height:75px;
	z-index:3;
	left: 125px;
	top: 313px;
}
#apDiv4 {
	position:absolute;
	width:68px;
	height:82px;
	z-index:4;
	left: 126px;
	top: 392px;
}
#apDiv5 {
	position:absolute;
	width:136px;
	height:148px;
	z-index:5;
	left: 614px;
	top: 422px;
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
	left: 620px;
	top: 252px;
}
#apDiv7 {
	position:absolute;
	width:597px;
	height:115px;
	z-index:7;
	left: 128px;
	top: 5px;
}
#apDiv8 {
	position:absolute;
	width:200px;
	height:80px;
	z-index:8;
	left: 716px;
	top: 26px;
}
#apDiv9 {
	position:absolute;
	width:64px;
	height:29px;
	z-index:9;
	left: 127px;
	top: 483px;
}
#apDiv10 {
	position:absolute;
	width:54px;
	height:29px;
	z-index:10;
	left: 841px;
	top: 262px;
}
#apDiv11 {
	position:absolute;
	width:79px;
	height:31px;
	z-index:11;
	left: 454px;
	top: 448px;
}
#apDiv12 {
	position:absolute;
	width:65px;
	height:35px;
	z-index:12;
	left: 845px;
	top: 449px;
}
#apDiv13 {
	position:absolute;
	width:62px;
	height:32px;
	z-index:13;
	left: 655px;
	top: 520px;
}
#apDiv14 {
	position:absolute;
	width:126px;
	height:113px;
	z-index:9;
	left: 256px;
}
#apDiv15 {
	position:absolute;
	width:498px;
	height:452px;
	z-index:9;
	left: 276px;
	top: 200px;
}
#apDiv16 {
	position:absolute;
	width:70px;
	height:82px;
	z-index:10;
	left: 125px;
	top: 129px;
}
#header #apDiv16 strong {
	color: #999;
}
#apDiv {
	position:absolute;
	width:52px;
	height:81px;
	z-index:10;
	left: 125px;
	top: 215px;
	color: #999;
}
#apDiv17 {
	position:absolute;
	width:200px;
	height:115px;
	z-index:11;
}
</style>
</head>
<body>
<!-- start header -->
 
<div id="header">
  <div id="logo">
    <h1>&nbsp;</h1>
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
    <p>&nbsp;</p>
    <div id="apDiv7">
      <div id="apDiv17"><img src="${request.static_url('fyp:static/images/logoo.PNG')}" alt="" width="86" height="92" /></div>
      <h1>&nbsp;</h1>
      <h1>Home Controller</h1>
    </div>
    <p>&nbsp;</p>
    <p>&nbsp;</p>
    <p>&nbsp;</p>
    <p>&nbsp;</p>
    <h1><a href="#"></a> </h1>
		<p>&nbsp;</p>
  </div>
	

  <p>&nbsp;</p>
  <div id="apDiv16"><strong><a href="${request.route_url('home')}">HOME</a></strong><a href = "${request.route_url('home')}"><img src="${request.static_url('fyp:static/images/cap1.PNG')}" alt="" width="69" height="60" /></a></div>
  <p>&nbsp;</p>
  <div id="apDiv4"><a href="${request.route_url('control')}"><strong>CONTROL</strong> <img src="${request.static_url('fyp:static/images/bulb.PNG')}" alt="" width="53" height="57" /></a></div>
  <div id="apDiv">
    <div align="center"><a href = "${request.route_url('audio')}"><strong>AUDIO</strong><img src="${request.static_url('fyp:static/images/BACK.PNG')}" alt="" width="54" height="69" /></a></div>
  </div>
  <p>&nbsp;</p>
  <div id="apDiv3"><strong><a href="#">SECURITY</a></strong> <a href="#"><img src="${request.static_url('fyp:static/images/security.PNG')}" alt="" width="61" height="50" /></a></div>
  <p>&nbsp;</p>
  <p>&nbsp;</p>
  <p>&nbsp;</p>
  <div id="apDiv9"><a href="${request.route_url('status')}"><strong>STATUS</strong> <img src="${request.static_url('fyp:static/images/status.PNG')}" alt="" width="58" height="60" /></a></div>
  <p>&nbsp;</p>
  <div id="apDiv2"><a href="${request.route_url('settings')}"><strong>SETTINGS</strong></a></strong><a href= "${request.route_url('settings')}"><img src="${request.static_url('fyp:static/images/settings77.PNG')}" alt="" width="53" height="67" /></a></div>
    <div class="CollapsiblePanelTab" tabindex="0">
      <div id="apDiv15">
        <p>Camera <img src="${request.static_url('fyp:static/images/security.PNG')}" alt="" width="64" height="47" /></p>
        <table width="497" height="453" border="1">
          <tr>
            <td height="209">&nbsp;</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
          </tr>
        </table>
      </div>
<p>&nbsp;</p>
  </div>
    <div class="CollapsiblePanelContent"></div>
</div>
</body>
</html>
