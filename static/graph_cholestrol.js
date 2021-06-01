$(document).ready(function() {
   var chart = {
      type: 'gauge',
      plotBackgroundColor: null,
      plotBackgroundImage: null,
      plotBorderWidth: 0,
      plotShadow: false
   };

   var title = {
      text: 'Cholesterol Level'
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
      }
   ]};

   // the value axis
   var yAxis = {
      min: 0,
      max: 240,

      minorTickInterval: 'auto',
      minorTickWidth: 1,
      minorTickLength: 10,
      minorTickPosition: 'inside',
      minorTickColor: '#666',

      tickPixelInterval: 40,
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
            from: 0,
            to: 129,
            color: '#55BF3B' // green

         },
         {
            from: 130,
            to: 159,
            color: '#DDDF0D' // yellow
         },
         {
            from: 160,
            to: 189,
            color: '#FF9A08' // orange
         },
         {
            from: 190,
            to: 240,
            color: '#DF5353' // red
         }
      ]
   };

   var credits = {
      enabled: false
   };

   var series = [{
      name: 'Cholesterol Level',
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
            $.getJSON("http://127.0.0.1:5000/data/cholestrol/", function(cholestrol) {
               var point = chart.series[0].points[0]
               point.y = cholestrol
               point.update(cholestrol);
            })
           
         }, 3000);
      }
   };

   $('#graph_cholestrol').highcharts(json,chartFunction);
});