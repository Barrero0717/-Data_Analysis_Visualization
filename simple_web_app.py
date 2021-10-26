import justpy as jp
import pandas
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt

chart_def = """
{

    chart: {
        type: 'lollipop'
    },

    accessibility: {
        point: {
            valueDescriptionFormat: ''
        }
    },

    legend: {
        enabled: false
    },

    title: {
        text: 'Top 10 Countries by Population'
    },

    tooltip: {
        shared: true
    },

    xAxis: {
        title: {
            text: 'Rating'
        },
        type: 'category'
    },

    yAxis: {
        title: {
            text: 'Count'
        }
    },

    series: [{
        name: 'Count',
        data: [{
            name: 'China',
            low: 1427647786
        }, {
            name: 'India',
            low: 1352642280
        }, {
            name: 'United States',
            low: 327096265
        }, {
            name: 'Indonesia',
            low: 267670543
        }, {
            name: 'Pakistan',
            low: 212228286
        }, {
            name: 'Brazil',
            low: 209469323
        }, {
            name: 'Nigeria',
            low: 195874683
        }, {
            name: 'Bangladesh',
            low: 161376708
        }, {
            name: 'Russia',
            low: 145734038
        }, {
            name: 'Mexico',
            low: 126190788
        }]
    }]
}
"""

description = """
<div class="q-pa-md q-gutter-sm">
    <q-btn label="Description of Maturity Ratings" color="primary" name="description_button" />
    <q-dialog name="description_dialog" persistent>
      <q-card>
        <q-card-section>
          <div class="text-h6">Description of Maturity Ratings</div>
        </q-card-section>

        <q-card-section>
          <p>You can find the meaning of each Rating in this URL:</p>
          <a href="https://help.netflix.com/en/node/2064/us" target="_blank">Netflix Help Center</a>       
        </q-card-section>

        <q-card-actions align="right">
          <q-btn flat label="OK" color="primary" v-close-popup />
        </q-card-actions>
      </q-card>
    </q-dialog>
</div>
"""

data = pandas.read_csv("netflix_titles.csv", parse_dates=["date_added"])
Rat = data["rating"].value_counts()

def open_dialog(self, msg):
    self.dialog.value = True

def app():
    wp = jp.QuasarPage(highcharts_theme='gray', title='Netflix Analysis', dark=True)
    wp.head_html = '<link href="https://fonts.googleapis.com/css2?family=Noto+Sans:wght@700&display=swap" rel="stylesheet">' 
    wp.css = 'body { font-family: Noto Sans, sans-serif; }' 
    
    d1 = jp.Div(classes='q-pa-md row justify-center', a=wp)
    t1 = jp.QDiv(classes='relative-position flex flex-left text-white text-h3',
            style='border-radius: 3px; height: 70px; width: 80%;', a=d1, text='Netflix Analysis')
    t2 = jp.QDiv(classes='relative-position flex flex-left text-white text-h5 ',
            style='border-radius: 3px; height: 70px; width: 80%;', a=d1, text='These graphs represent the Netflix Analysis')

    d2 = jp.Div(classes='m-2 p-2 border-2 flex justify-center', a=wp)
    
    hc1 = jp.HighCharts(a=d2, options=chart_def, classes='flex-grow m-1', style='width: 40%; margin: 5px')
    hc1.options.title.text = "Count of Maturity ratings in all TV Shows and Movies"
    hc1.options.xAxis.categories = list(Rat.index)
    hc1.options.series[0].data = list(Rat)
    
    hc2 = jp.HighCharts(a=d2, options=chart_def, classes='flex-grow m-1', style='width: 40%; margin: 5px')
    hc2.options.title.text = "Count of Maturity ratings in all TV Shows and Movies"
    hc2.options.xAxis.categories = list(Rat.index)
    hc2.options.series[0].data = list(Rat)
    
    c = jp.parse_html(description, a=wp, classes='q-pa-md row justify-center')
    c.name_dict["description_button"].dialog = c.name_dict["description_dialog"]
    c.name_dict["description_button"].on('click', open_dialog)
    
    return wp

if __name__ == '__main__':
    jp.justpy(app)
    
