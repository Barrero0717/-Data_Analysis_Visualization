import justpy as jp
import pandas
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt

chart_def_1 = """
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
            text: 'Maturity Ratings'
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

chart_Release = """
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
            text: 'Release Year'
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

chart_3 = """
{
    chart: {
        type: 'columnpyramid'
    },
    title: {
        text: 'The 5 highest pyramids in the World'
    },
    colors: ['#C79D6D', '#B5927B', '#CE9B84', '#B7A58C', '#C7A58C'],
    xAxis: {
        crosshair: true,
        labels: {
            style: {
                fontSize: '14px'
            }
        },
        type: 'category'
    },
    yAxis: {
        min: 0,
        title: {
            text: 'Number of movies'
        }
    },
    tooltip: {
        valueSuffix: ' movies'
    },
    series: [{
        name: '->',
        colorByPoint: true,
        data: [
            ['Pyramid of Khufu', 138.8],
            ['Pyramid of Khafre', 136.4],
            ['Red Pyramid', 104],
            ['Bent Pyramid', 101.1],
            ['Pyramid of the Sun', 75]
        ],
        showInLegend: false
    }]
}
"""

chart_4 = """
{
    chart: {
        type: 'columnpyramid'
    },
    title: {
        text: 'The 5 highest pyramids in the World'
    },
    colors: ['#C79D6D', '#B5927B', '#CE9B84', '#B7A58C', '#C7A58C'],
    xAxis: {
        crosshair: true,
        labels: {
            style: {
                fontSize: '14px'
            }
        },
        type: 'category'
    },
    yAxis: {
        min: 0,
        title: {
            text: 'Number of seasons'
        }
    },
    tooltip: {
        valueSuffix: ' seasons'
    },
    series: [{
        name: '->',
        colorByPoint: true,
        data: [
            ['Pyramid of Khufu', 138.8],
            ['Pyramid of Khafre', 136.4],
            ['Red Pyramid', 104],
            ['Bent Pyramid', 101.1],
            ['Pyramid of the Sun', 75]
        ],
        showInLegend: false
    }]
}
"""

data = pandas.read_csv("netflix_titles.csv", parse_dates=["date_added"])
Rat = data["rating"].value_counts()
Release = data["release_year"].value_counts()
Type = data["type"].value_counts()
TV_Dur = data[data["type"]=="TV Show"]["duration"].value_counts()
Movie_Dur = data[data["type"]=="Movie"]["duration"].value_counts()

def open_dialog(self, msg):
    self.dialog.value = True

def app():
    wp = jp.QuasarPage(highcharts_theme='gray', title='Netflix Analysis', dark=True)
    wp.head_html = '<link href="https://fonts.googleapis.com/css2?family=Noto+Sans:wght@700&display=swap" rel="stylesheet">' 
    wp.css = 'body { font-family: Noto Sans, sans-serif; }' 
    
    d1 = jp.Div(classes='q-pa-md row justify-center', a=wp)
    t1 = jp.QDiv(classes='relative-position flex flex-center text-white text-h3',
            style='border-radius: 3px; height: 70px; width: 80%;', a=d1, text='Netflix Analysis')
    t2 = jp.QDiv(classes='relative-position flex flex-right text-white text-h7 ',
            style='border-radius: 3px; height: 70px; width: 80%;', a=d1, text='These graphs represent a brief review of all Netflix TV Shows and Movies.')

    d2 = jp.Div(classes='q-pa-md row justify-center', a=wp)
    st1 = jp.QDiv(classes='flex text-blue text-h4', style='border-radius: 3px; height: 70px; width: 80%;', a=d2, text='')
    st1.text = "Number of Movies: " + str(Type[0])
    st2 = jp.QDiv(classes='flex text-blue text-h4', style='border-radius: 3px; height: 70px; width: 80%;', a=d2, text='')
    st2.text = "Number of TV Shows: " + str(Type[1])

    d3 = jp.Div(classes='m-2 p-2 border-2 flex justify-center', a=wp)    
    hc1 = jp.HighCharts(a=d3, options=chart_def_1, classes='flex-grow m-1', style='width: 40%; margin: 5px')
    hc1.options.title.text = "Count of Maturity ratings in all TV Shows and Movies"
    hc1.options.xAxis.categories = list(Rat.index)
    hc1.options.series[0].data = list(Rat)    
    
    hc2 = jp.HighCharts(a=d3, options=chart_Release, classes='flex-grow m-1', style='width: 40%; margin: 5px')
    hc2.options.title.text = "Count of Release Year in all TV Shows and Movies"
    hc2.options.xAxis.categories = list(Release.index)
    hc2.options.series[0].data = list(Release)
 
    hc3 = jp.HighCharts(a=d3, options=chart_3, style='width: 40%; margin: 5px')
    hc3.options.title.text = "Duration of the Movies"
    hc3.options.xAxis.categories = list(Movie_Dur.index)
    hc3.options.series[0].data = list(Movie_Dur)   
    
    hc4 = jp.HighCharts(a=d3, options=chart_4, style='width: 40%; margin: 5px')
    hc4.options.title.text = "Duration of the TV Shows"
    hc4.options.xAxis.categories = list(TV_Dur.index)
    hc4.options.series[0].data = list(TV_Dur)  

        
    return wp

if __name__ == '__main__':
    jp.justpy(app)
    
