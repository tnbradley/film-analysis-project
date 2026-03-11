# Tableau Dashboard Design

> **Film Analysis Project - Dashboard Wireframes**

---

## 📊 Dashboard 1: Executive Overview

**Purpose:** High-level insights for Film Leadership

### Layout
```
┌─────────────────────────────────────────────────────────────────┐
│  REGAL FILM ANALYSIS DASHBOARD          [Date Range Selector]  │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│   │  85,891      │  │   6.22       │  │   5,623      │         │
│   │  Total Films │  │  Avg Rating  │  │ Hidden Gems  │         │
│   │  (2000-2024) │  │  (0-10)      │  │  (≥7.5, <5K) │         │
│   └──────────────┘  └──────────────┘  └──────────────┘         │
│                                                                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   GENRE PERFORMANCE MATRIX                    [Genre Filter ▼]  │
│   ┌──────────────────────────────────────────────────────┐     │
│   │                                                      │     │
│   │    Y: Avg Rating                                     │     │
│   │    ↑                                                 │     │
│   │    │  ○ Documentary (7.0)                           │     │
│   │    │  ○ Biography (6.8)                             │     │
│   │    │           ○ Action (5.4)                       │     │
│   │    │              ○ Horror (4.3)                    │     │
│   │    └────────────────────────────→ X: Movie Count    │     │
│   │                                                      │     │
│   └──────────────────────────────────────────────────────┘     │
│                                                                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   RATING DISTRIBUTION           │   DECADE TRENDS              │
│   ┌──────────────────────┐      │   ┌──────────────────────┐   │
│   │   Bell Curve         │      │   │  Line + Bar Combo    │   │
│   │   (Rating 0-10)      │      │   │  Blue: Avg Rating    │   │
│   │   Mean: 6.22         │      │   │  Red: Movie Count    │   │
│   └──────────────────────┘      │   └──────────────────────┘   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**Key Metrics (KPIs):**
- Total Films Analyzed
- Average IMDb Rating
- Number of Hidden Gems
- % of Films by Rating Category

**Visualizations:**
1. **Genre Matrix** (Scatter Plot): X = Movie Count, Y = Avg Rating, Size = Avg Votes
2. **Rating Distribution** (Histogram): Distribution of all ratings with mean/median lines
3. **Decade Trends** (Combo Chart): Dual axis showing rating trend vs. production volume

---

## 📊 Dashboard 2: Genre Deep Dive

**Purpose:** Detailed genre analysis for booking strategy

### Layout
```
┌─────────────────────────────────────────────────────────────────┐
│  GENRE PERFORMANCE ANALYSIS             [Select Genre ▼]       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   ┌──────────────────────────────────────────────────────────┐  │
│   │  HORIZONTAL BAR CHART: Avg Rating by Genre (Top 10)      │  │
│   │  Sorted: Highest to Lowest Rating                        │  │
│   │  Color: Blue gradient based on rating                    │  │
│   └──────────────────────────────────────────────────────────┘  │
│                                                                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   GENRE COMPARISON TABLE                                        │
│   ┌─────────────┬───────────┬────────────┬───────────┬────────┐ │
│   │ Genre       │ Avg Rating│ Movie Count│ Avg Votes │ Trend  │ │
│   ├─────────────┼───────────┼────────────┼───────────┼────────┤ │
│   │ Documentary │   7.00    │   8,132    │   1,009   │  ↗️    │ │
│   │ Biography   │   6.80    │   3,525    │  15,550   │  →     │ │
│   │ Animation   │   6.17    │     996    │   5,507   │  ↗️    │ │
│   │ Drama       │   6.02    │  23,340    │   6,100   │  →     │ │
│   │ ...         │   ...     │    ...     │    ...    │  ...   │ │
│   └─────────────┴───────────┴────────────┴───────────┴────────┘ │
│                                                                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   POPULARITY vs QUALITY BY GENRE                               │
│   ┌──────────────────────────────────────────────────────────┐  │
│   │  SCATTER PLOT: X = Rating, Y = Votes (log scale)         │  │
│   │  Color = Genre, Size = Movie Count                       │  │
│   │  Trend line showing correlation                          │  │
│   └──────────────────────────────────────────────────────────┘  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**Interactivity:**
- Genre filter dropdown
- Hover for detailed metrics
- Click genre to drill down

---

## 📊 Dashboard 3: Hidden Gems Discovery

**Purpose:** Identify undervalued films for targeted marketing

