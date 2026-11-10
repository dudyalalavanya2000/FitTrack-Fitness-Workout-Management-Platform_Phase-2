# FitTrack – Fitness & Workout Management Platform

## Overview

FitTrack is a full-stack fitness and workout management application developed using **FastAPI, React, and SQLite**.

The platform helps users manage workouts, track daily fitness progress, set personal fitness goals, monitor performance through reports, schedule workouts, explore exercises, maintain workout streaks, earn achievement badges, and access a personalized fitness dashboard.

The project demonstrates full-stack application development, REST API integration, JWT authentication, database management, and data visualization.

## Project Objectives

- Provide secure user registration and login.
- Allow users to manage their workout activities.
- Track daily fitness progress and health-related activity metrics.
- Create and manage personal fitness goals.
- Generate fitness reports and analytics.
- Schedule workouts in advance.
- Provide an exercise library with search and filtering.
- Track workout consistency through streaks.
- Reward users with achievement badges.
- Provide a personalized fitness dashboard.
- Notify users about workout activities and fitness reminders.

## Technology Stack

### Backend
- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- JWT Authentication
- Bcrypt Password Hashing
- Uvicorn

### Frontend
- React.js
- Vite
- JavaScript
- HTML5
- CSS3
- Axios
- React Router DOM
- React Toastify
- Lucide React

## Project Modules

# PHASE 1: FITNESS TRACKING PLATFORM

### Module 1: User Authentication

Implemented secure user account management.

**Features:**
- User registration.
- User login.
- JWT-based authentication.
- Password hashing using bcrypt.
- Protected routes.
- Token storage using browser localStorage.

### Module 2: Workout Management

Allows users to manage their fitness activities.

**Features:**
- Add new workouts.
- View workout history.
- Edit existing workouts.
- Delete workouts.
- Track workout duration.
- Record calories burned.
- Categorize workout activities.

### Module 3: Daily Progress Tracking

Allows users to monitor their daily fitness activities.

**Features:**
- Record daily weight.
- Track calories consumed.
- Track water intake.
- Record exercise duration.
- View daily progress history.
- Update and delete progress records.
- Prevent duplicate daily progress entries.

### Module 4: Fitness Goal Management

Allows users to create and monitor personal fitness goals.

**Features:**
- Create fitness goals.
- Set target and current values.
- Define start and target dates.
- Track goal completion percentage.
- Update goal progress.
- Mark goals as completed.
- Reopen or delete goals.

### Module 5: Reports & Analytics

Provides insights into fitness performance.

**Features:**
- Fitness summary.
- Daily workout reports.
- Weekly workout summaries.
- Workout duration analysis.
- Calories burned tracking.
- Weight progress history.
- Fitness goal summaries.
- Goal completion statistics.

### Module 6: Notifications System

Keeps users informed about their fitness activities.

**Features:**
- Display notifications.
- Show unread notification count.
- Mark individual notifications as read.
- Mark all notifications as read.
- Delete notifications.
- Generate daily fitness reminders.
- Automatically generate workout-related notifications.
- Generate notifications when goals are completed.

---

# PHASE 2: ADVANCED TRACKING & USER ENGAGEMENT

Phase 2 enhances FitTrack with advanced tracking, workout scheduling, personalization, and motivational features to help users maintain consistent fitness habits.

### Module 7: Workout Plans & Scheduling

**Objective:** Allow users to plan workouts in advance.

**Features:**
- Create workout plans.
- Schedule workouts for future dates.
- View all scheduled workout plans.
- View upcoming workouts.
- Retrieve individual workout plans.
- Update workout schedules.
- Delete workout plans.
- Generate workout scheduling notifications.

**API Prefix:** `/api/v1/workout-plans/`

### Module 8: Exercise Library

**Objective:** Provide an exercise library for users.

**Features:**
- Add new exercises.
- View available exercises.
- Categorize exercises into Cardio, Strength, and Yoga.
- Search exercises by name.
- Filter exercises by category.
- Add exercises to workouts.
- View exercises associated with workouts.
- Update and delete exercises.

**API Prefix:** `/api/v1/exercises/`

### Module 9: Progress Comparison

**Objective:** Allow users to compare fitness performance over time.

