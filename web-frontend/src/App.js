import { useState } from "react";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  LineElement,
  PointElement,
} from "chart.js";
import { Bar, Line } from "react-chartjs-2";

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  LineElement,
  PointElement
);

function App() {
  const [summary, setSummary] = useState(null);

  const uploadCSV = async (e) => {
    const form = new FormData();
    form.append("file", e.target.files[0]);

    const res = await fetch("http://127.0.0.1:8000/api/upload/", {
      method: "POST",
      body: form,
    });

    const data = await res.json();
    setSummary(data);
  };

  return (
    <div style={{ padding: 30, fontFamily: "Arial, sans-serif" }}>
      <h1 style={{ textAlign: "center", marginBottom: 20 }}>
        Chemical Equipment Visualizer
      </h1>

      <div style={{ textAlign: "center", marginBottom: 30 }}>
        <input type="file" onChange={uploadCSV} />
      </div>

      {summary && (
        <>
          {/* SUMMARY CARDS */}
          <div
            style={{
              display: "flex",
              justifyContent: "space-around",
              flexWrap: "wrap",
              marginBottom: 40,
            }}
          >
            <SummaryCard
              title="Total Equipment"
              value={summary.total_equipment}
            />
            <SummaryCard
              title="Avg Flowrate"
              value={summary.avg_flowrate.toFixed(2)}
            />
            <SummaryCard
              title="Avg Pressure"
              value={summary.avg_pressure.toFixed(2)}
            />
            <SummaryCard
              title="Avg Temperature"
              value={summary.avg_temperature.toFixed(2)}
            />
          </div>

          {/* CHART 1 */}
          <Section title="Equipment Type Distribution">
            <Bar
              data={{
                labels: Object.keys(summary.type_distribution),
                datasets: [
                  {
                    label: "Count",
                    data: Object.values(summary.type_distribution),
                    backgroundColor: "rgba(54, 162, 235, 0.6)",
                    borderColor: "rgba(54, 162, 235, 1)",
                    borderWidth: 2,
                  },
                ],
              }}
            />
          </Section>

          {/* CHART 2 */}
          <Section title="Average Flowrate by Equipment Type">
            <Bar
              data={{
                labels: Object.keys(summary.avg_flowrate_by_type),
                datasets: [
                  {
                    label: "Flowrate",
                    data: Object.values(summary.avg_flowrate_by_type),
                    backgroundColor: "rgba(54, 162, 235, 0.6)",
                    borderColor: "rgba(54, 162, 235, 1)",
                    borderWidth: 2,
                  },
                ],
              }}
            />
          </Section>

          {/* CHART 3 */}
          <Section title="Average Pressure by Equipment Type">
            <Line
              data={{
                labels: Object.keys(summary.avg_pressure_by_type),
                datasets: [
                  {
                    label: "Pressure",
                    data: Object.values(summary.avg_pressure_by_type),
                    borderColor: "rgba(54, 162, 235, 1)",
                    backgroundColor: "rgba(54, 162, 235, 0.3)",
                    tension: 0.3,
                  },
                ],
              }}
            />
          </Section>

          {/* CHART 4 */}
          <Section title="Average Temperature by Equipment Type">
            <Line
              data={{
                labels: Object.keys(summary.avg_temperature_by_type),
                datasets: [
                  {
                    label: "Temperature",
                    data: Object.values(summary.avg_temperature_by_type),
                    borderColor: "rgba(54, 162, 235, 1)",
                    backgroundColor: "rgba(54, 162, 235, 0.3)",
                    tension: 0.3,
                  },
                ],
              }}
            />
          </Section>
        </>
      )}
    </div>
  );
}

/* ---------- Helper Components ---------- */

function SummaryCard({ title, value }) {
  return (
    <div
      style={{
        padding: 20,
        width: 220,
        margin: 10,
        background: "#f4f8ff",
        borderRadius: 12,
        textAlign: "center",
        boxShadow: "0 4px 10px rgba(0,0,0,0.1)",
      }}
    >
      <h3 style={{ marginBottom: 10 }}>{title}</h3>
      <p style={{ fontSize: 24, fontWeight: "bold", color: "#1e88e5" }}>
        {value}
      </p>
    </div>
  );
}

function Section({ title, children }) {
  return (
    <div style={{ marginBottom: 50 }}>
      <h2 style={{ marginBottom: 15 }}>{title}</h2>
      {children}
    </div>
  );
}

export default App;
