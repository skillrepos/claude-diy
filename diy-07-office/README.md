# DIY 7 — Claude in Excel and PowerPoint: one conversation, two apps

**Goes with:** Demo 7 in the talk (Excel + PowerPoint).
**Time:** about 10 minutes.
**Where:** desktop **Excel** and **PowerPoint** (Microsoft 365) with the **Claude add-in** installed in both and signed in to a paid Claude plan.
**The problem:** the owners' meeting is today. The finance workbook for **Harborview Coffee Co.** (made up) has a broken formula, and the owners' deck is missing its financial slide. In Excel, Claude finds and fixes the break, showing exactly which cells it means. Then, **without leaving Excel**, you ask it to build the missing slide in the open deck, on the deck's own template. The slide's numbers are only right *because* the workbook got fixed first.

**Files** (in [`files/`](files/), all sample data):

| File | What it is |
|---|---|
| `harborview-fy2026.xlsx` | A one-year P&L by quarter, in $000s. **One formula is broken**, and the error spreads. |
| `harborview-owners-review.pptx` | A 7-slide owners' deck on its own template. Slide 4, **"02 Financial results"**, has nothing after it. That's the gap. |

**What you'll practice:**

1. Claude works **inside** the apps you already use, on the live file, not a copy pasted into a chat.
2. **It shows its work:** cell references you can click, and a fix you approve.
3. **One conversation spans apps.** What it learned in Excel carries into PowerPoint, with no copy-paste.
4. **Your template, your brand:** it reads the deck's layouts, and the result stays editable.

---

## Get ready

From the top of this repo:

```bash
python3 setup_diy.py 7
```

It copies both files to `~/atc-diy/office/`. **Always open those copies**, so you can start over cleanly.

Then:

- [ ] Open `~/atc-diy/office/harborview-fy2026.xlsx` in Excel and `~/atc-diy/office/harborview-owners-review.pptx` in PowerPoint.
- [ ] In **both** apps, open the Claude add-in and check it's **signed in and answering** (send "hi", then start a new conversation). Not installed? Get it from the Office Add-ins store (search "Claude").
- [ ] In the add-in's settings, turn on **"Let Claude work across files"** (wording may vary) in both apps. With it on, Claude in Excel can read and change the open PowerPoint deck.
- [ ] In PowerPoint, go to **slide 4** ("02 Financial results").

---

## Steps

### 1. See the problem

In Excel, look at **Q2** and **FY Total**. Total Revenue, Gross Profit and Operating Income all show **#REF!** in Q2 and for the full year. Gross Margin for Q2 is blank.

### 2. Ask about your own data

In the **Excel** add-in, paste:

```text
Why are Q2 and the full-year totals showing #REF!, and how do I fix it?
```

**What you should see:** an answer that names the cells. **C8** (Q2 Total Revenue) is `=C5+C6+#REF!`: it lost its link to the **Online Store** row (C7), and the error spreads to **F8, C13, F13, C20 and F20** (and blanks C14). The cell references should be clickable. Click one and Excel jumps there.

### 3. Fix it, with your OK

Paste:

```text
Go ahead and fix it.
```

**What you should see:** if it asks before changing the cell, read it and approve. Then the errors clear:

| | Q1 | Q2 | Q3 | Q4 | FY |
|---|---|---|---|---|---|
| Total Revenue | 510 | **537** | 567 | 628 | **2,242** |
| Gross Profit | 341 | **360** | 377 | 426 | **1,504** |
| Operating Income | 107 | **119** | 133 | 168 | **527** |

One formula, and everything downstream recalculates. A correct fix is `=SUM(C5:C7)` or `=C5+C6+C7`; either gives 537.

### 4. Same conversation, different app

**Still in the Excel add-in**, paste:

```text
Now add a financial results slide to my open owners' deck, right after the "Financial results" divider: full-year revenue and operating income, a chart of operating income by quarter, and three short takeaways. Match the deck's template and the style of its other chart slide.
```

**What you should see:** it notes that it's working in PowerPoint. You didn't copy a number, switch windows or explain the workbook again.

### 5. Check the slide

Switch to PowerPoint and go to the new slide (slide 5).

- **The template:** same espresso footer, fonts and colors as the other slides, and ideally the same **"HV Chart and Takeaways"** layout as the "Wholesale accounts grew every quarter" slide (slide 6 before, slide 7 now). Flip to it and compare.
- **The numbers:** Q2 operating income is **119**, and the year is **527**. Those are only right because you fixed the workbook first.
- **It's editable:** click the chart. If the chart tools appear in the ribbon, it's a real PowerPoint chart, not a picture.

---

## Want more? (optional)

If you have **Word** with the Claude add-in, open a blank document and paste into either sidebar:

```text
Draft a five-sentence note to the owners in my open Word document: what was broken in the Q2 numbers, what we changed, and the corrected full-year operating income.
```

---

## Start over

Close the two files without saving (or quit Excel and PowerPoint), then:

```bash
python3 setup_diy.py 7   # from the top of this repo
```

Start a new conversation in each add-in.

## If something goes wrong

- **The add-in isn't answering:** sign in again from its sidebar.
- **Step 4 says it can't reach PowerPoint:** "work across files" is off, or the PowerPoint add-in isn't open. Workaround: in Excel ask *"Give me full-year revenue, operating income, and operating income by quarter as a small table,"* copy it, then in the **PowerPoint** add-in ask *"Add a slide after the Financial results divider with this data, a chart of operating income by quarter, and three takeaways, using this deck's template,"* and paste.
- **Q2 on the slide isn't 119:** it used the old numbers. Say so: *"Re-read the workbook and update the slide."* This is why you check.
- **It suggests a different fix:** read its reasoning. If Q2 revenue comes out at 537, it's right.
- **The chart is shapes, not a chart:** still fine: every piece is an editable PowerPoint shape.
- **No Excel or PowerPoint?** You can get a feel for it in a regular Claude chat: attach both files and ask the same questions. Claude will explain the fix and can make a new copy of the deck, but you lose the "live file, no copy-paste" part.
