<!--
Sync Impact Report
- Version change: (template) → 1.0.0
- Modified principles: Initial adoption (all new)
- Added sections: Core Principles (8), Security & Secrets, Development Workflow, Governance
- Removed sections: None (replaced template placeholders)
- Templates: plan-template.md ✅ (constitution gates documented inline in plan workflow)
                 spec-template.md ✅ (no change required; already mandates testing scenarios)
                 tasks-template.md ✅ updated (tests required per constitution)
- Follow-up TODOs: None
-->

# TensorX Constitution

## Core Principles

### I. Simplicity First

Use simple, boring technology. Prefer standard library and well-known dependencies over
novel frameworks. New abstractions MUST solve a concrete problem; YAGNI applies by default.

**Rationale**: This project is a focused local tool. Complexity increases maintenance cost
without proportional benefit.

### II. Small, Focused Files

Prefer small files with a single clear responsibility. Split when a file grows hard to
navigate or mixes unrelated concerns. Avoid premature package structure.

**Rationale**: Small files are easier to review, test, and change incrementally.

### III. Test Before Major Implementation

Write tests before major implementation work. For each feature slice: define acceptance
criteria, add failing tests, then implement until tests pass. Minor fixes and typos are
exempt; new behavior and refactors that change contracts are not.

**Rationale**: Tests encode intent and catch regressions early with minimal ceremony.

### IV. Locally Runnable

The app MUST run on a developer machine without cloud deploy steps. Setup instructions
MUST fit in a short README section. Dependencies MUST be installable with standard
project tooling (e.g., `pip`, `uv`).

**Rationale**: Local runnability keeps feedback loops fast and avoids hidden environment
assumptions.

### V. Clear Error Messages

Errors MUST tell the user what went wrong and what to do next (missing env var, bad file
path, API failure). Avoid bare stack traces as the only user-facing output for CLI paths.

**Rationale**: Most failures will be configuration or input mistakes; helpful messages
reduce debugging time.

### VI. No Unrequested External Services

Do not add external services (databases, queues, hosted auth, extra APIs) unless
explicitly requested in the feature spec. The TensorX API is allowed when the feature
requires inference; do not add others by default.

**Rationale**: Scope stays controlled; infrastructure creep is a common source of
over-engineering.

### VII. Document Every Feature

Every feature MUST include a short README note: what it does, how to run it, and any
required environment variables (names only, never values).

**Rationale**: Future-you and collaborators should not need to read the whole codebase
to use a feature.

### VIII. Never Commit Secrets

Do not commit API keys, tokens, passwords, or `.env` files. Secrets live in local `.env`
or environment variables only. Use `.env.example` with placeholder values for documentation.
Specs and READMEs MUST NOT contain real credentials.

**Rationale**: Prevents accidental credential leaks via version control.

## Security & Secrets

- `.env` MUST be listed in `.gitignore` before any secret is stored locally.
- Code MUST read secrets from environment variables, not hardcoded strings.
- Before any git push, verify no secrets appear in tracked files (`git diff`, readme, specs).

## Development Workflow

Recommended Spec Kit loop for this repo:

`constitution → specify → plan → tasks → implement → test/review → refine spec → repeat`

Quality gates before implementation:

- Constitution Check in `plan.md` MUST pass (see `.specify/templates/plan-template.md`).
- `/speckit.clarify` or `/speckit.analyze` SHOULD be used when specs or tasks are ambiguous.

## Governance

This constitution supersedes ad-hoc preferences in chat when they conflict. Amendments require:

1. Explicit user approval of the principle change.
2. Update to `.specify/memory/constitution.md` with version bump and amended date.
3. Sync check of dependent templates (`plan`, `spec`, `tasks`) when principles change.

All feature plans and reviews MUST verify compliance with Core Principles. Violations MUST
be documented in the plan's Complexity Tracking table with justification, or the design
MUST be simplified to comply.

**Version**: 1.0.0 | **Ratified**: 2026-06-03 | **Last Amended**: 2026-06-03
