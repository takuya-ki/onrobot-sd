# onrobot-sd

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![repo size](https://img.shields.io/github/repo-size/takuya-ki/onrobot-sd)

Controller for OnRobot screw driver.

## Requirements

- Python 3.10.12

## Installation

```bash
git clone git@github.com:takuya-ki/onrobot-sd.git && cd onrobot-sd
```

## Usage

1. Connect the cable between compute box and tool changer
2. Connect an ethernet cable between compute box and your computer
3. Execute a demo script as below  
```bash
python src/demo.py --id 0 --bit_ext 100 --ip 192.168.1.1
```

<img src="img/2x.gif" height="200">  

## Author / Contributor

[Takuya Kiyokawa](https://takuya-ki.github.io/)

## License

This software is released under the MIT License, see [LICENSE](./LICENSE).
