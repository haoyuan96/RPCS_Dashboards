var pcGameChart = echarts.init(document.getElementById("pcGameChart"));
var vrGameChart = echarts.init(document.getElementById("vrGameChart"));
$(document).ready(function(){
    getGame();
})
option_vrgame = {
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data: ['left hand score','right hand score']
    },
    toolbox: {
        show: true,
        feature: {
            magicType: {type: ['line', 'bar']},
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
            name: 'left hand score',
            type: 'line',
            data: [],
            //data = data.heartrate
            // data: [10, 19, 9, 13, 4, 13, 3],
        },
        {
            name: 'right hand score',
            type: 'line',
            data: [],
            //data = data.heartrate
            // data: [10, 89, 90, 3, 40, 13, 6],
        }
    ]
};
vrGameChart.setOption(option_vrgame);

option_pcgame = {
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
pcGameChart.setOption(option_pcgame);

function getGame() {
    $.ajax({
        type: 'GET',
        url:'/caregiver/game_metric',
        // contentType: "application/json; charset=utf-8",
        data:{},
        dataType:'json',
        success:function (data) {
            console.log(data);
            gamedata = data;
            console.log(gamedata);
            vrGameChart.setOption({
                xAxis : {
                    type:'category',
                    data: gamedata.game.time
                },
                series: [{
                    name: 'left hand score',
                    type: 'line',
                    //data = data.heartrate
                    data: gamedata.game.yvalue.TwistFitEasy.left
                },
                {
                    name: 'right hand score',
                    type: 'line',
                    //data = data.heartrate
                    data: gamedata.game.yvalue.TwistFitEasy.right
                }]
            });
            pcGameChart.setOption({
                xAxis : {
                    type:'category',
                    data: gamedata.game.time
                },
                series: [{
                    name: 'wordsearch',
                    type: 'line',
                    //data = data.heartrate
                    data: gamedata.game.yvalue.WordSearch,
                },
                {
                    name: 'tile matching',
                    type: 'line',
                    //data = data.heartrate
                    data: gamedata.game.yvalue.TileMatching,
                },
                {
                    name: 'brown peterson',
                    type: 'line',
                    //data = data.heartrate
                    data: gamedata.game.yvalue.BrownPeterson,
                }]
            });  
        },
        error:function(msg){
            console.log("error msg")
            console.log(msg)
        }
    });
}