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

### Configure Channels
- Locate and select the Device in the "Devices" Tab
- Select "Channels" in the Navigation Ribbon

![](../../assets/Banner/CreateChannel.png)
- Configure the Channel to use a "Custom" Protocol
- For the Application, enter "DXM100"
- In the app_specific_config (replacing "<>" with the register number to read) enter:
```
{
"register":"reg<>"
}
```

![](../../assets/Banner/ChannelConfiguration.png)
