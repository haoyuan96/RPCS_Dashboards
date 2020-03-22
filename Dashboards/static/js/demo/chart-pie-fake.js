var dom = document.getElementById("pieChart");
var myChart = echarts.init(dom);
var app = {};
option = null;
option = {
    title: {
        subtext: 'All data is fake at the moment',
        left:'center',
    },
    tooltip: {
        trigger: 'item',
        formatter: '{a} <br/>{b} : {c} ({d}%)'
    },
    legend: {
        orient: 'vertical',
        left: 'left',
        data: ['type A', 'type B', 'type C', 'type D', 'type E']
    },
    series: [
        {
            type: 'pie',
            radius: '55%',
            center: ['50%', '50%'],
            data: [
                {value: 335, name: 'type A'},
                {value: 310, name: 'type B'},
                {value: 234, name: 'type C'},
                {value: 135, name: 'type D'},
                {value: 1548, name: 'type E'}
            ],
            emphasis: {
                itemStyle: {
                    shadowBlur: 10,
                    shadowOffsetX: 0,
                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
            }
        }
    ]
};
myChart.setOption(option, true);

window.onresize = function(){
    myChart.resize();
}