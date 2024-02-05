import argparse


def generate_initial_rosta(days_in: int, days_out: int):
    return ["IN"] * days_in + ["OUT"] * days_out


def generate_complete_set(days_in: int, days_out: int, weeks: int = 52):
    initial = generate_initial_rosta(days_in, days_out)
    return [initial[-i:] + initial[:-i] for i in range(weeks)]


def generate_complete_rosta(people: int, days_in: int, days_out: int, weeks: int = 52):
    complete_set = generate_complete_set(days_in, days_out, weeks)
    return [complete_set[-i:] + complete_set[:-i] for i in range(people)]


def save_rosta_to_csv(rosta, filename):
    weeks = len(rosta[0])
    with open(filename, "w") as f:
        f.write(
            f'Person, {"".join(["Sunday,", "Monday,", "Tuesday,", "Wednesday,", "Thursday,", "Friday,", "Saturday,"]*weeks).strip(",")}\n'
        )
        for i, person in enumerate(rosta):
            new_ = []
            for j in person:
                new_ += j
            f.write(f"Person {i+1}, {','.join(new_)}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Create a rosta CSV for 52 weeks for a given number of people"
    )
    parser.add_argument(
        "--people", type=int, help="Number of people", required=True, default=13
    )
    parser.add_argument(
        "--days_in", type=int, help="Number of days in", required=True, default=5
    )
    parser.add_argument(
        "--days_out", type=int, help="Number of days out", required=True, default=2
    )
    parser.add_argument(
        "--weeks",
        type=int,
        help="Number of weeks to generate",
        default=52,
        required=False,
    )
    parser.add_argument(
        "--output",
        type=str,
        help="Output file name",
        default="rosta.csv",
        required=False,
    )

    args = parser.parse_args()

    assert args.people > 0, "Number of people must be greater than 0"
    assert args.days_in > 0, "Number of days in must be greater than 0"
    assert args.days_out > 0, "Number of days out must be greater than 0"
    assert args.days_in + args.days_out == 7, "Days in and days out must add up to 7"

    complete_rosta = generate_complete_rosta(
        args.people, args.days_in, args.days_out, args.weeks
    )
    save_rosta_to_csv(complete_rosta, args.output)
