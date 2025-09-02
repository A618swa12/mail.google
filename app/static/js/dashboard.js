document.addEventListener('DOMContentLoaded', function() {
    const canvas = document.getElementById('statusChart');
    const ctx = canvas.getContext('2d');
    const successCount = parseInt(canvas.dataset.success);
    const failCount = parseInt(canvas.dataset.fail);

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Success', 'Fail'],
            datasets: [{
                label: 'Submissions',
                data: [successCount, failCount],
                backgroundColor: ['rgba(26,115,232,0.7)', 'rgba(234,67,53,0.7)'],
                borderColor: ['rgba(26,115,232,1)', 'rgba(234,67,53,1)'],
                borderWidth: 1
            }]
        },
        options: { scales: { y: { beginAtZero: true } } }
    });
});