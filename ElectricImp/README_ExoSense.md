# Set up Electric Imp with Exosite

This guide will help you quickly set up your Electric Imp device to Exosite's Murano platform.


## 1. Electric Imp Quickstart

Familiarize yourself with your Electric Imp by setting it up using Electric Imp's [getting started page](https://developer.electricimp.com/gettingstarted).


## 2. Murano Setup
Start of by heading to Exosite's [Murano Platform](https://www.exosite.io/) and login/sign up.

### Create a Product and Get Product ID

Click the **New Solution** button and select **Add a Product**. Give your new product a name and under **Product Starting Point**, select **ExoSense Standard IoT Product Template**.
![](../../assets/ElectricImp/create_solution.png)
![](../../assets/ElectricImp/create_exosense_product.png)

Now select your newly created proudct. Click on the 'ID' tag to copy your unique product ID.
![](../../assets/ElectricImp/get_productid.png)

## 3. Connect Them!

Now that you have both the hardware and the platform set up, all that's left is to connect the two!

### impCentral
If you are not yet familiar with impCentral and want to learn mre, go ahead and follow the getting started page linked above, otherwise continue on with these simple steps.

1.	Get agent code from [here](https://github.com/electricimp/Exosite/blob/master/Example/example.agent.nut) and copy it into the Agent Code in impCentral
2.	Get device code from [here](https://github.com/electricimp/Exosite/blob/master/Example/example.device.nut) and copy it into the Device Code in impCentral
3.	Replace `<my_product_id>` your own Product ID in the Agent code
```
const PRODUCT_ID = "<my_product_id>";
```
4.	Build!

## 4. ExoSense

Now that you have data from your device streaming into Exosite's platform, it is time to set up an ExoSense instance.

1.	Navigate back to Murano, and create another solution, however this time, select **Add an Application**. Enter a domain name and under **Application Starting Point**, select **ExoSense**.
![](../../assets/ElectricImp/create_application.png)\
*Note: If you do not see ExoSense, at the top of the page, head to Exosite's IoT Marketplace and add ExoSense to your business.*
2.	Once created, click the *more* icon in your ExoSense instance, and select **Manage application**.
![](../../assets/ElectricImp/exosense_more.png)
3.	Under the **Services** tab, select the **Product Setup** menu. Once there, check the box next to the product you created and click on **Apply** to save the changes.
![](../../assets/ElectricImp/connect_product.png)
4.	In the top left corner, click on the url icon to go to yoru exosense page.\
![](../../assets/ElectricImp/exosense_webpage.png)
5.	Once on the home page of your exosense instance, go to the **Devices** tab and select **Unclaimed Devices**. Select your device, select a parent group, and click **Assign to group** to claim your device.
![](../../assets/ElectricImp/select_unclaimed_devices.png)
![](../../assets/ElectricImp/claim_device.png)
6.	Head back to the **Devices** tab and click on the *more* icon, from there select **Create Simple Asset**. In the pop-up window just click **Create 1 Asset**
![](../../assets/ElectricImp/device_more.png)
7.	Click on the dashboard icon in the upper right to view the dashboard for your device. Once there, Click the *+* icon, and then the graph icon to add a new panel. From there, select a panel type, a signal, and configure the panel how you'd like it. Click **SAVE** in the bottom right to create your panel. You may continue to add as many panels as you'd like.
![](../../assets/ElectricImp/view_dashboard.png)
![](../../assets/ElectricImp/add_panel.png)
