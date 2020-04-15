var dom = document.getElementById("moodChart");
var myChart = echarts.init(dom);
var app = {};
option = null;
option = {
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data: ['neutral','happiness','sadness','surprise','anger']
    },
    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: ['Sun', 'Mon', 'Tues', 'Wed', 'Thu', 'Fri', 'Sat']
    },
    yAxis: {
        type: 'value',
        min: 0,
        max: 100,
        axisLabel: {
            formatter: '{value}'
        }
    },
    series: [
        {
            name: 'neutral',
            type: 'line',
            //data = data.heartrate
            data: [10, 19, 9, 13, 4, 13, 3],
            smooth: true,
        },
        {
            name: 'happiness',
            type: 'line',
            //data = data.heartrate
            data: [10, 89, 90, 3, 40, 13, 6],
            smooth: true,
        },
        {
            name: 'sadness',
            type: 'line',
            //data = data.heartrate
            data: [10, 9, 9, 10, 4, 93, 3],
            smooth: true,
        },
        {
            name: 'surprise',
            type: 'line',
            //data = data.heartrate
            data: [10, 9, 9, 10, 4, 93, 3],
            smooth: true,
        },
        {
            name: 'anger',
            type: 'line',
            //data = data.heartrate
            data: [10, 9, 9, 10, 4, 93, 3],
            smooth: true,
        }
    ]
};
;
myChart.setOption(option, true);

setTimeout(function() {
    var ref = document.getElementById("heartChart").style.width+'px';
    document.getElementById("moodChart").style.width = ref;
    var dom = document.getElementById("moodChart");
    var myChart = echarts.init(dom);
}, 1000);