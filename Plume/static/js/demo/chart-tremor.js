var dom = document.getElementById("tremorChart1");
var myChart = echarts.init(dom);

function randomData() {
    now = new Date(+now + oneDay);
    value = value + Math.random() * 21 - 10;
    return {
        name: now.toString(),
        value: [
            [now.getFullYear(), now.getMonth() + 1, now.getDate()].join('/'),
            Math.round(value)
        ]
    };
}

var data = [];
var now = +new Date(2010, 1, 1);
var oneDay = 24 * 3600 * 1000;
var value = Math.random() * 1000;
for (var i = 0; i < 500; i++) {
    data.push(randomData());
}

option = {
    title: {
        subtext: 'Fake'
    },
    tooltip: {
        trigger: 'axis',
        formatter: function (params) {
            params = params[0];
            var date = new Date(params.name);
            return date.getDate() + '/' + (date.getMonth() + 1) + '/' + date.getFullYear() + ' : ' + params.value[1];
        },
        axisPointer: {
            animation: false
        }
    },
    xAxis: {
        type: 'time',
        splitLine: {
            show: false
        }
    },
    yAxis: {
        type: 'value',
        boundaryGap: [0, '100%'],
        splitLine: {
            show: false
        }
    },
    series: [{
        name: 'Fake real time data',
        type: 'line',
        showSymbol: false,
        hoverAnimation: false,
        data: data
    }]
};
myChart.setOption(option);

setInterval(function () {
    for (var i = 0; i < 5; i++) {
        data.shift();
        data.push(randomData());
    }
    myChart.setOption({
        series: [{
            name: 'Fake real time data',
            type: 'line',
            data: data
        }]
    });
}, 2000);


