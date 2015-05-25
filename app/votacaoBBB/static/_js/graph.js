var executaD3 = function (d3, dataset) {
  'use strict';

  var width = 260;
  var height = 260;
  var heightViewport = 191;
  var radius = Math.min(width, height) / 2;
  var donutWidth = 40;

  /*
   * Cheching initial votes
   */
  if (dataset[0].count === 0 && dataset[1].count === 0) {
    dataset[0].count = 1;
    dataset[1].count = 1;
  }

  var color = d3.scale.ordinal()
    .range(['#ff9516', '#c6c6c6']);

  var svg = d3.select('#donutchart')
    .append('svg')
    .attr('width', width)
    .attr('height', heightViewport)
    .append('g')
    .attr('transform', 'translate(' + (width / 2) +
      ',' + (height / 2) + ')');

  var arc = d3.svg.arc()
    .innerRadius(radius - donutWidth)
    .outerRadius(radius);

  var pie = d3.layout.pie()
    .value(function (d) { return d.count; })
    .startAngle(-135 * (Math.PI / 180))
    .endAngle(135 * (Math.PI / 180))
    .padAngle(Math.PI / 180)
    .sort(null);

  svg.selectAll('path')
    .data(pie(dataset))
    .enter()
    .append('path')
    .attr('d', arc)
    .attr('fill', function (d) {
      return color(d.data.label);
    });

};

var putPercentuals = function (dataset) {
  var percentual1 = 50;
  var percentual2 = 50;
  if (!(dataset[0].count === 0 && dataset[1].count === 0)) {
    percentual1 = Math.floor((dataset[0].count / (dataset[0].count + dataset[1].count) * 100));
    percentual2 = 100 - percentual1;
  }
  if (percentual1 === 0) {
    document.getElementById('percentual2').classList.add('percentualCenter');
    document.getElementById('percentual2').innerHTML = "100%";
  } else if (percentual2 === 0) {
    document.getElementById('percentual1').classList.add('percentualCenter');
    document.getElementById('percentual1').innerHTML = "100%";
  } else {
    document.getElementById('percentual1').innerHTML = percentual1 + "%";
    document.getElementById('percentual2').innerHTML = percentual2 + "%";
  }

};

executaD3(window.d3, dataset);
putPercentuals(dataset);