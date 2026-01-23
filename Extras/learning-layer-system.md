# Idea: Layered Learning System for ZoomCamp

## The Problem

Technical courses assume foundational knowledge:
- Commands are given without explanation
- Learners hit "knowledge knots" and get stuck
- Googling takes hours and breaks flow
- No mentor to ask quick questions

## The Vision

A "mentor in a box" - documentation that:
1. **Highlights** terms that need context
2. **Links** to explanations instantly
3. **Color-codes** by topic/depth
4. Lets learners **unknot quickly** and continue

## Example

```
BEFORE (current ZoomCamp):
"Run docker run -it --rm ubuntu"
→ Learner stuck: "What does -it mean?"

AFTER (with this system):
"Run docker run [-it] [--rm] ubuntu"
              │      │
              │      └── 🔵 Click → "Removes container on exit"
              └── 🟡 Click → "Interactive terminal mode"
→ Learner clicks, reads 10 seconds, continues
```

## Implementation Options

### Simple (Start Here)
- Markdown with anchor links to glossary
- `[term](#glossary-term)` format
- Works on GitHub natively

### Medium
- GitHub Pages with custom CSS
- Tooltips on hover
- Sidebar navigation

### Advanced
- Web app with React
- Database of concepts
- Progress tracking
- Search functionality

## Color System Idea

| Color | Meaning | Links To |
|-------|---------|----------|
| 🟢 Green | Beginner concept | Basic glossary |
| 🟡 Yellow | Intermediate | Detailed explanation |
| 🔴 Red | Advanced/Important | Deep dive document |

## Why This Matters

"When you have a teacher, you can ask questions. When you're self-learning, you don't even know how to ask the right question."

This system pre-curates the questions and answers.

## Next Steps

1. Continue building glossary.md with explanations
2. Start linking terms in module notes
3. Test with Module 1 content
4. Get feedback from other learners
5. Consider building a simple web interface

---

*Idea captured: January 2026*
*During: Data Engineering ZoomCamp Module 1*
