from ipaddress import IPv4Interface
import argparse


__version__ = '0.1.0'


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


def _to_bin(network):
    packed = network.packed
    return '.'.join(map(lambda o: '{:08b}'.format(o), map(int, packed)))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('ipaddr_prefix', nargs=1, help='x.x.x.x/xx')
    args = parser.parse_args()
    interface = IPv4Interface(args.ipaddr_prefix[0])

    p = KeyValuePrinter()
    p.add('address', interface.ip)
    p.add('network', interface.network.network_address)
    p.add('netmask', interface.network.netmask)
    p.add('broadcast', interface.network.broadcast_address)
    p.add('addressPrefix', interface.network.prefixlen)
    p.add('numAddresses', interface.network.num_addresses)
    p.add('addressBinary', _to_bin(interface.ip))
    p.add('networkBinary', _to_bin(interface.network.network_address))
    p.add('netmaskBinary', _to_bin(interface.network.netmask))
    p.add('broadcastBinary', _to_bin(interface.network.broadcast_address))
    p.print()


if __name__ == '__main__':
    main()
