# How I created the light on-off device control on the Micro820 Allen Bradley PLC

## Install CCW
Install [Connected Components Workbench Software](https://www.rockwellautomation.com/global/capabilities/industrial-automation-control/overview.page?docid=6b8425507e679dd6b2587d385b7b26e1&pagetitle=Design-and-Configuration-Software)

## Create a new project

### Configure IP Address
If we don't configure an IP Address, the PLC will get a 'random' IP adress each power cycle.

If you don't set a static IP, it's possible to temporarily get the IP address using the following:

```
$ ifconfig
```
example return:

```
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 169.254.169.88  netmask 255.255.0.0  broadcast 169.254.255.255
        inet6 fe80::cdcf:d572:e2f8:95d8  prefixlen 64  scopeid 0x20<link>
        ether b8:27:eb:67:31:07  txqueuelen 1000  (Ethernet)
        RX packets 3872  bytes 837566 (817.9 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 4769  bytes 733112 (715.9 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0       
```

Note the **broadcast 169.254.255.255**

Use this to ping and find the PLC with the following:

```
$ ping -b 169.254.255.255
```

### Map Modbus Register
This puts the modbus register as a global variable to use in the ladder program

Do this by selecting the top level leaf in the Project Organizer (Micro8**).

In the options, under controller, select "Modbus Mapping".

Then add a new mapping to the global variable.


### Create simple program
In the simple program we can just have a coil that is reading the global variable of the modbus register we mapped.

Then we have that directly attached to Digital Output 00.

  Direct Contact <-> Direct Coil
  
  Global Var     <-> \_IO\_EM\_DO\_00
  
       ---| |----------O---

## Circuit
The Allen Bradley Micro820 has Relay Digital outputs. What this means, is that power needs to be supplied to each output being used. For an LED demo, I used the EXTECH powersupply to provide this power.

The relay is used by providing power to the associated COM\<N\> pin. (Common pin on a single pole/double throw relay switch). The NU is the "Normally unopened" switch position (I think). Lastly, the O-\<N\> is the output pin that turns on and off.

**For the demo, power is supplied to the COM0 pin in the PLC, the O-00 pin is sent to a circuit with two LEDs and a resistor, with ground returning to the power supply.**


## config_io
Note in this config_io:

- boolean_int evaluation mode
- Modbus TCP
- port 502 is the default modbus port
- Register count is 1 for boolean, 8 for integer

```json
{
	"channels": {
		"000": {
			"display_name": "Test",
			"description": "Test",
			"control_properties": {
				"range": {
					"max": null,
					"min": null
				},
				"enum": []
			},
			"channel_name": "000",
			"properties": {
				"control": true,
				"data_unit": null,
				"data_type": "NUMBER",
				"min": null,
				"max": null,
				"device_diagnostic": false,
				"precision": null
			},
			"protocol_config": {
				"input_raw": {},
				"report_on_change": false,
				"report_rate": 5000,
				"application": "Modbus_TCP",
				"app_specific_config": {
					"byte_endianness": "little",
					"register_count": 1,
					"register_endianness": "little",
					"bitmask": "0xFFFF",
					"register_number": "1",
					"register_range": "HOLDING_COIL",
					"ip_address": "169.254.38.237",
					"port": "502",
					"evaluation_mode": "bitmask_int"
				},
				"sample_rate": 5000,
				"timeout": null,
				"interface": "eth0",
				"down_sample": "ACT"
			}
		}
	},
	"last_edited": "1573156472166"
}
