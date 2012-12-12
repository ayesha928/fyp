<%inherit file="base.mako"/>

<%def name="javascript()">

<script type="text/javascript">
    require(["dojo", "dijit/registry", "dojo/request"],
        function(dojo, registry, request) {
       
            dojo.connect(registry.byId("main_gate_light"), "onStateChanged", function(newState){
                // This is called when the state of the on/off button of main gate section is changed
                
                request.post("${request.route_url('status')}", {
                        data: {
                            command_type: "SET",
                            section: "main_gate",
                            device: "light1",
                            status: "ON"
                        }
                    }).then(function(ajax_return){
                        //code here executes after the ajax call completes.
                        alert("Server Returned = " + ajax_return); 
                    });
                
            });
              

            dojo.connect(registry.byId("dining_energy_savers"), "onStateChanged",  function(newState){
                // This is called when the state of the on/off button of main gate section is changed 
                
                request.post("${request.route_url('status')}", {
                        data: {
                            command_type: "SET",
                            section: "dining_energy_savers",
                            device: "light2",
                            status: "ON"
                        }
                    }).then(function(ajax_return){
                        //code here executes after the ajax call completes.
                        alert("Server Returned = " + ajax_return); 
                    });
                
            });
            
            dojo.connect(registry.byId("dining_fan"), "onStateChanged", function(newState){
                // This is called when the state of the on/off button of main gate section is changed
                
                request.post("${request.route_url('status')}", {
                        data: {
                            command_type: "SET",
                            section: "dining_fan",
                            device: "fan1",
                            status: "OFF"
                        }
                    }).then(function(ajax_return){
                        //code here executes after the ajax call completes.
                        alert("Server Returned = " + ajax_return); 
                    });
                
            });

            dojo.connect(registry.byId("current_sections"), "onStateChanged", function(newState){
                // This is called when the state of the on/off button of main gate section is changed
                
                request.post("${request.route_url('settings')}", {
                        data: {
                               sections: "current_sections"
                            
                       
                        }
                    }).then(function(ajax_return){
                        //code here executes after the ajax call completes.
                        alert("Server Returned = " + ajax_return); 
                    });
                
            });

}
      );
            
    
</script>
</%def>


<!-- the view or "page"; select it as the "home" screen -->
<div id="home" data-dojo-type="dojox.mobile.View" data-dojo-props="selected: true">
         
    <!-- a sample heading -->
    <h1 data-dojo-type="dojox.mobile.Heading">Home Controller</h1>
 
    <!-- a rounded rectangle list container -->
     <ul data-dojo-type="dojox.mobile.RoundRectList">
    <li data-dojo-type="dojox.mobile.ListItem" data-dojo-props="icon:'static/images/con.png', moveTo: 'control'">
    Control
    </li>
    <li data-dojo-type="dojox.mobile.ListItem" data-dojo-props="icon:'static/images/in.png', moveTo: 'status'">
    Status
    </li>
    <li data-dojo-type="dojox.mobile.ListItem" data-dojo-props="icon:'static/images/aud.png', moveTo: 'audio'">
    Audio
    </li>
     <li data-dojo-type="dojox.mobile.ListItem" data-dojo-props="icon:'static/images/sec.png', moveTo: 'security'">
    Security
    </li>
     <li data-dojo-type="dojox.mobile.ListItem" data-dojo-props="icon:'static/images/st.png', moveTo: 'settings'">
    Settings
    </li>
    </ul>
    
</div>


<div id="control" data-dojo-type="dojox.mobile.View"> 
    <ul data-dojo-type="dojox.mobile.RoundRectList">
        <h1 data-dojo-type="dojox.mobile.Heading" data-dojo-props="back:'Home', moveTo:'home'">
        Control
        </h1>
        <!-- list item with an icon containing a switch -->
        <li data-dojo-type="dojox.mobile.ListItem" data-dojo-props="icon:'', moveTo: 'main_gate'">
            Main Gate
            
        </li>
        <li data-dojo-type="dojox.mobile.ListItem"
              data-dojo-props="icon:'', moveTo: 'Drawing/Dining'">
            Drawing/Dining
        </li>
        <li data-dojo-type="dojox.mobile.ListItem"
              data-dojo-props="icon:'', moveTo: 'tv_lounge'">
            TV Lounge
        </li>
        <li data-dojo-type="dojox.mobile.ListItem"
              data-dojo-props="icon:'', moveTo: 'living_room'">
            Living Room
        </li>
        <li data-dojo-type="dojox.mobile.ListItem"
              data-dojo-props="icon:'', moveTo: 'kitchen'">
            Kitchen
        </li>
        
    </ul>
