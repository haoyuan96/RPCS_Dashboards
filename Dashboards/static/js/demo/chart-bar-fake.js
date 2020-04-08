var dom = document.getElementById("barChart");
var myChart = echarts.init(dom);
var app = {};
option = null;
option = {
    dataset: {
        source: [
            ['score', 'todayscore', 'product'],
            [9.3, 9.3, 'Sleep'],
            [57.1, 57.1, 'Mood'],
            [74.4, 74.4, 'Blood pressure'],
            [50.1, 50.1, 'Memory'],
            [89.7, 89.7, 'Eating'],
            [12.1, 12.1, 'Heart Rate'],
        ]
    },
    grid: {containLabel: true},
    xAxis: {name: 'amount'},
    yAxis: {type: 'category'},
    visualMap: {
        orient: 'horizontal',
        left: 'center',
        min: 10,
        max: 100,
        text: ['High Score', 'Low Score'],
        // Map the score column to color
        dimension: 0,
        inRange: {
            color: ['#D7DA8B', '#E15457']
        }
    },
    series: [
        {
            type: 'bar',
            encode: {
                // Map the "amount" column to X axis.
                x: 'todayscore',
                // Map the "product" column to Y axis
                y: 'product'
            }
        }
    ]
};
myChart.setOption(option, true);

window.onresize = function(){
    myChart.resize();
}