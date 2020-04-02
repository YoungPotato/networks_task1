import argparse
import traceroute


def main():
    hint = "Программа для определения AS по маршруту до конечной точки"
    parser = argparse.ArgumentParser(description=hint)
    parser.add_argument('-dst', type=str, required=True,
                        help='Destination ip address')
    args = parser.parse_args()
    program = traceroute.Program()
    program.get_statistics(args.dst)


if __name__ == "__main__":
    main()