### Layout
```
┌─────────────────────────────────────────────────────────────────┐
│  HIDDEN GEMS FINDER                     [Rating Min ▼] [Genre ▼]│
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   FILTER CONTROLS:                                              │
│   [Minimum Rating: 7.5 ▼]  [Max Votes: 5,000 ▼]  [Genre: All ▼]│
│                                                                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   HIDDEN GEMS SCATTER PLOT                                      │
│   ┌──────────────────────────────────────────────────────────┐  │
│   │                                                          │  │
│   │  Y: Number of Votes (Popularity)                         │  │
│   │  ↑                                                       │  │
│   │  │                                            ★          │  │
│   │  │        ★ (Good but known)                            │  │
│   │  │   ★                                                   │  │
│   │  │              ★★ (Hidden Gems!)                       │  │
│   │  │   ★ ★                                               │  │
│   │  └──────────────────────────────────────→ X: Rating    │  │
│   │                                                          │  │
│   │  Color: Genre    Size: Runtime    ★ = Annotated label  │  │
│   └──────────────────────────────────────────────────────────┘  │
│                                                                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   HIDDEN GEMS BY GENRE              │   TOP HIDDEN GEMS TABLE   │
│   ┌──────────────────────┐          │   ┌────────────────────┐  │
│   │  VERTICAL BAR CHART  │          │   │  Rank │ Title    │  │
│   │  Documentary: 2,235  │          │   │  1    │ Border.. │  │
│   │  Drama: 1,166        │          │   │  2    │ Story... │  │
│   │  Biography: 580      │          │   │  3    │ Ident... │  │
│   │  ...                 │          │   │  ...  │ ...      │  │
│   └──────────────────────┘          │   └────────────────────┘  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**Key Insight Areas:**
- **Sweet Spot:** Rating ≥7.5, Votes 1K-5K (known but not saturated)
- **Deep Cuts:** Rating ≥8.0, Votes <1K (undiscovered)
- **Filter by:** Genre, Year, Runtime

---

## 📊 Dashboard 4: Blockbuster Intelligence

**Purpose:** Understand what makes a theatrical hit

### Layout
```
┌─────────────────────────────────────────────────────────────────┐
│  BLOCKBUSTER ANALYSIS                   [Year Range ▼]         │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│   │   1,970      │  │    38%       │  │    6.81      │         │
│   │ Blockbusters │  │  Action      │  │  Avg Rating  │         │
│   │  (100K+ votes)│  │  Share       │  │  Blockbusters│         │
│   └──────────────┘  └──────────────┘  └──────────────┘         │
│                                                                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   BLOCKBUSTER GENRES                │   RATING DISTRIBUTION    │
│   ┌──────────────────────┐          │   ┌────────────────────┐  │
│   │  HORIZONTAL BAR      │          │   │  PIE / DONUT       │  │
│   │  Action: 752         │          │   │  Excellent: 8%     │  │
│   │  Comedy: 327         │          │   │  Good: 40%         │  │
│   │  Drama: 284          │          │   │  Average: 40%      │  │
│   │  Adventure: 220      │          │   │  Below Avg: 11%    │  │
│   └──────────────────────┘          │   └────────────────────┘  │
│                                                                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   BLOCKBUSTER TIMELINE                                          │
│   ┌──────────────────────────────────────────────────────────┐  │
│   │  AREA CHART: Blockbusters by Year (2000-2024)            │  │
│   │  Color stack by Genre                                    │  │
│   └──────────────────────────────────────────────────────────┘  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**Key Findings to Highlight:**
- Action dominates blockbusters (38%)
- Blockbusters average 6.81 rating (above overall mean of 6.22)
- Only 8% of blockbusters are "Excellent" (8.0+) — room for quality

---

## 🎨 Design Specifications

### Color Palette
| Use Case | Color | Hex |
|----------|-------|-----|
| Primary | Regal Blue | #1E3A5F |
| Secondary | Gold Accent | #D4AF37 |
| Success (High Rating) | Green | #2E7D32 |
| Warning (Medium) | Orange | #F57C00 |
| Danger (Low Rating) | Red | #C62828 |
| Background | White/Light Gray | #FAFAFA |

### Typography
- **Titles:** 18-24pt Bold
- **KPI Numbers:** 32-48pt Bold
- **Labels:** 11-12pt Regular
- **Tooltips:** 10pt

### Chart Best Practices
1. **Always include context:** Compare to overall average
2. **Use consistent scales:** 0-10 for ratings across all charts
3. **Highlight outliers:** Annotate interesting data points
4. **Enable drill-down:** Click genre → see films in that genre

---

## 🔗 Data Connection

**Primary Data Source:** `imdb_for_tableau.csv`

**Key Fields:**
- `primaryTitle` (Dimension)
- `primaryGenre` (Dimension)
- `startYear` (Dimension)
- `decade` (Dimension)
- `averageRating` (Measure)
- `numVotes` (Measure)
- `runtimeMinutes` (Measure)
- `ratingCategory` (Dimension)
- `popularityTier` (Dimension)

**Calculated Fields to Create:**
```
Hidden Gem Flag:
  IF [averageRating] >= 7.5 AND [numVotes] < 5000 THEN "Hidden Gem"
  ELSE "Standard" END

Blockbuster Flag:
  IF [numVotes] >= 100000 THEN "Blockbuster"
  ELSEIF [numVotes] >= 50000 THEN "Major"
  ELSEIF [numVotes] >= 10000 THEN "Popular"
  ELSE "Niche" END
```

---

## 📱 Dashboard Sizing

- **Desktop:** 1200 x 800 px (fixed)
- **Laptop:** 100% width, scrollable height
- **Export to PDF:** Landscape A4

---

**Next Steps:**
1. Import `imdb_for_tableau.csv` into Tableau
2. Create data source filters (remove nulls)
3. Build KPI cards first
4. Add charts one by one
5. Apply formatting and color palette
6. Test interactivity and filters
