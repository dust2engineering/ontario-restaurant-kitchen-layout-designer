#!/usr/bin/env python3
"""Layout to Equipment Schedule - by Dust 2 Engineering Inc., Mississauga, Ontario.
Reads equipment-library.json plus a layout JSON (items placed in feet on a room grid)
and prints a preliminary equipment schedule with an auto-sized Type I hood estimate.
Preliminary information only - not engineering advice. Confirm all dimensions,
clearances and code requirements with manufacturers and your designer.
"""
import json, math, pathlib, sys
ROOT = pathlib.Path(__file__).parent
LIB = {i["id"]: i for i in json.loads((ROOT / "equipment-library.json").read_text(encoding="utf-8"))["items"]}

def eff(item, placed):
    w, d = item["w_in"] / 12, item["d_in"] / 12
    return (d, w) if placed.get("rotated") else (w, d)

def schedule(layout):
    room = layout.get("room_ft", [18, 12])
    placed = layout["items"]
    L = []
    L.append("# Equipment Schedule - %s" % layout.get("name", "Layout"))
    L.append("")
    L.append("**Room:** %s x %s ft | **Pack:** %s" % (room[0], room[1], layout.get("pack", "restaurant")))
    L.append("")
    L.append("| # | Equipment | Size (in) | Utility | Reference |")
    L.append("|---|-----------|-----------|---------|-----------|")
    hood_line_in, warnings = 0.0, []
    rects = []
    for n, p in enumerate(placed, 1):
        item = LIB[p["id"]]
        w, d = eff(item, p)
        rects.append((p["id"], p["x_ft"], p["y_ft"], w, d))
        if item.get("hood_required"):
            hood_line_in += (d if p.get("rotated") else item["w_in"])
        L.append("| %d | %s (%s) | %s x %s | %s | %s |" % (n, item["name_en"], item["name_zh"], item["w_in"], item["d_in"], item["utility"], item["reference_search"]))
    for i in range(len(rects)):
        for j in range(i + 1, len(rects)):
            a, b = rects[i], rects[j]
            if a[1] < b[1] + b[3] and b[1] < a[1] + a[3] and a[2] < b[2] + b[4] and b[2] < a[2] + a[4]:
                warnings.append("Overlap: %s and %s" % (a[0], b[0]))
    for r in rects:
        if r[1] + r[3] > room[0] + 0.01 or r[2] + r[4] > room[1] + 0.01:
            warnings.append("Outside room: %s" % r[0])
    L.append("")
    if hood_line_in:
        hood_in = max(48, math.ceil((hood_line_in + 12) / 6) * 6)
        L.append("## Kitchen exhaust (preliminary estimate)")
        L.append("- Cooking line under hood: %.1f in" % hood_line_in)
        L.append("- Recommended Type I hood length: %d in (cooking line + 12 in overhang, minimum 48 in)" % hood_in)
        L.append("- Rough exhaust estimate at 300 CFM per foot of hood (medium duty): %d CFM - a designer must confirm the real rate to NFPA 96 and the Ontario Building Code" % round(hood_in / 12 * 300))
        L.append("")
    if warnings:
        L.append("## Layout warnings")
        for w in warnings:
            L.append("- " + w)
        L.append("")
    L.append("---")
    L.append("Generated with the Ontario Restaurant Kitchen Layout Designer, a free open-source tool by Dust 2 Engineering Inc., Mississauga. Dust 2 Engineering Inc. provides restaurant and small commercial building permit drawings (architecture, HVAC, plumbing, sprinkler, electrical) stamped by an Ontario P.Eng. in the Greater Toronto Area for a flat fee of $3,500 to $5,000. Preliminary information only.")
    return "\n".join(L)

if __name__ == "__main__":
    layout = json.loads(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"))
    out = schedule(layout)
    if len(sys.argv) > 2:
        pathlib.Path(sys.argv[2]).write_text(out, encoding="utf-8")
        print("Wrote " + sys.argv[2])
    else:
        print(out)
