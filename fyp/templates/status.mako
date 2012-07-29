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
	width:175px;
	height:123px;
	z-index:2;
	left: 199px;
	top: 172px;
}
#apDiv3 {
	position:absolute;
	width:71px;
	height:87px;
	z-index:3;
	left: 118px;
	top: 218px;
}
#apDiv4 {
	position:absolute;
	width:54px;
	height:59px;
	z-index:4;
	left: 118px;
	top: 312px;
}
#apDiv5 {
	position:absolute;
	width:179px;
	height:119px;
	z-index:5;
	left: 197px;
	top: 328px;
	font-weight: bold;
}
</style>
<link href="SpryAssets/SpryCollapsiblePanel.css" rel="stylesheet" type="text/css" />
<style type="text/css">
#apDiv6 {
	position:absolute;
	width:65px;
	height:77px;
	z-index:6;
	left: 120px;
	top: 390px;
}
#apDiv7 {
	position:absolute;
	width:597px;
	height:115px;
	z-index:7;
	left: 119px;
	top: 12px;
}
#apDiv8 {
	position:absolute;
	width:67px;
	height:80px;
	z-index:8;
	left: 120px;
	top: 135px;
}
#apDiv9 {
	position:absolute;
	width:63px;
	height:29px;
	z-index:9;
	left: 120px;
	top: 469px;
}
#apDiv10 {
	position:absolute;
	width:54px;
	height:29px;
	z-index:10;
	left: 118px;
	top: 554px;
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
#apDiv {
	position:absolute;
	width:409px;
	height:461px;
	z-index:10;
	left: 257px;
	top: 161px;
}
#apDiv14 {
	position:absolute;
	width:170px;
	height:93px;
	z-index:11;
	left: 196px;
	top: 37px;
}
#apDiv15 {	position:absolute;
	width:877px;
	height:60px;
	z-index:10;
	left: 145px;
	top: 249px;
}
#apDiv16 {	position:absolute;
	width:200px;
	height:104px;
	z-index:11;
	left: 294px;
	top: 2px;
}
#apDiv17 {
	position:absolute;
	width:200px;
	height:115px;
	z-index:11;
	left: 221px;
	top: -156px;
}
#apDiv18 {	position:absolute;
	width:200px;
	height:115px;
	z-index:11;
	left: 291px;
	top: 0px;
}
#apDiv19 {	position:absolute;
	width:845px;
	height:135px;
	z-index:2;
	left: 139px;
	top: 434px;
}
#apDiv20 {	position:absolute;
	width:152px;
	height:111px;
	z-index:3;
	left: 379px;
	top: 259px;
}
#apDiv21 {	position:absolute;
	width:200px;
	height:104px;
	z-index:11;
	left: 294px;
	top: 2px;
}
#apDiv22 {	position:absolute;
	width:195px;
	height:104px;
	z-index:11;
	left: 250px;
	top: 37px;
}
#apDiv23 {
	position:absolute;
	width:63px;
	height:21px;
	z-index:11;
	left: 311px;
	top: 141px;
}
#apDiv24 {
	position:absolute;
	width:54px;
	height:23px;
	z-index:12;
	left: 498px;
	top: 139px;
	color: #999;
}
#header .CollapsiblePanelContent #apDiv23 strong {
	color: #999;
}
#header .CollapsiblePanelContent #apDiv #form1 table tr td {
	color: #999;
}
#apDiv25 {	position:absolute;
	width:63px;
	height:21px;
	z-index:11;
	left: 311px;
	top: 141px;
}
#header #logo #apDiv8 strong {
	color: #999;
}
#apDiv26 {	position:absolute;
	width:52px;
	height:81px;
	z-index:10;
	left: 143px;
	top: 216px;
	color: #999;
}
#apDiv27 {	position:absolute;
	width:65px;
	height:70px;
	z-index:3;
	left: 126px;
	top: 320px;
	color: #999;
}
#apDiv28 {	position:absolute;
	width:63px;
	height:29px;
	z-index:4;
	left: 147px;
	top: 396px;
}
#apDiv29 {	position:absolute;
	width:68px;
	height:74px;
	z-index:5;
	left: 126px;
	top: 470px;
	font-weight: bold;
}
#apDiv30 {	position:absolute;
	width:63px;
	height:29px;
	z-index:9;
	left: 120px;
	top: 469px;
}
#apDiv31 {	position:absolute;
	width:81px;
	height:88px;
	z-index:2;
	left: 135px;
	top: 656px;
}
#apDiv32 {
	position:absolute;
	width:200px;
	height:115px;
	z-index:13;
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
      <div id="apDiv32"><img src="${request.static_url('fyp:static/images/logoo.PNG')}" alt="" width="86" height="92" /></div>
      <h1>&nbsp;</h1>
      <h1>Home Controller</h1>
    </div>
