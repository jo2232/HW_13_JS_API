d3.json("/getLastData", makeScatter)

function makeScatter(test) {
    followers = []
    sentiments = []
    //loop through each city
    for (key in test) {

        // loop through each tweet in each city
        for (var i = 0; i < test[key]['data'].bounding_box.length; i++) {
            followers.push(test[key]['data'].followers_count[i])
            sentiments.push(test[key]['data'].comp_sent[i])
        }
    }
    var data = {
        followers: followers,
        sentiments: sentiments
    }

    var trace3 = {
        x: data.followers,
        y: data.sentiments,
        mode: 'markers'
    };

    var data = [trace3];
    console.log(data)
    var layout = {
        plot_bgcolor: "#424242",
        paper_bgcolor: "#424242",
        font: {
            size: 18,
            color: '#000000'
          },
          xaxis: {
            title: 'Number of Followers',
            gridcolor: '#bdbdbd',
            gridwidth: 2,
            zerolinecolor: '#969696',
          },
          yaxis: {
            title: 'Tweet Sentiment',
            gridcolor: '#bdbdbd',
            gridwidth: 1,
            zerolinecolor: '#969696',
          }
    
    };
    Plotly.newPlot('scatter', data, layout);
}