var executaD3 = function(d3, dataset) {
        'use strict';

/*        var dataset = [
          { label: 'Participante 1', count: 55 }, 
          { label: 'Participante 2', count: 35 }
        ];*/

        var width = 260;
        var height = 260;
        var heightViewport = 191;
        var radius = Math.min(width, height) / 2;
        var donutWidth = 40

        var color = d3.scale.ordinal()
          .range(['#ff9516','#c6c6c6']);

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
          .value(function(d) { return d.count; })
          .startAngle(-135 * (Math.PI/180))
          .endAngle(135 * (Math.PI/180))
          .padAngle(1 * (Math.PI/180))
          .sort(null);

        var path = svg.selectAll('path')
          .data(pie(dataset))
          .enter()
          .append('path')
          .attr('d', arc)
          .attr('fill', function(d, i) { 
            return color(d.data.label);
          });

      };

executaD3(window.d3, dataset);