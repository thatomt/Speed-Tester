import speedtest

def check_internet_speed():
    speed_test = speedtest.Speedtest()
    
    print("Testing speed...")

    download = speed_test.download() / 1_000_000
    upload = speed_test.upload() / 1_000_000

    speed_test.get_best_server()
    ping = speed_test.results.ping
    return {
        "download": round(download, 2),
        "upload": round(upload, 2),
        "ping": round(ping, 2)
    }

speed = check_internet_speed()

print(f"Download: {speed['download']} Mbps")
print(f"Upload: {speed['upload']} Mbps")
print(f"Ping: {speed['ping']} ms" )
