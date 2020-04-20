var heartChart = echarts.init(document.getElementById("heartChart"));
var tremorChart1 = echarts.init(document.getElementById("tremorChart1"));
var tremorChart2 = echarts.init(document.getElementById("tremorChart2"));
var bloodChart = echarts.init(document.getElementById("bloodChart"));
var gameChart = echarts.init(document.getElementById("gameChart"));
var moodChart = echarts.init(document.getElementById("moodChart"));
var user = document.getElementById("username").value;
$(document).ready(function(user){
    getData(user);
})

option_heart = {
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
heartChart.setOption(option_heart);

option_tremor1 = {
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
        type: 'category',
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
                    {type: 'average', name: 'average tremor frequency'}
                ]
            }
        }
    ]
};
tremorChart1.setOption(option_tremor1);

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

option_game = {
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data: ['wordsearch','tile matching','brown peterson']
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
            data: [],
            //data = data.heartrate
            // data: [10, 19, 9, 13, 4, 13, 3],
        },
        {
            name: 'tile matching',
            type: 'line',
            data: [],
            //data = data.heartrate
            // data: [10, 89, 90, 3, 40, 13, 6],
        },
        {
            name: 'brown peterson',
            type: 'line',
            data: [],
            //data = data.heartrate
            // data: [10, 9, 9, 10, 4, 93, 3],
        }
    ]
};
gameChart.setOption(option_game);

option_mood = {
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data: ['neutral','happiness','sadness','surprise','anger']
    },
    xAxis: {
        type: 'category',
        boundaryGap: false,
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
            data: [],
            //data = data.heartrate
            // data: [10, 19, 9, 13, 4, 13, 3],
            smooth: true,
        },
        {
            name: 'happiness',
            type: 'line',
            data: [],
            //data = data.heartrate
            // data: [10, 89, 90, 3, 40, 13, 6],
            smooth: true,
        },
        {
            name: 'sadness',
            type: 'line',
            data: [],
            //data = data.heartrate
            // data: [10, 9, 9, 10, 4, 93, 3],
            smooth: true,
        },
        {
            name: 'surprise',
            type: 'line',
            data: [],
            //data = data.heartrate
            // data: [10, 9, 9, 10, 4, 93, 3],
            smooth: true,
        },
        {
            name: 'anger',
            type: 'line',
            data: [],
            //data = data.heartrate
            // data: [10, 9, 9, 10, 4, 93, 3],
            smooth: true,
        }
    ]
};
moodChart.setOption(option_mood);

option_tremor2 = {
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data: ['Tremor number']
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

function getData(user) {
    $.ajax({
        type: 'POST',
        url:'/doctor/metric_display',
        // contentType: "application/json; charset=utf-8",
        data:{username: user},
        dataType:'json',
        success:function (data) {
            console.log(data);
            app = data;
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
            moodChart.setOption({
                xAxis : {
                    type:'category',
                    data: app.mood.time
                },
                series: [{
                    name: 'neutral',
                    type: 'line',
                    //data = data.heartrate
                    data: app.mood.yvalue.neutral,
                    smooth: true,
                },
                {
                    name: 'happiness',
                    type: 'line',
                    //data = data.heartrate
                    data: app.mood.yvalue.happiness,
                    smooth: true,
                },
                {
                    name: 'sadness',
                    type: 'line',
                    //data = data.heartrate
                    data: app.mood.yvalue.sadness,
                    smooth: true,
                },
                {
                    name: 'surprise',
                    type: 'line',
                    //data = data.heartrate
                    data: app.mood.yvalue.surprise,
                    smooth: true,
                },
                {
                    name: 'anger',
                    type: 'line',
                    //data = data.heartrate
                    data: app.mood.yvalue.anger,
                    smooth: true,
                }]
            });
            gameChart.setOption({
                xAxis : {
                    type:'category',
                    data: app.heartrate.time
                },
                series: [{
                    name: 'wordsearch',
                    type: 'line',
                    //data = data.heartrate
                    data: app.game.yvalue.WordSearch,
                },
                {
                    name: 'tile matching',
                    type: 'line',
                    //data = data.heartrate
                    data: app.game.yvalue.TileMatching,
                },
                {
                    name: 'brown peterson',
                    type: 'line',
                    //data = data.heartrate
                    data: app.game.yvalue.BrownPeterson,
                }]
            });
            tremorChart1.setOption({
                xAxis : {
                    type:'category',
                    data: app.tremor1.time
                },
                series: [{
                    name: 'Tremor frequency',
                    type: 'line',
                    data: app.tremor1.yvalue
                }]
            });
            tremorChart2.setOption({
                xAxis : {
                    type:'category',
                    data: app.tremor2.time
                },
                series: [{
                    name: 'Tremor number',
                    type: 'line',
                    data: app.tremor2.yvalue
                }]
            });
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
        },
        error:function(msg){
            console.log("error msg")
            console.log(msg)
        }
    });
}