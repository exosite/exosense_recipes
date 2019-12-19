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
<img src="./assets/murano-ttn-element.png" alt="TTN IoT Connector Element" width="100"><br>
3.) Click the "*Create IoT Connector*" button. This adds the Connector to your account.<br>
<img src="./assets/murano-add-ttn-template.png" alt="Create the TTN IoT Connector" width="400"><br>
4.) Click "*Home*" to see your list of solutions and click the TTN Connector you deployed to "Manage IoT Connector"
<img src="./assets/murano-ttn-deployed.png" alt="Manage TTN IoT Connector" width="400"><br>

## 3. Connect TTN to Murano
1.) In Murano, click the "WWW" icon in the upper left to spawn a new tab with the external URL of the connector - copy the URL from the browser address bar<br>
<img src="./assets/murano-ttn-url.png" alt="Copy TTN C2C URL" width="400"><br>
2.) In TTN, go to the "Integrations" tab and click "add integration" and select the HTTP integration<br>
<img src="./assets/ttn-add-integration.png" alt="Add TTN HTTP integration" width="400"><br>
3.) Paste the URL from step one into the URL field in the HTTP integration (URL of the endpoint), and add "c2c/callback" at the end of the URL to specify the specific endpoint that the HTTP integration should POST to<br>
<img src="./assets/ttn-integration-settings.png" alt="Configure TTN HTTP integration" width="400"><br>
4.) Set a unique identifier (any number) in the Process ID field, select the "default key" for the Access Kay, and click "Add Integration" to start flowing data!<br>
<img src="./assets/ttn-integration-running.png" alt="TTN HTTP integration running" width="400"><br>
5.) Verify the connection is working correctly by either generating real device events, or, on a TTN Device page, add some data to the "Simulate Uplink" field and click "Send."  In Murano, go to the Logs subpage of your TTN connector and every time TTN sends data, you should see a new log message generated.
<img src="./assets/murano-callback-logs.png" alt="Murano logs showing TTN data" width="400"><br>

## 4. Configure Data Structure for ExoSense
1.) In the enpoints tab of the produ

## 5. Add Device in ExoSense
[Connect your device to ExoSense.](../../master/ExoSense/README.md)

Once a message has been transmitted from the device, the device will appear in "Unclaimed Devices" in ExoSense

