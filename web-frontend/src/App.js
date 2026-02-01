import { useState } from "react";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
} from "chart.js";
import { Bar } from "react-chartjs-2";

ChartJS.register(CategoryScale, LinearScale, BarElement);

function App() {
  const [summary, setSummary] = useState(null);

  const uploadCSV = async (e) => {
    const form = new FormData();
    form.append("file", e.target.files[0]);

    const res = await fetch("http://127.0.0.1:8000/api/upload/", {
      method: "POST",
      headers: {
        "Authorization": "Basic " + btoa("admin:password"),
      },
      body: form,
    });

    setSummary(await res.json());
  };

  return (
    <div>
      <h2>Chemical Equipment Visualizer</h2>
      <input type="file" onChange={uploadCSV} />

      {summary && (
        <Bar
          data={{
            labels: Object.keys(summary.type_distribution),
            datasets: [{
              label: "Equipment Count",
              data: Object.values(summary.type_distribution),
            }],
          }}
        />
      )}
    </div>
  );
}

export default App;
