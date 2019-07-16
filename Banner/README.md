#Banner Integration#
Integrating the Banner DXM100 with ExoSense


##Prerequisites##
- ExoSense Account with Banner Product connected and admin access #TODO:Expand on this
- Banner DXM100 connected to sensors

##Configuring the DXM100##
###Configure Registers###
- Mark registers for cloud read\
    Edit the local registers to be readable by the cloud. This can be done from the "Edit Register" tab or "Modify Multiple Registers" tab.
    
    ![](../../assets/Banner/DXM100_002.png)


###Connect to ExoSense###

- Find the Product ID
    - Navigate to the "Setup" page in ExoSense
    - Within the Setup page, navigate to "Data Sources" in the navigation ribbon. This will list all products that provide data to ExoSense
    - Locate your Banner product (may be the only product listed)
    - Make note of the ProductID listed (17 digit code)
- Navigate to "Settings" -> "Cloud Services" in the DXM Configuration application
- In the "Web Server" settings, input your productID appended with '.apps.exosite.io' for the Server name/IP
- Input '/data_in' as the Page

![](../../assets/Banner/DXM100_001.png)


##Configuring ExoSense##
- View in unclaimed devices
- Configure Channels
- DXM100 as protocol
- "register":"regXY" as app-specific-config





