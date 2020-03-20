var dom = document.getElementById("lineChart2");
var myChart = echarts.init(dom);
var app = {};
option = null;
option = {
    title: {
        subtext: 'All data is fake at this time'
    },
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data: ['metric1']
    },
    toolbox: {
        show: true,
        feature: {
            dataZoom: {
                yAxisIndex: 'none'
            },
            dataView: {readOnly: false},
            magicType: {type: ['line', 'bar']},
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
        axisLabel: {
            formatter: '{value}'
        }
    },
    series: [
        {
            name: 'metric1',
            type: 'line',
            data: [10, 19, 9, 13, 4, 13, 3],
            markPoint: {
                data: [
                    {type: 'max', name: 'maximum'},
                    {type: 'min', name: 'minimum'}
                ]
            },
            markLine: {
                data: [
                    {type: 'average', name: 'average'}
                ]
            }
        }
    ]
};
;
myChart.setOption(option, true);

window.onresize = function(){
    myChart.resize();
}