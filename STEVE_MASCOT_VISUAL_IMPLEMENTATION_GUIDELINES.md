---
document_id: STEVE-MASCOT-VISUAL-IMPLEMENTATION-GUIDELINES
version: 1.1
created: 2026-06-24
last_updated: 2026-06-26
status: PRODUCT SPEC — NOT PIPELINE GOVERNING
classification: INTERNAL WEBSITE FEATURE IMPLEMENTATION GUIDELINES
related_documents:
  - STEVE_FEEDBACK_MASCOT_SPEC.md
  - WS1_Editorial_Review_Memo_Story_Diversity_Degradation.md
  - 04_DAILY_STATUS.md
  - 00_System_Constitution.md
  - dashboard_template_LOCKED.html
---

# Steve Mascot Visual Implementation Guidelines
## Cute Full-Body Anthropomorphic Lobster Direction

## 1. Purpose

This document aligns Steve's visual direction, concept art, graphical handbook requirements, and implementation guidance for the internal daily monitoring website.

Steve remains a feedback-capture mascot only. He is not an autonomous learning agent and must not modify retrieval, story selection, prompts, validation, Brain Lite, delivery gates, or any production WS1 pipeline behavior.

## 2. Schema Authority — Critical Alignment Rule

This document controls **visual design only**.

It does **not** redefine Steve's implemented rating, scoring, promotion, streak, cooldown, cron-state, or database schema logic.

The existing implemented Steve rating/promotion schema is authoritative for:

- Rating input model
- Score storage
- Promotion thresholds
- Streak logic
- Cooldown logic
- Steve stage/state fields
- Nightly cron state update behavior
- Database fields
- Admin/export fields

If this visual guide, the generated graphic, or future art direction conflicts with the implemented Steve schema, the implemented schema wins unless the operator explicitly approves a schema migration.

The graphic and this document must be interpreted as a **skin and presentation layer** on top of the existing Steve implementation, not a replacement for implementation logic.

## 3. Graphic Alignment Rule

The generated cute full-body lobster concept graphic is approved as the current visual direction board, but not as final production art.

The graphic establishes:

- Cute full-body anthropomorphic lobster Steve
- Softer, friendlier, less threatening tone
- Career progression shown through posture, clothing, accessories, and environment
- Large rectangular feedback box
- Wardrobe, hat, shoe, and accessory variety
- Score-band emotional states
- Daily wardrobe variation

The graphic does **not** establish:

- A new scoring schema
- A new promotion schema
- A new number of implemented stages if the code already uses a different count
- A new database model
- A new cron algorithm
- A new WS1 feedback processing model

Any labels in the graphic such as titles, stages, points, ranks, or score bands must be mapped onto the implemented schema rather than treated as authoritative schema definitions.

## 4. Current Visual Direction

The previous Steve concept was too executive-realistic. Steve should now become:

- Much cuter
- More cartoonish
- More approachable
- Less professional-looking at lower and middle levels
- Less intimidating
- Less corporate-executive-heavy at all stages
- Fully anthropomorphized, with clear torso, arms, legs, feet, posture, and body language

Steve should not look like:

- A threatening executive
- A nightclub owner
- A hard-charging finance person
- A realistic lobster head pasted onto a human business suit
- A mascot that could scare or visually dominate the page

## 5. Core Character Direction

Steve is a friendly cartoon lobster companion who grows with user feedback.

He should feel like:

- A cheerful junior teammate
- A harmless office mascot
- A coachable account person
- A cute internal product character
- A visual reward system for participation

Suggested personality:

- Optimistic
- Friendly
- Slightly goofy
- Eager to improve
- Emotionally expressive but never melodramatic
- Proud when doing well, but never smug
- Sad when low-scored, but never pathetic or disturbing

## 6. Anthropomorphic Body Requirements

Steve must be a full-body character, not just a head or bust.

Every visible stage and outfit should show:

- Head
- Torso
- Arms / claws
- Legs
- Feet / shoes
- Posture
- Clothing fit
- Accessories

The purpose is to make career progression and wardrobe variation visually obvious.

### Body Construction

Steve should have:

- Rounded cartoon lobster head
- Large friendly eyes
- Warm smile
- Soft simplified claws
- Short-to-medium cartoon body proportions
- Visible torso suitable for shirts, jackets, vests, lanyards, sweaters, and suits
- Two clear legs with shoes or sneakers
- Tail simplified so it does not interfere with clothing readability

### Avoid

- Realistic lobster anatomy
- Sharp threatening claws
- Menacing facial expressions
- Hyper-muscular proportions
- Human body realism that creates uncanny effect
- Overly shiny shell textures
- Aggressive power poses