</div>


<div id="main_gate" data-dojo-type="dojox.mobile.View">
    <h1 data-dojo-type="dojox.mobile.Heading" data-dojo-props="back:'Control', moveTo:'control'">
           Main Gate
    </h1>
    <ul data-dojo-type="dojox.mobile.RoundRectList">
        <li data-dojo-type="dojox.mobile.ListItem" data-dojo-props="">
            Door Lights
            <!-- the switch -->
            <div class="mblItemSwitch" data-dojo-type="dojox.mobile.Switch" id="main_gate_light" value="off"></div>
        </li>
    </ul>
</div>


<div id="Drawing/Dining" data-dojo-type="dojox.mobile.View">
    <h1 data-dojo-type="dojox.mobile.Heading" data-dojo-props="back:'Control', moveTo:'control'">
           Drawing/Dining
    </h1>
    <ul data-dojo-type="dojox.mobile.RoundRectList">
        <li data-dojo-type="dojox.mobile.ListItem" data-dojo-props="">
            Energy savers
            <!-- the switch -->
            <div class="mblItemSwitch" data-dojo-type="dojox.mobile.Switch" id="dining_energy_savers" value="off"></div>
        </li>
        <li data-dojo-type="dojox.mobile.ListItem" data-dojo-props="">
            Fan
        <!-- the switch -->
            <div class="mblItemSwitch" data-dojo-type="dojox.mobile.Switch" id="dining_fan" value="on"></div>
        </li>
    </ul>
</div>


<div id="tv_lounge" data-dojo-type="dojox.mobile.View">
    <h1 data-dojo-type="dojox.mobile.Heading" data-dojo-props="back:'Control', moveTo:'control'">
            Tv Lounge
    </h1>
    <ul data-dojo-type="dojox.mobile.RoundRectList">
        <li data-dojo-type="dojox.mobile.ListItem" data-dojo-props="">
            Tube Light
            <!-- the switch -->
            <div class="mblItemSwitch" data-dojo-type="dojox.mobile.Switch"></div>
        </li>
    </ul>
</div>


<div id="living_room" data-dojo-type="dojox.mobile.View">
    <h1 data-dojo-type="dojox.mobile.Heading" data-dojo-props="back:'Control', moveTo:'control'">
            Living Room
    </h1>
    <ul data-dojo-type="dojox.mobile.RoundRectList">
        <li data-dojo-type="dojox.mobile.ListItem" data-dojo-props="">
            Living room's Lamp
            <!-- the switch -->
            <div class="mblItemSwitch" data-dojo-type="dojox.mobile.Switch"></div>
        </li>
        <li data-dojo-type="dojox.mobile.ListItem" data-dojo-props="moveTo:'wash_room'">
            Attached Washroom 
        </li>
    </ul>
</div>

<div id="wash_room" data-dojo-type="dojox.mobile.View">
    <h1 data-dojo-type="dojox.mobile.Heading" data-dojo-props="back:'Living Room', moveTo:'living_room'">
            Wash Room
    </h1>
    <ul data-dojo-type="dojox.mobile.RoundRectList">
        <li data-dojo-type="dojox.mobile.ListItem" data-dojo-props="">
            Energy Saver
            <!-- the switch -->
            <div class="mblItemSwitch" data-dojo-type="dojox.mobile.Switch"></div>
        </li>
    </ul>
</div>

<div id="kitchen" data-dojo-type="dojox.mobile.View">
    <h1 data-dojo-type="dojox.mobile.Heading" data-dojo-props="back:'Control', moveTo:'control'">
            Kitchen
    </h1>
    <ul data-dojo-type="dojox.mobile.RoundRectList">
        <li data-dojo-type="dojox.mobile.ListItem" data-dojo-props="">
            Bulb
            <!-- the switch -->
            <div class="mblItemSwitch" data-dojo-type="dojox.mobile.Switch"></div>
        </li>
        <li data-dojo-type="dojox.mobile.ListItem" data-dojo-props="">
            Fan
        <!-- the switch -->
            <div class="mblItemSwitch" data-dojo-type="dojox.mobile.Switch"></div>
        </li>
    </ul>
</div>

