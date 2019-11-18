import asyncio
import argparse
import sys
import socket


async def tcp_echo_client(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.3)
    try:
        s.connect((host, port))
        print(".", end="")
        return True
    except Exception:
        return False
    finally:
        s.settimeout(None)


async def main(host, port):
    start_port, end_port = port.split("-")
    result = []
    for port in range(int(start_port), int(end_port) + 1):
        if await tcp_echo_client(host, port):
            result.append(port)
        else:
            continue

    sys.stdout.write(f"\n{str(result)} ports are opened" + "\n")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""Port scanner, for use run programm with param --host <name or ip> and 
                                                 --ports <range> (ports by default have value 0-65535)"""
    )
    parser.add_argument("--host", help="enter host or IP", required=True)
    parser.add_argument(
        "--ports",
        help="Enter of start and end scan ports like 10-111",
        default="0-65535",
    )
    args = parser.parse_args()
    asyncio.run(main(args.host, args.ports))
