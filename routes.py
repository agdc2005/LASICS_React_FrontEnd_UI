from flask import render_template, request, url_for, redirect, make_response
from app import app
import sys
import json
#import datetime

@app.route('/')
@app.route('/index', methods=[ 'GET' ])
def index():
   return render_template("index.html")
#
#
@app.route('/getTargetNames', methods=[ 'GET' ])
def getTargetNames():
   #data = []
   targetNames = []
   targetIDs   = []
   targetTypes = []
   #with open('get_Targets_Test.json') as f:
   with open('get_Targets.json') as f:
       for line in f:
          #data.append(json.dumps(line))
          aDict = json.loads(line)
          # read as binary and return as file and set content type as json
   #print(type(data))
   f.close()
   #print('type data')
   #print(type(data))
   #print('type aDict')
   #print(type(aDict))
   #print(line)
   #print(aDict['SPS_Response']['Response']['Targets']['target'][0]['name'])
   #dump(data)
   #print(data['SPS_Response']['Response']['Targets']['target']['name'][0])
   #print(data['SPS_Response']['Response']['Targets']['target']['type'][0])
   for key in aDict['SPS_Response']['Response']['Targets']['target']:
      targetNames.append(key['name'])
      targetIDs.append(key['ID'])
      targetTypes.append(key['type'])
   #
   #return render_template('test.html', json.dumps(targetNames))

   return(json.dumps(targetNames))
   #return(json.dumps(data))
#
#------------TESTING
# serveTargets API Route
# @ signfies a decorator - way to wrap a function and modify its behavior
# flask will map a URL to a return value of function
import socket
import time
from recv_timeout import recv_timeout 
from convert_XMLFile_to_JSONFile import convert_XMLFile_to_JSONFile
@app.route('/serveTargets', methods=[ 'GET' ])
# The client route is pretty simple. 
# It creates a socket object, 
# Connects to the server and calls s.sendall() to send its message. 
# Lastly, it calls s.recv() to read the server’s reply and then prints it. 
def serveTargets():
    try:
       # create the socket
       # AF_INET == ipv4
       # SOCK_STREAM == TCP
       # create a socket object
       # create an INET, STREAMing socket 
       socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
       print (f"socket successfully created!")
    except socket.error as err: 
       print ("socket creation failed with error %s" %(err))

    socket_obj.settimeout(5.0)
    # default port for socket 
    port = 8416
  
    try: 
       #host_ip = '54.159.141.53' 
       host_ip = '146.165.248.44' 
       # connecting to the server 
       socket_obj.connect((host_ip, port)) 
       print("the socket has successfully connected to SPS_server  "+ host_ip + ":" + str(port) ) 
       print('*************************************************************************')
       # Send request 1 to server
       request = '<SPS_Request><Request>getTargets</Request></SPS_Request>'
       print("request sent to server is: 1   " + request)
       socket_obj.sendall(request.encode())
       print('**************************************************************************')
       # receive response from the server 
       # need to identify another logic that will represent the end of the data transfer
       #print("response received from server is: " )
       #print(response.decode("utf-8"))
       # Buffer Size is set to 8192 Bytes
       response = recv_timeout(socket_obj,8192)
       #print('the server response is : ')
       #print(response)
       # create the get_Targets.xml File in directory where flask server is started
       f = open('get_Targets.xml',mode='w',encoding="utf-8") # Open in byte mode for writing
       # inject the XML declaration string
       xmlLine1 = "<?xml version="+"\"1.0\""+" encoding=" + "\"UTF-8\"" +" ?>"
       #breakpoint()
       #print(type(xmlLine1))
       #print(type(response))
       f.write(xmlLine1+"\n")
       f.write(response)
       f.close()
       # create the get_Targets.json file from the get_Targets.xml file
       # in directory where flask server is started
       convert_XMLFile_to_JSONFile("get_Targets.xml","get_Targets.json")
       #       
       targetNames = []
       with open('get_Targets.json') as f:
          for line in f:
             #data.append(json.dumps(line))
             aDict = json.loads(line)
             #print(type(data))
       f.close()
       for key in aDict['SPS_Response']['Response']['Targets']['target']:
       #print(key['name'])
          targetNames.append(key['name'])
       return(json.dumps(targetNames))
       #return(json.dumps(data))
       socket_obj.close()
    except socket.timeout as e:
       print(f"Response TimeOut: {e}")
       print(f"FAILED")
       socket_obj.close()
       print('Using cached local file to serveTargets: get_Targets_Local.json')
       with open('get_Targets_Local.json') as f:
          for line in f:
             #data.append(json.dumps(line))
             aDict = json.loads(line)
             #print(type(data))
       f.close()
       for key in aDict['SPS_Response']['Response']['Targets']['target']:
       #print(key['name'])
          targetNames.append(key['name'])
       return(json.dumps(targetNames))
       socket_obj.close()
       #sys.exit()
    except socket.gaierror:
     # this means could not resolve the host 
       print("There was an ERROR resolving the host at:" + str(host_ip))
       sys.exit()
