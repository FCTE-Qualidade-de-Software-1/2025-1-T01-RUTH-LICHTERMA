function parseDate(utcDateStr) {
  const utcDate = new Date(utcDateStr);
  utcDate.setHours(utcDate.getHours() - 3);

  return utcDate.toISOString().substring(0, 10);
}

(async () => {
  const fetchedCommits = await fetch("https://api.github.com/repos/FCTE-Qualidade-de-Software-1/2025-1-T01-RUTH-LICHTERMA/commits?per_page=100").then((res) => res.json());
  const lastCommitDate = parseDate(fetchedCommits[0].commit.author.date);
  const firstCommitDate = parseDate(fetchedCommits.at(-1).commit.author.date);
  const totalCommits = fetchedCommits.length;

  const commitsByDay = fetchedCommits.reduce((acc, curr) => {
    const date = parseDate(curr.commit.author.date);
    acc[date] ??= 0;
    acc[date]++;
    return acc;
  }, {});

  const labels = [];
  const frequencyData = [];
  for (let date = new Date(firstCommitDate); date <= new Date(lastCommitDate); date.setDate(date.getDate() + 1)) {
    const label = date.toISOString().substring(0, 10);
    const frequency = commitsByDay[label] ?? 0;

    labels.push(label.split("-").reverse().join("/"));
    frequencyData.push(frequency);
  }
  const prefixSum = frequencyData.reduce((acc, curr) => {
    acc.push((acc.at(-1) ?? 0) + curr);
    return acc;
  }, []);
  const cumulativePercent = prefixSum.map(e => (e / totalCommits) * 100);

  const cycleTimeCtx = document.getElementById('cycleTimeChart').getContext('2d');
  new Chart(cycleTimeCtx, {
    type: 'bar',
    data: {
      labels: labels,
      datasets: [
        {
          type: 'line',
          label: 'Percentil',
          data: cumulativePercent,
          borderColor: '#cfca3c',
          backgroundColor: '#cfca3c',
          yAxisID: 'y1',
          tension: 0.3,
          pointRadius: 2
        },
        {
          type: 'bar',
          label: 'Atividades entregues',
          data: frequencyData,
          backgroundColor: '#3CCF59',
          yAxisID: 'y'
        }
      ]
    },
    options: {
      responsive: true,
      plugins: {
        title: {
          display: true,
          text: 'Cycle Time',
          font: {
            size: 18
          }
        },
        tooltip: {
          mode: 'index',
          intersect: false
        },
        legend: {
          position: 'top'
        }
      },
      interaction: {
        mode: 'index',
        intersect: false
      },
      scales: {
        x: {
          title: {
            display: true,
            text: 'Cycle Time (Dias)'
          }
        },
        y: {
          type: 'linear',
          position: 'left',
          title: {
            display: true,
            text: 'Frequência'
          },
          beginAtZero: true
        },
        y1: {
          type: 'linear',
          position: 'right',
          title: {
            display: true,
            text: 'Percentil (%)'
          },
          min: 0,
          max: 100,
          grid: {
            drawOnChartArea: false
          },
          ticks: {
            callback: function (value) {
              return value + '%';
            }
          }
        }
      }
    }
  });


  const teamVelocity = prefixSum.map((curr, i, arr) => {
    const velocityBurn = 4;
    const totalNow = curr - (arr[i - velocityBurn] ?? 0);
    return totalNow / (Math.min(i, velocityBurn - 1) + 1);
  });

  const teamVelocityCtx = document.getElementById('teamVelocityChart').getContext('2d');
  new Chart(teamVelocityCtx, {
    type: 'bar',
    data: {
      labels: labels,
      datasets: [
        {
          type: 'line',
          label: 'Velocidade',
          data: teamVelocity,
          borderColor: '#cfca3c',
          backgroundColor: '#cfca3c',
          yAxisId: 'y2',
          tension: 0.3,
          pointRadius: 0
        },
        {
          type: 'bar',
          label: 'Atividades entregues',
          data: frequencyData,
          backgroundColor: '#3CCF59',
          yAxisID: 'y'
        }
      ]
    },
    options: {
      responsive: true,
      plugins: {
        title: {
          display: true,
          text: 'Team Velocity',
          font: {
            size: 18
          }
        },
        tooltip: {
          mode: 'index',
          intersect: false
        },
        legend: {
          position: 'top'
        }
      },
      interaction: {
        mode: 'index',
        intersect: false
      },
      scales: {
        x: {
          title: {
            display: true,
            text: 'Dia'
          }
        },
        y: {
          type: 'linear',
          position: 'left',
          title: {
            display: true,
            text: 'Frequência'
          },
          beginAtZero: true
        },
        y1: {
          type: 'linear',
          position: 'right',
          title: {
            display: true,
            text: 'Velocidade'
          },
          min: 0,
          max: 100,
          grid: {
            drawOnChartArea: false
          },
          ticks: {
            callback: function (value) {
              return value + '%';
            }
          }
        }
      }
    }
  });
  const cumulativeFlowCtx = document.getElementById('cumulativeFlowChart').getContext('2d');

const flowLabels = [
  "08/05", "19/05", "28/05", "03/06", "06/07", "07/07"
];

const toDoData = [5, 4, 3, 3, 2, 1, 0];
const inProgressData = [0, 1, 2, 2, 3, 3, 2];
const doneData = [0, 0, 1, 2, 3, 4, 5];

new Chart(cumulativeFlowCtx, {
  type: 'line',
  data: {
    labels: flowLabels,
    datasets: [
      {
        label: 'To Do',
        data: toDoData,
        borderColor: '#f94144',
        backgroundColor: '#f94144',
        fill: true,
        tension: 0.3
      },
      {
        label: 'In Progress',
        data: inProgressData,
        borderColor: '#f3722c',
        backgroundColor: '#f3722c',
        fill: true,
        tension: 0.3
      },
      {
        label: 'Done',
        data: doneData,
        borderColor: '#90be6d',
        backgroundColor: '#90be6d',
        fill: true,
        tension: 0.3
      }
    ]
  },
  options: {
    responsive: true,
    stacked: true,
    plugins: {
      title: { display: true, text: 'Cumulative Flow Diagram', font: { size: 18 } },
      legend: { position: 'top' }
    },
    scales: {
      y: { stacked: true, beginAtZero: true, title: { display: true, text: 'Quantidade de tarefas' } },
      x: { title: { display: true, text: 'Data' } }
    }
  }
});
})();