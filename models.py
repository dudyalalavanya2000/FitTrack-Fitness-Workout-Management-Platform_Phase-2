from datetime import date

from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    DateTime,
    Float,
    Text,
    ForeignKey,
    UniqueConstraint,
    Boolean
)
from sqlalchemy.sql import func

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    hashed_password = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class Workout(Base):
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)

    name = Column(String(100), nullable=False)
    workout_type = Column(String(50), nullable=False)
    duration_minutes = Column(Integer, nullable=False)
    calories_burned = Column(Integer, nullable=True, default=0)
    notes = Column(Text, nullable=True)
    workout_date = Column(Date, nullable=False, default=date.today)

    created_at = Column(DateTime(timezone=True), server_default=func.now())


class Progress(Base):
    __tablename__ = "progress"

    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "progress_date",
            name="unique_user_progress_date"
        ),
    )

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)

    progress_date = Column(Date, nullable=False, default=date.today)
    weight_kg = Column(Float, nullable=True)
    calories_consumed = Column(Integer, nullable=False, default=0)
    water_intake_ml = Column(Integer, nullable=False, default=0)
    exercise_minutes = Column(Integer, nullable=False, default=0)
    notes = Column(Text, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())


class Goal(Base):
    __tablename__ = "goals"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)

    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    goal_type = Column(String(50), nullable=False)
    target_value = Column(Float, nullable=False)
    current_value = Column(Float, nullable=False, default=0)
    unit = Column(String(30), nullable=False)
    start_date = Column(Date, nullable=False, default=date.today)
    target_date = Column(Date, nullable=True)
    status = Column(String(20), nullable=False, default="active")

    created_at = Column(DateTime(timezone=True), server_default=func.now())


class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)

    title = Column(String(150), nullable=False)
    message = Column(Text, nullable=False)
    notification_type = Column(
        String(50),
        nullable=False,
        default="general"
    )
    is_read = Column(Boolean, nullable=False, default=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())


# Phase 2 - Module 7: Workout Plans & Scheduling

class WorkoutPlan(Base):
    __tablename__ = "workout_plans"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)

    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    scheduled_date = Column(Date, nullable=False, index=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())


# Phase 2 - Module 8: Exercise Library

class Exercise(Base):
    __tablename__ = "exercises"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)

    name = Column(String(100), nullable=False, index=True)
    category = Column(String(30), nullable=False, index=True)
    description = Column(Text, nullable=True)
    duration_minutes = Column(Integer, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())


class WorkoutExercise(Base):
    __tablename__ = "workout_exercises"

    __table_args__ = (
        UniqueConstraint(
            "workout_id",
            "exercise_id",
            name="unique_workout_exercise"
        ),
    )

    id = Column(Integer, primary_key=True, index=True)

    workout_id = Column(
        Integer,
        ForeignKey("workouts.id"),
        nullable=False,
        index=True
    )

    exercise_id = Column(
        Integer,
        ForeignKey("exercises.id"),
        nullable=False,
        index=True
    )

    created_at = Column(DateTime(timezone=True), server_default=func.now())


# Phase 2 - Module 10: Workout Streak Tracking

class Streak(Base):
    __tablename__ = "streaks"

    __table_args__ = (
        UniqueConstraint(
            "user_id",
            name="unique_user_streak"
        ),
    )

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
        index=True
    )

    current_streak = Column(Integer, nullable=False, default=0)
    longest_streak = Column(Integer, nullable=False, default=0)
    last_workout_date = Column(Date, nullable=True)

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )


# Phase 2 - Module 11: Achievement Badges

class Badge(Base):
    __tablename__ = "badges"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), unique=True, nullable=False, index=True)
    description = Column(Text, nullable=False)
    icon = Column(String(50), nullable=False)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )


class UserBadge(Base):
    __tablename__ = "user_badges"

    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "badge_id",
            name="unique_user_badge"
        ),
    )

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
        index=True
    )

    badge_id = Column(
        Integer,
        ForeignKey("badges.id"),
        nullable=False,
        index=True
    )

    earned_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )