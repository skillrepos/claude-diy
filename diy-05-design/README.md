# DIY 5 — Claude Design: from a lineup to a flyer you can edit

**Goes with:** Demo 5 in the talk (Claude Design).
**Time:** about 8 minutes, including a minute or two while the first version builds.
**Where:** [claude.ai](https://claude.ai) in your browser, or the Claude desktop app. Design needs a paid plan, and the feature is still marked as a preview, so menus move around. Go by what your screen shows.
**Files:** the Riverbend Hackathon's logo and brand notes in [`files/brand/`](files/brand/) (made up):

| File | What it is |
|---|---|
| `riverbend-logo.png` | The hackathon logo |
| `brand.md` | Colors, type and voice in five lines |

**The idea:** DIY 4 picked the three projects for Demo Night. Now you need a flyer. You give Claude the logo and colors and ask for one. It builds a real **design on a canvas** that you can change three ways: with your own hands, with a comment pinned to one spot, or by asking in chat. Then it leaves as a real file.

**What you'll practice:**

1. **Same Claude, new kind of output:** you ask in a normal conversation and get a canvas, not a picture.
2. **Feed it your stuff:** a logo, colors, an old deck, a screenshot of a page you like.
3. **Three ways to change it:** edit it directly, pin a comment to one element, or ask in chat for bigger changes.
4. **It leaves as a real file** (image, PDF, web page and more), or as a link others can comment on.

---

## Get ready

- Download `riverbend-logo.png` and `brand.md` from `files/brand/` (or clone this repo).
- Start a **new conversation**, and **not an incognito one**: Design isn't available in incognito chats (Claude will tell you it has no canvas and draw the flyer inline instead).
- A capable model works best: pick Opus (or similar) below the message box.
- **Did DIY 4 in the desktop app?** You can do this inside the same **Riverbend judging** project instead and skip attaching files; use the second prompt in step 1.

---

## Steps

### 1. Ask for a design

Attach **both brand files** (drag them in, or use the **+** button), then paste the prompt. You don't need to pick anything special: asking to "design" a flyer is enough. (Some versions also show a **Design** option in the message box; if yours does, you can pick it.)

```text
Design a one-page flyer for Riverbend Hackathon Demo Night: Thursday, January 28, 6:30-8:30 pm, Riverbend Public Library, Community Room. Feature the three finalist projects: "Ride Along" (volunteer drivers for Golden Years Senior Center), "ShelfCount" (donation tracking for Eastside Community Food Bank), and "Foster Match" (foster homes for Riverbend Animal Rescue). Free, all ages, snacks provided. Use the attached logo and brand colors. Warm and community-first, not techy.
```

**Inside your DIY 4 project instead** (no attachments needed):

```text
Design a one-page flyer for Demo Night, featuring the three projects picked in the judging spreadsheet. Use event.md for the details and the logo and colors in the brand folder. Warm and community-first, not techy.
```

### 2. Wait while it builds

It usually takes about two minutes. A design panel opens beside the chat while it works. It isn't drawing a picture: it's laying out a real page, with text you can edit and pieces you can move.

### 3. Look at the canvas

**What you should see:** the flyer on a letter-size artboard with design tools along the top (select, hand, text, frame, sticky note, pen, shapes, zoom), using the teal, sunflower and cream from `brand.md` and the logo near the top. Claude also explains its choices in the chat, and says what it made up (like an intro line) so you can change it.

**If the canvas says it has no artboards yet**, or still shows an older version after Claude says it's done: open the menu next to the design's title (top left of the panel) and choose **Refresh**, or reload the page.

### 4. Change it with your hands

Double-click the time (or any line of text) and retype it, for example change "6:30 - 8:30 pm" to **"6:30 - 9:00 pm"**. No prompt, no waiting. (Or pick the **T** text tool in the toolbar and click the text.)

### 5. Change one spot with a comment

Click the **speech-bubble** button at the top right of the panel to turn on comments, then click the **Foster Match** card and type:

```text
Make this one stand out: add a small "First Demo Night!" badge and a paw print.
```

If the comment doesn't seem to do anything, paste this into the chat instead (it worked in our test run):

```text
Make the Foster Match card stand out: add a small "First Demo Night!" badge and a paw print.
```

### 6. Change the whole thing with chat

Paste:

```text
Make a second version for Instagram: square, bigger headline, and only the date, place and the three project names.
```

**What you should see:** a second artboard, "Instagram post (square)", appears next to the flyer on the same canvas, with a huge "Demo Night" headline. (Use **Refresh** if it doesn't show up.)

### 7. Take it with you

Open the menu next to the design's title and choose **Export**. In our test it offered **HTML** (a web page), **PDF** (for printing), **PNG** (an image) and **More formats and apps**. The **Share** tab, or the **Share** button at the top right, lets you send a link others can view or comment on. Each artboard also has its own small download button.

---

## Start over

Start a new conversation. Nothing on your computer changes.

## If something goes wrong

- **It draws the flyer inline in the chat, or says it has no design canvas:** you're probably in an incognito chat. Start a normal new chat and send the prompt again. Otherwise add "as a design I can edit on a canvas" to your prompt.
- **Claude asks for the date or event name:** check the whole prompt got pasted; the first line carries the event details.
- **The logo doesn't appear:** ask in chat, *"Use the attached logo in the header."* First drafts miss things; that's what the chat is for.
- **Colors are off:** ask, *"Use exactly the colors in brand.md."*
- **The menus look different from this page:** they change often. Look for the same kind of control: edit text, comment, export, share.
