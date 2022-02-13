# python-ipv4calc

## Requirements

* Poetry 1.1+

## Installation

```powershell
gh repo clone kumarstack55/python-ipv4calc
cd python-ipv4calc
poetry install
```

## Usage

```console
PS > poetry run ipv4calc 192.168.0.1/24
address         : 192.168.0.1
network         : 192.168.0.0
netmask         : 255.255.255.0
broadcast       : 192.168.0.255
addressPrefix   : 24
numAddresses    : 256
addressBinary   : 11000000.10101000.00000000.00000001
networkBinary   : 11000000.10101000.00000000.00000000
netmaskBinary   : 11111111.11111111.11111111.00000000
broadcastBinary : 11000000.10101000.00000000.11111111
```

## License

MIT
