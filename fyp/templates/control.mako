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
    width:111px;
    height:126px;
    z-index:1;
    left: 812px;
    top: 233px;
}
#apDiv2 {
    position:absolute;
    width:72px;
    height:88px;
    z-index:2;
    left: 135px;
    top: 656px;
}
#apDiv3 {
    position:absolute;
    width:41px;
    height:30px;
    z-index:3;
    left: 142px;
    top: 318px;
}
#apDiv4 {
    position:absolute;
    width:69px;
    height:29px;
    z-index:4;
    left: 141px;
    top: 396px;
}
#apDiv5 {
    position:absolute;
    width:66px;
    height:75px;
    z-index:5;
    left: 142px;
    top: 480px;
    font-weight: bold;
}
</style>
<style type="text/css">
#apDiv6 {
    position:absolute;
    width:97px;
    height:76px;
    z-index:6;
    left: 208px;
    top: 17px;
}
#apDiv7 {
    position:absolute;
    width:597px;
    height:115px;
    z-index:7;
    left: 146px;
    top: 11px;
}
#apDiv8 {
    position:absolute;
    width:63px;
    height:66px;
    z-index:8;
    left: -1px;
    top: -83px;
}
#apDiv9 {
    position:absolute;
    width:67px;
    height:29px;
    z-index:9;
    left: 140px;
    top: 568px;
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
    width:55px;
    height:24px;
    z-index:10;
    left: 838px;
    top: 323px;
}
#apDiv15 {  position:absolute;
    width:121px;
    height:140px;
    z-index:1;
    left: 802px;
    top: 219px;
}
#apDiv16 {  position:absolute;
    width:34px;
    height:29px;
    z-index:9;
    left: 828px;
    top: 328px;
}
#apDiv17 {  position:absolute;
    width:33px;
    height:29px;
    z-index:10;
    left: 864px;
    top: 328px;
}
#apDiv18 {  position:absolute;
    width:55px;
    height:24px;
    z-index:10;
    left: 934px;
    top: 310px;
}
#apDiv19 {  position:absolute;
    width:55px;
    height:24px;
    z-index:10;
    left: 838px;
    top: 323px;
}
#apDiv20 {
    position:absolute;
    width:199px;
    height:36px;
    z-index:11;
    font-size: 18px;
    color: #999;
    left: 224px;
    top: 339px;
}
#apDiv21 {
    position:absolute;
    width:168px;
    height:27px;
    z-index:12;
    font-size: 18px;
    color: #999;
    left: 487px;
    top: 347px;
}
#apDiv22 {
    position:absolute;
    width:486px;
    height:735px;
    z-index:9;
    top: 164px;
    left: 242px;
    visibility: visible;
}
#logo #apDiv8 strong {
    color: #999;
}
</style>
<link href="SpryAssets/SpryCollapsiblePanel.css" rel="stylesheet" type="text/css" />
<style type="text/css">
#apDiv23 {
    position:absolute;
    width:200px;
    height:115px;
    z-index:10;
}
#apDiv {
    position:absolute;
    width:52px;
    height:81px;
    z-index:10;
    left: 143px;
    top: 221px;
    color: #999;
}
</style>
</head>
<body>
<!-- start header -->
 
<div id="header">
  <div id="logo">
    <h1>&nbsp;</h1>
<p>&nbsp;</p>

    <div id="apDiv7">
      <div id="apDiv23"><img src="${request.static_url('fyp:static/images/logoo.PNG')}" alt="" width="86" height="92" /></div>
      <h1>&nbsp;</h1>
      <h1>Home Controller</h1>
    </div>
    <p>&nbsp;</p>
<h1><a href="#"></a> </h1>
        <p>&nbsp;</p>
</div>
  <p>&nbsp;</p>
<p>&nbsp;</p>
<div id="apDiv">
<div id="apDiv8"><strong><a href="${request.route_url('home')}">HOME</a></strong><img src="${request.static_url('fyp:static/images/cap1.PNG')}" alt="" width="69" height="60" /></div>
  <div align="center"><a href = "#"><strong>CONTROL</strong><img src="${request.static_url('fyp:static/images/bulb.PNG')}" alt="" width="54" height="69" /></a></div>
