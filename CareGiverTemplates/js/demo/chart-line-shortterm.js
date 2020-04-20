var dom = document.getElementById("shorttermChart");
var myChart = echarts.init(dom);
var app = {};
option = null;
option = {
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data: ['wordsearch','tile_matching','brown_peterson']
    },
    toolbox: {
        show: true,
        feature: {
            dataZoom: {
                yAxisIndex: 'none'
            },
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
        max: 100,
        axisLabel: {
            formatter: '{value}'
        }
    },
    series: [
        {
            name: 'wordsearch',
            type: 'line',
            //data = data.heartrate
            data: [10, 19, 9, 13, 4, 13, 3],
        },
        {
            name: 'tile_matching',
            type: 'line',
            //data = data.heartrate
            data: [10, 89, 90, 3, 40, 13, 6],
        },
        {
            name: 'brown_peterson',
            type: 'line',
            //data = data.heartrate
            data: [10, 9, 9, 10, 4, 93, 3],
        }
    ]
};
;
myChart.setOption(option, true);

window.onresize = function(){
    myChart.resize();
}