var heartChart = echarts.init(document.getElementById("heartChart"));
// var tremorChart1 = echarts.init(document.getElementById("tremorChart1"));
var tremorChart2 = echarts.init(document.getElementById("tremorChart2"));
var bloodChart = echarts.init(document.getElementById("bloodChart"));
var moodChart = echarts.init(document.getElementById("moodChart"));
$(document).ready(function(){
    getData();
})

option_heart = {
    tooltip: {
        trigger: 'axis'
    },
    toolbox: {
        show: true,
        feature: {
            dataZoom: {
                yAxisIndex: 'none'
            },
            dataView: {readOnly: false},
            saveAsImage: {}
        }
    },
    xAxis: {
        type: 'category',
        // boundaryGap: false,
        // data : []
    },
    yAxis: {
        type: 'value',
        min: 25,
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
heartChart.setOption(option_heart);
heartChart.showLoading();

// option_tremor1 = {
//     tooltip: {
//         trigger: 'axis'
//     },
//     legend: {
//         data: ['Tremor frequency']
//     },
//     toolbox: {
//         show: true,
//         feature: {
//             dataZoom: {
//                 yAxisIndex: 'none'
//             },
//             dataView: {readOnly: false},
//             saveAsImage: {}
//         }
//     },
//     xAxis: {
//         type: 'category',
//         // boundaryGap: false,
//         // data : []
//     },
//     yAxis: {
//         type: 'value',
//         min: 0,
//         max: 200,
//         axisLabel: {
//             formatter: '{value}Hz'
//         }
//     },
//     series: [
//         {
//             name: 'Tremor frequency',
//             type: 'line',
//             //data = data.heartrate
//             data: [],
//             markLine: {
//                 data: [
//                     {type: 'average', name: 'average tremor frequency'}
//                 ]
//             }
//         }
//     ]
// };
// tremorChart1.setOption(option_tremor1);
// tremorChart1.showLoading();

option_blood = {
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
        min: 30,
        max: 210,
        axisLabel: {
            formatter: '{value}'
        }
    },
    series: [
        {
            name: 'systolic',
            type: 'line',
            //data = data.systolic
            data: [],
            // data: [11, 11, 15, 13, 12, 13, 5],
            markLine: {
                data: [
                    {type: 'average', name: 'average systolic'}
                ]
            }
        },
        {
            name: 'diastolic',
            type: 'line',
            data: [],
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
bloodChart.setOption(option_blood);
bloodChart.showLoading();

// option_mood = {
//     tooltip: {
//         trigger: 'axis'
//     },
//     legend: {
//         data: ['neutral','happiness','sadness','surprise','anger']
//     },
//     toolbox: {
//         show: true,
//         feature: {
//             saveAsImage: {}
//         }
//     },
//     xAxis: {
//         type: 'category',
//         boundaryGap: false,
//     },
//     yAxis: {
//         type: 'value',
//         min: 0,
//         max: 100,
//         axisLabel: {
//             formatter: '{value}'
//         }
//     },
//     series: [
//         {
//             name: 'neutral',
//             type: 'line',
//             data: [],
//             //data = data.heartrate
//             // data: [10, 19, 9, 13, 4, 13, 3],
//             smooth: true,
//         },
//         {
//             name: 'happiness',
//             type: 'line',
//             data: [],
//             //data = data.heartrate
//             // data: [10, 89, 90, 3, 40, 13, 6],
//             smooth: true,
//         },
//         {
//             name: 'sadness',
//             type: 'line',
//             data: [],
//             //data = data.heartrate
//             // data: [10, 9, 9, 10, 4, 93, 3],
//             smooth: true,
//         },
//         {
//             name: 'surprise',
//             type: 'line',
//             data: [],
//             //data = data.heartrate
//             // data: [10, 9, 9, 10, 4, 93, 3],
//             smooth: true,
//         },
//         {
//             name: 'anger',
//             type: 'line',
//             data: [],
//             //data = data.heartrate
//             // data: [10, 9, 9, 10, 4, 93, 3],
//             smooth: true,
//         }
//     ]
// };


option_mood = {
    legend: {},
    tooltip: {
        trigger: 'axis',
        showContent: false
    },
    dataset: {
        source: [
            ['emotion', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri','Sat'],
            ['happiness', 41.1, 30.4, 65.1, 53.3, 83.8, 98.7, 10],
            ['sadness', 86.5, 92.1, 85.7, 83.1, 73.4, 55.1, 20],
            ['neutral', 24.1, 67.2, 79.5, 86.4, 65.2, 82.5, 20],
            ['surprise', 55.2, 67.1, 69.2, 72.4, 43.9, 19.1, 49],
            ['anger', 15.2, 37.1, 69.2, 22.4, 13.9, 29.1, 1]
        ]
    },
    xAxis: {type: 'category'},
    yAxis: {gridIndex: 0},
    grid: {top: '10%', right: '40%'},
    series: [
        {type: 'line', smooth: true, seriesLayoutBy: 'row'},
        {type: 'line', smooth: true, seriesLayoutBy: 'row'},
        {type: 'line', smooth: true, seriesLayoutBy: 'row'},
        {type: 'line', smooth: true, seriesLayoutBy: 'row'},
        {type: 'line', smooth: true, seriesLayoutBy: 'row'},
        {
            type: 'pie',
            id: 'pie',
            radius: '40%',
            center: ['80%', '50%'],
            label: {
                formatter: '{b}: {@Sat} ({d}%)'
            },
            encode: {
                itemName: 'emotion',
                value: 'Sat',
                tooltip: 'Sat'
            }
        }
    ]
};

moodChart.on('updateAxisPointer', function (event) {
    var xAxisInfo = event.axesInfo[0];
    if (xAxisInfo) {
        var dimension = xAxisInfo.value + 1;
        moodChart.setOption({
            series: {
                id: 'pie',
                label: {
                    formatter: '{b}: {@[' + dimension + ']} ({d}%)'
                },
                encode: {
                    value: dimension,
                    tooltip: dimension
                }
            }
        });
    }
});
moodChart.setOption(option_mood);
// moodChart.showLoading();



option_tremor2 = {
    tooltip: {
        trigger: 'axis'
    },
    visualMap: {
        top: 5,
        left: 5,
        pieces: [{
            gt: 0,
            lte: 5,
            color: '#ff9933'
        }],
        outOfRange: {
            color: '#660099'
        }
    },
    toolbox: {
        show: true,
        feature: {
            dataZoom: {
                yAxisIndex: 'none'
            },
            dataView: {readOnly: false},
            magicType: {type: ['line', 'bar']},
            saveAsImage: {}
        }
    },
    xAxis: {
        type: 'category',
        // boundaryGap: false,
        // data : []
    },
    yAxis: {
        type: 'value',
        min: 0,
        max: 10,
        axisLabel: {
            formatter: '{value}'
        }
    },
    series: [
        {
            name: 'Tremor number',
            type: 'line',
            //data = data.heartrate
            data: [],
            markLine: {
                data: [
                    {type: 'average', name: 'average tremor number'}
                ]
            }
        }
    ]
};
tremorChart2.setOption(option_tremor2);
tremorChart2.showLoading();

function getData() {
    $.ajax({
        type: 'GET',
        url:'/caregiver/metric_display',
        // contentType: "application/json; charset=utf-8",
        data:{},
        dataType:'json',
        success:function (data) {
            console.log(data);
            app = data;
            console.log(app.blood);
            heartChart.setOption({
                xAxis : {
                    type:'category',
                    data: app.heartrate.time
                },
                series: [{
                    name: 'heartrate',
                    type: 'line',
                    data: app.heartrate.yvalue
                }]
            });
            heartChart.hideLoading();
            // moodChart.setOption({
            //     xAxis : {
            //         type:'category',
            //         data: app.mood.time
            //     },
            //     series: [{
            //         name: 'neutral',
            //         type: 'line',
            //         //data = data.heartrate
            //         data: app.mood.yvalue.neutral,
            //         smooth: true,
            //     },
            //     {
            //         name: 'happiness',
            //         type: 'line',
            //         //data = data.heartrate
            //         data: app.mood.yvalue.happiness,
            //         smooth: true,
            //     },
            //     {
            //         name: 'sadness',
            //         type: 'line',
            //         //data = data.heartrate
            //         data: app.mood.yvalue.sadness,
            //         smooth: true,
            //     },
            //     {
            //         name: 'surprise',
            //         type: 'line',
            //         //data = data.heartrate
            //         data: app.mood.yvalue.surprise,
            //         smooth: true,
            //     },
            //     {
            //         name: 'anger',
            //         type: 'line',
            //         //data = data.heartrate
            //         data: app.mood.yvalue.anger,
            //         smooth: true,
            //     }]
            // });
            // moodChart.hideLoading();
            // tremorChart1.setOption({
            //     xAxis : {
            //         type:'category',
            //         data: app.tremor1.time
            //     },
            //     series: [{
            //         name: 'Tremor frequency',
            //         type: 'line',
            //         data: app.tremor1.yvalue
            //     }]
            // });
            // tremorChart1.hideLoading();
            tremorChart2.setOption({
                xAxis : {
                    type:'category',
                    data: app.tremor2.time
                },
                series: [{
                    name: 'Tremor number',
                    type: 'line',
                    // data: app.tremor2.yvalue
                    data: [1,2,3,4,5,6,6,7,8,6,5,3,4,2,1,2,3,5,4,3,3,4,2,2,2,3,4,5,6,6]
                }]
            });
            tremorChart2.hideLoading();
            bloodChart.setOption({
                xAxis : {
                    type:'category',
                    data: app.blood.time
                },
                series: [{
                    name: 'systolic',
                    type: 'line',
                    data: app.blood.yvalue.systolic
                },
                {
                    name: 'diastolic',
                    type: 'line',
                    data: app.blood.yvalue.diastolic
                }]
            });
            bloodChart.hideLoading();
        },
        error:function(msg){
            console.log("error msg")
            console.log(msg)
        }
    });
}