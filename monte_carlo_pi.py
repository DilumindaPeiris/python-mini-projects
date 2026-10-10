"""Estimate pi with reproducible random samples."""
import argparse
import math
import random

def estimate_pi(samples, seed=42):
    if samples <= 0:
        raise ValueError("Samples must be positive.")
    rng = random.Random(seed)
    inside = sum(rng.random() ** 2 + rng.random() ** 2 <= 1 for _ in range(samples))
    return 4 * inside / samples

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--samples", type=int, default=10000)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--trials", type=int, default=1, help="Number of trials to run")
    args = parser.parse_args()
    if args.samples <= 0:
        parser.error("Samples must be positive.")
    if args.trials <= 0:
        parser.error("Trials must be positive.")
        
    if args.trials == 1:
        print(f"Estimated pi: {estimate_pi(args.samples, args.seed):.6f}")
    else:
        results = [estimate_pi(args.samples, args.seed + i) for i in range(args.trials)]
        mean = sum(results) / len(results)
        variance = sum((x - mean) ** 2 for x in results) / len(results)
        std_dev = math.sqrt(variance)
        print(f"Ran {args.trials} trials with {args.samples} samples each.")
        print(f"Mean estimated pi: {mean:.6f}")
        print(f"Standard deviation:  {std_dev:.6f}")

