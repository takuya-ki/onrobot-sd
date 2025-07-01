#!/usr/bin/env python3

import argparse

from onrobot import SD


def run_demo():
    """Runs shank moving demonstration once."""
    sd = SD(bit_extender, ip_address)

    if sd.isconn(sd_id):  # connected
        while True:
            if not sd.isBusy(sd_id):  # not busy
                print("Shank pose:", str(sd.get_shank_pos(sd_id)) + "mm")
                break
        
        while True:
            if not sd.isBusy(sd_id):  # not busy
                sd.move_shank(t_index=sd_id, shank_pos=10+bit_extender, f_wait=True)
                break

        while True:
            if not sd.isBusy(sd_id):  # not busy
                sd.move_shank(t_index=sd_id, shank_pos=30+bit_extender, f_wait=True)
                break


def get_options():
    """Returns user-specific options."""
    parser = argparse.ArgumentParser(description='Set options.')
    parser.add_argument(
        '--id', dest='id', type=int, default=0,
        help='set screw driver id')
    parser.add_argument(
        '--bit_ext', dest='bit_ext', type=int,
        default=100, choices=[0, 50, 100],
        help='set bit extender type, 0, 50, or 100')
    parser.add_argument(
        '--ip', dest='ip', type=str, default="192.168.1.1",
        help='set ip address')
    return parser.parse_args()


if __name__ == '__main__':
    args = get_options()
    sd_id = args.id
    bit_extender = args.bit_ext
    ip_address = args.ip
    run_demo()
