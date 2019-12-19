# TheThingsNetwork (TTN) and Murano Integration
The guide you will connect your TTN devices to your Exosite application.

## Table of Contents
   * [Verify TTN has Active Devices](#verify-ttn-has-active-devices)
   * [Configure Murano to Accept TTN Connections](#configure-murano-to-accept-ttn-connections)
   * [Connect TTN to Murano](#connect-ttn-console-to-murano)
   * [Configure Data Structure for ExoSense](#configure-data-structure-for-exosense)
   * [Add Device in ExoSense](#add-device-in-exosense)


## 1. Verify TTN has Active Devices
Setup TTN by:<br>
1.) Adding an Application<br>
<img src="./assets/ttn-add-app.png" alt="Add application in TTN" width="600"><br>
2.) Registering a Device<br>
<img src="./assets/ttn-register-device.png" alt="Register device in TTN" width="600"><br>
3.) Connecting the device to the TTN network per the device manufacturer's instructions<br>
4.) Verify the device is sending data<br>
<img src="./assets/ttn-device-data.png" alt="Device sending data" width="600"><br>

## 2. Configure Murano to Accept TTN Connections
1.) Navigate to Murano and select "*IoT Marketplace*" in the top ribbon<br>
2.) In *IoT Connector Templates*, find and select "*TTN Connector Template*"<br>
<img src="./assets/murano-ttn-element.png" alt="TTN IoT Connector Element" width="200"><br>
3.) Click the "*Create IoT Connector*" button. This adds the Connector to your account.<br>
<img src="./assets/murano-add-ttn-template.png" alt="Create the TTN IoT Connector" width="600"><br>
4.) Click "*Home*" to see your list of solutions and click the TTN Connector you deployed to "Manage IoT Connector"

## 3. Connect TTN to Murano
1.) In the enpoints tab of the product, copy the URL as shown below<br>
![Endpoint page in Murano](../../assets/RadioBridge/EndpointURL.png) <br>
2.) Paste this URL into the API settings of console.radiobridge.com<br>
3.) Append the URL with '*/radiobridge*'<br>
![from console.radiobridge.com](../../assets/RadioBridge/RadioBridgeConsoleAPI.png)

## 4. Configure Data Structure for ExoSense
1.) In the enpoints tab of the produ

## 5. Add Device in ExoSense
[Connect your device to ExoSense.](../../master/ExoSense/README.md)

Once a message has been transmitted from the device, the device will appear in "Unclaimed Devices" in ExoSense

