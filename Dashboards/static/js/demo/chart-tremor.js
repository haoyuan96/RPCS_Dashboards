var dom = document.getElementById("tremorChart");
var myChart = echarts.init(dom);
var app = {
    time:[],
    yvalue:[]
};
$(document).done(function(){
    getData();
});
option = {
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data: ['Tremor frequency']
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
        // type: 'category',
        // boundaryGap: false,
        // data : []
    },
    yAxis: {
        type: 'value',
        min: 0,
        max: 200,
        axisLabel: {
            formatter: '{value}Hz'
        }
    },
    series: [
        {
            name: 'Tremor frequency',
            type: 'line',
            //data = data.heartrate
            data: [],
            markLine: {
                data: [
                    {type: 'average', name: 'average heartrate'}
                ]
            }
        }
    ]
};
myChart.setOption(option);

function getData() {
    $.ajax({
        type: 'GET',
        url:'/metric_display',
        data:{},
        dataType:'json',
        success:function (data) {
            app.time = data.tremor1.time;
            app.yvalue = data.tremor1.yvalue;
            console.log(app.time);
            console.log(app.yvalue);
            myChart.setOption({
                xAxis : {
                    type:'category',
                    data: app.time
                },
                series: [{
                    name: 'Tremor frequency',
                    type: 'line',
                    data: app.yvalue
                }]
            });
            console.log(app.time);
            console.log(app.yvalue);
        }
    });
    return app;
}
// myChart.setOption({
//     xAxis : {
//         type:'category',
//         data: ["2020-03-01","2020-03-02","2020-03-03","2020-03-04","2020-03-05"]
//     },
//     series: [{
//         name: 'heartrate',
//         type: 'line',
//         data: [90, 99, 93, 84, 93, 1]
//     }]
// });


