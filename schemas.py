
from datetime import date, datetime
from typing import Literal

from pydantic import BaseModel, EmailStr, Field, ConfigDict


# Authentication schemas

class UserRegister(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)


class TokenResponse(BaseModel):
    access_token: str
    token_type: str


# Workout schemas

class WorkoutCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    workout_type: str = Field(min_length=2, max_length=50)
    duration_minutes: int = Field(gt=0)
    calories_burned: int = Field(default=0, ge=0)
    notes: str | None = None
    workout_date: date = Field(default_factory=date.today)


class WorkoutUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=100)
    workout_type: str | None = Field(default=None, min_length=2, max_length=50)
    duration_minutes: int | None = Field(default=None, gt=0)
    calories_burned: int | None = Field(default=None, ge=0)
    notes: str | None = None
    workout_date: date | None = None


class WorkoutResponse(BaseModel):
    id: int
    user_id: int
    name: str
    workout_type: str
    duration_minutes: int
    calories_burned: int
    notes: str | None
    workout_date: date

    model_config = ConfigDict(from_attributes=True)


# Daily progress schemas

class ProgressCreate(BaseModel):
    progress_date: date = Field(default_factory=date.today)
    weight_kg: float | None = Field(default=None, gt=0, le=500)
    calories_consumed: int = Field(default=0, ge=0)
    water_intake_ml: int = Field(default=0, ge=0)
    exercise_minutes: int = Field(default=0, ge=0)
    notes: str | None = None


class ProgressUpdate(BaseModel):
    progress_date: date | None = None
    weight_kg: float | None = Field(default=None, gt=0, le=500)
    calories_consumed: int | None = Field(default=None, ge=0)
    water_intake_ml: int | None = Field(default=None, ge=0)
    exercise_minutes: int | None = Field(default=None, ge=0)
    notes: str | None = None


class ProgressResponse(BaseModel):
    id: int
    user_id: int
    progress_date: date
    weight_kg: float | None
    calories_consumed: int
    water_intake_ml: int
    exercise_minutes: int
    notes: str | None

    model_config = ConfigDict(from_attributes=True)


# Fitness goal schemas

GoalType = Literal[
    "weight",
    "calories",
    "workout_duration",
    "water_intake",
    "exercise_minutes",
    "custom"
]

GoalStatus = Literal["active", "completed"]


class GoalCreate(BaseModel):
    title: str = Field(min_length=2, max_length=100)
    description: str | None = None
    goal_type: GoalType
    target_value: float = Field(gt=0)
    current_value: float = Field(default=0, ge=0)
    unit: str = Field(min_length=1, max_length=30)
    start_date: date = Field(default_factory=date.today)
    target_date: date | None = None
    status: GoalStatus = "active"


class GoalUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=2, max_length=100)
    description: str | None = None
    goal_type: GoalType | None = None
    target_value: float | None = Field(default=None, gt=0)
    current_value: float | None = Field(default=None, ge=0)
    unit: str | None = Field(default=None, min_length=1, max_length=30)
    start_date: date | None = None
    target_date: date | None = None
    status: GoalStatus | None = None


class GoalResponse(BaseModel):
    id: int
    user_id: int
    title: str
    description: str | None
    goal_type: str
    target_value: float
    current_value: float
    unit: str
    start_date: date
    target_date: date | None
    status: str

    model_config = ConfigDict(from_attributes=True)


# Notification schemas

NotificationType = Literal[
    "general",
    "workout",
    "goal",
    "daily_reminder"
]


class NotificationCreate(BaseModel):
    title: str = Field(min_length=2, max_length=150)
    message: str = Field(min_length=2)
    notification_type: NotificationType = "general"


class NotificationResponse(BaseModel):
    id: int
    user_id: int
    title: str
    message: str
    notification_type: str
    is_read: bool
    created_at: datetime | None

    model_config = ConfigDict(from_attributes=True)


# Phase 2 - Module 7: Workout Plan schemas

class WorkoutPlanCreate(BaseModel):
    title: str = Field(min_length=2, max_length=100)
    description: str | None = None
    scheduled_date: date


class WorkoutPlanUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=2, max_length=100)
    description: str | None = None
    scheduled_date: date | None = None


class WorkoutPlanResponse(BaseModel):
    id: int
    user_id: int
    title: str
    description: str | None
    scheduled_date: date
    created_at: datetime | None

    model_config = ConfigDict(from_attributes=True)


# Phase 2 - Module 8: Exercise Library schemas

ExerciseCategory = Literal["Cardio", "Strength", "Yoga"]


class ExerciseCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    category: ExerciseCategory
    description: str | None = None
    duration_minutes: int = Field(gt=0)


class ExerciseUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=100)
    category: ExerciseCategory | None = None
    description: str | None = None
    duration_minutes: int | None = Field(default=None, gt=0)


class ExerciseResponse(BaseModel):
    id: int
    user_id: int
    name: str
    category: str
    description: str | None
    duration_minutes: int
    created_at: datetime | None

    model_config = ConfigDict(from_attributes=True)


class WorkoutExerciseResponse(BaseModel):
    id: int
    workout_id: int
    exercise_id: int
    created_at: datetime | None

    model_config = ConfigDict(from_attributes=True)


# Phase 2 - Module 10: Streak schemas

class StreakResponse(BaseModel):
    id: int
    user_id: int
    current_streak: int
    longest_streak: int
    last_workout_date: date | None
    updated_at: datetime | None

    model_config = ConfigDict(from_attributes=True)


# Phase 2 - Module 11: Achievement Badge schemas

class BadgeResponse(BaseModel):
    id: int
    name: str
    description: str
    icon: str
    created_at: datetime | None

    model_config = ConfigDict(from_attributes=True)


class UserBadgeResponse(BaseModel):
    id: int
    user_id: int
    badge_id: int
    badge_name: str
    badge_description: str
    badge_icon: str
    earned_at: datetime | None


# Phase 2 - Module 12: Personalized Dashboard schemas

class DashboardProgressSummary(BaseModel):
    progress_date: date
    weight_kg: float | None
    calories_consumed: int
    water_intake_ml: int
    exercise_minutes: int


class DashboardDailySummary(BaseModel):
    summary_date: date
    workouts_completed: int
    total_duration_minutes: int
    calories_burned: int
    progress: DashboardProgressSummary | None


class DashboardGoalProgress(BaseModel):
    id: int
    title: str
    goal_type: str
    target_value: float
    current_value: float
    unit: str
    status: str
    target_date: date | None
    progress_percentage: float


class DashboardStreak(BaseModel):
    current_streak: int
    longest_streak: int
    last_workout_date: date | None


class DashboardBadge(BaseModel):
    id: int
    name: str
    description: str
    icon: str
    earned_at: datetime | None


class DashboardResponse(BaseModel):
    user_id: int
    username: str
    daily_summary: DashboardDailySummary
    upcoming_workouts: list[WorkoutPlanResponse]
    goals: list[DashboardGoalProgress]
    streak: DashboardStreak
    earned_badges: list[DashboardBadge]
