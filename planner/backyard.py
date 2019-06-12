# -*- coding: utf-8 -*-
import time

from udacidrone.connection import MavlinkConnection, WebSocketConnection  # noqa: F401

from plants.backyard_flyer import BackyardFlyer


if __name__ == "__main__":
    conn = MavlinkConnection('tcp:127.0.0.1:5760', threaded=False, PX4=False)
    #conn = WebSocketConnection('ws://127.0.0.1:5760')
    drone = BackyardFlyer(conn)
    time.sleep(2)
    drone.start()
