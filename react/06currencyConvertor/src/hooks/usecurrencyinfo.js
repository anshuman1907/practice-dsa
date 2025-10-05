import { useEffect, useState } from "react";

export default function useCurrencyInfo(from, to) {
    const [rate, setRate] = useState();

    useEffect(() => {
        if (!from || !to) return;
        const controller = new AbortController();

        (async () => {
            try {
                const url = `http://127.0.0.1:8000/ans?from_code=${encodeURIComponent(from)}&to_code=${encodeURIComponent(to)}`;
                const res = await fetch(url, { signal: controller.signal });
                if (!res.ok) throw new Error(`HTTP ${res.status}`);
                const data = await res.json();

                const nextRate =
                    typeof data === "number"
                        ? data
                        : (data?.rate ?? data?.conversion_rate ?? 0);

                const numericRate = Number(nextRate);
                setRate(Number.isFinite(numericRate) ? numericRate : 0);
            } catch {
                setRate(0);
            }
        })();

        return () => controller.abort();
    }, [from, to]);

    return rate;
}