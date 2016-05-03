from utils.dummy_adapter import DummyAdapter
from utils import db
from models import SerialData
import time
import sys
import plotly
from plotly.graph_objs import Scatter, Layout

class Serial2Sqlite(object):

    def __init__(self):
        self.adapter = DummyAdapter()


    def run(self):
        while True:
            data = SerialData(value=self.adapter.read_int())
            db.session.add(data)
            db.session.commit()
            print("Value added")
            time.sleep(5)

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
    mode = sys.argv[1]
    s2s = Serial2Sqlite()
    if mode == "run":
        s2s.run()
    else:
        s2s.generate_plot()