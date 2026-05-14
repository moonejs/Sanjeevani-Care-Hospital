<div align="center">

<img src="frontend/public/logoHMS.png" alt="Sanjeevani Logo" width="90"/>

# Sanjeevani Care Hospital 

### Hospital Management System

**A full-stack web application for managing hospital operations end-to-end —**  
patients, doctors, appointments, treatments, schedules, billing, and automated reports.

<br/>

[![Vue 3](https://img.shields.io/badge/Vue-3.x-42b883?style=flat-square&logo=vue.js)](https://vuejs.org/)
[![Flask](https://img.shields.io/badge/Flask-3.x-000000?style=flat-square&logo=flask)](https://flask.palletsprojects.com/)
[![Celery](https://img.shields.io/badge/Celery-5.x-37814A?style=flat-square&logo=celery)](https://docs.celeryq.dev/)
[![Redis](https://img.shields.io/badge/Redis-7.x-DC382D?style=flat-square&logo=redis)](https://redis.io/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.x-7952B3?style=flat-square&logo=bootstrap)](https://getbootstrap.com/)
[![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=flat-square&logo=sqlite)](https://sqlite.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)

</div>

---

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [System Architecture](#system-architecture)
- [Project Structure](#project-structure)
- [Data Models](#data-models)
- [User Roles & Permissions](#user-roles--permissions)
- [API Reference](#api-reference)
- [Background Tasks](#background-tasks)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
  - [Running Redis & Celery](#running-redis--celery)
  - [Default Credentials](#default-credentials)
- [Environment Variables](#environment-variables)
- [Screenshots](#screenshots)
- [Contributing](#contributing)

---

## Overview

**Sanjeevani HMS** is a production-ready Hospital Management System built for **Sanjeevani Care Hospital** (Est. 2005, NABH Accredited). It digitalises the complete hospital workflow — from patient registration and doctor scheduling to appointment booking, clinical treatment records, PDF billing, and automated email reminders.

The system is split into two independent services:

| Layer | Technology | Port |
|---|---|---|
| **Frontend SPA** | Vue 3 + Vite + Bootstrap 5 | `5173` |
| **Backend REST API** | Flask + Flask-RESTful + Flask-Security | `5000` |
| **Task Queue** | Celery + Redis | — |
| **Cache** | Redis | `6379` |
| **Database** | SQLite (dev) | — |

---

## Key Features

### 🏥 For Patients
- **Self-registration** with profile completion gate — patients cannot book until profile is complete
- **Browse departments** with speciality icons and doctor listings
- **Real-time slot booking** — view available morning / afternoon / evening slots per doctor per date
- **My Appointments** dashboard — view upcoming and past appointments with status badges
- **Download PDF bill** for any appointment (Celery-generated, branded with hospital logo)
- **Appointment history** with diagnosis, notes, medicines, and follow-up dates

### 👨‍⚕️ For Doctors
- **Personal dashboard** showing today's schedule and next appointment card
- **Appointment management** — confirm, complete, or cancel with reasons
- **Treatment recording** — add diagnosis, clinical notes, medicines (JSON), and follow-up dates after completing an appointment
- **Schedule management** — set date-wise availability for morning / afternoon / evening sessions, configure slot durations, max patients per slot, and toggle online booking
- **Patient profiles** — view complete medical and appointment history of assigned patients
- **Profile management** — personal info, education qualifications (JSON array), OPD timings, registration documents, bio, languages spoken
- **Download personal profile PDF** (branded, auto-generated)

### 🛡️ For Admins
- **Central dashboard** with system-wide statistics
- **Doctor management** — create doctor accounts, assign to departments, block/unblock with reason and timestamp
- **Department management** — create and manage hospital departments
- **Appointments overview** — view all appointments across the system with filters
- **Patient list** — view all registered patients with full details offcanvas
- **Bulk CSV exports** — export all doctors or all appointments as CSV in the background
- **Monthly PDF reports** emailed to each doctor on the 1st of every month

### ⚙️ System-Wide
- **Token-based authentication** via Flask-Security (`Authentication-Token` header)
- **Role-based access control** — `admin`, `doctor`, `patient` — with Vue Router guards
- **Redis caching** on frequently-read API endpoints
- **Automated daily reminders** — email sent to each patient with an appointment today
- **Automated monthly doctor reports** — per-doctor HTML email with appointment statistics
- **Celery beat scheduler** for all periodic tasks
- **File uploads** — separate folders for doctor and patient profile images, served via Flask static routes
- **Toast notifications** system-wide via Pinia store
- **Skeleton loading states** on all data-heavy pages
- **Pagination** on all list views
- **Search and filter** on appointments, doctors, patients

---

## Tech Stack

### Frontend
| Package | Version | Purpose |
|---|---|---|
| `vue` | 3.5.x | Composition API SPA framework |
| `vue-router` | 4.6.x | Client-side routing with navigation guards |
| `pinia` | 3.0.x | State management (auth, appointments, doctors, patients) |
| `axios` | 1.13.x | HTTP client with token interceptor |
| `bootstrap` | 5.3.x | UI framework — layout, components, utilities |
| `lucide-vue-next` | 0.563.x | Icon set |
| `@lottiefiles/dotlottie-vue` | 0.11.x | Lottie animations (landing page) |
| `vite` | 7.x | Build tool and dev server |

### Backend
| Package | Version | Purpose |
|---|---|---|
| `Flask` | 3.1.x | Web framework |
| `Flask-RESTful` | 0.3.x | REST API resource routing |
| `Flask-Security` | 5.7.x | Auth, token management, role enforcement |
| `Flask-SQLAlchemy` | 3.1.x | ORM |
| `Flask-Caching` | 2.3.x | Redis-backed caching |
| `Flask-Mail` | 0.10.x | Email sending |
| `Flask-CORS` | 6.0.x | Cross-origin requests |
| `Celery` | 5.6.x | Async task queue |
| `redis` | 7.2.x | Celery broker + result backend + cache |
| `reportlab` | 4.4.x | PDF generation (bills, profiles, reports) |
| `Pillow` | 12.x | Image handling |
| `SQLAlchemy` | 2.0.x | Database ORM |
| `SQLite` | — | Development database |

---

## System Architecture

```
┌──────────────────────────────────────────────────────────────────┐
│                         Browser (Vue 3 SPA)                      │
│                                                                  │
│   Landing Page → Auth → Patient / Doctor / Admin Dashboards      │
│   Pinia Stores │ Vue Router (role guards) │ Axios (token auth)   │
└─────────────────────────────┬────────────────────────────────────┘
                              │ HTTP REST  (port 5173 → 5000)
                              │ Authentication-Token header
┌─────────────────────────────▼────────────────────────────────────┐
│                    Flask REST API  (port 5000)                   │
│                                                                  │
│  Blueprints: /api/auth  /api/admin  /api/doctor                  │
│              /api/patient  /api/appointment  /api/department      │
│                                                                  │
│  Flask-Security  →  Role-based resource protection               │
│  Flask-Caching   →  Redis cache on GET endpoints                 │
│  Flask-Mail      →  SMTP email dispatch                          │
└──────┬────────────────────────────────────┬───────────────────────┘
       │ SQLAlchemy ORM                     │ Celery .delay()
┌──────▼──────────┐               ┌─────────▼──────────────────────┐
│  SQLite DB      │               │  Redis  (broker + backend)     │
│  hms.db         │               │  port 6379                     │
│                 │               └─────────┬──────────────────────┘
│  users          │                         │
│  roles          │               ┌─────────▼──────────────────────┐
│  patients       │               │  Celery Worker                 │
│  doctors        │               │                                │
│  departments    │               │  • generate_appointment_pdf    │
│  appointments   │               │  • generate_doctor_profile_pdf │
│  availability   │               │  • export_patient_treatments   │
│  treatments     │               │  • export_all_doctors_csv      │
│                 │               │  • export_all_appointments_csv │
└─────────────────┘               │                                │
                                  │  Celery Beat (scheduler)       │
                                  │  • send_daily_reminders        │
                                  │  • send_monthly_doctor_reports │
                                  └────────────────────────────────┘
```

---

## Project Structure

```
HMS/
├── backend/
│   ├── api/
│   │   ├── admin/            # Admin CRUD — doctors, patients, system stats
│   │   ├── appointment/      # Booking, availability, history, patient & doctor views
│   │   ├── auth/             # Login, register, current-user endpoints
│   │   ├── department/       # Department CRUD
│   │   ├── doctor/           # Doctor profile, patient resources
│   │   └── patient/          # Patient profile resources
│   ├── models/
│   │   ├── user.py           # Flask-Security User model
│   │   ├── role.py           # Role model + roles_users association
│   │   ├── patient.py        # Patient profile & relationships
│   │   ├── doctor.py         # Doctor profile, qualifications, availability
│   │   ├── department.py     # Department model
│   │   ├── appointment.py    # Appointment with status, type, session
│   │   ├── availability.py   # Per-date slot configuration per doctor
│   │   └── treatment.py      # Post-appointment diagnosis & medicines
│   ├── utils/
│   │   ├── email_utils.py    # SMTP email helper
│   │   ├── comman.py         # Shared helpers (is_doctor_bookable, etc.)
│   │   └── files.py          # File upload helpers
│   ├── uploads/
│   │   ├── doctors/profile/  # Doctor profile images
│   │   └── patients/profile/ # Patient profile images
│   ├── exports/              # Generated PDFs and CSVs (gitignored in prod)
│   ├── app.py                # Flask app factory + export routes
│   ├── config.py             # All configuration (DB, mail, redis, uploads)
│   ├── celery_app.py         # Celery init + beat schedule
│   ├── tasks.py              # All Celery task definitions
│   ├── extensions.py         # db, security, cache extension instances
│   └── requirements.txt
│
└── frontend/
    ├── public/
    │   ├── logoHMS.png        # Hospital logo (used in nav + PDFs)
    │   └── iconH.png          # Favicon
    ├── src/
    │   ├── api/               # Axios API modules per domain
    │   │   ├── axios.js       # Axios instance with token interceptor
    │   │   ├── auth.js
    │   │   ├── appointment.js
    │   │   ├── doctor.js
    │   │   ├── patient.js
    │   │   ├── admin.js
    │   │   └── department.js
    │   ├── router/
    │   │   ├── index.js       # Router + beforeEach navigation guards
    │   │   ├── admin.routes.js
    │   │   ├── doctor.routes.js
    │   │   ├── patient.routes.js
    │   │   ├── auth.routes.js
    │   │   └── public.routes.js
    │   ├── stores/            # Pinia stores
    │   │   ├── auth.store.js  # Token, role, profileCompleted
    │   │   ├── appointment.store.js
    │   │   ├── doctor.store.js
    │   │   ├── patient.store.js
    │   │   ├── admin.store.js
    │   │   ├── department.store.js
    │   │   └── toast.store.js
    │   ├── views/
    │   │   ├── LandingPage.vue
    │   │   ├── auth/           # Login, Register
    │   │   ├── admin/          # Dashboard, Doctors, Departments, Appointments, Patients
    │   │   ├── doctor/         # Dashboard, Appointments, Schedule, Patients, Profile
    │   │   └── patient/        # Dashboard, Departments, Doctors, Appointments, Profile
    │   ├── components/
    │   │   ├── common/         # Badge, Btn, Toast, Pagination, Search, Skeleton, etc.
    │   │   ├── layout/         # Navbars, BaseTable, Header
    │   │   ├── admin/          # Admin-specific table rows, modals
    │   │   └── Doctor/         # Doctor-specific appointment and schedule components
    │   ├── utils/
    │   │   ├── validators.js   # Form validators
    │   │   ├── departmentIcons.js
    │   │   ├── useSearchFilter.js
    │   │   └── comman.js
    │   ├── reusable/
    │   │   ├── useField.js         # Reactive field helper
    │   │   └── useFormValidation.js
    │   ├── assets/
    │   │   ├── images/         # Landing page illustration images (img-1 to img-10)
    │   │   └── main.css        # Global CSS variables and base styles
    │   └── main.js             # App bootstrap
    └── vite.config.js
```

---

## Data Models

### Entity Relationship Overview

```
User (Flask-Security)
 ├── roles  (M2M → Role: admin | doctor | patient)
 ├── patient  (1:1 → Patient)
 └── doctor   (1:1 → Doctor)

Patient
 ├── appointments  (1:M → Appointment)
 └── treatments    (1:M → Treatment)

Doctor
 ├── department    (M:1 → Department)
 ├── appointments  (1:M → Appointment)
 ├── availabilities (1:M → Availability)
 └── treatments    (1:M → Treatment)

Appointment
 ├── doctor    (M:1)
 ├── patient   (M:1)
 └── treatment (1:1 → Treatment)   ← created when doctor marks complete

Availability   (per doctor, per date)
 ├── morning_enabled / start / end / slot_duration / max_patients
 ├── afternoon_enabled / ...
 └── evening_enabled / ...
```

### Appointment Status Flow

```
pending  →  confirmed  →  completed
   ↓              ↓
cancelled      cancelled (with reason)
```

### Appointment Fields

| Field | Type | Description |
|---|---|---|
| `appointment_date` | Date | Date of appointment |
| `start_time` / `end_time` | Time | Slot time |
| `status` | String | `pending` / `confirmed` / `completed` / `cancelled` |
| `type` | String | `opd` / `emergency` / etc. |
| `session` | String | `morning` / `afternoon` / `evening` |
| `notes` | Text | Optional patient notes |
| `cancel_reason` | Text | Populated on cancellation |

---

## User Roles & Permissions

| Feature | Patient | Doctor | Admin |
|---|:---:|:---:|:---:|
| View Landing Page | ✅ | ✅ | ✅ |
| Register / Login | ✅ | — | — |
| Complete own profile | ✅ | ✅ | — |
| Browse departments | ✅ | — | — |
| Browse doctors & slots | ✅ | — | — |
| Book appointment | ✅ | — | — |
| Cancel own appointment | ✅ | — | — |
| Download appointment bill (PDF) | ✅ | — | — |
| View own appointments | ✅ | — | — |
| View assigned patients | — | ✅ | — |
| Confirm / Cancel appointment | — | ✅ | — |
| Mark appointment complete + add treatment | — | ✅ | — |
| Manage schedule & availability | — | ✅ | — |
| View patient treatment history | — | ✅ | — |
| Download own profile PDF | — | ✅ | — |
| Create doctors | — | — | ✅ |
| Block / Unblock doctors | — | — | ✅ |
| Manage departments | — | — | ✅ |
| View all appointments | — | — | ✅ |
| View all patients | — | — | ✅ |
| Export all doctors CSV | — | — | ✅ |
| Export all appointments CSV | — | — | ✅ |
| Receive monthly report email | — | ✅ | — |

> **Profile Gate:** Patients who have not completed their profile are automatically redirected to `/patient/profile` on every route navigation until the profile is complete.

---

## API Reference

All endpoints are prefixed with `/api`. Authentication uses the `Authentication-Token` header returned on login.

### Auth

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| `POST` | `/api/login` | — | Login, returns `authentication_token` |
| `POST` | `/api/register` | — | Register a new patient account |
| `GET` | `/api/me` | Token | Get current user info + role |
| `POST` | `/api/logout` | Token | Logout and invalidate token |

### Appointments

| Method | Endpoint | Role | Description |
|---|---|---|---|
| `GET` | `/api/appointment/availability` | Patient | Available slots for a given date |
| `POST` | `/api/appointment/book` | Patient | Book an appointment |
| `GET` | `/api/appointment/my` | Patient | Patient's own appointments |
| `GET` | `/api/appointment/doctor` | Doctor | Doctor's own appointments |
| `PATCH` | `/api/appointment/<id>/status` | Doctor | Confirm / cancel appointment |
| `POST` | `/api/appointment/<id>/complete` | Doctor | Mark complete + add treatment |
| `GET` | `/api/appointment/history/<patient_id>` | Doctor | Patient treatment history |
| `GET` | `/api/appointment/all` | Admin | All appointments system-wide |

### Doctors

| Method | Endpoint | Role | Description |
|---|---|---|---|
| `GET` | `/api/doctor/profile` | Doctor | Get own profile |
| `PUT` | `/api/doctor/profile` | Doctor | Update own profile |
| `GET` | `/api/doctor/schedule` | Doctor | Get availability schedule |
| `POST` | `/api/doctor/schedule` | Doctor | Set availability for a date |
| `GET` | `/api/doctor/patients` | Doctor | List assigned patients |
| `GET` | `/api/doctor/patients/<id>` | Doctor | Individual patient details |

### Admin

| Method | Endpoint | Role | Description |
|---|---|---|---|
| `GET` | `/api/admin/stats` | Admin | System-wide stats |
| `GET` | `/api/admin/doctors` | Admin | All doctors |
| `POST` | `/api/admin/doctors` | Admin | Create new doctor |
| `PATCH` | `/api/admin/doctors/<id>/block` | Admin | Block / unblock doctor |
| `GET` | `/api/admin/patients` | Admin | All patients |
| `GET` | `/api/admin/departments` | Admin | All departments |
| `POST` | `/api/admin/departments` | Admin | Create department |

### Export Routes (no `/api` prefix)

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/export-appointment/<id>` | Trigger async PDF generation for appointment |
| `GET` | `/export-status/<task_id>` | Poll Celery task status |
| `GET` | `/exports/<filename>` | Download generated file |
| `GET` | `/export-doctors` | Trigger all-doctors CSV export |
| `GET` | `/export-appointments` | Trigger all-appointments CSV export |
| `GET` | `/export-doctor/<id>` | Trigger doctor profile PDF |

---

## Background Tasks

All async work is handled by **Celery** with **Redis** as both broker and result backend.

### Scheduled Tasks (Celery Beat)

| Task | Schedule | Description |
|---|---|---|
| `send_daily_reminders` | Daily at 8:00 AM IST | Emails all patients with a pending/confirmed appointment today |
| `send_monthly_doctor_reports` | 1st of every month, 9:00 AM IST | Emails each doctor a branded HTML report of their previous month's completed appointments |

> **Dev mode:** Both beat tasks are set to `crontab(minute="*/1")` (every minute) for easy testing. Change to the commented production schedules before deploying.

### On-Demand Tasks

| Task | Trigger | Output |
|---|---|---|
| `generate_appointment_pdf` | `GET /export-appointment/<id>` | Branded PDF bill with patient info, appointment details, treatment, and billing summary |
| `generate_doctor_profile_pdf` | `GET /export-doctor/<id>` | PDF profile with doctor info, qualifications, bio, and appointment statistics |
| `export_patient_treatments` | API call | CSV of all treatments for a specific patient |
| `export_all_doctors_csv` | `GET /export-doctors` | CSV of all registered doctors |
| `export_all_appointments_csv` | `GET /export-appointments` | CSV of all appointments system-wide |

### Polling Pattern (Frontend)

```js
// 1. Trigger the task
const { data } = await axios.get('/export-appointment/42')
const taskId = data.task_id

// 2. Poll until done
const poll = setInterval(async () => {
  const { data } = await axios.get(`/export-status/${taskId}`)
  if (data.status === 'completed') {
    clearInterval(poll)
    window.open(`/exports/${data.filename}`)   // download
  }
}, 1500)
```

---

## Getting Started

### Prerequisites

| Tool | Minimum Version | Install |
|---|---|---|
| Python | 3.10+ | [python.org](https://python.org) |
| Node.js | 20.19+ or 22.12+ | [nodejs.org](https://nodejs.org) |
| Redis | 6+ | [redis.io/download](https://redis.io/download) |
| Git | any | [git-scm.com](https://git-scm.com) |

> **Windows users:** Redis is easiest via WSL2 or the [Memurai](https://www.memurai.com/) Windows port.

---

### Backend Setup

```bash
# 1. Clone the repository
git clone https://github.com/your-username/sanjeevani-hms.git
cd sanjeevani-hms/backend

# 2. Create and activate a virtual environment
python -m venv venv

# Linux / macOS
source venv/bin/activate

# Windows
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start a local SMTP server for email testing (in a separate terminal)
python -m smtpd -n -c DebuggingServer localhost:1025

# 5. Run the Flask app (also seeds the database on first run)
python app.py
```

The API will be available at **`http://localhost:5000`**.  
The database (`hms.db`) and `exports/` directory are created automatically.

---

### Frontend Setup

```bash
# In a new terminal
cd sanjeevani-hms/frontend

# Install dependencies
npm install

# Start the dev server
npm run dev
```

The app will be available at **`http://localhost:5173`**.

---

### Running Redis & Celery

You need **three** additional terminal processes running alongside Flask and Vue:

```bash
# Terminal 1 — Redis server
redis-server

# Terminal 2 — Celery worker (processes on-demand tasks)
cd backend
celery -A celery_app.celery worker --loglevel=info

# Terminal 3 — Celery beat (runs scheduled tasks)
cd backend
celery -A celery_app.celery beat --loglevel=info
```

> **All five processes at a glance:**
> 1. `python app.py` — Flask API
> 2. `npm run dev` — Vue frontend
> 3. `redis-server` — Redis
> 4. `celery worker` — Async tasks
> 5. `celery beat` — Scheduler
> 6. `python -m smtpd ...` — Local mail server (optional for dev)

---

### Default Credentials

The database is seeded automatically with a default admin account on first run:

| Role | Email | Password |
|---|---|---|
| Admin | `admin@sanjeevani.care.com` | `Admin@123` |

To create a **Doctor** account, log in as Admin, navigate to **Doctors → Add Doctor** — this creates a User+Doctor record. The doctor receives their login credentials and must complete their profile before accepting appointments.

To create a **Patient** account, use the public **Register** page at `/register`. Patients must complete their profile before they can book appointments.

---

## Environment Variables

The app reads configuration from `backend/config.py`. For production, set these as environment variables:

| Variable | Default | Description |
|---|---|---|
| `SECRET_KEY` | `moon-security` | Flask session secret key |
| `SECURITY_PASSWORD_SALT` | `moon-password-salt` | Password hashing salt |
| `SQLALCHEMY_DATABASE_URI` | `sqlite:///hms.db` | Database URI (swap for PostgreSQL in prod) |
| `CACHE_REDIS_URL` | `redis://localhost:6379/0` | Redis URL for cache |
| `CELERY_BROKER_URL` | `redis://localhost:6379/0` | Redis URL for Celery broker |
| `CELERY_RESULT_BACKEND` | `redis://localhost:6379/0` | Redis URL for Celery results |
| `MAIL_SERVER` | `localhost` | SMTP server |
| `MAIL_PORT` | `1025` | SMTP port |
| `MAIL_DEFAULT_SENDER` | `support@sanjeevani.care.com` | From address for all emails |

> ⚠️ **Always change `SECRET_KEY` and `SECURITY_PASSWORD_SALT` before deploying to production.**

---

## Screenshots

> Add screenshots here by dropping images into a `docs/screenshots/` folder and updating the paths below.

| Landing Page | Patient Dashboard | Doctor Schedule |
|---|---|---|
| ![Landing](docs/screenshots/landing.png) | ![Patient](docs/screenshots/patient-dashboard.png) | ![Schedule](docs/screenshots/doctor-schedule.png) |

| Admin Dashboard | Appointment Bill PDF | Monthly Report Email |
|---|---|---|
| ![Admin](docs/screenshots/admin.png) | ![Bill](docs/screenshots/bill-pdf.png) | ![Email](docs/screenshots/email-report.png) |

---

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork** the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Make your changes with clear, descriptive commits
4. Ensure the backend runs without errors: `python app.py`
5. Ensure the frontend lints cleanly: `npm run lint`
6. Open a **Pull Request** with a description of what you changed and why

### Code Style

- **Backend:** Follow PEP 8. Resource classes go in their module's `resources.py`. New models go in `models/` with a corresponding import in `models/__init__.py`.
- **Frontend:** Prettier + ESLint are configured. Run `npm run format` before committing. Components use `<script setup>` Composition API. Stores use Pinia `defineStore` with the setup function style.

---

<div align="center">

Built with ❤️ for **Sanjeevani Care Hospital**  
Est. 2005 · NABH · NABL · ISO 9001:2015 · JCI Accredited  
*Healing with Compassion, Excellence & Modern Science*

</div>
