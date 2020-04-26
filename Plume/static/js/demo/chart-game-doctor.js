var gameChart = echarts.init(document.getElementById("gameChart"));
$(document).ready(function(){
    getGame();
})
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

function getGame() {
    var user = document.getElementById("username").value;
    $.ajax({
        type: 'POST',
        url:'/doctor/metric_display',
        // contentType: "application/json; charset=utf-8",
        data:{'username': user},
        dataType:'json',
        success:function (data) {
            console.log(data);
            app = data;
            console.log(app.blood);
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
        },
        error:function(msg){
            console.log("error msg")
            console.log(msg)
        }
    });
}