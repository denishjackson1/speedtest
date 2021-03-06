from speedtest import Speedtest

st = Speedtest()

st.get_best_server()
print(f"Your ping is: {st.results.ping} ms")
print(f"Your download speed: {round(st.download() / 1000 / 1000, 1)} Mbps")
print(f"Your upload speed: {round(st.upload() / 1000 / 1000, 1)} Mbps")
#....