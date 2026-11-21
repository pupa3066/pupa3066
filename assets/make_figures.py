"""Draws the profile README figures as SVG, light and dark. Every number is a measured result from the public repo
github.com/pupa3066/gemma4-agent-track-blind-spots (research/RESULTS_LEDGER.md, SWE-bench Lite, 300 issues)."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
THEMES = {
    "light": dict(bg="#ffffff", fg="#1f2328", muted="#59636e", grid="#d1d9e0", a="#0969da", b="#bf8700", c="#8250df"),
    "dark": dict(bg="#0d1117", fg="#e6edf3", muted="#9198a1", grid="#3d444d", a="#4493f8", b="#d29922", c="#ab7df8"),
}
W, LEFT, RIGHT = 880, 250, 90


def bars(title, subtitle, rows, note, t):
    """rows: (label, value, color key); values are shares 0..1, drawn on a 0..0.6 axis. Final sizes are the static
    attributes; no animation, so the chart reads the same on GitHub, in print and in any viewer."""
    h = 96 + 46 * len(rows) + 54
    span, x0 = W - LEFT - RIGHT, LEFT
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{h}" viewBox="0 0 {W} {h}" '
           f'font-family="-apple-system,Segoe UI,Helvetica,Arial,sans-serif">',
           f'<rect width="{W}" height="{h}" rx="8" fill="{t["bg"]}"/>',
           f'<text x="24" y="36" font-size="19" font-weight="600" fill="{t["fg"]}">{title}</text>',
           f'<text x="24" y="60" font-size="13.5" fill="{t["muted"]}">{subtitle}</text>']
    for v in (0, 0.2, 0.4, 0.6):
        gx = x0 + span * v / 0.6
        out.append(f'<line x1="{gx:.1f}" y1="78" x2="{gx:.1f}" y2="{h - 48}" stroke="{t["grid"]}" stroke-width="1"/>')
        out.append(f'<text x="{gx:.1f}" y="{h - 30}" font-size="12" text-anchor="middle" fill="{t["muted"]}">{v:.1f}</text>')
    for i, (label, val, key) in enumerate(rows):
        y = 92 + 46 * i
        bw = span * val / 0.6
        out.append(f'<text x="{LEFT - 14}" y="{y + 19}" font-size="14" text-anchor="end" fill="{t["fg"]}">{label}</text>')
        out.append(f'<rect x="{x0}" y="{y}" width="{bw:.1f}" height="28" rx="4" fill="{t[key]}">'
                   f'</rect>')
        out.append(f'<text x="{x0 + bw + 10:.1f}" y="{y + 19}" font-size="14" font-weight="600" fill="{t["fg"]}">'
                   f'{val:.3f}</text>')
    out.append(f'<text x="24" y="{h - 10}" font-size="12" fill="{t["muted"]}">{note}</text>')
    out.append("</svg>")
    return "\n".join(out)


FIGS = {
    "coverage": ("What the index can see decides what search can find",
                 "Share of 300 real GitHub issues where search returned the changed code (dense retrieval, SWE-bench Lite)",
                 [("all code indexed", 0.263, "a"), ("a quarter of the code indexed", 0.143, "b")],
                 "Exact McNemar p = 7e-6; holds after Holm correction over 27 primary tests."),
    "chunk-length": ("Chunks longer than the embedder window hide code",
                     "Same 300 issues, same amount of returned text, two chunk sizes",
                     [("dense, 8-line chunks", 0.523, "a"), ("dense, 400-word chunks", 0.377, "b"),
                      ("BM25, 8-line chunks", 0.390, "a"), ("BM25, 400-word chunks", 0.447, "b")],
                     "Dense: p = 2.3e-5, holds after Holm correction. BM25 goes the other way, as an embedder-window effect predicts."),
}

if __name__ == "__main__":
    for name, (title, sub, rows, note) in FIGS.items():
        for theme, t in THEMES.items():
            with open(os.path.join(HERE, f"{name}-{theme}.svg"), "w") as fh:
                fh.write(bars(title, sub, rows, note, t))
    print(sorted(f for f in os.listdir(HERE) if f.endswith(".svg")))
