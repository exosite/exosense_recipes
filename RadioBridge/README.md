# RadioBridge and Murano Integration
The guide you will connect your RadioBridge devices to your Exosite product.

## Table of Contents
   * [Recommended Hardware](#recommended-hardware)
   * [Prerequisites](#prerequisites)
   * [Connecting RadioBridge and Exosite](#connecting-radiobridge-and-exosite)
      * [Add the RadioBridge Product Template to your account](#add-the-radiobridge-product-template-to-your-account)
      * [Add RadioBridge as a new product](#add-radiobridge-as-a-new-product)
      * [Connect RadioBridge Console to Murano](#connect-radiobridge-console-to-murano)
   * [Adding New Devices](#adding-new-devices)
      * [Create a new device](#create-a-new-device)
      * [Config IO needed????](#config-io-needed)


## Recommended Hardware
RadioBridge Water Sensor\
MultiTech MultiConnect Conduit

## Prerequisites
RadioBridge has an active connected device
![Screenshot from console.radiobridge.com](../../assets/RadioBridge/RadioBridgeDeviceActive.png)

## Connecting RadioBridge and Exosite
### Add the RadioBridge Product Template to your account
Navigate to Murano and select "IoT Marketplace" in the top ribbon\
In solutions, find and select "RadioBridge Product Template"\
Click the "Add Product" button. This adds the template to your account.\
![](../../assets/RadioBridge/RadioBridgeExchangeElement.png)


### Add RadioBridge as a new product
Navigate to Solutions->'+ New Solution'->'Add a product'\
![](../../assets/RadioBridge/CreateNewProduct.png)
Choose a name for your product, could be as simple as 'radiobridge', and select "RadioBridge Product Template" as the starting point.

### Connect RadioBridge Console to Murano
In the enpoints tab of the product, copy the URL as shown below\
![Endpoint page in Murano](../../assets/RadioBridge/EndpointURL.png)
Paste this URL into the API settings of console.radiobridge.com\
Append the URL with '/radiobridge'\
![from console.radiobridge.com](../../assets/RadioBridge/RadioBridgeConsoleAPI.png)
**Header Authorization code???**

## Adding New Devices
### Create a new device
Navigate to the devices tab in your Murano product\
Select "+ New Device" -> "Add one device"\
Input the DeviceID from RadioBridge into the Identity field\
Select "Add"\
![from console.radiobridge.com](../../assets/RadioBridge/AddDeviceDialog.png)


**I hope we can get rid of this step...**
From a terminal, execute the following curl command to provision the device using your product\_id and device\_id
curl -i 'https://<product id>.m2.exosite.io/provision/activate' -H 'Content-Type: application/x-www-form-urlencoded; charset=utf-8' -d 'id=<device id>'

### Config IO needed????