<div id="status" data-dojo-type="dojox.mobile.View">
<ul data-dojo-type="dojox.mobile.RoundRectList">
                <h1 data-dojo-type="dojox.mobile.Heading" data-dojo-props="back:'Home', moveTo:'home'">
                Status
                </h1>
                <!-- list item with an icon containing a switch -->
                <li data-dojo-type="dojox.mobile.ListItem" data-dojo-props="icon:'', moveTo: 'main_gate_status'">
                    Main Gate
                    
                </li>
                <li data-dojo-type="dojox.mobile.ListItem"
                      data-dojo-props="icon:'', moveTo: 'Drawing/Dinning_status'">
                    Drawing/Dining
                </li>
                <li data-dojo-type="dojox.mobile.ListItem"
                      data-dojo-props="icon:'', moveTo: 'tv_lounge_status'">
                    TV Lounge
                </li>
                <li data-dojo-type="dojox.mobile.ListItem"
                      data-dojo-props="icon:'', moveTo: 'bed_room_status'">
                    Living Room
                </li>
                <li data-dojo-type="dojox.mobile.ListItem"
                      data-dojo-props="icon:'', moveTo: 'kitchen_status'">
                    Kitchen
                </li>
                
            </ul>
 </div>
<div id="main_gate_status" data-dojo-type="dojox.mobile.View">
            <h1 data-dojo-type="dojox.mobile.Heading" data-dojo-props="back:'Status', moveTo:'status'">
                   Main Gate
            </h1>
            <ul data-dojo-type="dojox.mobile.RoundRectList">
                <li data-dojo-type="dojox.mobile.ListItem" data-dojo-props="">
                    Door Lights
                    <!-- the switch -->
                    <div class="mblItemSwitch" data-dojo-type="dojox.mobile.Switch"></div>
                </li>
            </ul>
        </div>
<div id="Drawing/Dinning_status" data-dojo-type="dojox.mobile.View">
            <h1 data-dojo-type="dojox.mobile.Heading" data-dojo-props="back:'Status', moveTo:'status'">
                   Drawing/Dining
            </h1>
            <ul data-dojo-type="dojox.mobile.RoundRectList">
                <li data-dojo-type="dojox.mobile.ListItem" data-dojo-props="">
                    Energy savers
                    <!-- the switch -->
                    <div class="mblItemSwitch" data-dojo-type="dojox.mobile.Switch"></div>
                </li>
                <li data-dojo-type="dojox.mobile.ListItem" data-dojo-props="">
                    Fan
                <!-- the switch -->
                    <div class="mblItemSwitch" data-dojo-type="dojox.mobile.Switch"></div>
                </li>
            </ul>
        </div>
<div id="tv_lounge_status" data-dojo-type="dojox.mobile.View">
            <h1 data-dojo-type="dojox.mobile.Heading" data-dojo-props="back:'Status', moveTo:'status'">
                    Tv Lounge
            </h1>
            <ul data-dojo-type="dojox.mobile.RoundRectList">
                <li data-dojo-type="dojox.mobile.ListItem" data-dojo-props="">
                    Tube Light
                    <!-- the switch -->
                    <div class="mblItemSwitch" data-dojo-type="dojox.mobile.Switch"></div>
                </li>
            </ul>
        </div>
<div id="living_room_status" data-dojo-type="dojox.mobile.View">
            <h1 data-dojo-type="dojox.mobile.Heading" data-dojo-props="back:'Status', moveTo:'status'">
                    Living Room
            </h1>
            <ul data-dojo-type="dojox.mobile.RoundRectList">
                <li data-dojo-type="dojox.mobile.ListItem" data-dojo-props="">
                    Living room's Lamp
                    <!-- the switch -->
                    <div class="mblItemSwitch" data-dojo-type="dojox.mobile.Switch"></div>
                </li>
                <li data-dojo-type="dojox.mobile.ListItem" data-dojo-props="moveTo:'wash_room_status'">
                    Attached Washroom 
                </li>
            </ul>
        </div>
<div id="wash_room_status" data-dojo-type="dojox.mobile.View">
            <h1 data-dojo-type="dojox.mobile.Heading" data-dojo-props="back:'Living Room', moveTo:'living_room'">
                    Wash Room
            </h1>
            <ul data-dojo-type="dojox.mobile.RoundRectList">
                <li data-dojo-type="dojox.mobile.ListItem" data-dojo-props="">
                    Energy Saver
                    <!-- the switch -->
                    <div class="mblItemSwitch" data-dojo-type="dojox.mobile.Switch"></div>
                </li>
            </ul>
        </div>
 <div id="kitchen_status" data-dojo-type="dojox.mobile.View">
            <h1 data-dojo-type="dojox.mobile.Heading" data-dojo-props="back:'Status', moveTo:'status'">
                    Kitchen
            </h1>
            <ul data-dojo-type="dojox.mobile.RoundRectList">
                <li data-dojo-type="dojox.mobile.ListItem" data-dojo-props="">
                    Bulb
                    <!-- the switch -->
                    <div class="mblItemSwitch" data-dojo-type="dojox.mobile.Switch"></div>
                </li>
                <li data-dojo-type="dojox.mobile.ListItem" data-dojo-props="">
                    Fan
                <!-- the switch -->
                    <div class="mblItemSwitch" data-dojo-type="dojox.mobile.Switch"></div>
                </li>
            </ul>
    </div>
    </div>