#------------END TESTING
#
#
@app.route('/getTargetRestrictions', methods=[ 'GET' ])
def getTargetRestrictions():
   #data = []
   targetNames = []
   targetConstraints = []
   with open('get_TargetRestrictions_Test.json') as f:
       for line in f:
          #data.append(json.dumps(line))
          aDict = json.loads(line)
   #print(type(data))
   f.close()
   #print('type data')
   #print(type(data))
   #print('type aDict')
   #print(type(aDict))
   #print(line)
   #print(aDict['SPS_Response']['Response']['Targets']['target'][0]['name'])
   #dump(data)
   #print(data['SPS_Response']['Response']['Targets']['target']['name'][0])
   #print(data['SPS_Response']['Response']['Targets']['target']['type'][0])
   for key in aDict['SPS_Response']['Response']['TargetRestrictions']['Restriction']:
      #print(key['name'])
      #targetNames.append(key['TargetName'])
      if (key['TargetName']) == 'AQUA' :
          targetConstraints.append(key['Constraint'])
      #targetTypes.append(key['type'])
   #
   #return render_template('test.html', json.dumps(targetNames))
   return(json.dumps(targetConstraints))
   #return(json.dumps(data))
#
#
@app.route('/serveDaysInPlanChoices')
def serveDaysInPlanChoices():
   #data = []
   DaysInPlan = [1,2,3,5,7,10,14,21,30,45,60]
   return(json.dumps(DaysInPlan))
#
#
@app.route('/serveTimeDiffbetnReferenceandTargetChoices')
def serveTimeDiffbetnReferenceandTargetChoices():
   #data = []
   # Default to 15.0 minutes
   TimeDiffbetnRefandTar = [15.0,5.0,10.0,20.0,30.0]
   return(json.dumps(TimeDiffbetnRefandTar))
#
#
@app.route('/serveSolarZenithAngleChoices')
def serveSolarZenithAngleChoices():
   # Default to 70.0
   SolarZenithAngles = [70.0,15.0,25.0,30.0,40.0,50.0,60.0,65.0,75.0,90.0]
   return(json.dumps(SolarZenithAngles))
#
#
@app.route('/serveViewZenithAngleChoices')
def serveViewZenithAngleChoices():
   # Default to 70.0
   ViewZenithAngles = [70.0,5.0,10.0,15.0,25.0,30.0,40.0,45.0,50.0,55.0,60.0,65.0]
   return(json.dumps(ViewZenithAngles))
#
#
# import modules that are needed in the next route
import uuid
# This send_TargetAltitudes_Request_to_SPS_Server.py file is in directory immediately above this routes.py file
from send_TargetAltitudes_Request_to_SPS_Server import send_TargetAltitudes_Request_to_SPS_Server
# This create_SPS_XML_Request.py file is in directory immediately above this routes.py file 
from create_SPS_XML_Request import create_SPS_XML_Request 
# This send_xml_object_to_SPS_Server.py file is in directory immediately above this routes.py file 
from send_xml_object_to_SPS_Server import send_xml_object_to_SPS_Server 
# This get_planID_from_SPS_Server_Response.py file is in directory immediately above this routes.py file 
from get_planID_from_SPS_Server_Response import get_planID_from_SPS_Server_Response
# This get_planStatus_from_SPS_Server_Response.py file is in directory immediately above this routes.py file 
from get_planStatus_from_SPS_Server_Response import get_planStatus_from_SPS_Server_Response
# This send_PlanStatus_Request_to_SPS_Server.py file is in directory immediately above this routes.py file
from send_PlanStatus_Request_to_SPS_Server import send_PlanStatus_Request_to_SPS_Server
# This send_PlanPlot_Request_to_SPS_Server.py file is in directory immediately above this routes.py file
from send_PlanPlot_Request_to_SPS_Server import send_PlanPlot_Request_to_SPS_Server
# This send_PlanResultsXMLFile_Request_to_SPS_Server.py file is in directory immediately above this routes.py file
from send_PlanResultsXMLFile_Request_to_SPS_Server import send_PlanResultsXMLFile_Request_to_SPS_Server
# This get_xmlFileTemplate.py file is in directory immediately above the directory containing routes.py
from get_xmlFileTemplate import get_xmlFileTemplate
# This get_target2Type.py file is in directory immediately above the directory containing routes.py
from get_target2Type import get_target2Type
# This vprint.py file is in directory immediately above this routes.py file
from vprint import vprint
# import sys
import datetime

