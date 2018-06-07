var someList = [];
var otu_ids = [];

function init() {
  data = [{
      x: [1, 2, 3, 4, 5],
      y: [1, 2, 4, 8, 16] }];
  var LINE = document.getElementById("plot");
  Plotly.plot(LINE, data);
}

function loadSamples() {
    d3.json("http://127.0.0.1:5000/names", function(error, data) {
        let dropdown = d3.select("#selDataset")
        for (var i=0; i < data.length;i++){
            var sampleItem = data[i];
            var nameItem = dropdown.append("option").attr("value", sampleItem).text(sampleItem);
        };
    getSamples(sampleItem)
    })
    
};
var otu_ids ;
function getSamples(sample) {
    d3.json(`http://127.0.0.1:5000/samples/${sample}`, function(error, data) {
        console.log(data)
        console.log(error)
        otu_ids = data
        getPlotly(otu_ids)
    })
};
var otu;
var samples;

function getPlotly(sample_data) {
    otu = sample_data[0]["otu_id"].slice(0,10)
    samples = sample_data[0]["sample_values"].slice(0,10)
    data = [{
        values: otu,
        type: "pie"}];
    var LINE = document.getElementById("plot");
    Plotly.plot(LINE, data);
}

function optionChanged(newSample) {
  var LINE = document.getElementById("selDataset");

  // Note the extra brackets around 'newx' and 'newy'
  Plotly.restyle(LINE, "x", [newx]);
  Plotly.restyle(LINE, "y", [newy]);
}

function updateSamplePlotly(value) {
  var PIE = document.getElementById("plot");
  Plotly.restyle(PIE, "values", [value]);
}


function getData(dataset) {

  // Initialize empty arrays to contain our axes
  var x = [];
  var y = [];

  // Fill the x and y arrays as a function of the selected dataset
  switch (dataset) {
      case "dataset1":
          x = [1, 2, 3, 4, 5];
          y = [0.1, 0.2, 0.3, 0.4, 0.5];
          break;
      case "dataset2":
          x = [10, 20, 30, 40, 50];
          y = [1, 10, 100, 1000, 10000];
          break;
      case "dataset3":
          x = [100, 200, 300, 400, 500];
          y = [10, 100, 50, 10, 0];
          break;
      default:
          x = [1, 2, 3, 4, 5];
          y = [1, 2, 3, 4, 5];
          break;
      }

  updatePlotly(x, y);
}

function optionChanged(value) {
    console.log(value);
    updateSamplePlotly(value);
    }

loadSamples();


//     var LOAD = document.getElementById("plot");
  
//     // Note the extra brackets around 'newx' and 'newy'
//     Plotly.restyle(LINE, "x", [newx]);
//     Plotly.restyle(LINE, "y", [newy]);
//   }
// init();
