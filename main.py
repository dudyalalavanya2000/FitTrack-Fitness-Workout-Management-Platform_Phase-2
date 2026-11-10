
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app import models

from app.routes import (
    auth,
    workouts,
    progress,
    goals,
    reports,
    notifications,
    workout_plans,
    exercises,
    streaks,
    badges,
    dashboard
)


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="FitTrack - Fitness & Workout Management Platform",
    description="Fitness tracking and workout management API",
    version="2.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


app.include_router(
    auth.router,
    prefix="/api/v1/auth",
    tags=["Authentication"]
)

app.include_router(
    workouts.router,
    prefix="/api/v1/workouts",
    tags=["Workouts"]
)

app.include_router(
    progress.router,
    prefix="/api/v1/progress",
    tags=["Daily Progress"]
)

app.include_router(
    goals.router,
    prefix="/api/v1/goals",
    tags=["Fitness Goals"]
)

app.include_router(
    reports.router,
    prefix="/api/v1/reports",
    tags=["Reports & Analytics"]
)

app.include_router(
    notifications.router,
    prefix="/api/v1/notifications",
    tags=["Notifications"]
)

app.include_router(
    workout_plans.router,
    prefix="/api/v1/workout-plans",
    tags=["Workout Plans & Scheduling"]
)

app.include_router(
    exercises.router,
    prefix="/api/v1/exercises",
    tags=["Exercise Library"]
)

app.include_router(
    streaks.router,
    prefix="/api/v1/streaks",
    tags=["Streak Tracking"]
)

app.include_router(
    badges.router,
    prefix="/api/v1/badges",
    tags=["Achievement Badges"]
)

app.include_router(
    dashboard.router,
    prefix="/api/v1/dashboard",
    tags=["Personalized Dashboard"]
)


@app.get("/")
def root():
    return {
        "message": "Welcome to FitTrack API",
        "status": "Running",
        "version": "2.0.0"
    }
