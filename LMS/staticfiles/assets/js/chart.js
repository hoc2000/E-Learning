document.addEventListener('DOMContentLoaded', () => {
    const ctx1 = document.getElementById('myChart').getContext('2d');
    const ctx2 = document.getElementById('myChart2').getContext('2d');

    // Sample data
    // const DataCoursePublish = {{ data_course_publish | safe}};
    // const DataCOurseDraft = {{ data_course_draft | safe}}
    const monthNames = ["January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"];

    let ZeroValMonthPuB = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    let ZeroValMonthD = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    let monthLabel = []
    let PcourseCount
    let DCourseCount = []
    console.log(DataCoursePublish);
    console.log(DataCOurseDraft);
    // Parse the dates to JS
    DataCoursePublish.forEach((d) => {
        ZeroValMonthPuB[d.date - 1] = d.y;
        PcourseCount = ZeroValMonthPuB
    });

    DataCOurseDraft.forEach((d) => {
        ZeroValMonthD[d.date2 - 1] = d.y;
        DCourseCount = ZeroValMonthD
    });
    console.log(monthLabel)

    // Render the chart
    let chart = new Chart(ctx1, {
        type: "bar",


        data: {
            labels: monthNames,
            datasets: [
                {
                    label: "Courses Publish",
                    backgroundColor: "#79AEC8",
                    borderColor: "#417690",
                    data: PcourseCount,
                },
                {
                    label: "Courses Draft",
                    backgroundColor: "#00FF00",
                    borderColor: "#00FF00",
                    data: DCourseCount,
                }
            ]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            },
            title: {
                text: "Monthly Statistics ",
                display: true
            }
        },
    });

    let chart2 = new Chart(ctx1, {
        type: "doughnut",


        data: {
            labels: monthNames,
            datasets: [
                {
                    label: "Courses Publish",
                    backgroundColor: "#79AEC8",
                    borderColor: "#417690",
                    data: PcourseCount,
                },
            ]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            },
            title: {
                text: "Monthly Statistics ",
                display: true
            }
        },
    });
});