
import type { CompetitionSummary } from "../types";

interface Props {
    data: CompetitionSummary[];
}

export function SummaryTable({ data }: Props) {
    return (
        <table>
            <thead>
                <tr>
                    <th>Competition</th>
                    <th>Number of Teams</th>
                </tr>
            </thead>
            <tbody>
                {data.map((row) => (
                    <tr key={row.competition}>
                        <td>{row.competition}</td>
                        <td>{row.number_of_teams}</td>
                    </tr>
                ))}
            </tbody>
        </table>
    );
}