# Setting Up a VPN with a linux based gateway for as little as $5/month


Some workflows require a VPN connection to a gateway on another network. Having a VPN allows a user to communicate with that gateway as if it was on the same network. This post will demonstrate setting up OpenVPN on a Moxa gateway.

Note: The cost of the VPN depends on the OpenVPN server used. The OpenVPN server used in this example allows two accounts to connect to the server (the user and the gateway). If more concurrent accounts are desired, an OpenVPN license will need to be aquired.

## What will be used
- Linux based gateway (Moxa) 
- DigitalOcean (OpenVPN server droplet)
- OpenVPN Client Software

## Outline
- Create OpenVPN server on https://www.digitalocean.com/
- Set up OpenVPN Server 
- Install and Connect OpenVPN on the Gateway
- Install and Connect OpenVPN from the user's machine
- Connect to the Gateway from the user's machine via VPN

### Creating an OpenVPN server
We will start by making an OpenVPN server for both the gateway and the user's machine to communicate through. We will use digital ocean due to it's simplicity and speed to setup.

1.) Login to digitalocean.com

2.) Create an OpenVPN droplet\
![Alt Text](https://github.com/exosite/exosense_recipes/blob/assets/OpenVPN/CreateOpenVPNDroplet.gif?raw=true)

3.) Using the username 'root' and the password e-mailed to you, login to the console
![Alt Text](https://github.com/exosite/exosense_recipes/blob/assets/OpenVPN/AccessConsole.png?raw=true)

4.) After typing ‘yes’ and hitting enter, the following questions defaults should be sufficient (hit ‘Enter’ to select default)

5.) run `passwd openvpn` to set a password for the user 'openvpn'

### Setup the OpenVPN server

1.) Login to https://\<ipAddress\>/admin (using the openvpn username/password that was just updated)
![Alt Text](https://github.com/exosite/exosense_recipes/blob/assets/OpenVPN/admin_login.png?raw=true)

2.) Navigate to "USER MANAGEMENT" &rightarrow; "USER PERMISSIONS"
![Alt Text](https://github.com/exosite/exosense_recipes/blob/assets/OpenVPN/UserPermissions.png?raw=true)

3.) Create two users (one for the gateway, one for yourself), be sure to add a password in “more settings”

4.) For the gateway, select "Allow Auto-Login"

### Connecting the Gateway

Moxa includes an OpenVPN client by default. It can also be installed via `sudo apt-get update && sudo apt-get install openvpn`

1.) Login as the gateway user to https://\<ipaddr\>/

2.) Download connection profile (auto-login)

3.) SCP or use FileZilla to copy the file to the Moxa gateway

4.) Run OpenVPN using the config file `sudo openvpn --config <path to config file>`

4.b) ##TODO: Make it a service?

5.) Under "STATUS" &rightarrow; "Current Users" you should see the gateway user connected
![Alt Text](https://github.com/exosite/exosense_recipes/blob/assets/OpenVPN/CurrentUsersMoxa.png?raw=true)

## Connecting the user to OpenVPN
1.) Log in to https://\<ipaddr\>/ under the user's account that was created earlier

2.) Download the correct OpenVPN Client App

3.) Download the connection profile

4.) Follow instructions specific to the client app to connect to the OpenVPN server

5.) Again, when signed into the admin page, you can see the user under the "Current Users" page

## Connect to the Gateway
Connect to the gateway using the "VPN Address" found in the "Current Users" tab, in the example above, this would be `172.27.232.23`.

This can be tested by using `ping 172.27.232.23` from a console
