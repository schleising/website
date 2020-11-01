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

function checkboxClicked(country) {
    var xmlhttp = new XMLHttpRequest();

    var checkbox = document.getElementById(country);
    var selected = checkbox.checked;
    var baseUrl = new URL(window.location.href);
    var url = new URL("/highcharts/checkbox_clicked", baseUrl.origin);
    url.searchParams.append("country", country);

    if (selected == true) {
        var present = false;
        for (current_series of myChart.series) {
            if (current_series.name == country) {
                current_series.setVisible(true);
                present = true
            }
        }

        if (present == false) {
            xmlhttp.onreadystatechange = function() {
                if (this.readyState == 4 && this.status == 200) {
                    var jsn = this.responseText;
                    newData(jsn);
                }
            };
            xmlhttp.open("GET", url, true);
            xmlhttp.send();
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