@app.route('/echoJSON', methods=['POST'])
def echoJSON():
# Get current module name for debug purposes
    current_module_name = sys.modules[__name__]
# set verbose = True to get all the optional print statements to execute
    verbose = False
    #print(request.get_json())
    request_data = request.get_json()

    PlanDurationInDays    = None
    PlanStartEpochDate    = None
    Reference_Name        = None
    Reference_MaxSZA      = 0.0
    Target_MaxVZA         = 0.0
    Target_Name           = None
    Max_Time_Diff_Ref_Tar = 0.0
    Requester_Email = ' '

# https://stackoverflow.com/questions/8653516/python-list-of-dictionaries-search

    if request_data:
       key_string = 'General:PlanDurationInDays'
       resultlist = [d  for d in request_data  if d.get('key', '') == key_string]
       if len(resultlist) > 0:
          PlanDurationInDays = str(resultlist[0].get('value')) 

       key_string = 'General:PlanStartEpochDate'
       resultlist = [d  for d in request_data  if d.get('key', '') == key_string]
       if len(resultlist) > 0:
          PlanStartEpochDate = str(resultlist[0].get('value'))

       key_string = 'Reference:Name'
       resultlist = [d  for d in request_data  if d.get('key', '') == key_string]
       if len(resultlist) > 0:
          Reference_Name = str(resultlist[0].get('value')) 

       key_string = 'Reference:Constraints:Constraint:ConstraintName:max_solar_zenith_angle'
       resultlist = [d  for d in request_data  if d.get('key', '') == key_string]
       if len(resultlist) > 0:
          Reference_MaxSZA = str(resultlist[0].get('value'))

#
       key_string = 'Targets:Target:TargetName'
       resultlist = [d  for d in request_data  if d.get('key', '') == key_string]
       if len(resultlist) > 0:
          Target_Name = str(resultlist[0].get('value'))
 
# -->>> For Target 2 = LEO-LASICS
       key_string = 'Targets:Target:Constraints:Constraint:ConstraintName:max_time_diff_ref_and_target'
       resultlist = [d  for d in request_data  if d.get('key', '') == key_string]
       if len(resultlist) > 0:
          Max_Time_Diff_Ref_Tar = str(resultlist[0].get('value')) 
# --<<<

# -->>> For Target 2 == LandNadir-LASICS TargetType or Target 2 == GEO-LASICS TargetType
       key_string = 'Targets:Target:Constraints:Constraint:ConstraintName:max_viewing_zenith_angle'
       resultlist = [d  for d in request_data  if d.get('key', '') == key_string]
       if len(resultlist) > 0:
          Target_MaxVZA = str(resultlist[0].get('value'))
