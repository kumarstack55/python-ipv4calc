# python-ipv4calc

A tool for expressing IPv4 addresses in binary and decimal numbers.

## Requirements

* Python 3.3+
* Poetry 1.1+

## Installation

```powershell
git clone https://github.com/kumarstack55/python-ipv4calc.git
cd python-ipv4calc
poetry install
```

## Usage

```console
PS > poetry run ipv4calc 192.168.1.0/24
address          : 192.168.1.0
network          : 192.168.1.0
netmask          : 255.255.255.0
broadcast        : 192.168.1.255
addressPrefix    : 24
numAddresses     : 256
addressBinary    : 11000000.10101000.00000001.00000000
networkBinary    : 11000000.10101000.00000001.00000000
netmaskBinary    : 11111111.11111111.11111111.00000000
broadcastBinary  : 11000000.10101000.00000001.11111111
addressDecimal   : 3232235776
networkDecimal   : 3232235776
netmaskDecimal   : 4294967040
broadcastDecimal : 3232236031
```

```console
PS > poetry run ipv4calc -h
usage: ipv4calc [-h] ipaddr_prefix

positional arguments:
  ipaddr_prefix  192.168.0.1/24 or 192.168.0.1 or 3232235521.

optional arguments:
  -h, --help     show this help message and exit
```

## License

MIT
