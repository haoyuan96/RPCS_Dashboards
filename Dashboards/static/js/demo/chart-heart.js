var dom = document.getElementById("heartChart");
var myChart = echarts.init(dom);
var app = {
    time:[],
    yvalue:[]
};
$(document).ready(function(){
    getData1();
})
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
        // type: 'category',
        // boundaryGap: false,
        // data : []
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
// function getData() {
//     $.ajax({
//         url:'/',
//         dataType:'json',
//         success:function (data) {
//             app.time = data.time;
//             app.yvalue = data.yvalue;
//             myChart.setOption({
//                 xAxis : {
//                     type:'time',
//                     data: app.time
//                 },
//                 series: [{
//                     name: 'heartrate',
//                     type: 'line',
//                     data: app.yvalue
//                 }]
//             })
//         }
//     })
// }
// app.yvalue.push(1);
// $.getJSON('/static/js/echarts_test_data.json',function (data) {
//     app.time = data.time;
//     // 打印"a, undefined, c"
//     for (let i = 0; i < data.yvalue.length; ++i) {
//         console.log(app.yvalue);
//         app.yvalue.push(data.yvalue[i]);
//     }
// });

// app.time = ["2020-03-01","2020-03-02","2020-03-03","2020-03-04","2020-03-05"];
// // app.yvalue = [90, 99, 93, 84, 93];
// myChart.setOption({
//     xAxis: {
//         type: 'category',
//         data: app.time
//     },
//     series:[
//         {
//             name: 'heartrate',
//             type: 'line',
//             data: app.yvalue
//         }]
// });

function getData1() {
    $.ajax({
        type: 'GET',
        url:'/caregiver/metric_display',
        data:{},
        dataType:'application/json',
        success:function (data) {
            app = eval(data);
            console.log(data.heartrate.time);
            console.log(data.heartrate.yvalue);
            myChart.setOption({
                xAxis : {
                    type:'category',
                    data: app.heartrate.time
                },
                series: [{
                    name: 'heartrate',
                    type: 'line',
                    data: app.heartrate.yvalue
                }]
            }, true);
            console.log(app.time);
            console.log(app.yvalue);
        },
        error:function(msg){
            console.log(msg)
        }
    });
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


