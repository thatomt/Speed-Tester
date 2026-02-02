import speedtest

def check_internet_speed():
    speed_test = speedtest.Speedtest()
    
    print("Testing speed...")

    download = speed_test.download() / 1_000_000
    upload = speed_test.upload() / 1_000_000

    speed_test.get_best_server()
    ping = speed_test.results.ping

