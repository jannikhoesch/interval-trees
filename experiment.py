from IntervalTree import IntervalTree
import random
import time
import matplotlib.pyplot as plt
from pympler import asizeof


def naive_stabbing(intervals, q):
    """Perform a naive stabbing query to find intervals containing the point q."""
    return [interval for interval in intervals if interval[0] <= q <= interval[1]]


def generate_intervals(n):
    """Generate a list of random intervals."""
    intervals = []
    for _ in range(n):
        start = random.randint(1, 10000)
        end = random.randint(1, 10000)
        if start > end:
            start, end = end, start
        intervals.append((start, end))
    return intervals


def run_experiment(n_intervals):
    """Run the experiment on a set number of intervals, collecting data on build and query times."""
    print(f"Running experiment for {n_intervals} intervals...")
    intervals = generate_intervals(n_intervals)

    # Build the tree with random intervals
    build_start = time.time()
    tree = IntervalTree(intervals)
    build_time = (time.time() - build_start) * 1000

    # Perform 100 random queries
    query_times_tree = []
    query_times_naive = []
    for _ in range(100):
        q = random.randint(1, 1000)

        # Solve with tree
        query_start = time.time()
        tree.query(q)
        query_times_tree.append(time.time() - query_start)

        # Solve naive
        query_start = time.time()
        naive_stabbing(intervals, q)
        query_times_naive.append(time.time() - query_start)

    avg_query_time_tree = (sum(query_times_tree) / len(query_times_tree)) * 1000
    avg_query_time_naive = (sum(query_times_naive) / len(query_times_naive)) * 1000
    memory = asizeof.asizeof(tree)

    return build_time, avg_query_time_tree, avg_query_time_naive, memory


def collect_data(n_range):
    """Collect data over a range of interval sizes."""
    results = {'build time': [], 'average query time': [], 'average query time naive': [], 'memory usage': []}
    for n in n_range:
        build_time, avg_query_time, avg_query_time_naive, memory = run_experiment(n)
        results['build time'].append(build_time)
        results['average query time'].append(avg_query_time)
        results['average query time naive'].append(avg_query_time_naive)
        results['memory usage'].append(memory)
    return results


def plot_results(n_range, results):
    """Plot results of the experiment."""
    # Plot for Average Query Times
    plt.figure(figsize=(10, 6))
    plt.plot(n_range, results['average query time'], label='IntervalTree Avg Query Time', color='blue')
    plt.plot(n_range, results['average query time naive'], label='Naive Avg Query Time', color='red')
    plt.xlabel('Number of Intervals')
    plt.ylabel('Average Query Time (milliseconds)')
    plt.title('Average Query Time Comparison')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot for Build Times
    plt.figure(figsize=(10, 6))
    plt.plot(n_range, results['build time'], label='Build Time', color='green')
    plt.xlabel('Number of Intervals')
    plt.ylabel('Build Time (milliseconds)')
    plt.title('Build Time Analysis')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot for Memory Usage
    plt.figure(figsize=(10, 6))
    plt.plot(n_range, results['memory usage'], label='Memory Usage', color='purple')
    plt.xlabel('Number of Intervals')
    plt.ylabel('Memory Usage (bytes)')
    plt.title('Memory Usage Analysis')
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    n_range = range(10, 100000, 1000)
    results = collect_data(n_range)
    plot_results(n_range, results)


if __name__ == "__main__":
    main()
