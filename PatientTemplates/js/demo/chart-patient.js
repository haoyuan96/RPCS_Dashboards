var dom = document.getElementById("patientChart1");
var myChart = echarts.init(dom);
var app = {};
option = null;
option = {
    tooltip: {
        formatter: '{a} <br/>{b} : {c}%'
    },
    toolbox: {
        feature: {
            restore: {},
            saveAsImage: {}
        }
    },
    series: [
        {
            name: 'matric A',
            type: 'gauge',
            detail: {formatter: '{value}%'},
            data: [{value: 86, name: 'score'}]
        }
    ]
};
myChart.setOption(option, true);

window.onresize = function(){
    myChart.resize();
}