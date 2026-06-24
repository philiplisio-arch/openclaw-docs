---
document_id: STEVE-FEEDBACK-MASCOT-SPEC
version: 1.0
created: 2026-06-24
last_updated: 2026-06-24
status: PRODUCT SPEC — NOT PIPELINE GOVERNING
classification: INTERNAL WEBSITE FEATURE SPEC
---

# Steve Feedback Mascot — Product and Implementation Spec

## 1. Purpose

Steve is a lightweight feedback-capture mascot for the internal daily monitoring website. He exists to make employee review more engaging and to collect structured human feedback on the daily report.

Steve is **not** an autonomous learning agent. Steve does not modify retrieval, article selection, prompts, validation, Brain Lite, delivery gates, or any production pipeline behavior. Steve captures feedback only. Any feedback-derived product improvement must be reviewed separately and converted into an operator-approved change packet or separate workstream.

## 2. Product Concept

Steve is an anthropomorphized PR executive who starts as an inexperienced intern and gradually develops into a more confident, polished, senior communications professional as users give high scores and constructive feedback.

The visual concept should be:

- Professional PR executive, not nightclub owner
- Corporate, polished, slightly playful
- Retro action-figure inspiration, but toned down for a business audience
- The same recognizable person over time, but physically and professionally maturing
- Early Steve: skinny, uncertain, eager, slightly awkward
- Later Steve: broader shoulders, better posture, more confidence, sharper executive presence

## 3. Core User Experience

Steve appears as a floating mascot widget on the internal daily monitoring report page.

Default label:

> Tell Steve what you think

When clicked, Steve opens a feedback panel where employees can:

1. Give the report a score from 1 to 10
2. Add written feedback
3. Select feedback categories
4. Optionally tag feedback to a specific article or section
5. See Steve react with an animation based on the score
6. See Steve's current career stage and progress toward promotion

## 4. Feedback Score Model

Users rate the daily report on a **1–10 scale**.

| Score | Meaning | Steve Reaction Type |
|---|---|---|
| 1 | Very poor | Strongly discouraged but professional |
| 2 | Poor | Worried / visibly concerned |
| 3 | Weak | Concerned, reviewing notes |
| 4 | Below average | Serious, focused on improvement |
| 5 | Acceptable | Neutral professional |
| 6 | Fair | Slightly encouraged |
| 7 | Good | Confident, appreciative |
| 8 | Very good | Pleased, energized |
| 9 | Excellent | Highly confident |
| 10 | Outstanding | Proud but restrained executive confidence |

Scores must be stored as numerical feedback and must not automatically change any pipeline behavior.

## 5. Animation System

Steve should have animations tied to score bands.

### 1–2: Poor Day

Animation ideas:

- Steve slumps slightly
- Loosens tie
- Rubs forehead
- Looks at a stack of marked-up reports
- Takes a deep breath and writes notes

Tone: disappointed but professional. No slapstick.

Suggested message:

> Rough day. I’ll take this seriously.

### 3–4: Needs Work

Animation ideas:

- Steve frowns slightly
- Checks notes
- Highlights a report page
- Looks determined but concerned

Suggested message:

> Got it. I need to improve this.

### 5–6: Acceptable / Neutral

Animation ideas:

- Steve nods
- Reviews papers
- Types notes
- Neutral expression

Suggested message:

> Thanks. I’ll keep working on it.

### 7–8: Good Day

Animation ideas:

- Steve smiles
- Gives a modest thumbs up
- Straightens tie
- Walks with improved confidence

Suggested message:

> Good feedback. I’m getting better.

### 9–10: Excellent Day

Animation ideas:

- Steve stands tall
- Confident handshake
- Presents a slide
- Gives a restrained executive smile
- Brief celebratory nod, not cartoon dancing

Suggested message:

> Great. This is the standard I’m aiming for.

## 6. Daily Wardrobe Variation

Every day Steve should appear in a different professional wardrobe combination.

### Required Rule

Steve must not appear in the exact same outfit on two consecutive days.

Outfit = suit + shirt + tie + optional accessory.

### Suit Pool

- Navy suit
- Charcoal suit
- Medium gray suit
- Dark brown suit
- Subtle navy pinstripe suit
- Subtle charcoal pinstripe suit
- Tan sport coat, lower-rank only
- Dark blue blazer, lower/mid-rank

### Shirt Pool

- White
- Light blue
- Pale pink
- Cream
- Light lavender
- Blue stripe
- White with subtle texture

### Tie Pool

- Navy solid
- Burgundy solid
- Silver
- Forest green
- Gold
- Conservative red stripe
- Conservative blue stripe
- Subtle paisley
- Small-dot pattern

### Accessory Pool

- Notebook
- Client research folder
- Laptop
- Coffee mug
- Briefcase
- Presentation clicker
- Conference badge
- Boardroom folder

### Wardrobe Rules by Rank

Early Steve:

- Slightly oversized shirt
- Less polished tie
- Simple trousers or inexpensive jacket
- Practical accessories: notebook, folder

Mid Steve:

- Better-fitting shirt
- More coordinated tie
- Standard business suit
- Accessories: laptop, research folder, briefcase

Senior Steve:

- Tailored suit
- Stronger posture
- Better grooming
- Executive accessories: boardroom folder, presentation clicker, conference badge

Very senior Steve:

- Premium but conservative suits
- No flashy nightclub styling
- No sunglasses except possibly as an Easter egg, disabled by default
- Corporate executive presence over glamour

## 7. Steve Career Ladder

Steve progresses through at least six career stages. Recommended full ladder:

| Stage | Title | Visual / Physical Character |
|---|---|---|
| 1 | Intern Steve | Skinny, uncertain, eager, slightly awkward posture |
| 2 | Account Coordinator Steve | Still slim, cleaner posture, learning the workflow |
| 3 | Account Executive Steve | More confident, stronger stance, better-fitting clothes |
| 4 | Senior Account Executive Steve | Noticeably broader shoulders, more polished, trusted operator |
| 5 | Account Manager Steve | Mature, composed, handles clients confidently |
| 6 | Director Steve | Senior presence, strong posture, calm authority |
| 7 | Senior Director Steve | Boardroom-ready, more physically substantial, executive maturity |
| 8 | Vice President Steve | Highly polished, confident, strategic presence |
| 9 | Senior Vice President Steve | Senior counselor energy, measured and authoritative |
| 10 | Managing Director Steve | Fully mature executive, understated confidence, premium but conservative wardrobe |

The six-stage minimum is Stage 1 through Stage 6. Stages 7–10 are stretch goals.

## 8. Promotion Logic

Promotion should be meaningful but not too slow.

### Core Promotion Rule

Steve earns a promotion when both conditions are met:

1. 7-day rolling average score is **8.0 or higher**
2. At least **5 consecutive scored days** are **7 or higher**

This prevents promotion from happening after one lucky day, but makes advancement visible within a realistic timeframe.

### First Promotion Adjustment

The first promotion should be slightly easier so users see the system working.

Intern Steve → Account Coordinator Steve requires:

- 5-day rolling average score of **7.5 or higher**
- At least **3 consecutive scored days** of **7 or higher**

All later promotions use the core rule.

### Promotion Cooldown

After a promotion, Steve cannot be promoted again for at least **5 scored days**.

This prevents rapid multi-stage jumps.

### Demotion Rule

Do not demote Steve by default. Poor scores should affect mood and slow progress, but demotion will feel punitive and less fun.

Optional future rule:

- If 10 consecutive scored days average below 4.0, Steve enters a temporary “performance improvement plan” visual state, but keeps his title.

## 9. Progress Calculation

For each day:

- Collect all submitted scores
- Calculate daily average score
- Store total number of scores
- Store written feedback count
- Store category counts
- Use daily average score for promotion calculation

If no feedback is submitted for a day:

- Do not count the day toward promotion or streaks
- Steve remains at current rank
- Wardrobe still updates if the page is viewed

## 10. Feedback Categories

Feedback categories should remain simple:

- Great selection
- Missed important story
- Wrong priority
- Too long
- Too short
- Writing unclear
- Needs stronger sources
- Useful client insight
- Too much repetition
- Other

Each feedback record may include one or more categories.

## 11. Data Model

### feedback table

```json
{
  "feedback_id": "uuid",
  "timestamp": "ISO datetime",
  "report_date": "YYYY-MM-DD",
  "report_type": "daily_monitoring",
  "section": "overall | article | executive_take | advisory_layer | source_list",
  "article_title": "optional",
  "article_url": "optional",
  "score": 1,
  "categories": ["wrong_priority", "needs_stronger_sources"],
  "comment": "free text",
  "user_id": "optional internal identifier",
  "steve_stage_at_submission": 1,
  "steve_title_at_submission": "Intern Steve"
}
```

### steve_state table

```json
{
  "state_id": "steve_global",
  "current_stage": 1,
  "current_title": "Intern Steve",
  "current_outfit_id": "stage1_20260624_variant_001",
  "last_outfit_id": "stage1_20260623_variant_004",
  "last_updated": "ISO datetime",
  "last_promotion_date": null,
  "rolling_7_day_average": 0,
  "consecutive_high_score_days": 0,
  "total_feedback_count": 0,
  "total_scored_days": 0
}
```

### steve_daily_summary table

```json
{
  "report_date": "YYYY-MM-DD",
  "average_score": 8.2,
  "score_count": 6,
  "written_feedback_count": 3,
  "category_counts": {
    "great_selection": 3,
    "too_long": 1
  },
  "promotion_eligible": false,
  "promotion_triggered": false,
  "stage_before": 2,
  "stage_after": 2,
  "outfit_id": "stage2_20260624_variant_003"
}
```

## 12. Nightly Steve Update Cron Job

