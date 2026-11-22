# Naag Shakti: Clinic Appointment Booking

A small web app for booking and looking up clinic appointments. Built at the **Innovation Sprint hackathon (Intel Unnati), April 2026**, in a fully offline environment: no internet access and no AI tools.

It was my first time connecting a frontend to a backend.

## What it does

- Book an appointment with patient ID, name, age, problem and preferred time
- List all booked appointments
- Search for an appointment by patient ID
- Validate input on both the frontend and the backend (numeric ID, time like `10 AM` or `2 PM`, no empty fields)

## Stack

| Layer | Technology |
|---|---|
| Backend | Python standard library (`http.server`), JSON over HTTP |
| Frontend | HTML5, CSS3, vanilla JavaScript (`fetch`) |

No frameworks or external packages.

## Run it

```bash
python main.py
```

The server starts on `http://127.0.0.1:5000`. Then open `frontend.html` in a browser.

## API

| Method | Path | Description |
|---|---|---|
| `GET` | `/appointments` | List all appointments |
| `GET` | `/search?id=<number>` | Find an appointment by patient ID |
| `POST` | `/appointments` | Create an appointment. JSON body: `id`, `name`, `age`, `problem`, `time` |

## Known limitations

This is a hackathon prototype, and I would fix these first:

- Appointments are stored in memory and lost when the server stops (no database)
- No user authentication
- No check for duplicate patient IDs or clashing time slots
- CORS is open to all origins

## What I learned

- How a request travels from a browser form to a server and back, and how to debug it without documentation
- A working backend is only the first step. The winning teams had authentication and a polished interface, so I now build both in from the start.
