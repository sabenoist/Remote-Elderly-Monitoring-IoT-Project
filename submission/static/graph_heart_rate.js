$(document).ready(function() {
   var title = {
      text: 'Resting Heart Rate'
   };

   var subtitle = {
   };

   var xAxis = {
      labels: {
         enabled: false
      }
   };

   var yAxis = {
      title: {
         text: 'resting heart rate (bpm)'
      },
      plotLines: [{
         value: 0,
         width: 1,
         color: '#808080'
      }]
   };

   var tooltip = {
      valueSuffix: 'beats/min'
   }

   var legend = {
      layout: 'vertical',
      align: 'right',
      verticalAlign: 'middle',
      borderWidth: 0
   };

   var credits = {
      enabled: false
   };

   var series =  [{
         name: 'beats/min',
         data: [0,0,0,0,0,0,0,0,0,0,0,0]
      },
   ];

   var json = {};
   json.title = title;
   json.subtitle = subtitle;
   json.xAxis = xAxis;
   json.yAxis = yAxis;
   json.tooltip = tooltip;
   json.legend = legend;
   json.series = series;

   $('#graph_heart_rate').highcharts(json);
   $('#graph_heart_rate').highcharts().xAxis.visible = false;

   var chartFunction = function() {
      var chart = $('#graph_heart_rate').highcharts();
      $.getJSON("http://127.0.0.1:5000/data/resting_heart_rate/", function(heart_rate) {
         chart.series[0].addPoint(heart_rate, true, true);
      });
   };

   setInterval(chartFunction, 3000);
});