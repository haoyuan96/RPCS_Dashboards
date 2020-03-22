function getVirtulData(year) {
    year = year || '2021';
    var date = +echarts.number.parseDate(year + '-01-01');
    var end = +echarts.number.parseDate((+year + 1) + '-01-01');
    var dayTime = 3600 * 24 * 1000;
    var data = [];
    for (var time = date; time < end; time += dayTime) {
        data.push([
            echarts.format.formatTime('yyyy-MM-dd', time),
            Math.floor(Math.random() * 10000)
        ]);
    }
    return data;
}

var data = getVirtulData(2020);
var dom = document.getElementById("calendarChart");
var myChart = echarts.init(dom);
var app = {};
option = null;

option = {
    // backgroundColor: '#404a59',

    title: {
        subtext: 'all data is fake at the moment',
        left: 'center',
    },
    tooltip: {
        trigger: 'item'
    },
    legend: {
        top: '30',
        left: '100',
        data: ['the number of falling', 'Top'],
        textStyle: {
            color: '#000'
        }
    },
    calendar: [{
        top: 'middle',
        left: 'center',
        cellSize: [28,28],
        range: ['2020-01-01', '2020-03-31'],
        splitLine: {
            show: true,
            lineStyle: {
                color: '#000',
                width: 3,
                type: 'solid'
            }
        },
        yearLabel: {
            formatter: '{start}  Jun - Mar',
            textStyle: {
                color: '#000'
            }
        },
        itemStyle: {
            // color: '#323c48',
            borderWidth: 1,
            borderColor: '#111'
        }
    }
],
    series: [
        {
            name: 'the number of falling',
            type: 'scatter',
            coordinateSystem: 'calendar',
            data: data,
            symbolSize: function (val) {
                return val[1] / 500;
            },
            itemStyle: {
                color: '#ddb926'
            }
        },
        {
            name: 'the number of falling',
            type: 'scatter',
            coordinateSystem: 'calendar',
            calendarIndex: 1,
            data: data,
            symbolSize: function (val) {
                return val[1] / 500;
            },
            itemStyle: {
                color: '#ddb926'
            }
        },
        {
            name: 'Top',
            type: 'effectScatter',
            coordinateSystem: 'calendar',
            calendarIndex: 1,
            data: data.sort(function (a, b) {
                return b[1] - a[1];
            }).slice(0, 12),
            symbolSize: function (val) {
                return val[1] / 500;
            },
            showEffectOn: 'render',
            rippleEffect: {
                brushType: 'stroke'
            },
            hoverAnimation: true,
            itemStyle: {
                color: '#f4e925',
                shadowBlur: 10,
                shadowColor: '#333'
            },
            zlevel: 1
        },
        {
            name: 'Top',
            type: 'effectScatter',
            coordinateSystem: 'calendar',
            data: data.sort(function (a, b) {
                return b[1] - a[1];
            }).slice(0, 12),
            symbolSize: function (val) {
                return val[1] / 500;
            },
            showEffectOn: 'render',
            rippleEffect: {
                brushType: 'stroke'
            },
            hoverAnimation: true,
            itemStyle: {
                color: '#f4e925',
                shadowBlur: 10,
                shadowColor: '#333'
            },
            zlevel: 1
        }
    ]
};
myChart.setOption(option, true);

window.onresize = function(){
    myChart.resize();
}