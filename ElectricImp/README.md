# Set up Electric Imp with Exosite

This guide will help you quickly set up your Electric Imp device to Exosite's Murano platform.


## 1. Prerequisites

Familiarize yourself with your Electric Imp by setting it up using Electric Imp's [getting started page](https://developer.electricimp.com/gettingstarted).

## 2. Murano Setup
Start of by heading to Exosite's [Murano Platform](https://www.exosite.io/) and login/sign up.

### Create a Product and Get Product ID

Click the **New Solution** button and select **Add a Product**. Give your new product a name and under **Product Starting Point**, select **ExoSense Standard IoT Product Template**.
![](../../assets/ElectricImp/create_solution.png)
![](../../assets/ElectricImp/create_exosense_product.png)

Now select your newly created product. Click on the 'ID' tag to copy your unique product ID.
![](../../assets/ElectricImp/get_productid.png)

## 3. Connect Them!

Now that you have both the hardware and the platform set up, all that's left is to connect the two!

### impCentral
If you are not yet familiar with impCentral and want to learn more, follow the getting started page linked above. Otherwise continue on with these simple steps:

1.	Get agent code from [here](https://github.com/electricimp/Exosite/blob/master/Example/example.agent.nut) and copy it into the Agent Code in impCentral
2.	Get device code from [here](https://github.com/electricimp/Exosite/blob/master/Example/example.device.nut) and copy it into the Device Code in impCentral
3.	Replace `<my_product_id>` your own Product ID in the Agent code
```
const PRODUCT_ID = "<my_product_id>";
```
4.	Build!

## 4. ExoSense

[Connect your device to ExoSense](../../master/ExoSense/README.md)

### Channel Configuration
To configure the channels in ExoSense to read correctly from the device. The key that the device uses for the data needs to be defined.

To achieve this, the user must have a "Custom" Protocol, with "ElectricImp" as the Application, and `{"key":<device's corresponding key>}`

For example, if the device calls
```
local conditions = {};
conditions.temp <- reading.temperature;
agent.send("reading.sent", conditions);
```

A corresponding channel configuration could look like the following:
![](../../assets/ChannelConfigurationExample.png)
