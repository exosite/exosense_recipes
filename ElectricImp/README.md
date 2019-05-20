# Set up Electric Imp with Exosite

This guide will help you quickly set up your Electric Imp device to Exosite's Murano platform.


## 1. Electric Imp Quickstart

Familiarize yourself with your Electric Imp by setting it up using Electric Imp's [getting started page]([https://developer.electricimp.com/gettingstarted].(https://developer.electricimp.com/gettingstarted))


## 2. Murano Setup
Start of by heading to Exosite's [Murano Platform]([https://www.exosite.io/](https://www.exosite.io/)) and login/sign  up.

### Create a Product and Get Product ID

Click the **New Solution** button and select **Add a Product**. Give your new product a name and under **Product Starting Point**, select **Start from Scratch**.

Now select your newly created proudct. In the upper right, click on the 'ID' tag to copy your unique product ID.

### Set Up Resources
In this step, you will be creating two resources for your Electric Imp device to send data to.

Navigate to **Resources** in product menu. 
(picture)
Click **New Resource** to create a new resource.
(picture)
Set the Alias of your first resource to '**config_io**', make it of **String** format, and check the box that allows you to modify from the cloud, leaving **Possible values** and **Units** blank.
(Picture)
Add another resource called '**data_in**' of **String** format, and leave the rest blank.

## 3. Connect Them!

Now that you have both the hardware and the platform set up, all that's left is to connect the two!

### impCentral
If you are not yet familiar with impCentral and want to learn mre, go ahead and follow the getting started page linked above, otherwise continue on with these simple steps.

1.	Get agent code from [here]([https://github.com/exosite/ElectricImp_Integration/blob/master/Exosite.agent.lib.nut](https://github.com/exosite/ElectricImp_Integration/blob/master/Exosite.agent.lib.nut)) and copy it into the Agent Code in impCentral
2.	Get device code from [here]([https://github.com/exosite/ElectricImp_Integration/blob/master/Example/example.device.nut](https://github.com/exosite/ElectricImp_Integration/blob/master/Example/example.device.nut)) and copy it into the Device Code in impCentral
3.	Build and you're done!