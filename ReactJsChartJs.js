import React from "react";
import { Doughnut, Bar } from "react-chartjs-2";
import {
  Chart,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";

export default function ChartData({ inputData }) {
  const performance = inputData?.map((res) => res.performance);
  const name = inputData?.map((res) => res.name);
  const data = {
    labels: name,
    datasets: [
      {
        data: performance,
        backgroundColor: ["red", "green", "yellow", "orange"],
      },
    ],
  };
  Chart.register(
    CategoryScale,
    LinearScale,
    BarElement,
    Title,
    Tooltip,
    Legend
  );
  const options = {
    responsive: true,
    plugins: {
      title: {
        display: true,
        text: "performance",
      },
    },
  };
  return (
    <div>
      <div className='status-bar w3-animate-opacity'>
        <Bar data={data} options={options} />
      </div>
    </div>
  );
}
