const options = JSON.parse(document.getElementById('options').textContent);
var myChart;

document.addEventListener('DOMContentLoaded', function () {
    myChart = Highcharts.chart('chart_div', options);
});

document.addEventListener("DOMContentLoaded", function() {
    for (current_series of myChart.series) {
        checkbox = document.getElementById(current_series.name);
        checkbox.checked = true;
    }
});

function checkboxClicked(country, token) {
    var xmlhttp = new XMLHttpRequest();
    var url = "/highcharts/checkbox_clicked";

    var checkbox = document.getElementById(country);
    var selected = checkbox.checked;

    if (selected == true) {
        var present = false;
        for (current_series of myChart.series) {
            if (current_series.name == country) {
                current_series.setVisible(true);
                present = true
            }
        }

        if (present == false) {
            var json_msg = {name:country, checked:selected};

            xmlhttp.onreadystatechange = function() {
                if (this.readyState == 4 && this.status == 200) {
                    var jsn = this.responseText;
                    newData(jsn);
                }
            };
            xmlhttp.open("POST", url, true);
            xmlhttp.setRequestHeader("X-CSRFToken", token); 
            xmlhttp.send(JSON.stringify(json_msg));
        }
    } else {
        for (current_series of myChart.series) {
            if (current_series.name == country) {
                current_series.setVisible(false);
            }
        }
    }
};

function newData(jsn) {
    const series = JSON.parse(jsn);
    var checkbox = document.getElementById(series.name);
    var selected = checkbox.checked;

    if (selected == true) {
        var present = false;

        for (const current_series of myChart.series) {
            if (current_series.name == series.name) {
                present = true;
            }
        }
        if (present == false) {
            myChart.addSeries(series, true);
        }
    }
};
