# TheThingsNetwork (TTN) and Murano Integration
The guide you will connect your TTN devices to your Exosite application.

## Table of Contents
   * [Verify TTN has Active Devices](#verify-ttn-has-active-devices)
   * [Configure Murano to Accept TTN Connections](#configure-murano-to-accept-ttn-connections)
   * [Connect TTN to Murano](#connect-ttn-console-to-murano)
   * [Configure Data Structure for ExoSense](#configure-data-structure-for-exosense)
   * [Add Device in ExoSense](#add-device-in-exosense)


## 1. Verify TTN has Active Devices
Familiarize yourself with your TTN-connected hardware by setting it up using Radio Bridge's [getting started page](https://radiobridge.com/documents/Quick%20Start%20Guide%20for%20Radio%20Bridge%20Sensors.pdf) and ensure Radio Bridge has an active connected device.<br>
![Screenshot from console.radiobridge.com](../../assets/RadioBridge/RadioBridgeDeviceActive.png)

## 2. Configure Murano to Accept TTN Connections
1.) Navigate to Murano and select "*IoT Marketplace*" in the top ribbon<br>
2.) In *IoT Connectors*, find and select "*RadioBridge Product Template*"<br>
3.) Click the "*Add Product*" button. This adds the template to your account.<br>
![](../../assets/RadioBridge/RadioBridgeExchangeElement.png)


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

