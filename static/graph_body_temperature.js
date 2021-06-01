$(document).ready(function() {
   var chart = {
      type: 'solidgauge'
   };

   var title = {
      text: 'Body Temperature'
      }

   var pane = {
      center: ['50%', '85%'],
      size: '160%',
      startAngle: -90,
      endAngle: 90,

      background: {
         backgroundColor: (
            Highcharts.theme && Highcharts.theme.background2) || '#EEE',

         innerRadius: '60%',
         outerRadius: '100%',
         shape: 'arc'
      }
   };

   var tooltip = {
      enabled: false
   };

   var yAxis = {
      stops: [
         [0.01, '#DF5353'], // red
         [0.30, '#DF5353'], // red
         [0.35, '#DDDF0D'], // yellow
         [0.40, '#55BF3B'], // green
         [0.55, '#DDDF0D'], // yellow
         [0.75, '#DF5353'] // red
      ],
      lineWidth: 0,
      minorTickInterval: null,
      tickPixelInterval: 0,
      tickWidth: 0,
      title: {
         y: -70
      },
      labels: {
         y: 16
      },
      min: 32,
      max: 42,

   };

   var plotOptions = {
      solidgauge: {
         dataLabels: {
            y: 5,
            borderWidth: 0,
            useHTML: true
         }
      }
   };

   var credits = {
      enabled: false
   };

   var series = [{
      name: 'body temperature',
      data: [0],
      dataLabels: {
         format: '<div style = "text-align:center"><span style = "font-size:25px;color:' +
            ((Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black') +
            '">{y}</span><br/>' +
            '<span style = "font-size:12px;color:silver">°C</span></div>'
      },
      tooltip: {
         valueSuffix: ' °C'
      }
   }];

   var json = {};
   json.chart = chart;
   json.title = title;
   json.pane = pane;
   json.tooltip = tooltip;
   json.yAxis = yAxis;
   json.credits = credits;
   json.series = series;
   $('#graph_body_temperature').highcharts(json);

   var chartFunction = function() {
      var chart = $('#graph_body_temperature').highcharts();
      var point;

      $.getJSON("http://127.0.0.1:5000/data/body_temperature/", function(temperature) {
         var point = chart.series[0].points[0]
         point.y = temperature
         point.update(temperature);
      });
   };

   setInterval(chartFunction, 3000);
});