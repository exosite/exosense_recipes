# Banner Integration
Integrating the Banner DXM100 with ExoSense


## Prerequisites
- ExoSense Account with Banner Product connected and admin access #TODO:Expand on this
- Banner DXM100 connected to sensors

## Configuring the DXM100
### Configure Registers
- Mark registers for cloud read\
    Edit the local registers to be readable by the cloud. This can be done from the "Edit Register" tab or "Modify Multiple Registers" tab.
    
    ![](../../assets/Banner/DXM100_002.PNG)


### Connect to ExoSense

- Find the Product ID
    - Navigate to the "Setup" page in ExoSense
    - Within the Setup page, navigate to "Data Sources" in the navigation ribbon. This will list all products that provide data to ExoSense
    - Locate your Banner product (may be the only product listed)
    - Make note of the ProductID listed (17 digit code)

![](../../assets/Banner/ProductID.png)

- Navigate to "Settings" -> "Cloud Services" in the DXM Configuration application
- In the "Web Server" settings, input your productID appended with '.apps.exosite.io' for the Server name/IP
- Input '/data_in' as the Page

![](../../assets/Banner/DXM100_001.PNG)


## Configuring ExoSense
### Claim the Device
- Once transmitting data, the device will appear in "Unclaimed devices"
- The device can be identified as it's serial number

Read more about devices here: https://exosense.readme.io/docs/devices

### Configure Channels
To configure the channels, upload the device's configuration XML.

Note: Each configuration for a device must have a unique GUID. (The GUID must update if the configuration changes on a single device)

1.) Navigate to "Devices" -> "Software Packages"
2.) Click the "+" button to add a software package
3.) Enter a name for the "Software Package" and select the associated product for the DXM
4.) For the version, ensure this matches the GUID in the configuration file (This is found near the top, inside of the <info> tag)
5.) Select "File" as the type and upload the configuration xml

![](../../assets/Banner/addSoftwarePackage.png)

### Next Steps
- Create an asset from the device. More can be read here: [https://exosense.readme.io/docs/how-to-create-an-asset](https://exosense.readme.io/docs/how-to-create-an-asset) \
- Lastly, create a dashboard to visualize the asset data. More can be read here: [https://exosense.readme.io/docs/how-to-create-a-dashboard](https://exosense.readme.io/docs/how-to-create-a-dashboard)

