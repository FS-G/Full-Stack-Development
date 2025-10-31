## Full-Stack Web Development Course

A hands-on course covering the essentials of frontend, backend, databases, and end-to-end development. The curriculum maps directly to this repository’s folders and example apps.

### Who this is for
- Beginners to intermediate learners who want a structured, practical path to building full-stack applications.
- Learners comfortable with basic programming concepts (variables, functions, conditionals).

### Learning outcomes
By the end, you will be able to:
- Design relational schemas and work confidently with MySQL.
- Build responsive user interfaces with HTML, CSS, and JavaScript.
- Implement RESTful backend APIs with Python and FastAPI.
- Connect frontend and backend with a database to ship a working full-stack app.
- Deploy a minimal app to a generic cloud provider.

---

## Course Structure and Outline
This repository is organized into modules that align with the course flow.

### Module 1 — Git and GitHub Basics
Path: `1_git_and_github/`
- `git_and_github.md`: Intro to Git workflow (init, clone, branch, commit, push/pull, merge).
- `github_lecture_notes.md`: Remote repositories, pull requests, code reviews, branching strategies.
- `class_practice/hello.py`: Simple Python file for practicing commits and version control.

Key skills:
- Creating and managing repositories.
- Authoring clean commit messages and pull requests.
- Resolving merge conflicts and collaborating effectively.

Deliverables:
- A personal repository with a feature branch and an opened pull request.

### Module 2 — Databases and SQL with MySQL
Path: `2_databases/`
- `1_mysql_installation_guide.md`: Installation and configuration notes.
- `2_intro_to_rdbms.md`: RDBMS fundamentals, normalization, keys, and relationships.
- `3_mysql.md`: Practical SQL (DDL, DML, queries, joins, indexes, transactions).

Key skills:
- Designing tables and relationships.
- Writing CRUD queries and joins.
- Applying indexes and understanding query performance basics.

Deliverables:
- A normalized schema and a set of SQL queries for a sample dataset.

### Module 3 — Intro to Web Development
Path: `3_intro_to_web_development/`
- `web_dev_lecture_notes.md`: HTTP, client-server model, REST, JSON, CORS, and tooling.
- Two minimal full-stack demo apps for practical lab work:
  - `full_stack_minimal_app/`
  - `full_stack_minimal_app_1/`

Each app contains:
- `index.html`: Minimal frontend page and form.
- `styles.css`: Basic styling.
- `script.js`: Frontend logic and API calls.
- `main.py`: FastAPI backend exposing REST endpoints.
- `setup_db.py`: Script to initialize a SQLite guestbook database (local demo).
- `requirements.txt`: Python dependencies.
- `guestbook.db`: Local SQLite DB file (created via setup script; safe to delete/regenerate).

Key skills:
- Understanding request/response life cycle.
- Building a tiny, end-to-end app with a database and API.
- Frontend-to-backend integration and form handling.

Deliverables:
- A working local full-stack app that accepts user input and persists records.

### Module 4 — Frontend Development Fundamentals
Path: `4_frontend_dev/`
- `1_html_lectures.md`: Semantic HTML, forms, accessibility basics.
- `2_css_beginners_lecture.md`: Layout, Flexbox, Grid, responsive design, variables.
- `3_js_lecture.md`: DOM, events, fetch API, modules, basic state management.

Key skills:
- Structuring pages with semantic HTML and accessible forms.
- Styling responsive layouts with CSS.
- Interacting with APIs using modern JavaScript.

Deliverables:
- A responsive page consuming a public API with graceful error handling.

### Module 5 — Backend Development with FastAPI
Path: `5_backend_development/`
- `1_backend_development_lectures_with_fastapi.md`: Routing, request/response models, validation.
- `2_backend_development_lectures_with_fastapi.md`: Dependency injection, middleware, auth basics.
- `3_full_stack_e2e.md`: Putting it all together, end-to-end considerations and deployment.

Key skills:
- Designing and implementing REST endpoints.
- Data validation with Pydantic models.
- Basic authentication patterns and middleware.

Deliverables:
- A small REST API with unit endpoints, validation, and error handling.

---




## Deployment (Generic Cloud Provider)
When you are ready to deploy, target a generic cloud provider.

High-level steps:
1. Containerize the backend with a lightweight Python base image.
2. Use environment variables for secrets and database URLs.
3. Provision a managed MySQL (or use SQLite for demos, not recommended for production).
4. Expose the FastAPI app via a reverse proxy (e.g., Nginx) or the provider’s native service.
5. Serve static frontend assets via the cloud’s static hosting or from the backend.
6. Configure HTTPS, health checks, and autoscaling as applicable.

Deployment deliverables:
- A running API endpoint and accessible frontend URL on a generic cloud provider.

---



## Repository Map
Quick reference to key paths:
- `1_git_and_github/` — Git basics, class practice.
- `2_databases/` — MySQL setup, RDBMS intro, SQL practice.
- `3_intro_to_web_development/` — Notes and two minimal full-stack apps.
- `4_frontend_dev/` — HTML, CSS, JS lectures.
- `5_backend_development/` — FastAPI lectures and end-to-end notes.

---