# --<<<

       key_string = 'PlanRequester:Email'
       resultlist = [d  for d in request_data  if d.get('key', '') == key_string]
       if len(resultlist) > 0:
          Requester_Email = str(resultlist[0].get('value'))
    #
    print(' ')
    print("The Target 1 Requested is                                                   : "+ Reference_Name)
    print("The Target 2 Requested is                                                   : "+ Target_Name)
    print("The Plan Duration Days Requested is (Days)                                  : "+ PlanDurationInDays)
    print("The Plan Start Epoch Date Requested                                         : "+ PlanStartEpochDate)
    print("The Max. Duration Constraint Requested betn Reference & Target is (Minutes) : ", Max_Time_Diff_Ref_Tar)
    print("The Max_SZA Constraint Requested is (Degrees)                               : ", Reference_MaxSZA)
    print("The Max_VZA Constraint Requested is (Degrees)                               : ", Target_MaxVZA)
    print("The Science Plan Requester email is                                         : "+ Requester_Email)

    # For LEO-LASICS and GEO-LASICS Cases
    # Switch Reference (Target 1) and Target (Target 2) so that Reference is always the satellite at lower earth orbit
    SPS_TargetAltitudes_Request = '<SPS_Request><Request>getSatelliteAltitudes</Request></SPS_Request>'
    SPS_Server_Response = send_TargetAltitudes_Request_to_SPS_Server(SPS_TargetAltitudes_Request)
    print(SPS_Server_Response)
    #f = open('get_TargetAltitudes.xml',mode='w',encoding="utf-8") # Open in byte mode for writing
    # inject the XML declaration string
    #xmlLine1 = "<?xml version="+"\"1.0\""+" encoding=" + "\"UTF-8\"" +" ?>"
    #f.write(xmlLine1+"\n")
    #f.write(SPS_Server_Response)
    #f.close()
    # create the get_Targets.json file from the get_Targets.xml file
    #convert_XMLFile_to_JSONFile("get_TargetAltitudes.xml","get_TargetAltitudes.json")
    #       
    #targetAltitudes = []
    #with open('get_TargetAltitudes.json') as f:
    #for line in f:
       #data.append(json.dumps(line))
       #aDict = json.loads(line)
       #print(type(data))
       #f.close()
    print('--------------------------------------------------------------')
    #
    # Create Unique User ID
    user_UUID = uuid.uuid4()
    # Create an ASCII Text File for email to User that shows their UI Selections

    #
    # Create a dict with Request Data
    User_Request_Data = { "Reference_Name": Reference_Name, 
                          "Target_Name" : Target_Name,
                          "PlanDurationInDays" : PlanDurationInDays,
                          "PlanStartEpochDate": PlanStartEpochDate,
                          "Max_Time_Diff_Ref_Tar": Max_Time_Diff_Ref_Tar,
                          "Reference_MaxSZA": Reference_MaxSZA,
                          "Target_MaxVZA": Target_MaxVZA, 
                          "Requester_Email": Requester_Email }

