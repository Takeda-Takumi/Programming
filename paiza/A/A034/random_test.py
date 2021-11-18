import random
import subprocess

TESTCASE_FILE = "random.in"
MAIN_FILE = "A034b.py"
GREEDY_FILE = "A034_other.py"


def read_random_case():
    with open(TESTCASE_FILE, "r", encoding="utf-8") as f:
        return "".join(map(str, f.readlines()))


# NOTE: 問題に合わせてランダムテストケースを作成する
def write_random_case():
    with open(TESTCASE_FILE, "w", encoding="utf-8") as f:
        lines = []

        # 1 <= N, X <= 10
        N = random.randint(1, 20)
        X = random.randint(1, 5000)
        lines.append(f"{N} {X}")

        for i in range(N):
            tmp = random.randint(1, 5000)
            lines.append(f"{tmp}")

        f.write("\n".join(lines))


def solve(proc_name):
    with open(TESTCASE_FILE, "r", encoding="utf-8") as f:
        res = subprocess.run(
            ["python3", proc_name], stdin=f, stdout=subprocess.PIPE, encoding="utf-8")
        return res.stdout


def main():
    while True:
        write_random_case()
        A = solve(MAIN_FILE)
        B = solve(GREEDY_FILE)
        if A != B:
            print("----------------------------------------")
            print("Wrong Answer")
            print("[test case]")
            print(read_random_case())
            print(f"[{MAIN_FILE}]")
            print(A, end="")
            print(f"[{GREEDY_FILE}]")
            print(B, end="")
            print("----------------------------------------")


if __name__ == "__main__":
    main()