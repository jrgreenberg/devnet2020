from webexteamssdk import WebexTeamsAPI

import meraki
from  webexteamssdk import WebexTeamsAPI
import creds


meraki_api_key = creds.meraki_api_key
mynetwork = creds.mynetwork
myWebexToken = creds.myWebexToken



msversion = '12-28'
mrversion = '26-6-1'
mxversion = '15-27'
mvversion = '4-0'

WebexRoomID = "Y2lzY29zcGFyazovL3VzL1JPT00vZmIwMWQ2MjAtZGU0Ni0xMWVhLWE3OTMtN2Q3YTJiMWQ1YmNj"

def sendConfirmation():
    wxteams = WebexTeamsAPI(access_token=myWebexToken)
    wxteams.messages.create(WebexRoomID, text='Meraki Compliance check completed successfully')
    return()


def getDeviceCompliance():
    switches = []
    swfail =[]
    swpassed = 0
    firewalls = []
    fwfail=[]
    fwpassed = 0
    wireless = []
    wirelessfail = []
    wirelesspass = 0
    cameras = []
    camfail = []
    campass = 0
    dashboard = meraki.DashboardAPI(meraki_api_key)
    response = dashboard.networks.getNetworkDevices(mynetwork)
    
    for item in response:
        deviceSN = item.get('serial')
        deviceModel = item.get('model')
        deviceFW = item.get('firmware')
        version = deviceFW.split('-')
        if len(version) == 3:
            version = version[1] + '-' + version[2]
        elif len(version == 4):
            version = version[1] + '-' + version[2] + '-' + version[3]

        deviceDict = {"SN" : deviceSN, 'Version' : version, "Model" : deviceModel}
        #print(deviceDict)
        if "MX" in deviceModel:
            firewalls.append(deviceDict)
        if "MR" in deviceModel:
            wireless.append(deviceDict)
        if "MV" in deviceModel:
            cameras.append(deviceDict)
        if "MS" in deviceModel:
            switches.append(deviceDict)
    #print(firewalls,"\n", wireless, "\n",cameras,"\n",switches)
    
    for item in switches:
        if item.get('Version') == msversion:
            swpassed = swpassed + 1
        else:
            swfail.append(item)
  
    for item in wireless:
        if item.get('Version') == mrversion:
            wirelesspass = wirelesspass + 1
        else:
            wirelessfail.append(item)

    for item in firewalls:
        if item.get('Version') == mxversion:
            fwpassed = fwpassed + 1
        else:
            fwfail.append(item)
   
    for item in cameras:
        if item.get('Version') == mvversion:
            campass = campass + 1
        else:
            camfail.append(item)
    print(f'Total switches that meet standard: {swpassed}  ')
    print(f'Total APs that meet standard: {wirelesspass}')
    print(f'Total Security Appliances that meet standard: {fwpassed}')
    print(f'Total Cameras that meet standard: {campass}')
    print(f'Devices that will need to be manually checked: \n{swfail}\n{wirelessfail}\n{fwfail}\n{camfail}')
    return()



def main():
  getDeviceCompliance()
  sendConfirmation()

if __name__ == "__main__":
    main()