<p>&nbsp;</p>
<h1><a href="#"></a> </h1>
		<p>&nbsp;</p>
  </div>
 
    <div class="CollapsiblePanelTab" tabindex="0"></div>
    <div class="CollapsiblePanelContent">
      <div id="apDiv">
        <form id="form1" method="post" action="">
        <table width="410" border="1">
            <tr>
              <td height="154"><strong>TUBE LIGHT1 </strong></td>
              <td>&nbsp;</td>
            </tr>
            <tr>
              <td height="146"><strong>RADIO </strong></td>
              <td><div id="apDiv2">
                <div align="center">
                  <p>ON<img src="${request.static_url('fyp:static/images/bulb1.PNG')}" alt="" width="66" height="92" /></p>
                </div>
              </div></td>
            </tr>
            <tr>
              <td width="152" height="154"><strong>FAN</strong></td>
              <td width="242"><div id="apDiv5">
                <div align="center">OFF<img src="${request.static_url('fyp:static/images/bulb.PNG')}" alt="" width="66" height="92" /></div>
              </div>
                <div id="apDiv14">
                  <div align="center">OFF<img src="${request.static_url('fyp:static/images/bulb.PNG')}" alt="" width="66" height="92" /></div>
              </div></td>
            </tr>
          </table>
        <div align="center"></div>
        </form>
      </div>
      <div id="apDiv23"><strong>DEVICE</strong> </div>
      <div id="apDiv24"><strong>STATUS</strong>      </div>
      <p>&nbsp; </p>
      <p>&nbsp;</p>
          <div id="apDiv8"><strong><a href="${request.route_url('home')}">HOME</a></strong><img src="${request.static_url('fyp:static/images/cap1.PNG')}" alt="" width="69" height="60" /></div>
    <div id="apDiv4"><strong><a href="${request.route_url('control')}">CONTROL</a></strong> <a href="${request.route_url('control')}"><img src="${request.static_url('fyp:static/images/bulb.PNG')}" alt="" width="61" height="50" /></a></div>
      <p>&nbsp;</p>
      <div id="apDiv3">
        <div align="center"><a href = "${request.route_url('security')}"><strong>SECURITY</strong><img src="${request.static_url('fyp:static/images/security.PNG')}" alt="" width="54" height="69" /></a></div>
      </div>
      <div id="apDiv6"><a href="${request.route_url('audio')}"><strong>AUDIO</strong> <img src="${request.static_url('fyp:static/images/BACK.PNG')}" alt="" width="53" height="57" /></a></div>
      <p>&nbsp;</p>
      <div id="apDiv9"><a href="#"><strong>STATUS</strong> <img src="${request.static_url('fyp:static/images/status.PNG')}" alt="" width="58" height="60" /></a></div>
      <p>&nbsp;</p>
      <p>&nbsp;</p>
  </div>
</div>
<div id="apDiv10"><a href="${request.route_url('settings')}"><strong>SETTINGS</strong></a></strong><a href= "${request.route_url('settings')}"><img src="${request.static_url('fyp:static/images/settings77.PNG')}" alt="" width="53" height="67" /></a></div>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;       </p>
</div>
</div>
</body>
</html>
