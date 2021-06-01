$(document).ready(function() {
   var title = {
      text: 'Blood Pressure'
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
         text: 'blood pressure (mmHg)'
      },
      plotLines: [{
         value: 0,
         width: 1,
         color: '#808080'
      }]
   };

   var tooltip = {
      valueSuffix: 'average mmHg/min'
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
         name: 'average mmHg/min',
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

   $('#graph_blood_pressure').highcharts(json);
   $('#graph_blood_pressure').highcharts().xAxis.visible = false;

   var chartFunction = function() {
      var chart = $('#graph_blood_pressure').highcharts();
      $.getJSON("http://127.0.0.1:5000/data/blood_pressure/", function(heart_rate) {
         chart.series[0].addPoint(heart_rate, true, true);
      });
   };

   setInterval(chartFunction, 3000);
});