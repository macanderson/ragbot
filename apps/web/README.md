# Ragbot (Web Application/Frontend)

A modern web application built with Next.js 14, React 18, and TypeScript. This frontend application serves as the user interface for the Ragbot project, providing an intuitive and responsive experience.

## Features

- Next.js 14 for server-side rendering and optimal performance
- React 18 with modern hooks and concurrent features
- TypeScript for type safety and better developer experience
- Tailwind CSS for styling
- ESLint and Prettier for code quality

## Prerequisites

- Node.js 18.x or later
- npm or yarn package manager

## Getting Started

First, install the dependencies:

```bash
npm install
# or
yarn install
```

### Development

### Start the FastAPI server

- Navigate to the FastAPI server directory (e.g., `apps/api`).
- Run the following command to start the server:

```bash
uvicorn main:app --reload
```

- The FastAPI server will be available at `http://localhost:8000`.

### Start the Next.js development server

In the `apps/web` directory, run:

```bash
npm run dev
# or
yarn dev
```

The Next.js application will be available at `http://localhost:3000`.

### Building for Production

To build the application for production, run:

```bash
npm run build
# or
yarn build
```

This will create an optimized production build in the `out` directory.

### Running the Production Build

To start the production server, run:

```bash
npm run start
# or
yarn start
```

The application will be available at `http://localhost:3000`.