</div>
<p>&nbsp;</p>
<div id="apDiv3"><strong><a href="${request.route_url('security')}">SECURITY</a></strong> <a href="{request.route_url('security')}"><img src="${request.static_url('fyp:static/images/security.PNG')}" alt="" width="61" height="50" /></a></div>
<p>&nbsp;</p>
<div id="apDiv4"><a href="${request.route_url('audio')}"><strong>AUDIO</strong> <img src="${request.static_url('fyp:static/images/BACK.PNG')}" alt="" width="53" height="57" /></a></div>
<p>&nbsp;</p>
<div id="apDiv5"><a href="${request.route_url('status')}"><strong>STATUS</strong> <img src="${request.static_url('fyp:static/images/status.PNG')}" alt="" width="58" height="60" /></a></div>
<p>&nbsp;</p>
<div id="apDiv9"><a href="${request.route_url('settings')}"><strong>SETTINGS</strong></a><img src="${request.static_url('fyp:static/images/settings77.PNG')}" alt="" width="53" height="67" /></a></div>
<p>&nbsp;</p>
<div id="apDiv22">
    <div class="CollapsiblePanelContent">ROOM1</div>
    <table width="489" height="720" border="1">
      <tr>
        <td width="170" height="106">TUBE LIGHT1</td>
        <td width="147"><div align="center"><a href= "#">OFF</a><img src="${request.static_url('fyp:static/images/bulb.PNG')}" alt="" width="66" height="92" /></div></td>
        <td width="150"><div align="center"><a href= "#">ON</a><img src="${request.static_url('fyp:static/images/bulb1.PNG')}" alt="" width="69" height="94" /></div></td>
      </tr>
      <tr>
        <td height="109">TUBE LIGHT2</td>
        <td> <div align="center"><a href= "#">OFF</a><img src="${request.static_url('fyp:static/images/bulb.PNG')}" alt="" width="66" height="92" /></div></td>
        <td><div align="center"><a href= "#">ON</a><img src="${request.static_url('fyp:static/images/bulb1.PNG')}" alt="" width="69" height="94" /></div></td>
      </tr>
      <tr>
        <td height="122">ENERGY SAVER</td>
        <td><div align="center"><a href= "#">OFF</a><img src="${request.static_url('fyp:static/images/bulb.PNG')}" alt="" width="66" height="92" /></div></td>
        <td><div align="center"><a href= "#">ON</a><img src="${request.static_url('fyp:static/images/bulb1.PNG')}" alt="" width="69" height="94" /></div></td>
      </tr>
      <tr>
        <td height="115">FAN</td>
        <td><div align="center">OFF<img src="${request.static_url('fyp:static/images/bulb.PNG')}" alt="" width="66" height="92" /></div></td>
        <td><div align="center"><a href= "#">ON</a><img src="${request.static_url('fyp:static/images/bulb1.PNG')}" alt="" width="69" height="94" /></div></td>
      </tr>
      <tr>
        <td height="109">TABLE LAMP</td>
        <td><div align="center"><a href= "#">OFF</a><img src="${request.static_url('fyp:static/images/bulb.PNG')}" alt="" width="66" height="92" /></div></td>
        <td><div align="center"><a href= "#">ON</a><img src="${request.static_url('fyp:static/images/bulb1.PNG')}" alt="" width="69" height="94" /></div></td>
      </tr>
      <tr>
        <td height="116">TELEVISION </td>
        <td><div align="center"><a href= "#">OFF</a><img src="${request.static_url('fyp:static/images/bulb.PNG')}" alt="" width="66" height="92" /></div></td>
        <td><div align="center"><a href= "#">ON</a><img src="${request.static_url('fyp:static/images/bulb1.PNG')}" alt="" width="69" height="94" /></div></td>
      </tr>
    </table></div>
</div>
</div>
</body>
</html>
