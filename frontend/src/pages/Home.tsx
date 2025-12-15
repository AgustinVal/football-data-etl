import { useEffect, useState } from "react";
import { fetchSummary } from "../api/client";
import type { CompetitionSummary } from "../types";
import { SummaryTable } from "../components/SummaryTable";

export function Home() {
    // Estado para almacenar los datos del backend
    const [data, setData] = useState<CompetitionSummary[]>([]);
    const [loading, setLoading] = useState(true);

    // Se ejecuta una sola vez al montar el componente
    useEffect(() => {
        fetchSummary()
            .then(setData)
            .finally(() => setLoading(false));
    }, []);
    
    if (loading) return <p>Loading...</p>;
    
    return (
        <>
            <h1>Football Competitions Summary</h1>
            <SummaryTable data={data} />
        </>
    );
}