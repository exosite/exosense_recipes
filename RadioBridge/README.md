# RadioBridge and Murano Integration
The guide you will connect your RadioBridge devices to your Exosite product.

## Table of Contents
   * [Prerequisites](#prerequisites)
   * [Connecting RadioBridge and Exosite](#connecting-radiobridge-and-exosite)
      * [Add the RadioBridge Product Template to your account](#add-the-radiobridge-product-template-to-your-account)
      * [Add RadioBridge as a new product](#add-radiobridge-as-a-new-product)
   * [Connect RadioBridge Console to Murano](#connect-radiobridge-console-to-murano)
   * [Add Device in ExoSense](#add-device-in-exosense)
   * [Supported RadioBridge Sensors](#supported-radiobridge-sensors)


## 1. Prerequisites
Familiarize yourself with your Radio Bridge hardware by setting it up using Radio Bridge's [getting started page](https://radiobridge.com/documents/Quick%20Start%20Guide%20for%20Radio%20Bridge%20Sensors.pdf) and ensure Radio Bridge has an active connected device.\
![Screenshot from console.radiobridge.com](../../assets/RadioBridge/RadioBridgeDeviceActive.png)

## 2. Connecting RadioBridge and Exosite
### Add the RadioBridge Product Template to your account
1.) Navigate to Murano and select "*IoT Marketplace*" in the top ribbon\
2.) In solutions, find and select "*RadioBridge Product Template*"\
3.) Click the "*Add Product*" button. This adds the template to your account.\
![](../../assets/RadioBridge/RadioBridgeExchangeElement.png)

### Add RadioBridge as a new product
1.) Navigate to '*Solutions*'->'*+ New Solution*'->'*Add a product*'\
2.) Choose a name for your product, could be as simple as '*radiobridge*', and select "*RadioBridge Product Template*" as the starting point.\
![](../../assets/RadioBridge/CreateNewProduct.png)

## 3. Connect RadioBridge Console to Murano
1.) In the enpoints tab of the product, copy the URL as shown below\
![Endpoint page in Murano](../../assets/RadioBridge/EndpointURL.png) \
2.) Paste this URL into the API settings of console.radiobridge.com\
3.) Append the URL with '*/radiobridge*'\
![from console.radiobridge.com](../../assets/RadioBridge/RadioBridgeConsoleAPI.png)

## 4. Add Device in ExoSense

[Connect your device to ExoSense.](../../master/ExoSense/README.md)

Once a message has been transmitted from the device, the device will appear in "Unclaimed Devices" in ExoSense

-----------------------

# Supported RadioBridge Sensors
| TYPE | MODEL |
| ---- | ----- |
| DOOR/WINDOW SENSOR | RBS101-DWS-RCZ1 |
| DOOR/WINDOW SENSOR | RBS101-DWS-RCZ2 |
| DOOR/WINDOW SENSOR | RBS101-DWS-RCZ4 |
| DOOR/WINDOW SENSOR | RBS301-DWS-US |
| DOOR/WINDOW SENSOR | RBS301-DWS-EU |
| DOOR/WINDOW SENSOR | RBS301-DWS-AU |
| DOOR/WINDOW SENSOR | RBS106-DWS-RCZ2 |
| DOOR/WINDOW SENSOR | RBS306-DWS-US |
| ULTRASONIC LEVEL SENSOR | RBS101-US5M-RCZ1 |
| ULTRASONIC LEVEL SENSOR | RBS101-US5M-RCZ2 |
| ULTRASONIC LEVEL SENSOR | RBS101-US5M-RCZ4 |
| ULTRASONIC LEVEL SENSOR | RBS301-US5M-US |
| ULTRASONIC LEVEL SENSOR | RBS301-US5M-EU |
| ULTRASONIC LEVEL SENSOR | RBS301-US5M-AU |
| ULTRASONIC LEVEL SENSOR | RBS106-US5M-RCZ2 |
| ULTRASONIC LEVEL SENSOR | RBS306-US5M-US |
| WIRELESS CONTACT SENSOR| RBS101-CON-RCZ1 |
| WIRELESS CONTACT SENSOR| RBS101-CON-RCZ2 |
| WIRELESS CONTACT SENSOR| RBS101-CON-RCZ4 |
| WIRELESS CONTACT SENSOR| RBS301-CON-US |
| WIRELESS CONTACT SENSOR| RBS301-CON-EU |
| WIRELESS CONTACT SENSOR| RBS301-CON-AU |
| EXTERNAL PROBE TEMPERATURE SENSOR| RBS101-TEMP-EXT-RCZ1 |
| EXTERNAL PROBE TEMPERATURE SENSOR| RBS101-TEMP-EXT-RCZ2 |
| EXTERNAL PROBE TEMPERATURE SENSOR| RBS101-TEMP-EXT-RCZ4 |
| EXTERNAL PROBE TEMPERATURE SENSOR| RBS301-TEMP-EXT-US |
| EXTERNAL PROBE TEMPERATURE SENSOR| RBS301-TEMP-EXT-EU |
| EXTERNAL PROBE TEMPERATURE SENSOR| RBS301-TEMP-EXT-AU |
| EXTERNAL PROBE TEMPERATURE SENSOR| RBS106-TEMP-EXT-RCZ2 |
| EXTERNAL PROBE TEMPERATURE SENSOR| RBS306-TEMP-EXT-US |
| WATER SENSOR | RBS101-WAT-RCZ1 |
| WATER SENSOR | RBS101-WAT-RCZ2 |
| WATER SENSOR | RBS101-WAT-RCZ4 |
| WATER SENSOR | RBS301-WAT-US |
| WATER SENSOR | RBS301-WAT-EU |
| WATER SENSOR | RBS301-WAT-AU |
| WATER SENSOR | RBS106-WAT-RCZ2 |
| WATER SENSOR | RBS306-WAT-US |
| WATER SENSOR | RBS101-WRIM-RCZ1 |
| WATER SENSOR | RBS101-WRIM-RCZ2 |
| WATER SENSOR | RBS101-WRIM-RCZ4 |
| WATER SENSOR | RBS301-WRIM-US |
| WATER SENSOR | RBS301-WRIM-EU |
| WATER SENSOR | RBS301-WRIM-AU |
| WATER SENSOR | RBS306-WRIM-US |
| ACCELERATION SENSOR | RBS101-ABM-RCZ1 |
| ACCELERATION SENSOR | RBS101-ABM-RCZ2 |
| ACCELERATION SENSOR | RBS101-ABM-RCZ4 |
| ACCELERATION SENSOR | RBS301-ABM-US |
| ACCELERATION SENSOR | RBS301-ABM-EU |
| ACCELERATION SENSOR | RBS301-ABM-AU |
| ACCELERATION SENSOR | RBS306-ABM-US |
| VIBRATION SENSOR | RBS101-VS-RCZ1 |
| VIBRATION SENSOR | RBS101-VS-RCZ2 |
| VIBRATION SENSOR | RBS101-VS-RCZ4 |
| VIBRATION SENSOR | RBS301-VS-US |
| VIBRATION SENSOR | RBS301-VS-EU |
| VIBRATION SENSOR | RBS301-VS-AU |
| VIBRATION SENSOR | RBS106-VS-RCZ2 |
| VIBRATION SENSOR | RBS306-VS-US |