**Features:**
- Compare weekly workout performance.
- Generate monthly fitness statistics.
- Analyze workout duration.
- Track calories burned.
- Monitor weight progress.
- Generate daily progress reports.
- Display fitness improvement trends.
- Analyze goal completion statistics.

**API Prefix:** `/api/v1/reports/`

### Module 10: Streak Tracking System

**Objective:** Encourage users to maintain consistent workout habits.

**Features:**
- Track daily workout streaks.
- Calculate current workout streak.
- Maintain longest workout streak.
- Automatically recalculate streaks.
- Reset current streak when workout days are missed.
- Display workout streak statistics.
- Update streak information when workouts change.

**API Prefix:** `/api/v1/streaks/`

### Module 11: Achievement Badges

**Objective:** Motivate users by rewarding fitness milestones.

**Features:**
- Create default achievement badges.
- Award badges for completing the first workout.
- Award badges for maintaining a 3-day streak.
- Award badges for maintaining a 7-day streak.
- Award badges for completing 10 workouts.
- Award badges for completing fitness goals.
- Prevent duplicate badge awards.
- View all available badges.
- View badges earned by individual users.

**API Prefix:** `/api/v1/badges/`

### Module 12: Personalized Dashboard

**Objective:** Provide users with a personalized overview of their fitness activities.

**Features:**
- Display daily workout summary.
- Show total workout duration.
- Display total calories burned.
- Show daily fitness progress.
- Display upcoming workout schedules.
- Track fitness goal progress percentages.
- Display current workout streak.
- Display longest workout streak.
- Show earned achievement badges.
- Retrieve user-specific dashboard information.

**API Prefix:** `/api/v1/dashboard/`

---

## Database Tables

The application uses SQLite with SQLAlchemy ORM.

### Phase 1 – Existing Tables

| Table | Description |
|---|---|
| Users | Stores user account information |
| Workouts | Stores workout activities |
| Progress | Stores daily fitness progress |
| Goals | Stores personal fitness goals |
| Notifications | Stores user notifications |

### Phase 2 – Additional Tables

| Table | Description |
|---|---|
| Workout_Plans | Stores scheduled workout plans |
| Exercises | Stores exercise library information |
| Workout_Exercises | Connects exercises with workouts |
| Streaks | Stores workout streak information |
| Badges | Stores achievement badge definitions |
| User_Badges | Stores badges earned by users |

The database maintains user-specific records and relationships between users and their fitness activities.

## Security Features

- JWT-based authentication.
- Bcrypt password hashing.
- Protected API endpoints.
- User ownership validation.
- Pydantic request and response validation.
- Environment-based configuration.
- CORS configuration for frontend-backend integration.
- Database uniqueness constraints to prevent duplicate records.
- User-specific data access and authorization.

## Project Structure

```text
FitTrack/
│
├── backend/
│   ├── app/
│   │   ├── auth/
│   │   ├── routes/
│   │   │   ├── auth.py
│   │   │   ├── workouts.py
│   │   │   ├── progress.py
│   │   │   ├── goals.py
│   │   │   ├── reports.py
│   │   │   ├── notifications.py
│   │   │   ├── workout_plans.py
│   │   │   ├── exercises.py
│   │   │   ├── streaks.py
│   │   │   ├── badges.py
│   │   │   └── dashboard.py
│   │   │
│   │   ├── services/
│   │   ├── database.py
│   │   ├── dependencies.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── streak_utils.py
│   │   ├── badge_utils.py
│   │   └── main.py
│   │
│   ├── generated_files/
│   ├── venv/
│   ├── .env
│   ├── requirements.txt
│   └── fittrack.db
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── context/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── index.css
│   │   └── main.jsx
│   │
│   ├── package.json
│   └── index.html
│
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd FitTrack
```

### 2. Backend Setup

Navigate to the backend directory:

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment.

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Environment Configuration

Create a `.env` file inside the backend directory.

Configure the required environment variables:

