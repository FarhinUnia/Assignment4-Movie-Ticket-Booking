# Movie Ticket Booking System

CSCN73010 – Software Quality III: Build and Release  
Assignment 4 – Fall 2026

## Description

A Python-based Movie Ticket Booking System that allows customers
to book movie tickets while enforcing business rules.

## Business Rules

1. Customers must be at least 13 years old.
2. Ticket quantity must be greater than zero.
3. Customers cannot book more tickets than available seats.
4. Successful bookings reduce available seats.
5. Sold-out movies cannot accept additional bookings.

## Project Structure

- `src/movie_booking/` – Application classes.
- `drivers/` – Application Driver Layer.
- `tests/unit/` – Unit tests.
- `tests/acceptance/` – Acceptance testing scenarios.

## Packaging

The application is configured using `pyproject.toml` and supports
Source Distribution (`.tar.gz`) and Wheel (`.whl`) packages.
