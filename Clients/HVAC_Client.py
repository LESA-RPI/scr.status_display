from Client_util import *

if __name__ == "__main__":

    while True:

        temps = hvac_control.get_temp()
        eps = hvac_control.get_ep()
        humidity = hvac_control.get_rh()
        co2 = hvac_control.get_co2()

        temp_avg = min(24, max(18, sum(temps)/len(temps)))
        co2_avg = min(1000, max(400, int(co2)))

        temps = [("%.1f"%x)+"C" for x in temps]
        eps =   [("%.1f"%x)+"%" for x in eps]
        humidity = str(int(humidity)) + "%"
        co2 = str(int(co2)) + "p"

        post_request('Status_HVAC', {"temp": temps,
                                     "ep": eps,
                                     "humidity": humidity,
                                     "co2": co2})

        post_request('Status_TempChart', {"temp": temp_avg,
                                          "co2": co2_avg})
        time.sleep(60)