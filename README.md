# EdgeX Foundry Simple CLI Tool

A Simple CLI Tool for EdgeX Founrdy.

Written in Python using [Python Fire](https://github.com/google/python-fire) library.


## Functiona

Currently only LIST and DELETE functions work properly.

* Addressable
    * LIST
    * DELETE
* Value Descriptor
    * LIST
    * DELETE
* Device Profile
    * LIST
    * DELETE
* Device Service
    * LIST
    * DELETE
* Device
    * LIST
    * DELETE

## Usage

```sh
SYNOPSIS
    edgex-cli.py --host=HOST GROUP SUBCOMMAND [<ID>]

HOST
    Specify hostname or IP address where the core services work.

GROUP
    GROUP is one of the following:

     addressable
       List or Delete "Addressable" object(s).
    
     device
       List or Delete "Device" object(s).

     deviceprofile
       List or Delete "Device Profile" object(s).

     deviceservice
       List or Delete "Device Service" object(s).

     valuedescriptor
       List or Delete "Value Descriptor" object(s).

SUBCOMMAND
    SUBCOMMAND is one of the following:

     list
       Simply lists all of specified object(s).
       We can get raw JSON data instead of "ID" and "Name" if we use this with "--raw" switch.
    
     delete
       Delete specified object with followed ID.
```

## Sample

```sh
$ python3 edgex-cli.py --host 192.168.0.220 addressable list
['2b61edd7-16c7-43b5-aaf9-72ed79363def', 'device-virtual']
['4e754706-207f-453e-857c-d4b9e8b4627c', 'camera control']
['0c937575-01c6-4911-865b-ec4aaf02caf5', 'camera1 address']
```

```sh
$ python3 edgex-cli.py --host 192.168.0.220 addressable delete 0c937575-01c6-4911-865b-ec4aaf02caf5
[200] true
```

