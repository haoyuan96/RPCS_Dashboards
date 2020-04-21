var dom = document.getElementById("barChart");
var myChart = echarts.init(dom);
$(document).ready(function(){
    getData();
})
option = {
    // dataset: {
    //     source: [
    //         ['score', 'todayscore', 'product'],
    //         [9.3, 9.3, 'Sleep'],
    //         [57.1, 57.1, 'Mood'],
    //         [74.4, 74.4, 'Blood pressure'],
    //         [50.1, 50.1, 'Memory'],
    //         [89.7, 89.7, 'Eating'],
    //         [12.1, 12.1, 'Heart Rate'],
    //     ]
    // },
    grid: {containLabel: true},
    xAxis: {type: 'value',
        min: 0,
        max: 100
    },
    yAxis: {
        type: 'category',
        data:['neutral','happiness','sadness','surprise','anger']
    },
    // visualMap: {
    //     orient: 'horizontal',
    //     left: 'center',
    //     min: 0,
    //     max: 100,
    //     text: ['High Score', 'Low Score'],
    //     // Map the score column to color
    //     dimension: 0,
    //     inRange: {
    //         color: ['#E15457','#D7DA8B']
    //     }
    // },
    series: [
        // {
        //     type: 'bar',
        //     encode: {
        //         // Map the "amount" column to X axis.
        //         x: 'todayscore',
        //         // Map the "product" column to Y axis
        //         y: 'product'
        //     }
        // }
    ]
};
myChart.setOption(option, true);

window.onresize = function(){
    myChart.resize();
}

function getData() {
    $.ajax({
        type: 'GET',
        url:'/caregiver/view_general',
        // contentType: "application/json; charset=utf-8",
        data:{},
        dataType:'json',
        success:function (data) {
            console.log(data);
            app = data;
            console.log(app.mood);
            myChart.setOption({
                series: [{
                    type: 'bar',
                    data: app.mood.yvalue
                }
            ]
            });
        },
        error:function(msg){
            console.log("error msg")
            console.log(msg)
        }
    });
}