$(document).ready(function() {
   var chart = {
      type: 'gauge',
      plotBackgroundColor: null,
      plotBackgroundImage: null,
      plotBorderWidth: 0,
      plotShadow: false
   };

   var title = {
      text: 'Fasting Blood Sugar Level '
   };

   var pane = {
   startAngle: -150,
   endAngle: 150,
   background: [
      {
         backgroundColor: {
            linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1 },
            stops: [
               [0, '#FFF'],
               [1, '#333']
            ]
         },
         borderWidth: 0,
         outerRadius: '109%'
      },
      {
         backgroundColor: {
            linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1 },
            stops: [
               [0, '#333'],
               [1, '#FFF']
            ]
         },
         borderWidth: 1,
         outerRadius: '107%'
      },
      {
         // default background
      },
      {
         backgroundColor: '#DDD',
         borderWidth: 0,
         outerRadius: '105%',
         innerRadius: '113%'
      }]
   };

   // the value axis
   var yAxis = {
      min: 0,
      max: 200,

      minorTickInterval: 'auto',
      minorTickWidth: 1,
      minorTickLength: 10,
      minorTickPosition: 'inside',
      minorTickColor: '#666',

      tickPixelInterval: 50,
      tickWidth: 2,
      tickPosition: 'inside',
      tickLength: 15,
      tickColor: '#666',

      labels: {
         step: 2,
         rotation: 'auto'
      },
      title: {
         text: 'mg/dL'
      },
      plotBands: [
         {
            from: 1,
            to: 64,
            color: '#DF5353' // red
         },
         {
            from: 65,
            to: 79,
            color: '#DDDF0D' // yellow
         },
         {
            from: 80,
            to: 119,
            color: '#55BF3B' // green
         },
         {
            from: 120,
            to: 134,
            color: '#DDDF0D' // yellow
         },
         {
            from: 135,
            to: 200,
            color: '#DF5353' // red
         }
      ]
   };

   var credits = {
      enabled: false
   };

   var series = [{
      name: 'fasting blood sugar level ',
      data: [0],
      tooltip: {
         valueSuffix: ' mg/dL'
      }
   }];

   var json = {};
   json.chart = chart;
   json.title = title;
   json.pane = pane;
   json.yAxis = yAxis;
   json.series = series;

   var chartFunction = function (chart) {
      if (!chart.renderer.forExport) {
         setInterval(function () {
            $.getJSON("http://127.0.0.1:5000/data/fasting_blood_sugar/", function(bloodsugar) {
               var point = chart.series[0].points[0]
               point.y = bloodsugar
               point.update(bloodsugar);
            })
           
         }, 3000);
      }
   };

   $('#graph_blood_sugar').highcharts(json,chartFunction);
});