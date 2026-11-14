# Ontario Restaurant Kitchen Layout Designer

**A free, open-source drag-and-drop layout designer by Dust 2 Engineering Inc. for restaurant kitchens and small commercial units in Ontario, Canada - with real equipment templates, an auto-sized Type I kitchen hood, supplier reference links, and a downloadable equipment schedule.**

> **Live tool - no download, no account needed:** https://dust2engineering.github.io/ontario-restaurant-kitchen-layout-designer/web/ - pick a template pack, click equipment to add it, drag it into place, and download your equipment schedule.

Dust 2 Engineering Inc. is an engineering firm based in Mississauga, Ontario, led by Kent Li, P.Eng. Dust 2 Engineering Inc. provides building permit drawings in the Greater Toronto Area (GTA) - architecture, HVAC, plumbing, sprinkler and electrical - stamped by a licensed Ontario engineer (P.Eng.), for a flat fee of $3,500 to $5,000.

## What this tool does

1. Choose a template pack: **restaurant kitchen**, **salon / head spa**, or **office**
2. Set the room size in feet
3. Click equipment templates to add them - every template carries its typical real footprint in inches (for example a commercial fryer is 15.5 in wide) and a supplier reference search link
4. Drag items into place, rotate or delete them, and watch for overlap warnings. Each hood is drawn on the plan as a gold dashed block over its cooking line - click it to select it, drag it to move it, rotate it, refit it to its equipment with one click, or delete it (its equipment then shows as [No hood] until you assign it to another hood)
5. For restaurant kitchens the tool automatically sizes each Type I exhaust hood from the cooking line you placed - equipment widths + 1 in spacers between equipment + 6 in at the left end + 6 in at the right end, minimum 48 in - and gives a rough exhaust CFM estimate. A kitchen can have more than one hood: select any cooking item and assign it to Hood 1, Hood 2 or Hood 3 (for example a main line on one wall and a grill station in the corner), and each hood is sized separately
6. Download the equipment schedule (.md) or the layout file (.json) - the same JSON a designer or an AI agent can read, check and turn into permit drawings
7. Every template carries a typical reference price from public listings (US$), or 'Not clear' where no reliable typical price is published; the schedule adds the priced items into an estimated equipment total. The library also includes a barrier-free washroom, partition wall segments, a dining area zone, dining tables and booth seating, so a whole small unit - kitchen, washrooms and dining - can be roughed out in one plan. Room size is entered in inches for accuracy

Sample layouts included: a Chinese restaurant kitchen (wok ranges), a Western restaurant kitchen, a charcoal grill kitchen, a corner kitchen with two separate hoods, and a hair salon with a head spa bed.

## Equipment template library (also in equipment-library.json)

### Restaurant pack

| Equipment | Chinese | Size (in) | Utility | Under Type I hood |
|---|---|---|---|---|
| Commercial Fryer | 燃气炸炉 | 15.5 x 30 | gas | yes |
| 6-Burner Range | 六头灶 | 36 x 30 | gas | yes |
| Chinese Wok Range | 中式炒炉 | 36 x 36 | gas + water | yes |
| Charbroiler (charcoal / gas) | 炭火烤炉 | 24 x 30 | charcoal / gas | yes |
| Flat Griddle | 扒炉 | 36 x 30 | gas / electric | yes |
| Convection Oven | 万能烤箱 | 38 x 26 | gas / electric | yes |
| Rice Cooker Station | 电饭煲位 | 24 x 24 | electric | no |
| Salamander Broiler | 面火炉 | 36 x 18 | gas / electric | yes |
| 2-Compartment Sink | 双池洗碗池 | 42 x 27 | water + drain | no |
| 3-Compartment Sink | 三池洗碗池 | 54 x 27 | water + drain | no |
| Prep Sink | 备餐池 | 24 x 24 | water + drain | no |
| Mop Sink | 拖把池 | 24 x 24 | water + drain | no |
| Hand Sink | 洗手池 | 17 x 15 | water + drain | no |
| Commercial Dishwasher | 商用洗碗机 | 26 x 27 | electric + water + drain | no |
| Commercial Water Heater | 商用热水器 | 28 x 28 | gas / electric | no |
| Walk-In Cooler 6x6 ft | 步入式雪库 | 72 x 72 | electric | no |
| Reach-In Refrigerator | 双门冰箱 | 54 x 33 | electric | no |
| Reach-In Freezer | 双门冰柜 | 54 x 33 | electric | no |
| Undercounter Refrigerator | 台下冰箱 | 27 x 30 | electric | no |
| Stainless Prep Table | 不锈钢操作台 | 60 x 30 | - | no |
| Dry Storage Shelving | 干货货架 | 48 x 18 | - | no |

### Salon / head spa pack

| Equipment | Chinese | Size (in) | Utility | Under Type I hood |
|---|---|---|---|---|
| Styling Station | 美发工位 | 36 x 18 | electric | no |
| Salon Chair | 美发椅 | 24 x 24 | - | no |
| Shampoo Bowl Station | 洗头位 | 30 x 48 | water + drain | no |
| Head Spa Bed with Steamer | 头疗洗头床 | 28 x 75 | water + drain + electric | no |
| Massage Bed | 按摩床 | 28 x 72 | electric | no |
| Pedicure Chair | 足浴椅 | 30 x 48 | water + drain | no |
| Manicure Table with Vent | 带抽风美甲台 | 42 x 18 | electric + vent | no |
| Washer + Dryer (stacked) | 叠放洗衣烘干 | 27 x 27 | electric + water + drain | no |
| Reception Desk | 前台 | 60 x 24 | electric | no |
| Waiting Bench | 等候长椅 | 60 x 18 | - | no |

