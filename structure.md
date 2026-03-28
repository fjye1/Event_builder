event_builder/
│
├── app/
│   ├── __init__.py              # create_app(), extensions init
│   ├── config.py
│
│   ├── extensions.py           # db, login_manager, migrate, etc.
│
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py             # users + roles
│   │   ├── event.py            # main event model
│   │   ├── staff.py
│   │   ├── client.py
│   │   ├── venue.py
│   │   ├── product.py
│   │   ├── vehicle.py
│   │   ├── extras.py
│   │   ├── joins.py            # ALL join tables (important later)
│   │   ├── availability.py     # staff availability / scheduling logic
│   │   └── notification.py     # notification jobs/logs
│
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py             # login/register/logout
│   │   ├── events.py           # create/edit/view events
│   │   ├── data.py             # edit reference data (staff, venue, etc.)
│   │   ├── analysis.py         # reports + filters
│   │   ├── profile.py
│   │   └── api.py              # webhooks / external triggers
│
│   ├── services/               # 👈 this is key for complexity
│   │   ├── __init__.py
│   │   ├── event_service.py        # create/update logic
│   │   ├── scheduling_service.py   # heavy logic (conflicts, optimisation)
│   │   ├── notification_service.py # send discord/webhooks
│   │   ├── permission_service.py   # role checks
│   │   └── analytics_service.py
│
│   ├── templates/
│   │   ├── base/
│   │   ├── auth/
│   │   ├── events/
│   │   ├── data/
│   │   ├── analysis/
│   │   └── profile/
│
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│
│   └── utils/
│       ├── helpers.py
│       ├── datetime.py
│       └── decorators.py       # login/role decorators
│
├── migrations/                 # alembic
│
├── scripts/                    # background jobs / cron style
│   ├── run_scheduler.py        # check conflicts / assign staff
│   ├── send_notifications.py
│   └── seed_data.py
│
├── instance/                   # local config, secrets
│
├── .env
├── run.py                      # entry point
└── requirements.txt


