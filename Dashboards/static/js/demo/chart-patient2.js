var dom1 = document.getElementById("patientChart1");
var myChart1 = echarts.init(dom1);
var app = {};
option = null;
option1 = {
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
myChart1.setOption(option, true);

var dom2 = document.getElementById("patientChart2");
var myChart2 = echarts.init(dom2);
var app = {};
option = null;
option2 = {
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
            data: [{value: 20, name: 'score'}]
        }
    ]
};
myChart2.setOption(option, true);

var dom3 = document.getElementById("patientChart3");
var myChart3 = echarts.init(dom3);
var app = {};
option = null;
option3 = {
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
            data: [{value: 50, name: 'score'}]
        }
    ]
};
myChart3.setOption(option, true);

var dom4 = document.getElementById("patientChart4");
var myChart4 = echarts.init(dom4);
var app = {};
option = null;
option4 = {
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
            data: [{value: 69, name: 'score'}]
        }
    ]
};
myChart4.setOption(option, true);