from utils.serial_reader import SerialDataAdapter
from utils import db
from models import SerialData
import time
import sys
import plotly
from plotly.graph_objs import Scatter, Layout

class Serial2Sqlite(object):

    def __init__(self, sample_rate, **kwargs):
        self.sample_rate = sample_rate
        self.adapter = SerialDataAdapter(port=kwargs['port'], baudrate=kwargs['baudrate'])


    def run(self):
        while True:
            data = SerialData(value=self.adapter.read_int())
            db.session.add(data)
            db.session.commit()
            print("Value added")
            time.sleep(sample_rate)

    def generate_plot(self):
        values = []
        dates = []
        for value in db.session.query(SerialData.value).all():
            values.append(value[0])
        for added in db.session.query(SerialData.added).all():
            dates.append(added[0])
        plotly.offline.plot({
            "data": [
                Scatter(x=dates, y=values)
            ],
            "layout": Layout(title="Serial data")
        })


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} port baudrate sample_rate mode, mode is run or plot".format(sys.argv[0]))
        sys.exit(1)
    port = sys.argv[1]
    baudrate = sys.argv[2]
    sample_rate = sys.argv[3]
    mode = sys.argv[4]
    s2s = Serial2Sqlite(sample_rate, port=port, baudrate=baudrate)
    if mode == "run":
        s2s.run()
    else:
        s2s.generate_plot()