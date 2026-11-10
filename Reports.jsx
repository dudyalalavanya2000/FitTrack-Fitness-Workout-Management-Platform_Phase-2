import { useEffect, useState } from "react";
import {
  BarChart3,
  Activity,
  Flame,
  Clock,
  CalendarDays,
  Target,
  Scale,
  RefreshCw,
} from "lucide-react";
import { toast } from "react-toastify";
import api from "../services/api";

function formatDate(value) {
  if (!value) return "-";

  const date = new Date(`${String(value).slice(0, 10)}T00:00:00`);

  return Number.isNaN(date.getTime())
    ? value
    : date.toLocaleDateString();
}

function Reports() {
  const [summary, setSummary] = useState(null);
  const [daily, setDaily] = useState([]);
  const [weekly, setWeekly] = useState([]);
  const [progress, setProgress] = useState([]);
  const [goals, setGoals] = useState([]);
  const [goalSummary, setGoalSummary] = useState(null);
  const [loading, setLoading] = useState(true);

  const fetchReports = async () => {
    setLoading(true);

    try {
      const results = await Promise.allSettled([
        api.get("/reports/summary"),
        api.get("/reports/daily"),
        api.get("/reports/weekly"),
        api.get("/reports/progress"),
        api.get("/reports/goals"),
      ]);

      const failed = results.filter(
        (result) => result.status === "rejected"
      );

      if (failed.length === results.length) {
        throw failed[0].reason;
      }

      const [summaryResult, dailyResult, weeklyResult, progressResult, goalsResult] =
        results;

      if (summaryResult.status === "fulfilled") {
        setSummary(summaryResult.value.data);
      }

      if (dailyResult.status === "fulfilled") {
        setDaily(dailyResult.value.data.daily_reports || []);
      }

      if (weeklyResult.status === "fulfilled") {
        setWeekly(weeklyResult.value.data.weekly_reports || []);
      }

      if (progressResult.status === "fulfilled") {
        setProgress(progressResult.value.data.progress_reports || []);
      }

      if (goalsResult.status === "fulfilled") {
        setGoals(goalsResult.value.data.goals || []);
        setGoalSummary(goalsResult.value.data.goal_summary || null);
      }

      if (failed.length > 0) {
        toast.warning(
          "Some report sections could not be loaded. Please check the reports APIs."
        );
      }
    } catch (error) {
      toast.error(
        error.response?.data?.detail || "Unable to load reports."
      );
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchReports();
  }, []);

  const fitness = summary?.fitness_summary || {};

  const totalWorkouts = Number(fitness.total_workouts || 0);
  const totalMinutes = Number(
    fitness.total_workout_duration_minutes || 0
  );
  const totalCalories = Number(fitness.total_calories_burned || 0);

  const latestWeight =
    progress.length > 0
      ? progress[0].weight_kg
      : null;

  const maxWeeklyMinutes = Math.max(
    1,
    ...weekly.map((item) => Number(item.total_duration_minutes || 0))
  );

  return (
    <div className="page-content">
      <div className="page-heading">
        <div>
          <p className="section-label">FITNESS INSIGHTS</p>
          <h1>Reports & Analytics</h1>
          <p className="page-description">
            Review your workout activity and fitness progress.
          </p>
        </div>

        <button
          className="primary-button reports-refresh-button"
          onClick={fetchReports}
          disabled={loading}
        >
          <RefreshCw size={17} />
          {loading ? "Loading..." : "Refresh Reports"}
        </button>
      </div>

      <div className="reports-stats">
        <div className="report-stat-card">
          <div className="report-stat-icon purple">
            <Activity size={22} />
          </div>
          <div>
            <p>Total Workouts</p>
            <h2>{totalWorkouts}</h2>
          </div>
        </div>

        <div className="report-stat-card">
          <div className="report-stat-icon blue">
            <Clock size={22} />
          </div>
          <div>
            <p>Workout Duration</p>
            <h2>{totalMinutes} min</h2>
          </div>
        </div>

        <div className="report-stat-card">
          <div className="report-stat-icon orange">
            <Flame size={22} />
          </div>
          <div>
            <p>Calories Burned</p>
            <h2>{totalCalories.toLocaleString()}</h2>
          </div>
        </div>

        <div className="report-stat-card">
          <div className="report-stat-icon green">
            <Scale size={22} />
          </div>
          <div>
            <p>Latest Recorded Weight</p>
            <h2>
              {latestWeight != null ? `${latestWeight} kg` : "--"}
            </h2>
          </div>
        </div>
      </div>

      {loading ? (
        <div className="content-card">
          <p className="empty-message">Loading your fitness reports...</p>
        </div>
      ) : (
        <>
          <div className="reports-grid">
            <div className="content-card report-panel">
              <div className="card-heading">
                <div>
                  <h2>Weekly Workout Activity</h2>
                  <p>{weekly.length} weekly records</p>
                </div>
                <BarChart3 size={22} />
              </div>

              {weekly.length === 0 ? (
                <p className="empty-message">
                  No weekly workout data available.
                </p>
              ) : (
                <div className="weekly-chart">
                  {weekly.map((item, index) => {
                    const minutes = Number(
                      item.total_duration_minutes || 0
                    );
                    const width = Math.max(
                      3,
                      (minutes / maxWeeklyMinutes) * 100
                    );

                    return (
                      <div className="weekly-chart-row" key={item.week || index}>
                        <div className="weekly-chart-label">
                          <strong>{item.week || `Week ${index + 1}`}</strong>
                          <span>
                            {formatDate(item.week_start)} –{" "}
                            {formatDate(item.week_end)}
                          </span>
                        </div>

                        <div className="weekly-bar-track">
                          <div
                            className="weekly-bar"
                            style={{ width: `${width}%` }}
                          />
                        </div>

                        <div className="weekly-chart-value">
                          {minutes} min
                        </div>
                      </div>
                    );
                  })}
                </div>
              )}
            </div>

            <div className="content-card report-panel">
              <div className="card-heading">
                <div>
                  <h2>Goal Overview</h2>
                  <p>Your fitness goal summary</p>
                </div>
                <Target size={22} />
              </div>

              {goalSummary && (
                <div className="goal-summary-values">
                  {Object.entries(goalSummary).map(([key, value]) => (
                    <div className="goal-summary-item" key={key}>
                      <span>
                        {key.replaceAll("_", " ")}
                      </span>
                      <strong>
                        {typeof value === "object"
                          ? JSON.stringify(value)
                          : String(value ?? "-")}
                      </strong>
                    </div>
                  ))}
                </div>
              )}

              {goals.length === 0 ? (
                <p className="empty-message">No goal records available.</p>
              ) : (
                <div className="report-goal-list">
                  {goals.map((goal) => (
                    <div className="report-goal-item" key={goal.id}>
                      <div>
                        <strong>{goal.title || goal.name || "Fitness Goal"}</strong>
                        <span>
                          {goal.status || goal.goal_status || "Goal"}
                        </span>
                      </div>
                      <span className="report-goal-target">
                        {goal.target_value != null
                          ? `Target: ${goal.target_value}`
                          : ""}
                      </span>
                    </div>
                  ))}
                </div>
              )}
            </div>
          </div>

          <div className="content-card report-table-card">
            <div className="card-heading">
              <div>
                <h2>Daily Activity Report</h2>
                <p>{daily.length} daily records</p>
              </div>
              <CalendarDays size={22} />
            </div>

            {daily.length === 0 ? (
              <p className="empty-message">
                No daily activity records available.
              </p>
            ) : (
              <div className="table-wrapper">
                <table className="workout-table">
                  <thead>
                    <tr>
                      <th>Date</th>
                      <th>Workouts</th>
                      <th>Duration</th>
                      <th>Calories Burned</th>
                      <th>Calories Consumed</th>
                      <th>Water Intake</th>
                      <th>Exercise</th>
                      <th>Weight</th>
                    </tr>
                  </thead>
                  <tbody>
                    {daily.map((item, index) => (
                      <tr key={item.date || index}>
                        <td>{formatDate(item.date)}</td>
                        <td>{item.workout_count ?? 0}</td>
                        <td>{item.workout_duration_minutes ?? 0} min</td>
                        <td>{item.calories_burned ?? 0} kcal</td>
                        <td>{item.calories_consumed ?? 0} kcal</td>
                        <td>{item.water_intake_ml ?? 0} ml</td>
                        <td>{item.progress_exercise_minutes ?? 0} min</td>
                        <td>
                          {item.weight_kg != null
                            ? `${item.weight_kg} kg`
                            : "-"}
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            )}
          </div>

          <div className="content-card report-table-card">
            <div className="card-heading">
              <div>
                <h2>Weight & Progress History</h2>
                <p>{progress.length} progress records</p>
              </div>
              <Scale size={22} />
            </div>

            {progress.length === 0 ? (
              <p className="empty-message">
                No progress history available.
              </p>
            ) : (
              <div className="table-wrapper">
                <table className="workout-table">
                  <thead>
                    <tr>
                      <th>Date</th>
                      <th>Weight</th>
                      <th>Calories Consumed</th>
                      <th>Water Intake</th>
                      <th>Exercise</th>
                      <th>Notes</th>
                    </tr>
                  </thead>
                  <tbody>
                    {progress.map((item, index) => (
                      <tr key={item.id || index}>
                        <td>{formatDate(item.date)}</td>
                        <td>
                          {item.weight_kg != null
                            ? `${item.weight_kg} kg`
                            : "-"}
                        </td>
                        <td>{item.calories_consumed ?? 0} kcal</td>
                        <td>{item.water_intake_ml ?? 0} ml</td>
                        <td>{item.exercise_minutes ?? 0} min</td>
                        <td>{item.notes || "-"}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            )}
          </div>
        </>
      )}
    </div>
  );
}

export default Reports;