<div id="settings" data-dojo-type="dojox.mobile.View">
           <h1 data-dojo-type="dojox.mobile.Heading" data-dojo-props="back:'Home', moveTo:'home'">
                Settings
            </h1>
    <ul data-dojo-type="dojox.mobile.RoundRectList">
    <li data-dojo-type="dojox.mobile.ListItem" data-dojo-props="icon:'', moveTo: 'section_settings'">
     Section
    </li>
    <li data-dojo-type="dojox.mobile.ListItem" data-dojo-props="icon:'', moveTo: 'device_settings'">
        Device
        </li>
    </ul>
</div>
<div id="section_settings" data-dojo-type="dojox.mobile.View">
            <h2 data-dojo-type="dojox.mobile.Heading" data-dojo-props="back:'Settings', moveTo:'settings'">
             Section Settings
            </h2> 
            <ul data-dojo-type="dojox.mobile.RoundRectList">
                <li data-dojo-type="dojox.mobile.ListItem" data-dojo-props="icon:'', moveTo: 'current_sections'">
                    Current Sections
                </li>
                <li data-dojo-type="dojox.mobile.ListItem" data-dojo-props="">
                    Add a new Section
                </li>
                <li data-dojo-type="dojox.mobile.ListItem" data-dojo-props="">
                    Delete a Section
                </li>
                <li data-dojo-type="dojox.mobile.ListItem" data-dojo-props="">
                   Rename a Section
                </li>
</div>

<div id="device_settings" data-dojo-type="dojox.mobile.View">
            <h1 data-dojo-type="dojox.mobile.Heading" data-dojo-props="back:'Settings', moveTo:'settings'">
             Device Settings
            </h1>
            <ul data-dojo-type="dojox.mobile.RoundRectList">
                <li data-dojo-type="dojox.mobile.ListItem" data-dojo-props="icon:'', moveTo: 'current_devices'">
                    Current Devices
                </li>
                <li data-dojo-type="dojox.mobile.ListItem" data-dojo-props="">
                    Add a new Device
                </li>
                <li data-dojo-type="dojox.mobile.ListItem" data-dojo-props="">
                    Delete a Device
                </li>
                <li data-dojo-type="dojox.mobile.ListItem" data-dojo-props="">
                   Rename a Device
                </li>
</div>


 <div id="current_sections" data-dojo-type="dojox.mobile.View">
            <h1 data-dojo-type="dojox.mobile.Heading" data-dojo-props="back:'Section Settings', moveTo:'section_settings'">
                    Current Sections
            </h1>
</div>

 <div id="current_devices" data-dojo-type="dojox.mobile.View">
            <h1 data-dojo-type="dojox.mobile.Heading" data-dojo-props="back:'Device Settings', moveTo:'device_settings'">
                    Current Devices
            </h1>
</div>

<div id="audio" data-dojo-type="dojox.mobile.View">
            <h1 data-dojo-type="dojox.mobile.Heading" data-dojo-props="back:'Home', moveTo:'home'">
                   Audio 
            </h1>
            <ul data-dojo-type="dojox.mobile.RoundRectList">
                <li data-dojo-type="dojox.mobile.ListItem" data-dojo-props="">
                    Play Audio Device
                    <!-- the switch -->
                    <div class="mblItemSwitch" data-dojo-type="dojox.mobile.Switch"></div>
                </li>
            </ul>
        </div>

<div id="security" data-dojo-type="dojox.mobile.View">
            <h1 data-dojo-type="dojox.mobile.Heading" data-dojo-props="back:'Home', moveTo:'home'">
                   Security
            </h1>
            <ul data-dojo-type="dojox.mobile.RoundRectList">
                <li data-dojo-type="dojox.mobile.ListItem" data-dojo-props="">
                    Security Camera 
                    <!-- the switch -->
                    <div class="mblItemSwitch" data-dojo-type="dojox.mobile.Switch"></div>
                </li>
            </ul>
        </div>