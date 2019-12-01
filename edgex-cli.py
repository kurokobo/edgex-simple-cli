#!/usr/bin/python

import fire
import requests
import json
from tabulate import tabulate


class Addressable(object):
    def list(self, host, port=48081, raw=False):
        url = "http://%s:%s/api/v1/addressable" % (host, port)
        list_by_url(url, raw)

    def delete(self, host, id, port=48081):
        url = "http://%s:%s/api/v1/addressable/id/%s" % (host, port, id)
        delete_by_url(url)


class ValueDescriptor(object):
    def list(self, host, port=48080, raw=False):
        url = "http://%s:%s/api/v1/valuedescriptor" % (host, port)
        list_by_url(url, raw)

    def delete(self, host, id, port=48080):
        url = "http://%s:%s/api/v1/valuedescriptor/id/%s" % (host, port, id)
        delete_by_url(url)


class DeviceProfile(object):
    def list(self, host, port=48081, raw=False):
        url = "http://%s:%s/api/v1/deviceprofile" % (host, port)
        list_by_url(url, raw)

    def delete(self, host, id, port=48081):
        url = "http://%s:%s/api/v1/deviceprofile/id/%s" % (host, port, id)
        delete_by_url(url)


class DeviceService(object):
    def list(self, host, port=48081, raw=False):
        url = "http://%s:%s/api/v1/deviceservice" % (host, port)
        list_by_url(url, raw)

    def delete(self, host, id, port=48081):
        url = "http://%s:%s/api/v1/deviceservice/id/%s" % (host, port, id)
        delete_by_url(url)


class Device(object):
    def list(self, host, port=48081, raw=False):
        url = "http://%s:%s/api/v1/device" % (host, port)
        list_by_url(url, raw)

    def delete(self, host, id, port=48081):
        url = "http://%s:%s/api/v1/device/id/%s" % (host, port, id)
        delete_by_url(url)


class EdgeX(object):
    """
    A Simple CLI Tool for EdgeX Founrdy
    """

    def __init__(self):
        self.addressable = Addressable()
        self.valuedescriptor = ValueDescriptor()
        self.deviceprofile = DeviceProfile()
        self.deviceservice = DeviceService()
        self.device = Device()


def list_by_url(url, raw=False):
    response = requests.get(url)
    data = response.json()

    list = []
    if raw is False:
        for item in data:
            list.append([item["id"], item["name"]])
        print(tabulate(list, ["ID", "Name"], tablefmt="simple"))
    else:
        print(json.dumps(data, indent=2))


def delete_by_url(url):
    response = requests.delete(url)
    print("[%s] %s" % (response.status_code, response.text))


if __name__ == "__main__":
    fire.Fire(EdgeX)
