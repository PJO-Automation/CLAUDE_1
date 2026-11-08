# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository status

This file describes **Shinobi**, a Next.js blog built as a Claude Code learning project. The application code (`src/`, `package.json`) has **not been committed yet**: the repo currently holds only this file and an empty `README.md`. Until that code is added, the commands and paths below will not resolve. Check before relying on them.

Node.js and npm are not on the PATH on the current Windows machine, so `npm` commands fail until Node is installed.

## Commands

- `npm run dev` - dev server with Turbopack
- `npm run build` - production build
- `npm run start` - serve the production build
- `npm run lint` - Next.js linting
- `npm run test` - run the Vitest suite
- `npm run test:ui` - Vitest with the browser UI
- `npx vitest run src/path/to/file.test.tsx` - run one test file
- `npx vitest run -t "test name"` - run tests whose name matches

## Stack

Next.js 15 (App Router, Turbopack), React 19 + TypeScript, Tailwind CSS v4, Vitest + React Testing Library (jsdom), DOMPurify, and Hygraph as a headless CMS queried over GraphQL.

## Architecture

### Content flow
- Blog content comes from Hygraph. GraphQL queries live in `src/lib/queries.ts` and shared types in `src/lib/types.ts`.
- The `HYGRAPH_ENDPOINT` environment variable must be set, or blog pages cannot fetch data.
- Pages render on the server with 1-hour revalidation (ISR).
- CMS HTML is untrusted. It must pass through `src/lib/sanitize.ts` (DOMPurify with a strict allowlist) before it is rendered. Never bypass this when adding a new place that renders CMS content.

### Routes (`src/app/`)
- `layout.tsx` - root layout; renders the header and the dark-mode toggle
- `page.tsx` - homepage linking to the blog and preview pages
- `blog/` - post listing and individual post pages
- `preview/` - component preview page

### Theming
- Colors are CSS variables in `globals.css`, with separate light and dark values, and are mapped to Tailwind color tokens.
- Dark mode is applied by toggling a class on the root `<html>` element (`src/components/DarkModeToggle.tsx`).
- Components mix Tailwind classes and inline styles.
- Fonts: Rubik for headings and Merriweather for body text, both loaded from Google Fonts.

### Conventions
- Import from `src` using the `@/*` path alias.
- Reusable hooks go in `src/components/hooks/`, and UI primitives in `src/components/ui/` (for example `ui/Button/` with variants).
- Test setup is in `src/test/setup.ts`, and custom Vitest type declarations are in `src/test/vitest.d.ts`.
