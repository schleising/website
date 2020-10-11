function drawMap(gjf, graduations) {
    var mymap = L.map('mapid').setView([54.003644, -2.547859], 5);

    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        id: 'mapbox/streets-v11',
        tileSize: 512,
        zoomOffset: -1,
        accessToken: 'pk.eyJ1Ijoic3NjaGxlaXNpbmciLCJhIjoiY2tmdHA1b2huMG04YjJyczhkcmdtNG9haiJ9.NEp_uyjkvxE-_eEEvzi9zQ'
    }).addTo(mymap);

    geojson = L.geoJson(gjf, {
        style: style,
        onEachFeature: onEachFeature
    }).addTo(mymap);

    var info = L.control();

    info.onAdd = function (map) {
        this._div = L.DomUtil.create('div', 'info'); // create a div with a class "info"
        this.update();
        return this._div;
    };

    // method that we will use to update the control based on feature properties passed
    info.update = function (props) {
        this._div.innerHTML = '<h4>Upper Tier Local Authority</h4>' +  (props ?
            `<b>${props.ctyua19nm}</b><br/><b style="color: dodgerblue">${props.cumCasesByPublishDate}</b> Cases<br/><b style="color: dodgerblue">${props.ConfPerCap.toFixed(0)}</b> Cases per 100,000 People<br/>Last Updated on <b style="color: dodgerblue">${props.date}</b>`
            : 'Tap or Hover over an Upper Tier Unitary Authority');
    };

    info.addTo(mymap);

    // var legend = L.control({position: 'bottomright'});

    // legend.onAdd = function (map) {

    //     var div = L.DomUtil.create('div', 'info legend'),
    //         grades = [0, 10, 20, 50, 100, 200, 500, 1000],
    //         labels = [];

    //     // loop through our density intervals and generate a label with a colored square for each interval
    //     for (var i = 0; i < grades.length; i++) {
    //         div.innerHTML +=
    //             '<i style="background:' + getColor(grades[i] + 1) + '"></i> ' +
    //             grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1] + '<br>' : '+');
    //     }

    //     return div;
    // };

    // legend.addTo(mymap);

    function getColor(d) {
        return d > graduations[6] ? '#08519c' :
               d > graduations[5] ? '#08519c' :
               d > graduations[4] ? '#3182bd' :
               d > graduations[3] ? '#6baed6' :
               d > graduations[2] ? '#9ecae1' :
               d > graduations[1] ? '#c6dbef' :
               d > graduations[0] ? '#eff3ff' : '#eff3ff';
    }

    function style(feature) {
        return {
            fillColor: getColor(feature.properties.ConfPerCap),
            weight: 1,
            opacity: 1,
            color: 'blue',
            dashArray: '3',
            fillOpacity: 0.7
        };
    }

    function highlightFeature(e) {
        var layer = e.target;

        layer.setStyle({
            weight: 2,
            color: 'blue',
            dashArray: '',
            fillOpacity: 0.7
        });

        if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
            layer.bringToFront();
        }

        info.update(layer.feature.properties);
    }

    function resetHighlight(e) {
        geojson.resetStyle(e.target);
        info.update();
    }

    function zoomToFeature(e) {
        mymap.fitBounds(e.target.getBounds());
    }

    function onEachFeature(feature, layer) {
        layer.on({
            mouseover: highlightFeature,
            mouseout: resetHighlight,
            click: zoomToFeature
        });
    }
}

const geojsonFeature = JSON.parse(document.getElementById('geo_data').textContent);
const graduations    = JSON.parse(document.getElementById('graduations').textContent);

drawMap(geojsonFeature, graduations);
