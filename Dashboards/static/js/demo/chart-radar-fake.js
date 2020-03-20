var dom = document.getElementById("radarChart");
var myChart = echarts.init(dom);
var app = {};
option = null;
option = {
    title: {
        text: ''
    },
    legend: {
        left: 'left',
        data: ['today','yesterday']
    },
    radar: [
        {
            indicator: [
                { text: 'Metric 1' },
                { text: 'Metric 2' },
                { text: 'Metric 3' },
                { text: 'Metric 4' },
                { text: 'Metric 5' }
            ],
            // center: ['25%', '50%'],
            radius: 120,
            startAngle: 90,
            splitNumber: 4,
            shape: 'circle',
            name: {
                formatter: '【{value}】',
                textStyle: {
                    color: '#72ACD1'
                }
            },
            splitArea: {
                areaStyle: {
                    color: ['rgba(114, 172, 209, 0.2)',
                        'rgba(114, 172, 209, 0.4)', 'rgba(114, 172, 209, 0.6)',
                        'rgba(114, 172, 209, 0.8)', 'rgba(114, 172, 209, 1)'],
                    shadowColor: 'rgba(0, 0, 0, 0.3)',
                    shadowBlur: 10
                }
            },
            axisLine: {
                lineStyle: {
                    color: 'rgba(255, 255, 255, 0.5)'
                }
            },
            splitLine: {
                lineStyle: {
                    color: 'rgba(255, 255, 255, 0.5)'
                }
            }
        }
    ],
    series: [
        {
            name: '雷达图',
            type: 'radar',
            emphasis: {
                lineStyle: {
                    width: 4
                }
            },
            data: [
                {
                    value: [100, 8, 0.40, -80, 2000],
                    name: 'yesterday',
                    symbol: 'rect',
                    symbolSize: 5,
                    lineStyle: {
                        type: 'dashed'
                    }
                },
                {
                    value: [60, 5, 0.30, -100, 1500],
                    name: 'today',
                    areaStyle: {
                        color: 'rgba(255, 255, 255, 0.5)'
                    }
                }
            ]
        }
    ]
};
myChart.setOption(option, true);

window.onresize = function(){
    myChart.resize();
}