# call the create_SPS_XML_Request Module and  update the XML document
    print(User_Request_Data)
    # create user request xml file for submission to SPS server via sockets
    # xmlFile is template which is updated with User_Request_Data
    # This file is in directory above current workind directory with routes.py file
    # Determine which xmlFile to use based on Target Type corresponding to Target_Name
    #xmlFile = 'LASICS_SPS_Request_Template_LEOLASICS.xml'
    #xmlFile = 'LASICS_SPS_Request_Template.GEOLASICS.xml'
    #xmlFile = 'LASICS_SPS_Request_Template.LandNadirLASICS.xml'
    print('Target_Name: ', Target_Name)
    xmlFile = get_xmlFileTemplate(Target_Name)
    print('xmlFileTemplate used: ', xmlFile)
    #xmlFile = 'LASICS_SPS_Request_Template.xml'
    target2Type = get_target2Type(Target_Name)
    print('Target 2 Type is: ', target2Type)
    #user_UUID = uuid.uuid4()
    #xml_object = create_SPS_XML_Request(xmlFile,user_UUID,User_Request_Data)
    xml_object = create_SPS_XML_Request(xmlFile,target2Type,user_UUID,User_Request_Data)
    print('User Unique ID: ', user_UUID)
    vprint(verbose,xml_object)
    SPS_Server_Response = send_xml_object_to_SPS_Server(xml_object)
    print(current_module_name)
    print('********************RESPONSE RECEIVED from AWS LASICS SPS***************************')
    print(SPS_Server_Response)
    # SPS_Server_Response e.g. <SPS_Response><Response><planID>23</planID></Response></SPS_Response>
    # extract/get the planID value from SPS_Server_Response
    plan_ID = get_planID_from_SPS_Server_Response(SPS_Server_Response)
    print('plan_ID is: ', plan_ID)
    # 
    # Check plan status every 30(= checkTimeInterval) minutes ?? 
    # Create the planStatus Request as below
    SPS_PlanStatus_Request = '<SPS_Request><Request>getPlanStatus</Request><planID>'+str(plan_ID)+'</planID></SPS_Request>'
    # get planStatus Response as below
    SPS_Server_Response = send_PlanStatus_Request_to_SPS_Server(SPS_PlanStatus_Request)
    print(SPS_Server_Response)
    # extract/get Initial planStatus value
    plan_Status = get_planStatus_from_SPS_Server_Response(SPS_Server_Response)
    print('For user_UUID: ', user_UUID, ' plan_Status: ', plan_Status)
    startTime = time.time()
    # If value is 0 continue waiting for 60 seconds
    if ( plan_Status == 0 ):
      while True:
           # Keep pinging server for plan_Status again
           SPS_Server_Response = send_PlanStatus_Request_to_SPS_Server(SPS_PlanStatus_Request)
           plan_Status = get_planStatus_from_SPS_Server_Response(SPS_Server_Response)
           #print('plan_Status: ', plan_Status)
           print('For user_UUID: ', user_UUID, ' plan_Status: ', plan_Status)
           if ( plan_Status == 1):  #No errors and plan completed successfully
             # If value is 1 get the plan xmlfile with Science Opportunities
             # If value is 1 get the plan plot
             print('For user_UUID: ', user_UUID, ' plan_Status: ', plan_Status)
             print('Elapsed Time (Minutes)= ',(time.time() - startTime)/60.0) 
             # If value is 1 get the plan plot by sending planPlot Request
             SPS_PlanPlot_Request = '<SPS_Request><Request>getPlanPlot</Request><planID>'+str(plan_ID)+'</planID></SPS_Request>'
             SPS_Server_Response = send_PlanPlot_Request_to_SPS_Server(SPS_PlanPlot_Request)
             # If value is 1 get the plan xmlfile with Science Opportunities
             SPS_PlanResultsXMLFile_Request = '<SPS_Request><Request>getPlanResultsFile</Request><planID>'+str(plan_ID)+'</planID></SPS_Request>'
             SPS_Server_Response = send_PlanResultsXMLFile_Request_to_SPS_Server(SPS_PlanResultsXMLFile_Request)
             now_date = datetime.datetime.now()
             with open("LASICS_SciencePlan_"+now_date.isoformat()+".xml",'w') as fout:
                fout.write(SPS_Server_Response)
             fout.close()
             print('--------------------------------------------------------------')
             # email User results to User when available
             # email is : User_Request_Data['Requester_Email']
             break
           if ( plan_Status == 2):   #Errors but plan still in process
             SPS_Server_Response = "Errors have occured but Plan is still in process."
             print('Plan_Status is: ', plan_Status + SPS_Server_Response) 
                  # Keep pinging server for plan_Status again
           if ( plan_Status == 3):
             # Error Completed (Plan is Complete but with Errors)
             # possibly TLE's not found for Target 1 and or Target 2
             print('For user_UUID: ', user_UUID, ' plan_Status: ', plan_Status)
             print('Elapsed Time (Minutes)= ',(time.time() - startTime)/60.0) 
             SPS_Server_Response_1 = "Plan Complete: With Errors " 
             SPS_Server_Response_2 = "Possible Reason 1: TLE's not found for Target 1: " + Reference_Name 
             SPS_Server_Response_3 = "Possible Reason 2: TLE's not found for Target 2: " + Target_Name 
             SPS_Server_Response_4 = "For Selected PlanStartEpochDate: " + PlanStartEpochDate
             SPS_Server_Response_5 = "Possible Reason 3: No Orbital Overlap between Target-1 and Target-2 for the Day(s) in question" 
             now_date = datetime.datetime.now()
             with open("LASICS_SciencePlan_"+now_date.isoformat()+".xml",'w') as fout:
                fout.write(SPS_Server_Response_1)
                fout.write("\n")
                fout.write(SPS_Server_Response_2)
                fout.write("\n")
                fout.write(SPS_Server_Response_3)
                fout.write("\n")
                fout.write(SPS_Server_Response_4)
                fout.write("\n")
                fout.write(SPS_Server_Response_5)
             fout.close()
             print('--------------------------------------------------------------')
             # email User results to User when available
             # email is : User_Reqeust_Data['Requester_Email']
             break
           if ( plan_Status == 4):
             print('For user_UUID: ', user_UUID, ' plan_Status: ', plan_Status)
             print('Elapsed Time (Minutes)= ',(time.time() - startTime)/60.0) 
             SPS_Server_Response = "Error Plan Incomplete: critical error in the Science Planning System"
             now_date = datetime.datetime.now()
             with open("LASICS_SciencePlan_"+now_date.isoformat()+".xml",'w') as fout:
                fout.write(SPS_Server_Response)
             fout.close()
             # Critical SPS Error
             # email User results to User when available
             # email is : User_Reqeust_Data['Requester_Email']
             break
           ###
           ###
           print('tick-tick-tick')
           time.sleep(60.0 - ((time.time() - startTime) % 60.0))
    ######
    #return()
    #return make_response('Reference Requested is: ')
    return('Success: REACT to FLASK Comm: 200')
    #return redirect(url_for("userInput", refname=Reference_Name))

#
#@app.route('/<refname>')
#def userInput(refname):
#    return f"<h1>{refname}</h1>"
