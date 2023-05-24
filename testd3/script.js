// script.js

// 在这里编写D3.js代码来创建可视化
const svg = d3.select("#visualization")
  .append("svg")
  .attr("width", 500)
  .attr("height", 300);

svg.append("circle")
  .attr("cx", 100)
  .attr("cy", 100)
  .attr("r", 50)
  .style("fill", "steelblue");