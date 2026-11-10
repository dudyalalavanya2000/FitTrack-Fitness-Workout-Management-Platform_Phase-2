
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { ToastContainer } from "react-toastify";

import Sidebar from "./components/Sidebar";
import Navbar from "./components/Navbar";
import ProtectedRoute from "./components/ProtectedRoute";

import Login from "./pages/Login";
import Register from "./pages/Register";
import Dashboard from "./pages/Dashboard";
import Workouts from "./pages/Workouts";
import Progress from "./pages/Progress";
import Goals from "./pages/Goals";
import Reports from "./pages/Reports";
import Notifications from "./pages/Notifications";

import "react-toastify/dist/ReactToastify.css";

function AppLayout() {
  return (
    <div className="app-layout">
      <Sidebar />

      <div className="main-section">
        <Navbar />

        <main className="main-content">
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/workouts" element={<Workouts />} />
            <Route path="/progress" element={<Progress />} />
            <Route path="/goals" element={<Goals />} />
            <Route path="/reports" element={<Reports />} />
            <Route path="/notifications" element={<Notifications />} />

            <Route path="*" element={<Navigate to="/" replace />} />
          </Routes>
        </main>
      </div>
    </div>
  );
}

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />

        <Route element={<ProtectedRoute />}>
          <Route path="/*" element={<AppLayout />} />
        </Route>
      </Routes>

      <ToastContainer position="top-right" autoClose={3000} />
    </BrowserRouter>
  );
}

export default App;
