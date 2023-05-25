const chart = {
  // Configuration options
  width: 1000,
  height: 100,

  // Data for the chart
  data: [10, 20, 30, 40, 50],

  // Function to initialize and render the chart
  render: function() {
    const self = this;

    // Create SVG container
    const svg = d3.create("svg")
      .attr("width", this.width)
      .attr("height", this.height);

    // Create rectangles based on data
    const rects = svg.selectAll("rect")
      .data(this.data)
      .join("rect")
      .attr("x", (d, i) => i * 50)
      .attr("y", (d) => this.height - d)
      .attr("width", 40)
      .attr("height", (d) => d)
      .attr("fill", "steelblue");

    // Add interactivity to rectangles
    rects.on("mouseover", function(d, i) {
        d3.select(this)
          .attr("fill", "orange");
      })
      .on("mouseout", function(d, i) {
        d3.select(this)
          .attr("fill", "steelblue");
      })
      .on("click", function(d, i) {
        // Update data on click
        self.updateData();
        // Re-render the chart
        self.render();
      });

    // Append SVG to a target element with id "vis"
    d3.select("#map").node().appendChild(svg.node());
  },

  // Function to update the data
  updateData: function() {
    // Generate random data
    this.data = Array.from({ length: 5 }, () => Math.floor(Math.random() * 50) + 10);
  }
};

// Call the render function to generate the initial chart
chart.render();
