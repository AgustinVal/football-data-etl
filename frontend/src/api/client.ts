

import type { CompetitionSummary } from "../types";

// URL base del backend FastAPI
// En producción esto podría venir desde una variable de entorno
const API_URL = "http://localhost:8000";

export async function fetchSummary(): Promise<CompetitionSummary[]> {
    const res = await fetch(`${API_URL}/summary`);

    // Manejo básico de errores HTTP
    if (!res.ok) {
        throw new Error("Failed to fetch summary");
    }

    // El backend devuelve JSON con la forma:
    // { competition: string, number_of_teams: number }
    return res.json();
}