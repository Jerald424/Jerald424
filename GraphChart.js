import React, { useEffect } from "react";
import { Chart } from "react-charts";

export default function ChartData({ inputData }) {
  console.log(inputData, "the chart page final data");
  const performance = inputData?.map((res) => res.performance);
  console.log(performance, "the performance");
  useEffect(() => {}, [performance]);
  const data = React.useMemo(() => [
    {
      label: "Series 1",
      data: [
        [0, 7],
        [1, 3],
        [2, 5],
        [3, 7],
      ],
    },
  ]);
  const axes = React.useMemo(
    () => [
      { primary: true, type: "linear", position: "bottom" },
      { type: "linear", position: "left" },
    ],
    []
  );
  const series = React.useMemo(
    () => ({
      type: "line",
    }),
    []
  );
  return (
    <div>
      <div
        style={{
          width: "400px",
          height: "300px",
        }}>
        <Chart data={data} axes={axes} tooltip series={series} />
      </div>
    </div>
  );
}