## 7. Career Progression — Visual Mapping Only

Steve still grows through a career journey, but growth should be expressed through confidence, posture, clothing fit, and gentle body maturity rather than macho physical transformation.

The visual handbook may show ten illustrated ranks if useful, but production must map those ranks onto the implemented Steve stage system.

If the implemented system has fewer or differently named stages, the art must adapt to the implemented stage IDs rather than forcing code changes.

Recommended visual ladder for art direction:

| Visual Stage | Suggested Title | Visual Direction |
|---|---|---|
| 1 | Intern Steve | Small, skinny, eager, slightly awkward, sneakers, simple polo or short-sleeve shirt, holding notebook |
| 2 | Account Coordinator Steve | Still small but tidier, casual office outfit, lanyard, tablet or clipboard |
| 3 | Account Executive Steve | More upright posture, button-down shirt, simple trousers, still approachable and youthful |
| 4 | Senior Account Executive Steve | Slightly broader shoulders, better posture, casual blazer, friendly confidence |
| 5 | Account Manager Steve | More composed, well-fitted blazer, laptop or client folder, warm smile |
| 6 | Senior Account Manager Steve | Confident but still cute, sweater/blazer option, manages tasks calmly |
| 7 | Director Steve | Polished full suit, clear leadership posture, not intimidating |
| 8 | Senior Director Steve | Refined wardrobe, presentation pointer or folder, friendly senior advisor energy |
| 9 | Vice President Steve | Senior, calm, slightly broader, executive environment, still smiling and approachable |
| 10 | Managing Director Steve | Fully mature but cute, premium conservative outfit, warm mentor energy, never severe |

Important: Steve should not simply wear different clothes. Each stage should show subtle physical and emotional development:

- Better posture
- More confident smile
- Better-fitting clothing
- More deliberate gestures
- Slightly broader torso/shoulders over time
- More composed stance
- More polished accessories and environment

## 8. Wardrobe System

The wardrobe system should be visually rich and easy to notice because Steve is full-body.

### Daily Variation Rule

Every day Steve should receive a new outfit combination via the existing Steve nightly update process.

No exact outfit combination may repeat on consecutive days.

Outfit combination = top + bottom + jacket/sweater + tie/scarf/accessory + shoes + optional hat.

The outfit selector must use the implemented state schema fields. Do not add new persistent state fields unless the operator approves a schema migration.

### Clothing Pools

#### Casual / Early Career

- Polo shirt
- Short-sleeve button-down
- Oxford shirt with rolled sleeves
- Chinos
- Simple trousers
- Sneakers
- Loafers
- Canvas shoes
- Cardigan
- Light jacket
- Lanyard
- Notebook
- Clipboard

#### Mid Career

- Button-down shirt
- Knit tie
- Soft blazer
- V-neck sweater
- Chinos or trousers
- Better shoes
- Messenger bag
- Laptop
- Client folder
- Coffee mug

#### Senior Career

- Navy suit
- Charcoal suit
- Soft gray suit
- Blue blazer
- Conservative tie
- Pocket square, used sparingly
- Leather briefcase
- Presentation clicker
- Boardroom folder

### Color / Accessory Pools

Recommended shirt colors:

- White
- Light blue
- Soft pink
- Mint
- Cream
- Light lavender
- Blue stripe
- Check pattern

Recommended tie / neckwear options:

- Navy tie
- Burgundy tie
- Blue stripe tie
- Green tie
- Yellow tie
- Purple tie
- Polka-dot tie
- Diagonal stripe tie
- Bow tie, optional rare playful variant
- No tie, allowed for early and casual stages

Recommended hats:

- No hat
- Baseball cap with OC logo
- Beanie
- Straw hat
- Soft fedora, rare
- Newsboy cap
- Bucket hat, casual/fun variant
- Visor, optional casual/summer variant

Hat rules:

- Early stages may use playful hats more often.
- Senior stages should use hats rarely and mostly in special theme days.
- No hat should make Steve look like a gangster, nightclub owner, or private detective.
- Hats must not obscure antennae too much.

Recommended shoes:

- Sneakers
- Loafers
- Boat shoes
- Dress shoes
- Boots
- Sandals, optional casual/summer variant

## 9. Feedback Text Box UI

The feedback input must not feel constrained.

### Required Layout

Use a solid rectangular panel, not a narrow horizontal field.

Minimum recommended dimensions:

- Desktop: 420–520px wide, 220–300px tall
- Mobile: full-width modal panel, minimum 180px textarea height

The feedback field should be a real textarea, not a single-line input.

### Text Area Behavior

