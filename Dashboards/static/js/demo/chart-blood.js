var dom = document.getElementById("bloodChart");
var myChart = echarts.init(dom);
var app = {
    time:[],
    yvalue:[]
};
$(document).ready(function(){
    getData();
});
option = null;
option = {
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data: ['systolic', 'diastolic']
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
        // data = data.time
        // data: ['Sun', 'Mon', 'Tues', 'Wed', 'Thu', 'Fri', 'Sat']
    },
    yAxis: {
        type: 'value',
        min: 0,
        max: 260,
        axisLabel: {
            formatter: '{value}'
        }
    },
    series: [
        {
            name: 'systolic',
            type: 'line',
            //data = data.systolic
            // data: [11, 11, 15, 13, 12, 13, 5],
            markLine: {
                data: [
                    {type: 'average', name: 'average diastolic'}
                ]
            }
        },
        {
            name: 'diastolic',
            type: 'line',
            //data = data.diastolic
            // data: [21, 81, 80, 93, 92, 93, 95],
            markLine: {
                data: [
                    {type: 'average', name: 'average diastolic'}
                ]
            }
        }
    ]
};
;
myChart.setOption(option, true);

function getData() {
    $.ajax({
        type: 'GET',
        url:'/cargiver/metric_display',
        data:{},
        dataType:'json',
        success:function (data) {
            app = eval(data);
            myChart.setOption({
                xAxis : {
                    type:'category',
                    data: app.heartrate.time
                },
                series: [{
                    name: 'systolic',
                    type: 'line',
                    data: app.heartrate.yvalue.systolic
                },
                {
                    name: 'diastolic',
                    type: 'line',
                    data: app.heartrate.yvalue.diastolic
                }]
            });
            console.log(app.time);
            console.log(app.yvalue);
        }
    });
    return app;
}

window.onresize = function(){
    myChart.resize();
}