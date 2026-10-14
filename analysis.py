"""Basic analysis of made-up student test scores."""

import statistics

SCORES = {
    "Alice": {"Math": 92, "Science": 88, "English": 79},
    "Bob": {"Math": 75, "Science": 64, "English": 82},
    "Charlie": {"Math": 58, "Science": 71, "English": 66},
    "Diana": {"Math": 98, "Science": 95, "English": 91},
    "Ethan": {"Math": 81, "Science": 77, "English": 85},
    "Fiona": {"Math": 67, "Science": 83, "English": 94},
    "George": {"Math": 45, "Science": 52, "English": 60},
    "Hannah": {"Math": 88, "Science": 90, "English": 73},
}

GRADE_BOUNDARIES = [(90, "A"), (80, "B"), (70, "C"), (60, "D"), (0, "F")]


def letter_grade(score):
    for threshold, grade in GRADE_BOUNDARIES:
        if score >= threshold:
            return grade


def summarize(values):
    return {
        "mean": statistics.mean(values),
        "median": statistics.median(values),
        "stdev": statistics.stdev(values),
        "min": min(values),
        "max": max(values),
    }


def main():
    subjects = list(next(iter(SCORES.values())))

    print("=== Subject statistics ===")
    print(f"{'Subject':<10}{'Mean':>8}{'Median':>8}{'StDev':>8}{'Min':>6}{'Max':>6}")
    for subject in subjects:
        s = summarize([scores[subject] for scores in SCORES.values()])
        print(
            f"{subject:<10}{s['mean']:>8.1f}{s['median']:>8.1f}"
            f"{s['stdev']:>8.1f}{s['min']:>6}{s['max']:>6}"
        )

    print("\n=== Student averages (ranked) ===")
    averages = {name: statistics.mean(s.values()) for name, s in SCORES.items()}
    ranked = sorted(averages.items(), key=lambda kv: kv[1], reverse=True)
    for rank, (name, avg) in enumerate(ranked, start=1):
        print(f"{rank}. {name:<8} {avg:6.1f}  ({letter_grade(avg)})")

    print("\n=== Grade distribution (all scores) ===")
    all_scores = [v for s in SCORES.values() for v in s.values()]
    for _, grade in GRADE_BOUNDARIES:
        count = sum(1 for v in all_scores if letter_grade(v) == grade)
        print(f"{grade}: {'#' * count} ({count})")

    print("\n=== Highlights ===")
    for subject in subjects:
        top = max(SCORES, key=lambda n: SCORES[n][subject])
        print(f"Top in {subject}: {top} ({SCORES[top][subject]})")

    overall_mean = statistics.mean(all_scores)
    struggling = [n for n, a in averages.items() if a < 65]
    print(f"Overall class average: {overall_mean:.1f}")
    print(f"Students below 65 average: {', '.join(struggling) or 'none'}")


if __name__ == "__main__":
    main()
