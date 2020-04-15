var dom = document.getElementById("heartChart");
var myChart = echarts.init(dom);
var app = {};
option = null;
option = {
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data: ['heartrate']
    },
    toolbox: {
        show: true,
        feature: {
            dataZoom: {
                yAxisIndex: 'none'
            },
            dataView: {readOnly: false},
            restore: {},
            saveAsImage: {}
        }
    },
    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: ['Sun', 'Mon', 'Tues', 'Wed', 'Thu', 'Fri', 'Sat']
    },
    yAxis: {
        type: 'value',
        min: 0,
        max: 200,
        axisLabel: {
            formatter: '{value}'
        }
    },
    series: [
        {
            name: 'heartrate',
            type: 'line',
            //data = data.heartrate
            data: [90, 99, 99, 93, 84, 93, 83],
            markLine: {
                data: [
                    {type: 'average', name: 'average heartrate'}
                ]
            }
        }
    ]
};
;
myChart.setOption(option, true);
