const barCtx = document.getElementById("barChart");

if (barCtx) {
    new Chart(barCtx, {
        type: "bar",
        data: {
            labels: ["Python", "Java", "SQL", "HTML", "CSS", "JavaScript"],
            datasets: [{
                label: "Skill Demand",
                data: [95, 80, 85, 75, 70, 90]
            }]
        }
    });
}

const lineCtx = document.getElementById("lineChart");

if (lineCtx) {
    new Chart(lineCtx, {
        type: "line",
        data: {
            labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
            datasets: [{
                label: "Hiring Trend",
                data: [40, 55, 70, 60, 80, 95]
            }]
        }
    });
}

const pieCtx = document.getElementById("pieChart");

if (pieCtx) {
    new Chart(pieCtx, {
        type: "pie",
        data: {
            labels: ["Frontend", "Backend", "Full Stack", "Data"],
            datasets: [{
                data: [25, 30, 30, 15]
            }]
        }
    });
}

const doughnutCtx = document.getElementById("doughnutChart");

if (doughnutCtx) {
    new Chart(doughnutCtx, {
        type: "doughnut",
        data: {
            labels: ["Remote", "Hybrid", "Onsite"],
            datasets: [{
                data: [45, 35, 20]
            }]
        }
    });
}