```env
DATABASE_URL=sqlite:///./fittrack.db
SECRET_KEY=your_secure_random_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Use a strong secret key for actual deployments. Do not upload real credentials or secrets to GitHub.

### 4. Start the Backend Server

```bash
uvicorn app.main:app --reload
```

Backend URL:

http://127.0.0.1:8000

Swagger API Documentation:

http://127.0.0.1:8000/docs

### 5. Frontend Setup

Open another terminal and navigate to the frontend directory:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the frontend development server:

```bash
npm run dev
```

Frontend URL:

http://localhost:5173

## API Integration

The React frontend communicates with the FastAPI backend using Axios.

### API Modules

| Module | API Prefix |
|---|---|
| Authentication | `/api/v1/auth/` |
| Workouts | `/api/v1/workouts/` |
| Daily Progress | `/api/v1/progress/` |
| Fitness Goals | `/api/v1/goals/` |
| Reports & Analytics | `/api/v1/reports/` |
| Notifications | `/api/v1/notifications/` |
| Workout Plans | `/api/v1/workout-plans/` |
| Exercise Library | `/api/v1/exercises/` |
| Streak Tracking | `/api/v1/streaks/` |
| Achievement Badges | `/api/v1/badges/` |
| Personalized Dashboard | `/api/v1/dashboard/` |

All protected APIs require a valid JWT access token.

## Application Features

- Secure user registration and login.
- Personal fitness dashboard API.
- Workout history management.
- Daily progress monitoring.
- Fitness goal tracking.
- Reports and analytics.
- Notification management.
- Daily fitness reminders.
- Workout scheduling.
- Exercise library and search.
- Weekly and monthly progress comparison.
- Workout streak tracking.
- Achievement badge management.
- Personalized dashboard data.
- User-specific fitness information.

## Testing

Phase 1 and Phase 2 backend modules have been implemented and tested through Swagger UI.

Testing includes:

- User registration and authentication.
- Workout CRUD operations.
- Daily progress creation and management.
- Fitness goal management.
- Reports and analytics.
- Notification management.
- Workout plan scheduling.
- Exercise library and workout associations.
- Weekly and monthly progress comparisons.
- Streak calculation and reset behavior.
- Achievement badge awarding and duplicate prevention.
- Personalized dashboard data aggregation.
- JWT authentication and user ownership validation.

## Project Completion Status

### Phase 1: Fitness Tracking Platform

| Module | Status |
|---|---|
| Module 1 – User Authentication | Completed |
| Module 2 – Workout Management | Completed |
| Module 3 – Daily Progress Tracking | Completed |
| Module 4 – Fitness Goal Management | Completed |
| Module 5 – Reports & Analytics | Completed |
| Module 6 – Notifications System | Completed |

### Phase 2: Advanced Tracking & User Engagement

| Module | Status |
|---|---|
| Module 7 – Workout Plans & Scheduling | Completed |
| Module 8 – Exercise Library | Completed |
| Module 9 – Progress Comparison | Completed |
| Module 10 – Streak Tracking System | Completed |
| Module 11 – Achievement Badges | Completed |
| Module 12 – Personalized Dashboard | Completed |

**Backend Phase 1: Completed and Tested.**

**Backend Phase 2: Completed and Tested.**

**Frontend:** React integration and verification of the Phase 2-specific UI responsibilities remain separate from the completed backend testing.

## Future Enhancements

- Complete and enhance frontend integration for all Phase 2 modules.
- Interactive workout calendar.
- Advanced fitness charts and performance visualizations.
- Achievement notification popups.
- Monthly fitness reports.
- Navbar notification bell with live unread count.
- Scheduled automatic reminders.
- Integration with wearable fitness devices.
- Personalized fitness recommendations.

## Conclusion

FitTrack is a full-stack fitness and workout management platform developed using FastAPI, React, and SQLite.

Phase 1 established the core fitness tracking functionality, including authentication, workout management, daily progress tracking, goal management, reports, and notifications.

Phase 2 extended the platform with workout scheduling, an exercise library, progress comparisons, streak tracking, achievement badges, and personalized dashboard APIs.

The project demonstrates practical experience in backend API development, frontend integration, database management, authentication, data analytics, and real-world full-stack application development.

**Project:** FitTrack – Fitness & Workout Management Platform  
**Backend:** FastAPI  
**Frontend:** React + Vite  
**Database:** SQLite  
**Phase 1:** Completed  
**Phase 2 Backend:** Completed and Tested