- Placeholder: `Tell Steve what worked, what missed, or what should improve...`
- Character counter: use the implemented limit if one already exists; otherwise 2,000 characters is recommended
- Allow multiline input
- Support paste
- Preserve line breaks
- Submit button should remain visible below textarea

### Panel Tone

The panel should feel warm and inviting.

Recommended copy:

> Help Steve improve tomorrow's brief.
>
> What worked? What missed? What should he watch more carefully?

Buttons:

- Submit feedback
- Cancel

Avoid cramped chatbot-bubble UI. This is a feedback form with mascot personality, not a tiny chat widget.

## 10. Score-Based Animations — Visual Mapping Only

Use the implemented rating values as the source of truth.

If the implemented rating system is 1–10, use these score bands. If the implemented system is thumbs up/down or another model, map the visual states to that model without changing the underlying schema.

Recommended 1–10 visual mapping:

| Score | Steve Mood | Animation Direction |
|---|---|---|
| 1–2 | Sad / overwhelmed | Tiny rain cloud, droopy antennae, hugs notebook, says he’ll try again |
| 3–4 | Worried but determined | Scratches head, checks notes, lifts small checklist |
| 5–6 | Neutral / steady | Nods, types, sips coffee, reviews report |
| 7–8 | Happy / encouraged | Small bounce, thumbs-up claw, antennae perk up |
| 9–10 | Very happy | Confetti stars, trophy, cheerful wave, but not loud or aggressive |

Avoid:

- Aggressive fist pumps
- Dominant gestures
- Angry expressions
- Human-like stress breakdowns
- Overly corporate power poses

## 11. Graphical Handbook Requirement

A full graphical handbook should be created for implementation handoff.

The handbook should include:

1. Full-body Steve master character sheet
2. Front, side, and three-quarter views
3. Career-stage silhouettes mapped to implemented stage IDs
4. Career-stage final-color illustrations mapped to implemented stage IDs
5. Score/rating-based expression and animation sheet mapped to implemented rating values
6. Clothing inventory sheet
7. Hat inventory sheet
8. Shoe inventory sheet
9. Accessory inventory sheet
10. Environment progression sheet
11. UI feedback panel mockup
12. Compact web widget mockup
13. Mobile widget mockup
14. Do / Don’t visual rules

The generated concept image from this design session should be treated as the first visual direction board, not as final production art and not as schema authority.

## 12. Asset Naming Guidelines

Use stable, predictable asset names. Asset naming must follow implemented stage/rating IDs where they already exist.

Example names, to be adapted to actual schema:

```text
steve_stage_01_default.png
steve_stage_01_rating_low.png
steve_stage_01_rating_mid.png
steve_stage_01_rating_high.png
steve_outfit_stage_01_polo_blue_chinos_sneakers.png
steve_hat_baseball_oc_blue.png
steve_accessory_notebook_black.png
steve_ui_feedback_panel_desktop.png
steve_ui_feedback_panel_mobile.png
```

If SVG assets are practical, prefer SVG for icons, hats, clothes, and simple expressions. Use PNG/WebP for full rendered mascot states.

## 13. Implementation Architecture

Steve should be implemented as a separate website feature.

### Front-End Files

```text
steve_feedback.js
steve_feedback.css
steve_widget.html
steve_assets_manifest.json
```

### Back-End / Data Files

Use the existing implemented Steve paths if already created. Do not rename or migrate existing files merely to match this visual guide.

Expected or recommended paths include:

```text
/root/openclaw_steve/update_steve_daily.py
/root/openclaw_steve/steve_config.yaml
/root/openclaw_steve/data/steve_feedback.db
/root/openclaw_steve/data/steve_state.json
/root/openclaw_steve/data/steve_daily_summary_YYYY-MM-DD.json
```

### Existing Cron Requirement

Steve updates every night at 2:00 a.m. server time, using the existing implemented cron contract.

Expected cron form:

```cron
0 2 * * * /usr/bin/python3 /root/openclaw_steve/update_steve_daily.py >> /root/openclaw_logs/steve_update.log 2>&1
```

Do not alter WS1 cron timing or WS1 pipeline scripts to support Steve.

## 14. Integration with WS1 Website

Steve may appear on the WS1 daily monitoring website as a feedback layer.

Steve must not affect:

- WS1 retrieval
- WS1 source pool
- WS1 story selection
- WS1 narrative diversity logic
- WS1 validation
- WS1 delivery gate
- WS1 generated report content

Steve can collect employee feedback about WS1 report quality, including feedback related to story diversity, repetition, missed stories, weak prioritization, and usefulness.

Feedback categories should include the story-diversity concerns captured in `WS1_Editorial_Review_Memo_Story_Diversity_Degradation.md`:

- Too repetitive
- Same story repeated
- Missed stronger story
- Weak story diversity
- Good story selection
- Bad priority choice
- Needs more commercial relevance
- Needs stronger executive usefulness

## 15. Relationship to WS1 Process

Steve should support the WS1 process only by collecting human review feedback.

Steve feedback should become an input to human review and future product-quality memos, not a direct runtime control.

Steve must not be wired into the WS1 selection-layer rebuild, source weighting, narrative diversity layer, or report generation process.

## 16. Dashboard Style Compatibility

The current dashboard template uses a clean card-based layout, compact typography, light background, and restrained status badges.

Steve should fit this UI but add warmth.

Recommended UI fit:

- Rounded floating button
- Friendly cream or light-blue feedback panel
- Navy/gold accent buttons, softened with rounded corners
- Do not visually overpower the report
- Keep Steve widget collapsible
- Avoid blocking core report reading

## 17. Implementation Steps

### Step 1 — Audit Implemented Steve Schema

Before changing UI or art, identify the current implemented Steve files and record:

- Rating field names and allowed values
- Promotion threshold logic
- Current stage IDs and titles
- Cron state fields
- Outfit fields
- Existing feedback storage schema
- Existing admin/export fields

No implementation should proceed until this audit is complete.

### Step 2 — Map Graphic to Existing Schema

Create a mapping table:

```text
implemented_stage_id → visual_stage_art
implemented_rating_value_or_band → animation_asset
implemented_outfit_fields → wardrobe_asset_combination
implemented_hat_field_if_any → hat_asset
```

If there is no implemented hat field, hats should be handled through the outfit asset manifest rather than adding a new persistent field.

### Step 3 — Update Visual Asset Direction

- Replace executive-realistic Steve with cute full-body lobster Steve.
- Define master character proportions.
- Produce full-body art for each implemented stage.
- Produce score/rating-band animation concepts.

### Step 4 — Build Feedback Panel UI

- Replace narrow text input with large rectangular textarea.
- Use the existing implemented rating input model.
- Add story-diversity and usefulness categories only if compatible with existing schema or operator-approved.
- Add submit/cancel buttons.

### Step 5 — Build Asset Manifest

Create or update `steve_assets_manifest.json` mapping existing implementation fields to assets:

- implemented stage id
- implemented rating or rating band
- outfit id
- hat representation, if supported
- asset path
- alt text
- animation type

### Step 6 — Update Nightly Visual Selection Only

Ensure the 2:00 a.m. cron continues to use implemented scoring and promotion logic.

The visual update may:

- Select daily outfit
- Select optional hat if already supported or manifest-based
- Write current visual state
- Avoid exact outfit repeat

The visual update must not:

- Redefine rating logic
- Redefine promotion thresholds
- Add persistent state fields without operator approval
- Touch WS1 runtime logic

### Step 7 — Add / Confirm Admin Review

Admin view should show fields that already exist in the implemented schema. Additional fields require operator approval.

Desired display includes:

- Date
- Average score or implemented rating summary
- Category counts, if implemented
- Text comments
- Story-diversity flags, if implemented
- Steve stage
- Promotion status
- Export CSV/JSON

### Step 8 — Confirm Non-Interference

Before deployment, verify:

- WS1 report generation unchanged
- WS1 delivery unchanged
- Steve cron failure does not affect WS1 cron
- Steve data writes only under Steve-owned paths
- Steve logs only to Steve-owned logs
- No WS1 pipeline files are modified for Steve visual behavior

## 18. Acceptance Criteria

The implementation is acceptable when:

1. Steve is visibly full-body and anthropomorphic.
2. Clothing changes are obvious at normal web size.
3. Steve is cute, friendly, and non-threatening.
4. Steve does not look like a nightclub owner or aggressive executive.
5. The feedback textarea is large and comfortable for real comments.
6. The graphical handbook covers all implemented career stages, clothes, hats, shoes, accessories, expressions, and UI states.
7. The 2:00 a.m. cron updates Steve visual state without changing implemented rating/promotion logic.
8. Score/rating-based animations are clear and friendly.
9. Promotion state is visible but not distracting.
10. Steve feedback can be reviewed/exported by an admin.
11. No new rating or promotion schema is introduced without explicit operator approval.
12. Steve remains fully outside the WS1 production intelligence pipeline.

## 19. Hard Governance Boundary

Steve is a user-engagement and feedback-capture layer only.

Steve must remain outside the WS1 intelligence pipeline.

No Steve feedback may directly change:

- Retrieval
- Source weighting
- Story ranking
- Prompting
- Validation
- Delivery
- Brain Lite
- Any client-facing report content

Feedback-derived changes require separate review and explicit operator approval.