Steve should be updated every night at **2:00 a.m.** server time.

### Cron Schedule

```cron
0 2 * * * /usr/bin/python3 /root/openclaw_steve/update_steve_daily.py >> /root/openclaw_logs/steve_update.log 2>&1
```

### Cron Responsibilities

The nightly Steve job should:

1. Read the prior day’s feedback
2. Calculate daily average score
3. Update rolling 7-day average
4. Update consecutive high-score streak
5. Determine whether Steve qualifies for promotion
6. Select the next daily wardrobe combination
7. Ensure the outfit does not repeat the prior day’s exact outfit
8. Update `steve_state`
9. Write one daily summary record
10. Log all actions clearly

### Required Log Events

Use these log tags:

```text
[STEVE] update_started
[STEVE] feedback_loaded
[STEVE] daily_score_calculated
[STEVE] promotion_check_started
[STEVE] promotion_triggered
[STEVE] promotion_not_triggered
[STEVE] outfit_selected
[STEVE] state_write_completed
[STEVE] update_completed
[STEVE] update_failed
```

### Failure Behavior

Steve failures must be non-blocking.

If the Steve cron job fails:

- Log `[STEVE] update_failed`
- Do not affect the daily monitoring website delivery
- Do not affect retrieval
- Do not affect validation
- Do not affect Brain Lite
- Keep the prior Steve state visible on the website

## 13. File / Directory Structure

Recommended VPS structure:

```text
/root/openclaw_steve/
  update_steve_daily.py
  steve_config.yaml
  steve_assets_manifest.json
  README.md

/root/openclaw_steve/data/
  steve_feedback.db
  steve_state.json
  steve_daily_summary_YYYY-MM-DD.json

/root/openclaw_steve/assets/
  stage_01_intern/
  stage_02_account_coordinator/
  stage_03_account_executive/
  stage_04_senior_ae/
  stage_05_account_manager/
  stage_06_director/
  stage_07_senior_director/
  stage_08_vp/
  stage_09_svp/
  stage_10_managing_director/
```

Recommended website files:

```text
steve_feedback.js
steve_feedback.css
steve_widget.html
```

## 14. Front-End Requirements

The daily website should read Steve’s current state from either:

- `/api/steve-state`, if a backend exists, or
- a generated static `steve_state.json`, if the site remains static

The widget must display:

- Current Steve image / animation
- Current title
- Current daily outfit
- Score input, 1–10
- Feedback category buttons
- Comment field
- Promotion progress indicator
- Message based on score after submission

## 15. Admin Review View

The admin view should show:

- Date
- Average score
- Score count
- Written feedback count
- Category distribution
- Comments
- Steve stage before / after
- Promotion status
- Export CSV / JSON option

Admin should be able to mark feedback as:

- Reviewed
- Useful
- Requires operator follow-up
- Candidate for change packet

## 16. Governance Boundary

Steve is a feedback capture and engagement feature only.

Steve must not directly alter:

- Retrieval queries
- Source ranking
- Article selection
- Agent prompt
- Validator logic
- Scrubber logic
- Delivery gate
- Brain Lite schema
- Client configuration

Human review is required before any feedback affects the OpenClaw product or pipeline.

## 17. Success Criteria

MVP is successful if:

1. Steve appears on the daily monitoring website
2. Users can submit a 1–10 score and optional comment
3. Feedback is stored reliably
4. Steve reacts appropriately to the score
5. Steve’s outfit changes daily
6. Steve does not repeat the same outfit on consecutive days
7. The 2:00 a.m. cron job updates Steve state successfully
8. Promotion logic works using rolling score and streak rules
9. Steve failures do not affect the monitoring report pipeline
10. Admin can review/export feedback

## 18. Recommended Build Phases

### Phase 1 — MVP Feedback Widget

- Floating Steve icon
- Feedback panel
- 1–10 score
- Comment field
- Store feedback
- Basic score reaction

### Phase 2 — Nightly Steve State Cron

- `update_steve_daily.py`
- SQLite or JSON state store
- Daily average score
- Rolling average
- Streak calculation
- 2:00 a.m. cron job
- Logging

### Phase 3 — Wardrobe Variation

- Outfit manifest
- Daily outfit selection
- No consecutive duplicate outfit rule
- Rank-appropriate wardrobe pools

### Phase 4 — Promotion System

- Career ladder
- First-promotion rule
- Standard promotion rule
- Cooldown
- Progress display

### Phase 5 — Admin Dashboard

- Feedback review table
- Filters
- Export
- Mark reviewed/useful/follow-up

### Phase 6 — Improved Animation Assets

- Stage-specific Steve art
- Score-band animations
- More polished wardrobe variants
- Optional seasonal or campaign-specific wardrobe sets

## 19. Implementation Note

Because Steve is outside the OpenClaw production intelligence pipeline, this feature can be implemented as a separate internal website workstream. The only integration point should be the report webpage UI and a read/write feedback store.
