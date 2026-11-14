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
    room = [v / 12 for v in layout["room_in"]] if layout.get("room_in") else layout.get("room_ft", [18, 12])
    placed = layout["items"]
    L = []
    L.append("# Equipment Schedule - %s" % layout.get("name", "Layout"))
    L.append("")
    L.append("**Room:** %s x %s ft | **Pack:** %s" % (room[0], room[1], layout.get("pack", "restaurant")))
    L.append("")
    L.append("| # | Equipment | Size (in) | Utility | Typical price (US$) | Reference |")
    L.append("|---|-----------|-----------|---------|---------------------|-----------|")
    price_total, price_n, clear_n = 0, 0, 0
    hood_groups, warnings = {}, []
    rects = []
    for n, p in enumerate(placed, 1):
        item = LIB.get(p["id"])
        if item is None:
            warnings.append("Unknown equipment id skipped: %s" % p["id"])
            continue
        w, d = eff(item, p)
        rects.append((p["id"], p["x_ft"], p["y_ft"], w, d))
        tag = ""
        if item.get("hood_required"):
            g = p.get("hood_group", 1)
            if g:
                hood_groups.setdefault(g, [0.0, 0])
                hood_groups[g][0] += item["d_in"] if p.get("rotated") else item["w_in"]
                hood_groups[g][1] += 1
                tag = " [Hood %d]" % g
            else:
                tag = " [No hood]"
        price = item.get("price_usd_typical")
        if price:
            price_total += price; price_n += 1; price_cell = "~$" + format(price, ",")
        else:
            clear_n += 1; price_cell = "Not clear"
        L.append("| %d | %s (%s)%s | %s x %s | %s | %s | %s |" % (n, item["name_en"], item["name_zh"], tag, item["w_in"], item["d_in"], item["utility"], price_cell, item["reference_search"]))
    L.append("")
    L.append("**Estimated equipment total (typical reference prices, US$): $%s** across %d priced item(s); %d item(s) Not clear and not included. Prices are rough public-listing references only - confirm current prices with suppliers before budgeting." % (format(price_total, ","), price_n, clear_n))
    for i in range(len(rects)):
        for j in range(i + 1, len(rects)):
            a, b = rects[i], rects[j]
            if a[1] < b[1] + b[3] and b[1] < a[1] + a[3] and a[2] < b[2] + b[4] and b[2] < a[2] + a[4]:
                warnings.append("Overlap: %s and %s" % (a[0], b[0]))
    for r in rects:
        if r[1] + r[3] > room[0] + 0.01 or r[2] + r[4] > room[1] + 0.01:
            warnings.append("Outside room: %s" % r[0])
    L.append("")
    if hood_groups:
        L.append("## Kitchen exhaust (preliminary estimate)")
        L.append("Hood sizing rule used by this tool: hood length = total equipment width + 1 in spacer between each pair of equipment + 6 in at the left end + 6 in at the right end, minimum 48 in. A kitchen can have more than one hood - assign cooking equipment to Hood 1, Hood 2, Hood 3 in the designer.")
        for g in sorted(hood_groups):
            equip, count = hood_groups[g]
            line = equip + (count - 1) * 1
            hood_in = max(48, line + 12)
            cfm = int(hood_in / 12 * 300 + 0.5)
            L.append("- Hood %d: equipment %.1f in + %d x 1 in spacers + 6 in left + 6 in right = %.1f in minimum hood length; rough exhaust at 300 CFM per foot of hood (medium duty): %d CFM - a designer must confirm the real rate to NFPA 96 and the Ontario Building Code" % (g, equip, count - 1, hood_in, cfm))
        L.append("")
    plan_hoods = layout.get("hoods") or []
    if plan_hoods:
        L.append("## Hoods shown on the plan")
        for h in plan_hoods:
            L.append("- Hood %s: drawn at x %s ft, y %s ft%s, length %s in" % (h.get("group"), h.get("x_ft"), h.get("y_ft"), ", vertical" if h.get("rotated") else "", h.get("length_in")))
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
