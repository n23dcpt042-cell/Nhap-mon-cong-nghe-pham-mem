# Lab02 - Hotel Booking System

Artifacts for Lab 02 (Phân tích yêu cầu & Thiết kế Use Case)

## Cấu trúc
- diagrams/        : PlantUML sources + PNG
- sql/             : schema.sql, seed.sql
- backend/         : prototype Flask (demo)
- README.md

## Hướng dẫn chạy DB (local)
1. mysql -u root -p < sql/schema.sql
2. mysql -u root -p < sql/seed.sql

## PlantUML
Generate images:
plantuml diagrams/*.puml

## Git workflow
- Branch từ `main` → feature branches
- Commit messages: `HOTEL-<ISSUE> <SHORT>: <message>`
