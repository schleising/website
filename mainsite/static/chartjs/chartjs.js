var ctx = document.getElementById('chart_canvas').getContext('2d');
const chart = JSON.parse(document.getElementById('chart').textContent);
var myChart = new Chart(ctx, chart);

for (dataset of myChart.data.datasets) {
    checkbox = document.getElementById(dataset.label);
    checkbox.checked = true;
}

function checkboxClicked(country) {
    var xmlhttp = new XMLHttpRequest();

    var checkbox = document.getElementById(country);
    var selected = checkbox.checked;
    var baseUrl = new URL(window.location.href);
    var url = new URL("/chartjs/checkbox_clicked", baseUrl.origin);
    url.searchParams.append("country", country);

    if (selected == true) {
        var present = false;
        for (dataset of myChart.data.datasets) {
            if (dataset.label == country) {
                dataset.showLine = true;
                myChart.update();
                present = true;
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
        for (dataset of myChart.data.datasets) {
            if (dataset.label == country) {
                dataset.showLine = false;
                myChart.update();
            }
        }
    }
};

function newData(jsn) {
    const dataset = JSON.parse(jsn);
    console.log(dataset.label);
    var checkbox = document.getElementById(dataset.label);
    var selected = checkbox.checked;

    if (selected == true) {
        var present = false;

        for (const current_dataset of myChart.data.datasets) {
            if (current_dataset.label == dataset.label) {
                present = true;
            }
        }
        if (present == false) {
            myChart.data.datasets.push(dataset);
            myChart.update();
        }
    }
};
