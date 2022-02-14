from ipaddress import IPv4Interface
from typing import Union
import argparse


__version__ = '0.1.1'


class KeyValuePrinter(object):
    def __init__(self):
        self._data = []
        self._key_len_max = 0

    def add(self, key: str, value: str):
        self._data.append((key, value,))
        self._key_len_max = max(self._key_len_max, len(key))

    def print(self):
        format_string = '{0:%ds} : {1}' % (self._key_len_max)
        for key, value in self._data:
            print(format_string.format(key, value))


def _to_dec(network):
    value = 0
    for index, octet in enumerate(network.packed):
        value *= 2 ** 8
        value += octet
    return value


def _to_bin(network):
    packed = network.packed
    return '.'.join(map(lambda o: '{:08b}'.format(o), map(int, packed)))


def get_ipv4_address(address: str) -> Union[int, str]:
    try:
        return int(address)
    except ValueError:
        return address


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
            'ipaddr_prefix', nargs=1,
            help='192.168.0.1/24 or 192.168.0.1 or 3232235521.')
    args = parser.parse_args()

    interface = IPv4Interface(get_ipv4_address(args.ipaddr_prefix[0]))

    address = interface.ip
    network = interface.network.network_address
    netmask = interface.network.netmask
    broadcast = interface.network.broadcast_address

    p = KeyValuePrinter()
    p.add('address', address)
    p.add('network', network)
    p.add('netmask', netmask)
    p.add('broadcast', broadcast)
    p.add('addressPrefix', interface.network.prefixlen)
    p.add('numAddresses', interface.network.num_addresses)
    p.add('addressBinary', _to_bin(address))
    p.add('networkBinary', _to_bin(network))
    p.add('netmaskBinary', _to_bin(netmask))
    p.add('broadcastBinary', _to_bin(broadcast))
    p.add('addressDecimal', _to_dec(address))
    p.add('networkDecimal', _to_dec(network))
    p.add('netmaskDecimal', _to_dec(netmask))
    p.add('broadcastDecimal', _to_dec(broadcast))
    p.print()


if __name__ == '__main__':
    main()