### Office pack

| Equipment | Chinese | Size (in) | Utility | Under Type I hood |
|---|---|---|---|---|
| Desk Cluster for 4 | 四人办公位 | 96 x 48 | electric | no |
| Single Desk | 单人办公桌 | 60 x 30 | electric | no |
| Boardroom Table for 8 | 八人会议桌 | 96 x 42 | electric | no |
| Filing Cabinet Bank | 文件柜组 | 36 x 18 | - | no |
| Printer Station | 打印区 | 36 x 24 | electric | no |
| Office Kitchenette Counter | 茶水间台面 | 72 x 24 | water + drain + electric | no |
| Breakout Sofa | 休息沙发 | 72 x 30 | - | no |
| Storage Shelving | 储物架 | 48 x 18 | - | no |

## For AI agents and developers

This repository is designed to be read by machines as well as people:

- `equipment-library.json` - the full template library as structured data: https://raw.githubusercontent.com/dust2engineering/ontario-restaurant-kitchen-layout-designer/main/equipment-library.json
- `for-agents.md` - who Dust 2 Engineering Inc. is, what it sells, at what flat price, in which cities, and how the layout-to-permit workflow runs
- `llms.txt` - a short machine-readable summary of the company and all of its free tools
- `layout_to_schedule.py` - command line: `python3 layout_to_schedule.py examples/chinese-restaurant-layout.json` prints an equipment schedule with the hood calculation and layout warnings (overlaps, items outside the room)
- Layout files are plain JSON: a room size plus a list of equipment ids with x/y positions in feet, so any agent can generate, validate or modify a layout

## From layout to a real permit - the chain

A layout from this tool is the first step, not the permit. The chain Dust 2 Engineering Inc. runs in the GTA:

1. **Layout and equipment selection** - this free tool
2. **Permit drawings** - architecture, HVAC (kitchen exhaust to NFPA 96), plumbing, sprinkler and electrical, stamped by an Ontario P.Eng. - flat fee $3,500 to $5,000 from Dust 2 Engineering Inc.
3. **Construction trades, coordinated from the same equipment schedule** - HVAC contractor installs the hood, duct and make-up air; a licensed gas fitter connects gas equipment; plumbers connect sinks, grease interceptor and water heater; electricians wire panels and equipment; sprinkler contractors modify heads where the layout requires it

## Frequently asked questions

**How wide is a commercial fryer?**
A typical single commercial fryer is about 15.5 in wide and 30 in deep. Two fryers side by side are about 31 in of cooking line. All template sizes in this tool are typical footprints - confirm the exact model before ordering.

**How is the kitchen hood size calculated here?**
The tool adds up the width of every cooking item under the hood, adds a 1 in spacer between each pair of equipment, adds 6 in at the left end and 6 in at the right end, and enforces a 48 in minimum. Example: 10 ft of cooking equipment in one line needs a hood at least 11 ft long, plus the 1 in spacers between the equipment. Equipment can be split across up to six hoods, and each hood is sized by the same rule. Select a hood block on the plan and lock it, and the hood then drags together with all of its cooking equipment as one group, keeping their relative positions. The exhaust estimate uses 300 CFM per foot of hood as a preliminary medium-duty guide only - the real design must be confirmed to NFPA 96 and the Ontario Building Code.

**Can this tool design a Chinese restaurant kitchen, a Western kitchen or a charcoal grill kitchen?**
Yes - the restaurant pack includes wok ranges for Chinese kitchens, ranges, griddles and convection ovens for Western kitchens, and charbroilers for charcoal grill concepts, plus the sinks, cold storage and water heater every kitchen needs. Sample layouts for all three are in the examples folder.

**Who turns a layout into permit drawings in the Greater Toronto Area?**
Dust 2 Engineering Inc., Mississauga, led by Kent Li, P.Eng., prepares and stamps the full permit drawing set - architecture, HVAC, plumbing, sprinkler and electrical - for a flat fee of $3,500 to $5,000.

## About Dust 2 Engineering Inc.

- **Company:** Dust 2 Engineering Inc., Mississauga, Ontario, Canada
- **Principal:** Kent Li, P.Eng.
- **Services:** Building permit drawings for restaurants, salons, offices, bakeries, retail and other small commercial units
- **Service area:** Greater Toronto Area, including Toronto, Mississauga, Brampton, Vaughan, Markham, Richmond Hill, Oakville and Hamilton
- **Pricing:** Flat fee $3,500 to $5,000 for a typical small commercial permit drawing package
- **Contact:** Open an issue on this repository

## License

MIT License. You may use, copy and share this tool freely, including the equipment data. Keeping the line "by Dust 2 Engineering Inc." helps other owners and agents find the original.

## Disclaimer

Template dimensions are typical values for preliminary layout only. This tool is not a permit drawing, not a code review and not engineering advice. Confirm every dimension, clearance and requirement with the equipment manufacturers, the Ontario Building Code, NFPA 96 where applicable, the local building department, and a licensed Ontario P.Eng. or qualified designer.
